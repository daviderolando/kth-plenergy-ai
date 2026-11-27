"""Build a Quarto/Pandoc reference doc from the KTH PowerPoint template.

Pandoc picks slide layouts by their standard names ("Title Slide", "Title and
Content", ...). The KTH template uses its own names, so Pandoc would fall back
to its default look. This script copies the template, gives seven KTH layouts
the standard names and removes the sample slides.

Usage: uv run python scripts/make_reference_pptx.py
"""
from copy import deepcopy
from pathlib import Path

from lxml import etree
from pptx import Presentation

SRC = Path("resources/kth_template_presentation.pptx")
DST = Path("resources/kth_reference.pptx")

# Pandoc layout name -> KTH layout name
LAYOUTS = {
    "Title Slide": "Title, navy blue",
    "Section Header": "Title/chapter, navy blue",
    "Title and Content": "Headline and content",
    "Two Content": "Two parts",
    "Comparison": "Two parts, subheader",
    "Content with Caption": "Text and image",
    "Blank": "Empty",
}

prs = Presentation(SRC)

by_name = {layout.name: layout for layout in prs.slide_layouts}
for pandoc_name, kth_name in LAYOUTS.items():
    by_name[kth_name]._element.cSld.set("name", pandoc_name)

# Remove the sample slides so the file only carries masters and layouts.
slide_ids = prs.slides._sldIdLst
for slide_id in list(slide_ids):
    prs.part.drop_rel(slide_id.rId)
    slide_ids.remove(slide_id)

# Pandoc uses "Content with Caption" for a slide with text followed by a table
# or image: it needs a title, a text (body) placeholder and a content placeholder.
# The KTH "Text and image" layout is half text, half picture, so reshape it to
# the "Headline and content" geometry with a caption line above the content.
caption = by_name["Text and image"]
headline = by_name["Headline and content"]
title_box = {s.placeholder_format.idx: s for s in headline.placeholders}[0]
content_box = {s.placeholder_format.idx: s for s in headline.placeholders}[1]

for shape in list(caption.placeholders):
    idx = shape.placeholder_format.idx
    if idx == 13:  # picture
        shape._element.getparent().remove(shape._element)
    elif idx == 0:
        shape.left, shape.top, shape.width, shape.height = (
            title_box.left, title_box.top, title_box.width, title_box.height)
    elif idx == 1:
        shape.left, shape.top, shape.width = (
            content_box.left, content_box.top + 780000, content_box.width)
        shape.height = content_box.height - 780000
        body_source = shape

body = deepcopy(body_source._element)
ns = {"p": "http://schemas.openxmlformats.org/presentationml/2006/main",
      "a": "http://schemas.openxmlformats.org/drawingml/2006/main"}
ph = body.find(".//p:ph", ns)
ph.attrib.pop("sz", None)
ph.set("type", "body")
ph.set("idx", "14")
body.find(".//p:cNvPr", ns).set("id", "90")
body.find(".//p:cNvPr", ns).set("name", "Caption placeholder")
off = body.find(".//a:off", ns)
ext = body.find(".//a:ext", ns)
off.set("y", str(content_box.top))
ext.set("cy", "700000")
tx = body.find(".//p:txBody", ns)
tx.find("a:lstStyle", ns).append(etree.fromstring(
    '<a:lvl1pPr xmlns:a="%s" marL="0" indent="0"><a:buNone/></a:lvl1pPr>' % ns["a"]))
for para in tx.findall("a:p", ns)[1:]:
    tx.remove(para)
caption.shapes._spTree.append(body)

prs.save(DST)
print(f"{DST} ({DST.stat().st_size / 1e6:.1f} MB)")

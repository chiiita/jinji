#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
リードマグネット（公開版クリーン・手順書スタイル）markdown → ブランドPDF（スマホ最適）。
reportlab + 内蔵日本語CIDフォント（外部依存なし）。出力 checklist.pdf。
★スマホ可読性優先：ページを縦長・幅狭（110×196mm）にして画面にフィット、フォント大きめ・行間広め。
"""
import re, html, pathlib
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table,
                                TableStyle, HRFlowable, PageBreak, KeepTogether, Image)

JP = "HeiseiKakuGo-W5"
pdfmetrics.registerFont(UnicodeCIDFont(JP))
pdfmetrics.registerFontFamily(JP, normal=JP, bold=JP, italic=JP, boldItalic=JP)

NAVY = colors.HexColor("#2C3E50")
INK = colors.HexColor("#1F2933")
SUB = colors.HexColor("#5A6270")

# ★スマホ最適ページ（縦長・スマホ縦横比≒9:16）。幅を確保しつつ画面フィット。
PAGE = (128*mm, 228*mm)

SRC = pathlib.Path("../lead_magnet_公開版クリーン_2026-06-29.md")
text = SRC.read_text(encoding="utf-8")
text = re.sub(r"<!--.*?-->", "", text, count=1, flags=re.DOTALL).strip()
lines = text.split("\n")

def inl(s):
    s = html.escape(s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", s)
    return s

# styles（フォント大きめ・行間広め）
body = ParagraphStyle("body", fontName=JP, fontSize=12, leading=20, textColor=INK, spaceAfter=9)
h2 = ParagraphStyle("h2", fontName=JP, fontSize=15.5, leading=22, textColor=NAVY, spaceBefore=16, spaceAfter=5)
h3 = ParagraphStyle("h3", fontName=JP, fontSize=13.5, leading=19, textColor=INK, spaceBefore=13, spaceAfter=3)
li = ParagraphStyle("li", fontName=JP, fontSize=12, leading=19, textColor=INK, leftIndent=12, bulletIndent=2, spaceAfter=4)
check = ParagraphStyle("check", fontName=JP, fontSize=12, leading=22, textColor=INK, leftIndent=2, spaceAfter=3)
qrcap = ParagraphStyle("qrcap", fontName=JP, fontSize=11, leading=17, textColor=SUB, alignment=TA_CENTER, spaceBefore=6)
boxp = ParagraphStyle("boxp", fontName=JP, fontSize=11.5, leading=19, textColor=INK)
stepp = ParagraphStyle("stepp", fontName=JP, fontSize=12, leading=19, textColor=INK)
cover_kick = ParagraphStyle("ck", fontName=JP, fontSize=11, leading=17, textColor=NAVY, alignment=TA_CENTER)
cover_title = ParagraphStyle("ct", fontName=JP, fontSize=17, leading=26, textColor=INK, alignment=TA_CENTER)
cover_sign = ParagraphStyle("cs", fontName=JP, fontSize=11, leading=17, textColor=SUB, alignment=TA_CENTER)

doc = SimpleDocTemplate("checklist.pdf", pagesize=PAGE,
                        leftMargin=11*mm, rightMargin=11*mm, topMargin=12*mm, bottomMargin=12*mm,
                        title="退職で損する人としない人の分かれ目")
CW = doc.width

def step_box(n, txt):
    p = Paragraph(f'<b>{n}.</b>&nbsp;&nbsp;{txt}', stepp)
    t = Table([[p]], colWidths=[CW])
    t.setStyle(TableStyle([
        ("BACKGROUND",(0,0),(-1,-1), colors.HexColor("#F4F7FB")),
        ("LINEBEFORE",(0,0),(0,-1), 2.4, NAVY),
        ("LEFTPADDING",(0,0),(-1,-1),9),("RIGHTPADDING",(0,0),(-1,-1),9),
        ("TOPPADDING",(0,0),(-1,-1),8),("BOTTOMPADDING",(0,0),(-1,-1),8),
    ]))
    return t

def color_box(txt, bg, accent):
    p = Paragraph(txt, boxp)
    t = Table([[p]], colWidths=[CW])
    t.setStyle(TableStyle([
        ("BACKGROUND",(0,0),(-1,-1), bg),
        ("LINEBEFORE",(0,0),(0,-1), 2.4, accent),
        ("LEFTPADDING",(0,0),(-1,-1),10),("RIGHTPADDING",(0,0),(-1,-1),10),
        ("TOPPADDING",(0,0),(-1,-1),9),("BOTTOMPADDING",(0,0),(-1,-1),9),
    ]))
    return t

story = []
title = None
i, n = 0, len(lines)
for l in lines:
    if l.strip().startswith("# "):
        title = l.strip()[2:].strip(); break

# cover
story += [Spacer(1, 38*mm),
          Paragraph("人事10年・何百人の退職を見送ってきた中の人より", cover_kick),
          Spacer(1, 8*mm),
          Paragraph(inl(title), cover_title),
          Spacer(1, 6*mm),
          HRFlowable(width=54, thickness=3, color=NAVY, spaceBefore=2, spaceAfter=10),
          Paragraph("知らないだけで損する側じゃなく、知ってる側でいられるように。", cover_sign),
          PageBreak()]

while i < n:
    s = lines[i].strip()
    if not s:
        i += 1; continue
    if s.startswith("# "):
        i += 1; continue
    if s.startswith("## "):
        story.append(Paragraph(inl(s[3:].strip()), h2))
        story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor("#E3E0D8"), spaceBefore=2, spaceAfter=7))
        i += 1; continue
    if s.startswith("### "):
        story.append(Paragraph(inl(s[4:].strip()), h3)); i += 1; continue
    if s.startswith("---"):
        story.append(HRFlowable(width="100%", thickness=0.7, color=colors.HexColor("#D8D4CB"),
                                dash=(2,2), spaceBefore=12, spaceAfter=12)); i += 1; continue
    if s.startswith(">"):
        q = []
        while i < n and lines[i].strip().startswith(">"):
            q.append(lines[i].strip()[1:].strip()); i += 1
        bodytxt = inl(" ".join(q).strip())
        if "人事の本音" in q[0]:
            story.append(color_box(bodytxt, colors.HexColor("#F1EFEA"), colors.HexColor("#9097A0")))
        else:
            story.append(color_box(bodytxt, colors.HexColor("#E9F5EF"), colors.HexColor("#1D7050")))
        story.append(Spacer(1, 5)); continue
    if re.match(r"^\d+\.\s", s):
        while i < n and re.match(r"^\d+\.\s", lines[i].strip()):
            m = re.match(r"^(\d+)\.\s(.*)", lines[i].strip())
            story.append(step_box(m.group(1), inl(m.group(2))))
            story.append(Spacer(1, 5)); i += 1
        story.append(Spacer(1, 4)); continue
    if s.startswith("- "):
        while i < n and lines[i].strip().startswith("- "):
            item = lines[i].strip()[2:]
            if item.startswith("□"):
                story.append(Paragraph(inl(item), check))
            else:
                story.append(Paragraph(inl(item), li, bulletText="・"))
            i += 1
        story.append(Spacer(1, 5)); continue
    if s == "[[QR]]":
        story.append(Spacer(1, 10))
        try:
            avatar = Image("icon_round.png", width=15*mm, height=15*mm)
        except Exception:
            avatar = Paragraph("", body)
        name_cell = Paragraph(
            '<b>会社に振り回されたくない人事</b><br/><font color="#5A6270" size="10">@jinji_honne</font>',
            ParagraphStyle("nm", fontName=JP, fontSize=11.5, leading=15, textColor=INK))
        head = Table([[avatar, name_cell]], colWidths=[18*mm, CW - 18*mm])
        head.setStyle(TableStyle([
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ("LEFTPADDING", (0, 0), (-1, -1), 0), ("RIGHTPADDING", (0, 0), (-1, -1), 0),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
        ]))
        story.append(head)
        try:
            qr = Image("threads_qr.png", width=30*mm, height=30*mm); qr.hAlign = "CENTER"
            story.append(qr)
        except Exception:
            pass
        story.append(Paragraph(
            '<a href="https://www.threads.com/@jinji_honne"><b><font color="#2C3E50">▶ Threadsでフォローする</font></b></a>'
            '<br/><a href="https://www.threads.com/@jinji_honne"><font color="#5A6270" size="9">www.threads.com/@jinji_honne</font></a>',
            qrcap))
        i += 1; continue
    story.append(Paragraph(inl(s), body)); i += 1

doc.build(story)
print("wrote checklist.pdf")

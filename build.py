#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
人事の本音 プロフィール・リンクページ（ミニLP・エディトリアル調）。
icon256.png を base64 でヒーロー/フッターに埋め込み、単一HTMLで完結。
URLの入れ方：各 <a class="cta"> の href を差し替え。未確定リンクは、その <section> ごと
コメントアウトするか href を "#" のままにする。PR表記はフッターに1回だけ。
"""
import base64, pathlib

here = pathlib.Path(__file__).parent
icon = "data:image/jpeg;base64," + base64.b64encode((here / "icon256.png").read_bytes()).decode()

HTML = """<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>会社に振り回されたくない人事｜退職で損しないために</title>
<meta name="description" content="人事10年・退職を何百件も見送ってきた中の人が、知らないと損する準備を全部置いています。">
<style>
  :root { --ink:#26241E; --ink2:#3D3A31; --mut:#6B665A; --mut2:#8A8578; --line:#E6E1D5; --bg:#F7F5F0; --accent:#9A7B55; --icon:#3A4A63; }
  * { box-sizing:border-box; margin:0; padding:0; }
  body { background:var(--bg); color:var(--ink); font-family:system-ui,-apple-system,"Hiragino Sans","Noto Sans JP",sans-serif; -webkit-font-smoothing:antialiased; }
  .wrap { max-width:440px; margin:0 auto; }
  .hero { text-align:center; padding:40px 28px 30px; }
  .hero img { width:66px; height:66px; border-radius:50%; object-fit:cover; }
  .hero .kicker { font-size:11px; letter-spacing:2.5px; color:var(--mut2); margin:16px 0 14px; }
  .hero h1 { font-size:27px; line-height:1.5; font-weight:600; letter-spacing:.5px; color:var(--ink); margin:0 0 14px; }
  .hero h1 .thin { font-weight:300; }
  .hero p { font-size:13px; line-height:1.9; color:var(--mut); }
  .hero .met { font-size:11px; color:#A39D8E; margin-top:18px; letter-spacing:.5px; }
  .rule { width:28px; height:1px; background:#C9C3B4; margin:26px auto; }
  .sec { padding:6px 28px 36px; }
  .eyebrow { font-size:11px; letter-spacing:2px; color:var(--accent); margin-bottom:10px; }
  .eyebrow .no { color:#C9C3B4; margin-right:8px; }
  .sec h2 { font-size:21px; font-weight:700; letter-spacing:.5px; color:#14120C; margin:0 0 8px; }
  .sec .sub { font-size:13px; line-height:1.85; color:var(--mut); margin:0 0 18px; }
  .list { margin:0 0 20px; }
  .li { display:flex; align-items:center; gap:13px; padding:13px 2px; border-top:1px solid var(--line); }
  .li:last-child { border-bottom:1px solid var(--line); }
  .li svg { flex:none; stroke:var(--icon); }
  .li .t { font-size:13.5px; color:var(--ink2); letter-spacing:.3px; }
  .flow { display:flex; align-items:stretch; margin:4px 0 20px; }
  .flow .fb { flex:1; text-align:center; padding:14px 8px; font-size:12px; line-height:1.5; color:var(--ink2); }
  .flow .fb .n { display:block; font-size:10px; letter-spacing:1px; color:#B3AC9B; margin-bottom:5px; }
  .flow .sp { flex:none; width:1px; background:var(--line); }
  .who { font-size:12.5px; color:var(--mut); margin:0 0 16px; padding-left:12px; border-left:2px solid #C9C3B4; line-height:1.7; }
  .cta { display:block; text-align:center; text-decoration:none; background:var(--ink); color:var(--bg); border-radius:2px; padding:16px; font-size:14.5px; font-weight:600; letter-spacing:1px; }
  .cta.ghost { background:transparent; color:var(--ink); border:1px solid var(--ink); }
  .cta .s { display:block; font-size:11px; font-weight:400; letter-spacing:.3px; margin-top:5px; opacity:.72; }
  .secline { height:1px; background:var(--line); margin:0 28px; }
  .foot { text-align:center; padding:34px 28px 40px; margin-top:6px; border-top:1px solid var(--line); }
  .foot img { width:52px; height:52px; border-radius:50%; object-fit:cover; }
  .foot .nm { font-size:14px; font-weight:600; margin-top:10px; }
  .foot .hd { font-size:11.5px; color:var(--mut2); letter-spacing:.5px; }
  .foot p { font-size:12.5px; line-height:1.85; color:var(--mut); margin:14px 0 18px; }
  .foot .prnote { font-size:10.5px; color:#A39D8E; margin-top:22px; letter-spacing:.3px; }
</style>
</head>
<body>
<main class="wrap">

  <header class="hero">
    <img src="__ICON__" alt="会社に振り回されたくない人事">
    <div class="kicker">中堅企業の人事 ・ 10年</div>
    <h1><span class="thin">辞める前に、</span><br>これだけは。</h1>
    <p>退職を何百件も見送ってきた中の人が、<br>「知らないと損する準備」を全部置いています。</p>
    <div class="met">— 採用の面接も、退職の手続きも —</div>
  </header>

  <div class="rule"></div>

  <!-- 01 無料PDF -->
  <section class="sec">
    <div class="eyebrow"><span class="no">01</span>まず、無料でこれを</div>
    <h2>退職まるごとチェックリスト</h2>
    <p class="sub">辞めた後のお金の手続きを、いつ・何をするかの手順で。保存版チェックリスト付き。</p>
    <div class="list">
      <div class="li"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke-width="1.6"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg><span class="t">20日・14日の期限まわり</span></div>
      <div class="li"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke-width="1.6"><path d="M12 3v18M7 8h7a2 2 0 010 4H8a2 2 0 000 4h8"/></svg><span class="t">戻ってくるお金・還付申告</span></div>
      <div class="li"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke-width="1.6"><rect x="4" y="4" width="16" height="16" rx="1.5"/><path d="M8 9h8M8 13h5"/></svg><span class="t">退職金の税金・控除</span></div>
      <div class="li"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke-width="1.6"><path d="M20 6L9 17l-5-5"/></svg><span class="t">やることチェックリスト</span></div>
    </div>
    <div class="who">辞めるか迷っている／損したくない、すべての人へ。</div>
    <a class="cta" href="checklist.pdf" target="_blank" rel="noopener">無料で受け取る<span class="s">辞める前でも、見ておくだけで損を防げます</span></a>
  </section>

  <div class="secline"></div>

  <!-- 02 退職代行（もしも・弁護士ガイア） -->
  <section class="sec">
    <div class="eyebrow"><span class="no">02</span>言い出せなくて、しんどいなら</div>
    <h2>弁護士の退職代行</h2>
    <div class="flow">
      <div class="fb"><span class="n">NOW</span>言い出せない<br>もう限界</div>
      <div class="sp"></div>
      <div class="fb"><span class="n">DAY 1</span>弁護士が<br>会社に伝える</div>
      <div class="sp"></div>
      <div class="fb"><span class="n">DONE</span>もう<br>行かなくていい</div>
    </div>
    <div class="who">引き止めが強い／自分ではもう言えない人へ。</div>
    <a class="cta ghost" href="http://msm.to/BarmIR4" target="_blank" rel="noopener sponsored">無料で相談してみる<span class="s">相談だけでもOK・使うかは後で決めていい</span></a>
  </section>

  <div class="secline"></div>

  <!-- 03 転職エージェント（A8・転職AGENT Navi） -->
  <section class="sec">
    <div class="eyebrow"><span class="no">03</span>次に、受かる側へ</div>
    <h2>自分に合う転職エージェント</h2>
    <p class="sub">焦って一社目に飛びつく前に。合うエージェントを、プロが選んで紹介してくれます。</p>
    <div class="list">
      <div class="li"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke-width="1.6"><circle cx="8" cy="9" r="2.5"/><circle cx="16" cy="9" r="2.5"/><path d="M4 18c0-2.2 1.8-3.5 4-3.5M20 18c0-2.2-1.8-3.5-4-3.5"/></svg><span class="t">プロが複数社から選んで紹介</span></div>
      <div class="li"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke-width="1.6"><path d="M3 12h4l2-7 4 14 2-7h4"/></svg><span class="t">非公開の求人も見られる</span></div>
      <div class="li"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke-width="1.6"><path d="M5 4h11l3 3v13H5z"/><path d="M9 12h6M9 16h4"/></svg><span class="t">職務経歴書の添削も無料</span></div>
    </div>
    <div class="who">焦って一社目に飛びつきたくない人へ。</div>
    <a class="cta ghost" href="https://px.a8.net/svt/ejp?a8mat=4B67CH+FNTMII+5BJK+5Z6WY" target="_blank" rel="noopener sponsored">無料で相談する<span class="s">相場も、受かる書類の型も、先に知っておける</span></a>
  </section>

  <div class="secline"></div>

  <!-- 04 20代の転職相談所（A8） -->
  <section class="sec">
    <div class="eyebrow"><span class="no">04</span>20代・第二新卒の方へ</div>
    <h2>20代の転職相談所</h2>
    <p class="sub">適性や転職の緊急度を、無料で診断。20代専門の相談コースがあります。</p>
    <div class="list">
      <div class="li"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke-width="1.6"><path d="M12 3a9 9 0 100 18 9 9 0 000-18z"/><path d="M12 8v4l2 2"/></svg><span class="t">適性・転職の緊急度を無料診断</span></div>
      <div class="li"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke-width="1.6"><path d="M12 14l8-4-8-4-8 4 8 4z"/><path d="M6 11v4c0 1.5 3 2.5 6 2.5s6-1 6-2.5v-4"/></svg><span class="t">20代専門の相談コース</span></div>
      <div class="li"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke-width="1.6"><path d="M4 6h16M4 12h16M4 18h10"/></svg><span class="t">非公開求人への応募も可能</span></div>
    </div>
    <div class="who">20代・第二新卒で、今の会社が合わないと感じる人へ。</div>
    <a class="cta ghost" href="https://px.a8.net/svt/ejp?a8mat=4B67CI+758T6+10SQ+C4DVL" target="_blank" rel="noopener sponsored">適性を無料で診断する<span class="s">まず自分の市場価値と方向性を知るところから</span></a>
  </section>

  <footer class="foot">
    <img src="__ICON__" alt="">
    <div class="nm">会社に振り回されたくない人事</div>
    <div class="hd">@jinji_honne</div>
    <p>退職のときだけじゃなく、在職中も「知らないと損」は毎日あります。その都度、知ってる側でいられるように、中の人目線でThreadsに置いています。</p>
    <a class="cta" href="https://www.threads.com/@jinji_honne" target="_blank" rel="noopener">Threadsでフォローする</a>
    <div class="prnote">本ページはアフィリエイト広告（PR）を含みます。</div>
  </footer>

</main>
</body>
</html>
"""

out = here / "index.html"
out.write_text(HTML.replace("__ICON__", icon), encoding="utf-8")
print("wrote", out, f"({out.stat().st_size//1024} KB)")

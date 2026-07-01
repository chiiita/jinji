#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
人事の本音 リンク集約ページ ビルダー。
icon256.png を base64 で index.html に埋め込み、単一ファイルで完結させる。
（GitHub Pages へは index.html 1枚を置けばよい／file:// 直開きでも表示可）

URL の入れ方：
  各ボタンの href="#" を、確定したリンクURL（lit.link不要・直接でOK）に差し替える。
  まだURLが無いボタンは、その <a> タグに hidden を付ければ非表示になる（死リンク防止）。
"""
import base64, pathlib

here = pathlib.Path(__file__).parent
icon_b64 = base64.b64encode((here / "icon256.png").read_bytes()).decode()
icon_uri = f"data:image/png;base64,{icon_b64}"

HTML = """<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>会社に振り回されたくない人事｜リンク集</title>
<meta name="description" content="人事10年。退職で損しない準備と、次に受かる側の話を、中の人目線で。">
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body {
    font-family: system-ui, -apple-system, "Hiragino Sans", "Noto Sans JP", sans-serif;
    background: #FBFAF7;
    color: #1F2933;
    line-height: 1.6;
    -webkit-font-smoothing: antialiased;
    padding: 32px 18px 48px;
    display: flex;
    justify-content: center;
  }
  .wrap { width: 100%; max-width: 460px; }
  .head { text-align: center; padding: 8px 0 22px; }
  .avatar {
    width: 96px; height: 96px; border-radius: 50%;
    object-fit: cover; display: block; margin: 0 auto 14px;
    border: 3px solid #fff; box-shadow: 0 2px 10px rgba(44,62,80,.12);
  }
  .name { font-size: 18px; font-weight: 600; color: #1F2933; }
  .bio { font-size: 13px; color: #6B7280; margin-top: 8px; line-height: 1.75; }

  .btn {
    display: block; text-decoration: none; color: inherit;
    background: #fff; border: 1px solid #ECE9E2; border-radius: 14px;
    padding: 15px 17px; margin-bottom: 13px;
    transition: transform .12s ease, border-color .12s ease, box-shadow .12s ease;
  }
  .btn[hidden] { display: none; }
  .btn:hover { transform: translateY(-1px); border-color: #D8D4CB; box-shadow: 0 3px 12px rgba(44,62,80,.08); }
  .btn.primary { border: 2px solid #2C3E50; }
  .btn-top { display: flex; align-items: center; justify-content: space-between; gap: 10px; }
  .btn-title { font-size: 15px; font-weight: 600; color: #1F2933; }
  .btn-desc { font-size: 12.5px; color: #6B7280; margin-top: 5px; }

  .badge-free {
    flex: none; font-size: 11px; font-weight: 600; color: #1D7050;
    background: #E1F5EE; padding: 3px 9px; border-radius: 999px;
  }
  .badge-pr {
    flex: none; font-size: 10px; font-weight: 600; color: #8A8F98;
    border: 1px solid #CDD1D7; padding: 1px 6px; border-radius: 5px; letter-spacing: .5px;
  }

  .foot { text-align: center; margin-top: 22px; }
  .foot a {
    font-size: 13px; color: #2C3E50; text-decoration: none; font-weight: 500;
    display: inline-flex; align-items: center; gap: 6px;
  }
  .foot a:hover { text-decoration: underline; }
  .note { text-align: center; font-size: 11px; color: #A2A6AD; margin-top: 16px; line-height: 1.7; }
</style>
</head>
<body>
  <main class="wrap">
    <div class="head">
      <img class="avatar" src="__ICON__" alt="会社に振り回されたくない人事">
      <div class="name">会社に振り回されたくない人事</div>
      <div class="bio">人事10年、何百人の退職を見送ってきました。<br>退職で損しない準備と、次に受かる側の話を、中の人目線で。</div>
    </div>

    <!-- ①無料PDFチェックリスト（最上段・唯一PRなし）／同リポジトリの checklist.pdf -->
    <a class="btn primary" href="checklist.pdf" target="_blank" rel="noopener" data-link="pdf">
      <div class="btn-top">
        <span class="btn-title">退職まるごとチェックリスト</span>
        <span class="badge-free">無料</span>
      </div>
      <div class="btn-desc">健康保険・年金・住民税・傷病手当・戻る税金…辞めた後のお金を「いつ・何をするか」の手順で。全8ページ。</div>
    </a>

    <!-- ②退職代行【PR】／もしも 弁護士法人ガイア（退職代行・成果14000円・弁護士型・SNS OK・どこでもリンク） -->
    <a class="btn" href="http://msm.to/BarmIR4" target="_blank" rel="noopener sponsored" data-link="taishoku_daiko">
      <div class="btn-top">
        <span class="btn-title">言い出しづらい人の選択肢｜退職代行</span>
        <span class="badge-pr">PR</span>
      </div>
      <div class="btn-desc">消耗して辞めそうな人へ。合う人には、逃げ道があります。</div>
    </a>

    <!-- ③転職エージェント【PR】／A8 転職AGENT Navi（circus）成果=無料相談登録 -->
    <a class="btn" href="https://px.a8.net/svt/ejp?a8mat=4B67CH+FNTMII+5BJK+5Z6WY" target="_blank" rel="noopener sponsored" data-link="tenshoku_agent">
      <div class="btn-top">
        <span class="btn-title">次に受かる側へ｜自分に合う転職エージェント</span>
        <span class="badge-pr">PR</span>
      </div>
      <div class="btn-desc">焦って一社目に飛びつく前に。合うエージェントをプロが紹介。（無料相談）</div>
    </a>

    <!-- ③b 20代の転職相談所【PR】／A8 ブラッシュアップ・ジャパン（20代・第二新卒特化・成果5000円） -->
    <a class="btn" href="https://px.a8.net/svt/ejp?a8mat=4B67CI+758T6+10SQ+C4DVL" target="_blank" rel="noopener sponsored" data-link="tenshoku_agent_20s">
      <div class="btn-top">
        <span class="btn-title">20代・第二新卒の方はこちら｜転職相談所</span>
        <span class="badge-pr">PR</span>
      </div>
      <div class="btn-desc">適性や転職の緊急度を無料で診断。20代専門の相談コース。</div>
    </a>

    <!-- ④転職サイト【PR】／A8 審査後に href を差し替え。URL未確定のため hidden で非表示 -->
    <a class="btn" hidden href="#" data-link="tenshoku_site">
      <div class="btn-top">
        <span class="btn-title">求人だけ先に見る｜転職サイト</span>
        <span class="badge-pr">PR</span>
      </div>
      <div class="btn-desc">下見しておくと、心の余裕が変わります。</div>
    </a>

    <div class="foot">
      <a href="https://www.threads.com/@jinji_honne" target="_blank" rel="noopener">@jinji_honne ・ Threadsはこちら</a>
    </div>
    <div class="note">【PR】の表記はアフィリエイト広告（広告主との提携）を含みます。</div>
  </main>
</body>
</html>
"""

out = here / "index.html"
out.write_text(HTML.replace("__ICON__", icon_uri), encoding="utf-8")
print("wrote", out, f"({out.stat().st_size//1024} KB)")

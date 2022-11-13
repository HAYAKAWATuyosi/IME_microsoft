
# Table of Contents

1.  [大まかな手順](#org82f425f)
2.  [リモートリポジトリの作成](#org5144692)
3.  [IME辞書の登録](#org21bb91e)
4.  [辞書のエクスポート](#org3b232ac)
5.  [ローカルリポジトリの作成](#org9d4ddda)
6.  [プッシュ](#org35a786a)
7.  [クローン](#orga32736a)
8.  [IME辞書のインポート](#org2062409)


<a id="org82f425f"></a>

# 大まかな手順

<table border="1" cellspacing="0" cellpadding="6" rules="all" frame="border">


<colgroup>
<col  class="org-right" />

<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />
</colgroup>
<tbody>
<tr>
<td class="org-right">順番</td>
<td class="org-left">操作対象</td>
<td class="org-left">操作の概要</td>
<td class="org-left">操作の詳細</td>
</tr>


<tr>
<td class="org-right">1</td>
<td class="org-left">github.com</td>
<td class="org-left">リモートリポジトリの作成</td>
<td class="org-left">github.com上にリモートリポジトリを作る。</td>
</tr>


<tr>
<td class="org-right">2</td>
<td class="org-left">手元のPCて</td>
<td class="org-left">IME辞書の登録</td>
<td class="org-left">IMEの辞書に短縮よみなどを登録する。</td>
</tr>


<tr>
<td class="org-right">3</td>
<td class="org-left">手元のPC</td>
<td class="org-left">辞書のエクスポート</td>
<td class="org-left">IMEの辞書をエクスポートする。</td>
</tr>


<tr>
<td class="org-right">4</td>
<td class="org-left">手元のPC</td>
<td class="org-left">ローカルリポジトリの作成</td>
<td class="org-left">IMEの辞書をエクスポートした宛て先のフォルダをgitのローカルリポジトリにする。</td>
</tr>


<tr>
<td class="org-right">5</td>
<td class="org-left">手元のPC</td>
<td class="org-left">プッシュ</td>
<td class="org-left">エクスポートされたIMEの辞書をgithub.com（リモートレポジトリ）へプッシュする。</td>
</tr>


<tr>
<td class="org-right">6</td>
<td class="org-left">別のPC</td>
<td class="org-left">クローン</td>
<td class="org-left">リモートリポジトリからローカルリポジトリへクローンする。</td>
</tr>


<tr>
<td class="org-right">7</td>
<td class="org-left">別のPC</td>
<td class="org-left">IME辞書のインポート</td>
<td class="org-left">IMEの辞書をインポートする。</td>
</tr>
</tbody>
</table>


<a id="org5144692"></a>

# リモートリポジトリの作成

github.com上にリモートリポジトリを作ります。

1.  github.com を開き、右上のメニューから"New repository"を選択します。
    -   <a href="./images/01-GITHUB_create-new-repository_1-starting.png"><img src="./images/thumbnails/01-GITHUB_create-new-repository_1-starting.png"></a>
2.  リポジトリ名を入力し、"Private"を選択します。下の方の設定はお好みで。
    -   <a href="./images/02-GITHUB_create-new-repository_2-editing.png"><img src="./images/thumbnails/02-GITHUB_create-new-repository_2-editing.png"></a>
3.  "Create repository"をクリックするとリポジトリが作成され、セットアップ方法の画面へ遷移します。
    -   <a href="./images/03-GITHUB_create-new-repository_3-created.png"><img src="./images/thumbnails/03-GITHUB_create-new-repository_3-created.png"></a>


<a id="org21bb91e"></a>

# IME辞書の登録

-   もしIMEの辞書がまだ登録されていなければ、短縮よみなどを、何か登録してみてください。
    -   なにかしら登録してあれば、[次の辞書のエクスポート](#org3b232ac)までスキップしてください。
-   gitで扱うファイルはIMEの辞書でなくても構いません。その場合には、以降の手順を適宜読み替えてください。

-   『Microsoft IME ユーザー辞書ツール』の ツールバーから 編集(E) &#x2013;> 新規登録(A) と選択してください。
    -   <a href="./images/04-IME_add-new-item-to-dictionary_1-starting.png"><img src="./images/thumbnails/04-IME_add-new-item-to-dictionary_1-starting.png"></a>
-   短縮よみなどを、何か登録してみてください。
    -   <a href="./images/05-IME_add-new-item-to-dictionary_2-editing.png"><img src="./images/thumbnails/05-IME_add-new-item-to-dictionary_2-editing.png"></a>
-   追加されたアイテムが上から2行目に表示されています。
    -   <a href="./images/06-IME_add-new-item-to-dictionary_3-added.png"><img src="./images/thumbnails/06-IME_add-new-item-to-dictionary_3-added.png"></a>


<a id="org3b232ac"></a>

# 辞書のエクスポート

IMEの辞書をエクスポートします。

1.  『Microsoft IME ユーザー辞書ツール』の ツールバーから ツール(T) &#x2013;> 一覧の出力(P) と選択してください。
    -   <a href="./images/07-IME_export-dictionary_1-starting.png"><img src="./images/thumbnails/07-IME_export-dictionary_1-starting.png"></a>
2.  出力先のパス（フォルダ および ファイル名）を指定します。
    -   出力先のフォルダ も ファイル名も、デフォルト値から変えてしまっても全く問題ありません。
    -   僕は以下のパスにしました。
        -   c:\work\tools\IME\_microsoft\dict.txt
    -   <a href="./images/08-IME_export-dictionary_2-exporting.png"><img src="./images/thumbnails/08-IME_export-dictionary_2-exporting.png"></a>
3.  エクスポートが完了するとポップアップが出ますので、"終了"をクリックして閉じます。
    -   <a href="./images/09-IME_export-dictionary_3-exported.png"><img src="./images/thumbnails/09-IME_export-dictionary_3-exported.png"></a>


<a id="org9d4ddda"></a>

# ローカルリポジトリの作成

IMEの辞書をエクスポートした先のフォルダを
最初の手順で作ったリモートリポジトリに紐づけることで、
そのフォルダをローカルリポジトリにします。

1.  リモートリポジトリ作成後に遷移した画面の "&#x2026;or create a new repository on the command line" の部分に記されているコマンド群をコピーします。
    -   "echo" から "git push &#x2026;" までの7つコマンドを全てコピーします。
    -   画像下部の右端に描画されている、正方形が2つ重なっているアイコンをクリックすると、7つコマンドが全てコピーされます。
    -   <a href="./images/10-GIT_initialize-local-repository-1-copying-commands.png"><img src="./images/thumbnails/10-GIT_initialize-local-repository-1-copying-commands.png"></a>
2.  コピーされたコマンドを順に実行します。
    -   以下のスクリーンショットでは、お行儀よく、1行ずつ貼り付けて実行していますが、一括して貼り付けてしまっても、シェルが、順次、実行してくれるはずです。
    -   <a href="./images/11-GIT_initialize-local-repository-2-initializing.png"><img src="./images/thumbnails/11-GIT_initialize-local-repository-2-initializing.png"></a>


<a id="org35a786a"></a>

# プッシュ

エクスポートされたIMEの辞書をgithub.com上のリモートリポジトリへプッシュします。

1.  上の直近のコマンドだけでは、IMEの辞書はリモートレポジトリにまだプッシュされていませんので、ローカルレポジトリ および リモートレポジトリの操作をして、プッシュしていきます。
    -   コマンドは以下の通り
        1.  エクスポート先のフォルダに移動する。
        2.  git add ./dict.txt
            -   必須
        3.  git status
            -   オプション
            -   IMEの辞書が staged されていることを確認します。
        4.  git commit -m "&#x2026;"
            -   必須
            -   IMEの辞書をローカルリポジトリにコミットします。
        5.  git push
            -   必須
            -   IMEの辞書をリモートリポジトリにプッシュします。
        6.  git status
            -   オプション
            -   IMEの辞書がプッシュされたので、ローカルリポジトリがリモートリポジトリの最新状況と同期していることを確認します。
    -   <a href="./images/12-GIT_push-exported-dictionary_1-adding-and-pushing.png"><img src="./images/thumbnails/12-GIT_push-exported-dictionary_1-adding-and-pushing.png"></a>
2.  リモートリポジトリにプッシュされた様子
    -   <a href="./images/13-GIT_push-exported-dictionary_2-on-github-after-pushed.png"><img src="./images/thumbnails/13-GIT_push-exported-dictionary_2-on-github-after-pushed.png"></a>
3.  コミット履歴にも反映されています。
    -   <a href="./images/14-GIT_push-exported-dictionary_3-history-of-commits.png"><img src="./images/thumbnails/14-GIT_push-exported-dictionary_3-history-of-commits.png"></a>


<a id="orga32736a"></a>

# クローン

github.com上のリモートリポジトリからローカルリポジトリへ、
IMEの辞書ファイルをクローンします。

<p class="verse">
ここまでの操作を会社で行ったならば、以後の操作はご自宅で行ってください。<br />
または逆に、ここまでがご自宅でならば、以後は会社にて。<br />
<br />
掲載されているスクリーンショットは、資料作成の便益のために、ここまでの操作も以後の操作も、両方とも、拙宅で行った様子です。<br />
そのため、以下のどちらかの状況だと読み替えながら、お読みください。<br />
</p>

<table border="1" cellspacing="0" cellpadding="6" rules="all" frame="border">


<colgroup>
<col  class="org-left" />

<col  class="org-left" />
</colgroup>
<tbody>
<tr>
<td class="org-left">パス</td>
<td class="org-left">ローカルリポジトリの所在地</td>
</tr>


<tr>
<td class="org-left"><i>mnt/c/work/tools/IME_microsoft</i></td>
<td class="org-left">会社</td>
</tr>


<tr>
<td class="org-left"><i>mnt/c/work/junk/IME_microsoft_CLONED</i></td>
<td class="org-left">自宅</td>
</tr>
</tbody>
</table>

<table border="1" cellspacing="0" cellpadding="6" rules="all" frame="border">


<colgroup>
<col  class="org-left" />

<col  class="org-left" />
</colgroup>
<tbody>
<tr>
<td class="org-left">パス</td>
<td class="org-left">ローカルリポジトリの所在地</td>
</tr>


<tr>
<td class="org-left"><i>mnt/c/work/tools/IME_microsoft</i></td>
<td class="org-left">自宅</td>
</tr>


<tr>
<td class="org-left"><i>mnt/c/work/junk/IME_microsoft_CLONED</i></td>
<td class="org-left">会社</td>
</tr>
</tbody>
</table>

1.  github.com の リポートリポジトリからURLをコピーします。
    -   <a href="./images/15-GIT_clone-another-local-repository_1-copying-URL.png"><img src="./images/thumbnails/15-GIT_clone-another-local-repository_1-copying-URL.png"></a>
2.  クローン先となるフォルダにて以下のコマンドを実行します。

        git clone 【コピーしたURL】 ./

    -   空（から）フォルダにて実行することをおすすめします。
    -   <a href="./images/16-GIT_clone-another-local-repository_2-cloning.png"><img src="./images/thumbnails/16-GIT_clone-another-local-repository_2-cloning.png"></a>


<a id="org2062409"></a>

# IME辞書のインポート

-   github.com の リモートリポジトリからクローンされたIMEの辞書ファイルを『Microsoft IME ユーザー辞書ツール』へインポートしてみます。
-   ここでは分かり易くするために、アイテムが一つも登録されていない状態に辞書をインポートしてみます。

1.  ツールバーから ツール(T) &#x2013;> テキストファイルからの登録(T) と選択してください。
    -   <span style="background-color: black;color:  red"> 注意: このとき誤って最下段の "テキストファイルで削除(D)" を選択してしまうと、『Microsoft IME ユーザー辞書ツール』に登録済みのアイテムが削除されてしまうので、お気を付けください。</span>
    -   <a href="./images/17-IME_import-dictionary_1-starting.png"><img src="./images/thumbnails/17-IME_import-dictionary_1-starting.png"></a>
2.  github.comからクローンしたファイルを選択します。
    -   <a href="./images/18-IME_import-dictionary_2-selecting-exported-file.png"><img src="./images/thumbnails/18-IME_import-dictionary_2-selecting-exported-file.png"></a>
3.  インポート完了するとポップアップが出ますので、"終了"をクリックして閉じます。
    -   <a href="./images/19-IME_import-dictionary_3-popup-after-importing.png"><img src="./images/thumbnails/19-IME_import-dictionary_3-popup-after-importing.png"></a>
4.  無事に20個のアイテムがインポートされました。
    -   もちろん、始めのほうの手順で登録した"いじしつ"の短縮よみもインポートされています。
    -   <a href="./images/20-IME_import-dictionary_4-imported.png"><img src="./images/thumbnails/20-IME_import-dictionary_4-imported.png"></a>

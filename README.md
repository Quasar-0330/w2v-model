# w2v-model
ラズパイで作成したWord2Vecのモデルとモデル作成プログラム。

# Requirements
* gensim

# Usage
### モデルの読み込み

* `python`
* `from gensim.models import word2vec`
* `model = word2vec.Word2Vec.load("w2v.model").wv`

### 単語をベクトル化

* `model["<ベクトルにしたい英単語>"]`

### 単語同士がどのくらい似ているか

* `model.similarity("<英単語>", "<比べたい英単語>")`

### 似ている単語

* `model.most_similar(positive=["<調べたい英単語>"])`

### 最も遠い単語

* `medel.most_similar(negative=["<調べたい英単語>"])`

### 単語の計算

##### 引き算

* `model.most_similar(positive=["<単語>"], negative=["<引きたい英単語>"])`

##### 足し算

* `model.most_similar(positive=["英単語", "足したい英単語"])`

##### 例
##### 王 - 男 ＋ 女 = ?

* `model.most_similar(positive=["king", "woman"], negative=["man"])`

### モデル作成
##### 学習用テキスト用意

このサイトがわかりやすい
https://note.com/npaka/n/n30a0cef78f42

また、上のサイトで作成したテキストから以下のコマンド
を実行し、ドットやカンマを消去すると正確になる。(apple. やapple, を一単語として認識するのを防ぐ)

* `sed -i 's/\.//g' wiki.txt`
* `sed -i 's/,//g' wiki.txt`

LinuxのコマンドなのでWindowsとMacの場合は知らない。

##### モデル作成プログラム実行

学習用テキスト(wiki.txt)と**make-model.py**を同じディレクトリに置いて以下のコマンドで作成できる。

* `python make-model.py`

学習用テキストはファイル名が違うと出来ないから注意、ちゃんとwiki.txtにしてね。ファイル名にこだわりが有る変な人はプログラムファイルを開いて6行目のwiki.txtの部分を書き換えてね。

**make-model.py**の7行目を編集すると次元数が増えたりして正確になるけどメモリ使用量がヤバいことになるので注意、メモリ足りなくて固まった時とかは編集すると動くようになるよ。詳しくはggrks

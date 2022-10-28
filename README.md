# w2v-model
ラズパイで作成したWord2Vecのモデルとモデル作成プログラム。

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

### 例

##### 王 - 男 ＋ 女 = ?

* `model.most_similar(positive=["king", "woman"], negative=["man"])`

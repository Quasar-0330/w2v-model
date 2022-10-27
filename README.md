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

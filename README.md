# calc_distance

## Usage

python calc_distance.py points1.csv points2.csv

## 注意事項

CSVファイルはUTF-8で保存して下さい。

CSVファイルには以下のヘッダーの列を持つ必要があります。

* ID
* Latitude
* Longitude

points1とpoints2の距離をVincenty法で算出し、最も近いIDとそこまでの距離を新規列として追加します。

## TODO

* 照合する座標を近傍の座標に限定する


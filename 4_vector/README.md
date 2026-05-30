# ベクトルの演算

## ベクトル間の演算

### 内積 / ドット積 (Inner Product / Dot Product)

2つのベクトル $\mathbf{a} = (a_1, a_2, \ldots, a_n)$、$\mathbf{b} = (b_1, b_2, \ldots, b_n)$ に対して、内積はスカラー値を返す演算。

$$\mathbf{a} \cdot \mathbf{b} = \sum_{i=1}^{n} a_i b_i $$

幾何学的には、ベクトルのなす角 $\theta$ を用いて次のように表せる。

$$\mathbf{a} \cdot \mathbf{b} = |\mathbf{a}||\mathbf{b}|\cos\theta$$

**性質:**
- 交換則: $\mathbf{a} \cdot \mathbf{b} = \mathbf{b} \cdot \mathbf{a}$
- 分配則: $\mathbf{a} \cdot (\mathbf{b} + \mathbf{c}) = \mathbf{a} \cdot \mathbf{b} + \mathbf{a} \cdot \mathbf{c}$
- $\mathbf{a} \perp \mathbf{b} \iff \mathbf{a} \cdot \mathbf{b} = 0$

---

### クロス積 (Cross Product)

しばし、外積 (Outer Product)とも呼ばれる。テンソル積も外積と呼ぶことがあるので、注意が必要。

3次元ベクトル $\mathbf{a} = (a_1, a_2, a_3)$、$\mathbf{b} = (b_1, b_2, b_3)$ に対して定義される演算で、結果は両ベクトルに直交するベクトルになる。

$$\mathbf{a} \times \mathbf{b} = \begin{vmatrix} \mathbf{e}_1 & \mathbf{e}_2 & \mathbf{e}_3 \\ a_1 & a_2 & a_3 \\ b_1 & b_2 & b_3 \end{vmatrix} = (a_2 b_3 - a_3 b_2,\ a_3 b_1 - a_1 b_3,\ a_1 b_2 - a_2 b_1)$$

大きさはなす角 $\theta$ を用いて次のように表せる（平行四辺形の面積に等しい）。

$$|\mathbf{a} \times \mathbf{b}| = |\mathbf{a}||\mathbf{b}|\sin\theta$$

**性質:**
- 反交換則: $\mathbf{a} \times \mathbf{b} = -(\mathbf{b} \times \mathbf{a})$
- 分配則: $\mathbf{a} \times (\mathbf{b} + \mathbf{c}) = \mathbf{a} \times \mathbf{b} + \mathbf{a} \times \mathbf{c}$
- $\mathbf{a} \parallel \mathbf{b} \iff \mathbf{a} \times \mathbf{b} = \mathbf{0}$
- 3次元にのみ定義される（7次元への拡張は存在するが一般的でない）

---

### テンソル積 / 直積 (Tensor Product / Direct Sum)

しばし、外積 (Outer Product)とも呼ばれる。テンソル積も外積と呼ぶことがあるので、注意が必要。
集合論における直積 (direct Product) と類似していることから、同様に直積とも呼ばれる。


ベクトル $\mathbf{a} \in \mathbb{R}^m$、$\mathbf{b} \in \mathbb{R}^n$ に対して、結果は $m \times n$ 行列（ランク1テンソル）になる演算。外積 (outer product) とも呼ばれる。

$$\mathbf{a} \otimes \mathbf{b} = \mathbf{a}\mathbf{b}^\top = \begin{pmatrix} a_1 b_1 & a_1 b_2 & \cdots & a_1 b_n \\ a_2 b_1 & a_2 b_2 & \cdots & a_2 b_n \\ \vdots & \vdots & \ddots & \vdots \\ a_m b_1 & a_m b_2 & \cdots & a_m b_n \end{pmatrix}$$

成分表示: $(\mathbf{a} \otimes \mathbf{b})_{ij} = a_i b_j$

**性質:**
- 非可換: $\mathbf{a} \otimes \mathbf{b} \neq \mathbf{b} \otimes \mathbf{a}$（形も異なりうる）
- 双線形: $(\mathbf{a} + \mathbf{b}) \otimes \mathbf{c} = \mathbf{a} \otimes \mathbf{c} + \mathbf{b} \otimes \mathbf{c}$
- 結果は常にランク1行列
- 内積との関係: $\mathbf{a} \cdot \mathbf{b} = \mathrm{tr}(\mathbf{a} \otimes \mathbf{b})$（$m = n$ のとき）

---

### 直和 (Direct Sum)

ベクトル $\mathbf{a} \in \mathbb{R}^m$、$\mathbf{b} \in \mathbb{R}^n$ を連結して $\mathbb{R}^{m+n}$ のベクトルを作る演算。

$$\mathbf{a} \oplus \mathbf{b} = \begin{pmatrix} \mathbf{a} \\ \mathbf{b} \end{pmatrix} = (a_1, \ldots, a_m, b_1, \ldots, b_n)$$

集合論の直和 $\mathbb{R}^m \times \mathbb{R}^n \cong \mathbb{R}^{m+n}$ に対応しており、テンソル積の「掛け合わせ」に対して直和は「並べる」操作に相当する。

行列の文脈では、対角ブロック行列として拡張される。

$$A \oplus B = \begin{pmatrix} A & 0 \\ 0 & B \end{pmatrix}$$

**性質:**
- 交換則は成立しない: $\mathbf{a} \oplus \mathbf{b} \neq \mathbf{b} \oplus \mathbf{a}$（次元が同じでも順序が異なる）
- 結合則: $(\mathbf{a} \oplus \mathbf{b}) \oplus \mathbf{c} = \mathbf{a} \oplus (\mathbf{b} \oplus \mathbf{c})$
- 次元の加法性: $\dim(\mathbf{a} \oplus \mathbf{b}) = \dim(\mathbf{a}) + \dim(\mathbf{b})$
- テンソル積との対比: $\dim(\mathbf{a} \otimes \mathbf{b}) = \dim(\mathbf{a}) \times \dim(\mathbf{b})$

---

### アダマール積 (Hadamard Product)

要素ごとの積 (element-wise product) とも呼ばれる。同次元のベクトル $\mathbf{a} = (a_1, a_2, \ldots, a_n)$、$\mathbf{b} = (b_1, b_2, \ldots, b_n)$ に対して、対応する要素どうしの積をとる演算。

$$\mathbf{a} \odot \mathbf{b} = (a_1 b_1,\ a_2 b_2,\ \ldots,\ a_n b_n)$$

成分表示: $(\mathbf{a} \odot \mathbf{b})_i = a_i b_i$

**性質:**
- 交換則: $\mathbf{a} \odot \mathbf{b} = \mathbf{b} \odot \mathbf{a}$
- 結合則: $(\mathbf{a} \odot \mathbf{b}) \odot \mathbf{c} = \mathbf{a} \odot (\mathbf{b} \odot \mathbf{c})$
- 分配則: $\mathbf{a} \odot (\mathbf{b} + \mathbf{c}) = \mathbf{a} \odot \mathbf{b} + \mathbf{a} \odot \mathbf{c}$
- 内積との関係: $\mathbf{a} \cdot \mathbf{b} = \mathbf{1}^\top (\mathbf{a} \odot \mathbf{b})$（全要素の総和）

---

## 比較まとめ

| 演算 | 入力 | 出力 | 次元制約 |
|------|------|------|----------|
| 内積 $\mathbf{a} \cdot \mathbf{b}$ | $\mathbb{R}^n \times \mathbb{R}^n$ | スカラー $\mathbb{R}$ | 同次元 |
| クロス積 $\mathbf{a} \times \mathbf{b}$ | $\mathbb{R}^3 \times \mathbb{R}^3$ | ベクトル $\mathbb{R}^3$ | 3次元のみ |
| テンソル積 $\mathbf{a} \otimes \mathbf{b}$ | $\mathbb{R}^m \times \mathbb{R}^n$ | 行列 $\mathbb{R}^{m \times n}$ | 任意 |
| 直和 $\mathbf{a} \oplus \mathbf{b}$ | $\mathbb{R}^m \times \mathbb{R}^n$ | ベクトル $\mathbb{R}^{m+n}$ | 任意 |
| アダマール積 $\mathbf{a} \odot \mathbf{b}$ | $\mathbb{R}^n \times \mathbb{R}^n$ | ベクトル $\mathbb{R}^n$ | 同次元 |


---

## ベクトル間の距離 (Distance)

ベクトル $\mathbf{a},\ \mathbf{b} \in \mathbb{R}^n$ に対して、差ベクトル $\mathbf{a} - \mathbf{b}$ のノルムとして定義される。

**ユークリッド距離 ($L^2$ 距離):**

$$d_2(\mathbf{a}, \mathbf{b}) = \|\mathbf{a} - \mathbf{b}\|_2 = \sqrt{\sum_{i=1}^{n} (a_i - b_i)^2}$$

**マンハッタン距離 ($L^1$ 距離):**

$$d_1(\mathbf{a}, \mathbf{b}) = \|\mathbf{a} - \mathbf{b}\|_1 = \sum_{i=1}^{n} |a_i - b_i|$$

**チェビシェフ距離 ($L^\infty$ 距離):**

$$d_\infty(\mathbf{a}, \mathbf{b}) = \|\mathbf{a} - \mathbf{b}\|_\infty = \max_{i}\ |a_i - b_i|$$

**$L^p$ 距離（一般化）:**

$$d_p(\mathbf{a}, \mathbf{b}) = \|\mathbf{a} - \mathbf{b}\|_p = \left(\sum_{i=1}^{n} |a_i - b_i|^p\right)^{1/p}$$

$p = 1, 2, \infty$ はそれぞれ上記の特殊ケース。

**距離の公理（全ての $L^p$ 距離が満たす性質）:**
- 非負性: $d(\mathbf{a}, \mathbf{b}) \geq 0$、等号は $\mathbf{a} = \mathbf{b}$ のとき
- 対称性: $d(\mathbf{a}, \mathbf{b}) = d(\mathbf{b}, \mathbf{a})$
- 三角不等式: $d(\mathbf{a}, \mathbf{c}) \leq d(\mathbf{a}, \mathbf{b}) + d(\mathbf{b}, \mathbf{c})$

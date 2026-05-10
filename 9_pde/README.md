# 偏微分方程式

## 偏微分方程式について

n個の独立変数（$x_1, x_2,...x_n$）をもつ未知関数 $u$ とその偏微分を含む方程式を**偏微分方程式 (Partial Differential Equation; PDE)** という。

### 数値解法

解析解が得られない場合、以下の数値解法が用いられる。

- 有限差分法 (Finite Difference Method; FDM): 偏微分を差分近似で置き換え、格子点上の値を求める。実装が簡単で構造格子向き。
- 有限要素法 (Finite Element Method; FEM): 領域を要素に分割し、弱形式（変分原理）で離散化する。複雑な形状や境界条件に強い。
- 境界要素法 (Boundary Element Method; BEM): 領域の境界のみを離散化する。次元が1つ下がるため、無限領域問題などに有効。

## 2階線形偏微分方程式

2変数 $x, y$ の2階線形PDEの一般形は以下のように書ける。

$$a(x,y) \frac{\partial^2 u}{\partial x^2} + b(x,y) \frac{\partial^2 u}{\partial x \partial y} + c(x,y) \frac{\partial^2 u}{\partial y^2} + \cdots = F(x,y,u,\frac{\partial u}{\partial x},\frac{\partial u}{\partial y})$$

判別式 $D = b^2 - 4ac$ の符号によって3つに分類される。

| 型 | 条件 | 代表例 |
|---|---|---|
| 双曲型 (hyperbolic) | $D > 0$ | 波動方程式 |
| 放物型 (parabolic) | $D = 0$ | 熱伝導方程式 |
| 楕円型 (elliptic) | $D < 0$ | Poisson方程式 |

### 波動方程式（双曲型）

$$\frac{\partial^2 u}{\partial t^2} = c^2 \frac{\partial^2 u}{\partial x^2}$$

$c$ は波の伝播速度。初期変位と初期速度を与える初期値問題として解く。

### 熱伝導方程式（放物型）

$$\frac{\partial u}{\partial t} = \alpha \frac{\partial^2 u}{\partial x^2}$$

$\alpha$ は熱拡散率。時間方向に初期値、空間方向に境界条件を与える初期値境界値問題として解く。

### Poisson方程式（楕円型）

$$\frac{\partial^2 u}{\partial x^2} + \frac{\partial^2 u}{\partial y^2} = f(x, y)$$

右辺が $0$ の場合はLaplace方程式と呼ばれる。境界値問題として解く。

## 有限差分法について

空間・時間を均等な格子で離散化し、偏微分を差分商で近似する。

### 差分近似

格子幅 $h$ での1階・2階偏微分の近似（Taylor展開より）。

| 種類 | 近似式 | 精度 |
|---|---|---|
| 前進差分 | $\frac{\partial u}{\partial x} \approx \frac{u_{i+1} - u_i}{h}$ | $O(h)$ |
| 後退差分 | $\frac{\partial u}{\partial x} \approx \frac{u_i - u_{i-1}}{h}$ | $O(h)$ |
| 中心差分 | $\frac{\partial u}{\partial x} \approx \frac{u_{i+1} - u_{i-1}}{2h}$ | $O(h^2)$ |
| 2階中心差分 | $\frac{\partial^2 u}{\partial x^2} \approx \frac{u_{i+1} - 2u_i + u_{i-1}}{h^2}$ | $O(h^2)$ |


### 離散化について

以降、以下のように離散化のための変数を定義する。

空間格子幅 $\Delta x$、時間ステップ $\Delta t$、格子点 $(i, n)$ を $u_i^n = u(i\Delta x, n\Delta t)$ とおく。領域は $x \in [0, L]$、格子点数は $N+1$（$i = 0, 1, \ldots, N$）。

### 熱伝導方程式の離散化

#### 陽的差分法（前進オイラー + 中心差分）

$$\frac{u_i^{n+1} - u_i^n}{\Delta t} = \alpha \frac{u_{i+1}^n - 2u_i^n + u_{i-1}^n}{(\Delta x)^2}$$

$$u_i^{n+1} = u_i^n + r(u_{i+1}^n - 2u_i^n + u_{i-1}^n), \quad r = \frac{\alpha \Delta t}{(\Delta x)^2}$$

安定条件（CFL条件）: $r \leq \dfrac{1}{2}$

#### 陰的差分法（後退オイラー）

$$\frac{u_i^{n+1} - u_i^n}{\Delta t} = \alpha \frac{u_{i+1}^{n+1} - 2u_i^{n+1} + u_{i-1}^{n+1}}{(\Delta x)^2}$$

各時刻で連立1次方程式を解く必要があるが、無条件安定（ステップ幅の制約なし）。

### 波動方程式の離散化

$$\frac{u_i^{n+1} - 2u_i^n + u_i^{n-1}}{(\Delta t)^2} = c^2 \frac{u_{i+1}^n - 2u_i^n + u_{i-1}^n}{(\Delta x)^2}$$

$$u_i^{n+1} = 2u_i^n - u_i^{n-1} + \lambda^2(u_{i+1}^n - 2u_i^n + u_{i-1}^n), \quad \lambda = \frac{c\,\Delta t}{\Delta x}$$

安定条件（Courant条件）: $\lambda \leq 1$

### Poisson方程式の離散化

2次元格子 $(i, j)$ で離散化すると、

$$\frac{u_{i+1,j} - 2u_{i,j} + u_{i-1,j}}{(\Delta x)^2} + \frac{u_{i,j+1} - 2u_{i,j} + u_{i,j-1}}{(\Delta y)^2} = f_{i,j}$$

時間発展がないため、境界条件を与えた上で連立1次方程式を解く。格子点数が多い場合は反復法（ガウス-ザイデル法、SOR法、共役勾配法など）が使われる。

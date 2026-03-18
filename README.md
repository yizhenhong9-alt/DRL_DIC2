# 🧠 GridWorld Value Iteration Visualization

本專案實作經典 Reinforcement Learning 問題 **GridWorld**，並使用 **Value Iteration** 演算法求解最佳策略，同時透過 **Flask + HTML/CSS/JavaScript** 建立互動式視覺化介面，動態展示價值函數收斂過程與最佳路徑。

Demo: https://drl-dic2.onrender.com/
---

## 📌 專案特色

✨ 本專案具備以下功能：

* 🔄 **Value Iteration 動態展示**

  * 顯示每一輪 iteration 的 V(s) 變化
* 🧭 **最佳策略 (Policy) 可視化**

  * 使用箭頭 (↑ ↓ ← →) 表示最佳行動
* 🟨 **最佳路徑高亮**

  * 從 Start 到 Goal 的最佳路徑以黃色標示
* 🎨 **清晰視覺設計**

  * Start：🟩 綠色
  * Goal：🟥 紅色
  * Block：⬛ 灰色
* ⚡ **即時互動**

  * 一鍵執行 Value Iteration 並播放動畫

---

## 🗺️ GridWorld 設定

| 項目          | 設定                  |
| ----------- | ------------------- |
| Grid 大小     | 5 × 5               |
| 起點 (Start)  | (0, 0)              |
| 終點 (Goal)   | (4, 4)              |
| 障礙物 (Block) | (1,1), (2,2), (3,3) |

---

## ⚙️ 獎勵設計

| 情境        | Reward |
| --------- | ------ |
| 一般移動      | -1     |
| 到達終點      | +10    |
| 撞牆 / 無效移動 | -5     |

---

## 🧮 演算法說明

本專案使用 **Value Iteration**：

### Bellman Optimality Equation

```
V(s) = max_a [ R(s,a) + γ V(s') ]
```

* γ (discount factor) = 0.9
* 持續更新直到收斂（Δ < θ）

---

## 🏗️ 專案架構

```
gridworld-value-iteration/
│
├── app.py                  # Flask 後端（Value Iteration + API）
├── requirements.txt        # 套件需求
│
├── templates/
│     └── index.html        # 前端頁面
│
└── static/
      └── style.css         # UI 設計
```

---

## 🚀 安裝與執行

### 1️⃣ Clone 專案

```
git clone https://github.com/<your-username>/gridworld-value-iteration.git
cd gridworld-value-iteration
```

---

### 2️⃣ 安裝套件

建議使用虛擬環境：

```
pip install -r requirements.txt
```

---

### 3️⃣ 執行 Flask

```
python app.py
```

開啟瀏覽器：

```
http://127.0.0.1:5000
```

---

## 🌐 部署（Render）

本專案已支援部署到 Render：

### 🔧 必要設定

在 `app.py` 中：

```python
import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
```

---

### 🚀 Render 設定

* Build Command：

```
pip install -r requirements.txt
```

* Start Command：

```
python app.py
```

---

## 🎮 使用方式

1️⃣ 點擊 **Run Value Iteration**
2️⃣ 觀察：

* 每一輪 V(s) 更新
* 箭頭策略變化
* 收斂過程

3️⃣ 最終顯示：

* 最佳策略
* 最佳路徑（黃色標註）

---

## 🖥️ 視覺化說明

| 元素     | 說明              |
| ------ | --------------- |
| Start  | 🟩 綠色 + "Start" |
| Goal   | 🟥 紅色 + "Goal"  |
| Block  | ⬛ 灰色            |
| Path   | 🟨 黃色           |
| Policy | 箭頭方向            |

---

## 📈 動畫流程

```
Iteration 0 → 初始化
Iteration 1 → 初始更新
Iteration 2 → 價值擴散
...
Iteration N → 收斂
→ 顯示最佳路徑
```

---

## 🔧 技術使用

* Python
* Flask
* NumPy
* HTML / CSS / JavaScript

---

## 📚 適用場景

本專案適合：

* 強化學習課程展示
* Value Iteration 教學
* RL 視覺化 demo
* 專題報告展示

---

## 🔮 未來改進方向

* 🔥 Heatmap 顯示 V(s)
* 🎞️ Agent 移動動畫
* 🎚️ Iteration Slider
* 🤖 支援 Policy Iteration / Q-learning
* 📊 可調參數 (γ, reward)


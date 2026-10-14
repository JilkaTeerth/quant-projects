<p align="center"><img src="assets/banner.svg" alt="Quant Projects" width="100%"></p>

<p align="center">
  <img alt="progress" src="https://img.shields.io/badge/progress-1%2F10-2a78d6?style=flat-square">
  <img alt="license" src="https://img.shields.io/badge/license-MIT-lightgrey?style=flat-square">
</p>

Probability, statistics and markets, built up one small idea at a time.

Each folder is one small, self contained project that does one thing. They get harder as the numbers go up: first scripts, then data and charts, then Java, SQL and APIs, then a first machine learning model.

## Projects

| # | Project | What it does | Language | Status |
|:-:|---|---|:-:|:-:|
| 01 | **[Compound interest calculator](./01-compound-interest)** | Shows how money grows year by year at a fixed rate. | ![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white) | ✅ |
| 02 | Coin flip streaks simulator | Flips a coin thousands of times and finds the longest streak. | ![Java](https://img.shields.io/badge/Java-ED8B00?logo=openjdk&logoColor=white) | 🔜 |
| 03 | Dice rolls: simulated vs theoretical odds | Compares simulated dice sums with the exact probabilities. | ![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white) | ⬜ |
| 04 | Mean, median, std from scratch | Computes basic statistics with no libraries. | ![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white) | ⬜ |
| 05 | Daily returns of one stock | Turns a price CSV into daily percentage returns. | ![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white) | ⬜ |
| 06 | Random walk stock plot | Simulates a fake stock price as a random walk. | ![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white) | ⬜ |
| 07 | Matrix calculator | Adds, multiplies and transposes matrices. | ![Java](https://img.shields.io/badge/Java-ED8B00?logo=openjdk&logoColor=white) | ⬜ |
| 08 | Moving average crossover signals | Marks buy and sell signals where two moving averages cross. | ![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white) | ⬜ |
| 09 | Stock prices in SQLite | Stores prices in a database and queries the best and worst days. | ![SQL](https://img.shields.io/badge/SQL-003B57?logo=sqlite&logoColor=white) | ⬜ |
| 10 | Linear regression: a stock's beta | Estimates how much a stock moves with the S&P 500. | ![ML](https://img.shields.io/badge/ML-F7931E?logo=scikitlearn&logoColor=white) | ⬜ |

✅ done &nbsp; 🔜 up next &nbsp; ⬜ planned

## Running a project

```bash
git clone https://github.com/JilkaTeerth/quant-projects.git
cd quant-projects/01-...
```

Every folder has its own README with the exact commands. Python projects need `pip install -r requirements.txt`, Java projects compile with plain `javac`.

---

<sub>Part of a series of six project collections. See them all at [github.com/JilkaTeerth](https://github.com/JilkaTeerth).</sub>

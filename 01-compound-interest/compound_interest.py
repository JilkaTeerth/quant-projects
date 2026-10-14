"""Compound interest calculator.

Shows how an amount of money grows each year at a fixed interest rate,
prints a year by year table and saves a chart comparing it with simple interest.
"""
import matplotlib.pyplot as plt


def grow(principal, rate, years):
    """Return the balance at the end of each year, starting with year 0."""
    balances = [principal]
    for year in range(years):
        balances.append(balances[-1] * (1 + rate))
    return balances


def simple(principal, rate, years):
    """Balance if interest is only ever paid on the original amount."""
    return [principal + principal * rate * year for year in range(years + 1)]


def main():
    principal = float(input("Starting amount ($): "))
    rate = float(input("Yearly interest rate (%): ")) / 100
    years = int(input("Number of years: "))

    compound = grow(principal, rate, years)
    flat = simple(principal, rate, years)

    print(f"\n{'Year':>4}  {'Balance':>12}  {'Interest earned':>16}")
    for year, balance in enumerate(compound):
        earned = balance - compound[year - 1] if year > 0 else 0
        print(f"{year:>4}  {balance:>12,.2f}  {earned:>16,.2f}")

    print(f"\nAfter {years} years: ${compound[-1]:,.2f} with compound interest")
    print(f"vs ${flat[-1]:,.2f} with simple interest")
    print(f"Compounding earned you an extra ${compound[-1] - flat[-1]:,.2f}")

    plt.rcParams.update({"figure.facecolor": "#fffdf7", "axes.facecolor": "#fffdf7",
                         "axes.edgecolor": "#14212b", "text.color": "#14212b",
                         "axes.labelcolor": "#14212b", "xtick.color": "#4e5b66", "ytick.color": "#4e5b66"})
    plt.plot(compound, label="Compound interest", color="#2a78d6", linewidth=2.5)
    plt.plot(flat, label="Simple interest", color="#8a8273", linestyle="--")
    plt.title(f"${principal:,.0f} at {rate * 100:g}% for {years} years", loc="left", fontweight="bold")
    plt.xlabel("Year")
    plt.ylabel("Balance ($)")
    plt.legend(frameon=False)
    plt.grid(color="#dce3e8")
    plt.gca().spines[["top", "right"]].set_visible(False)
    plt.savefig("growth.png", dpi=150, bbox_inches="tight")
    print("Chart saved to growth.png")


if __name__ == "__main__":
    main()

import sys
import pandas as pd
import matplotlib.pyplot as plt

class CountryData:
    def __init__(self, name):
        self.name = name
        self.data = None

    #  using pandas to load and organize the data
    def load_data(self, filepath):
        df = pd.read_csv(filepath)

        df = df[df["Area"] == self.name]

        df = df.pivot_table(
            index="Year",
            columns="Element",
            values="Value"
        ).reset_index()

        df = df.rename(columns={
            "Area harvested": "Area harvested",
            "Yield": "Yield",
            "Production": "Production"
        })

        self.data = df

    def show_table(self):
        print(f"\n--- {self.name} ---")
        print(self.data)

    # plotting scatter plots
    def plot_scatter(self):
        years = self.data["Year"]
        yields = self.data["Yield"]

        fig, ax = plt.subplots()
        ax.scatter(years, yields)
        ax.set_title(f"Yield over Years in {self.name}")
        ax.set_xlabel("Year")
        ax.set_ylabel("Yield")
        ax.grid(True, linestyle="-")
        plt.show()

    # plotting bar charts
    def plot_bar_chart(self):
        years = self.data["Year"]
        areas = self.data["Area harvested"]

        fig, ax = plt.subplots()
        ax.bar(years, areas)
        ax.set_title(f"Area harvested over Years in {self.name}")
        ax.set_xlabel("Year")
        ax.set_ylabel("Area Harvested")
        ax.grid(True, linestyle="-")
        plt.show()

class Ghana(CountryData):
    def __init__(self):
        super().__init__("Ghana")

class IvoryCoast(CountryData):
    def __init__(self):
        super().__init__("Côte d'Ivoire")

def plot_combined(ghana, ivory_coast, output_file="combined_plots.pdf"):
    fig, axes = plt.subplots(2, 2, figsize=(12, 8))
    fig.suptitle("Ghana and Ivory Coast data analytics", fontsize=16, fontweight="bold")
    # Ghana Yield scatter plot
    axes[0,0].scatter(ghana.data["Year"], ghana.data["Yield"], color="tab:pink")
    axes[0,0].set_title("Ghana - Yield over Years")
    axes[0,0].set_xlabel("Year")
    axes[0,0].set_ylabel("Yield")
    axes[0,0].grid(True, linestyle="-")

    # Ivory Coast Yield scatter plot
    axes[0,1].scatter(ivory_coast.data["Year"], ivory_coast.data["Yield"], color="tab:purple")
    axes[0,1].set_title("Côte d'Ivoire - Yield over Years")
    axes[0,1].set_xlabel("Year")
    axes[0,1].set_ylabel("Yield")
    axes[0,1].grid(True, linestyle="-")

    # Ghana Area harvested bar chart
    axes[1,0].bar(ghana.data["Year"], ghana.data["Area harvested"], color="tab:orange")
    axes[1,0].set_title("Ghana - Area Harvested over Years")
    axes[1,0].set_xlabel("Year")
    axes[1,0].set_ylabel("Area Harvested")
    axes[1,0].grid(True, linestyle="-")

    # Ivory Coast Area harvested bar chart
    axes[1,1].bar(ivory_coast.data["Year"], ivory_coast.data["Area harvested"], color="crimson")
    axes[1,1].set_title("Côte d'Ivoire - Area Harvested over Years")
    axes[1,1].set_xlabel("Year")
    axes[1,1].set_ylabel("Area Harvested")
    axes[1,1].grid(True, linestyle="-")

    # Adjust layout
    plt.tight_layout(rect=(0,0,1,0.96))

    # save figure as PDF
    fig.savefig(output_file)
    plt.show()
    print(f"Combined plot saved as {output_file}")

def main():
    filepath = "FAOSTAT_data_7-23-2022 (1).csv"

    # Ghana
    ghana = Ghana()
    ghana.load_data(filepath)
    ghana.show_table()
    ghana.plot_scatter()
    ghana.plot_bar_chart()

    # Ivory Coast
    ivory_coast = IvoryCoast()
    ivory_coast.load_data(filepath)
    ivory_coast.show_table()
    ivory_coast.plot_scatter()
    ivory_coast.plot_bar_chart()

    # Ghana and Ivory Coast combined plots
    plot_combined(ghana, ivory_coast)

    return 0

if __name__ == "__main__":
    sys.exit(main())
import matplotlib.pyplot as plt

def plot_hists(data):
    for i in range(len(data.columns)):
        plt.hist(data.iloc[:, i].dropna())
        plt.title(data.columns[i])
        plt.xticks(rotation=90)
        plt.show()

def get_missing_data(data):
    return print(f'% of Missing Data:\n{data.isnull().sum() / len(data) * 100}\n')
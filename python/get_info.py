import matplotlib.pyplot as plt
import seaborn as sns


def plot_hists(data, title):
    """
    Plots histogram of the data inputted
    :param data: dataset
    :param title: title of the collection of histograms
    :return: None
    """

    edit = data.iloc[:, 1:-1]

    sns.set()
    plt.figure(figsize=(20, 20))

    for i in range(len(edit.columns)):
        ax = plt.subplot(int(len(edit.columns) / 6), 6, i + 1)
        _ = sns.histplot(data=data, x=edit.columns[i], ax=ax, hue='label')
        _ = plt.title(edit.columns[i])
        _ = plt.xticks(rotation=90)
        _ = plt.ylabel('Count')
    _ = plt.tight_layout()
    _ = plt.suptitle(f'{title}', y=1.02, size=24)
    _ = plt.show()

    return None


def plot_violin(data, title):
    '''
    Plots violin plot of the data inputted
    :param data: dataset
    :param title: title of the collection of violin plots
    :return: None
    '''
    plt.figure(figsize=(20, 20))
    # copy = data.copy(deep=True)
    edit = data.iloc[:, 1:-2]

    for i in range(len(edit.columns)):
        ax = plt.subplot(int(len(edit.columns) / 6), 6, i + 1)
        sns.violinplot(x='all', y=edit.columns[i], data=data, ax=ax, hue='label', inner='quartile', palette='muted',
                       split=True)
        plt.title(edit.columns[i])
        plt.xticks(rotation=90)
        plt.ylabel('Count')
    plt.tight_layout()
    plt.suptitle(f'{title}', y=1.02, size=24)
    plt.show()
    return None


def get_missing_data(data):
    '''
    Print percentage of data that is missing in the dataset
    :param data: dataset
    :return:
    '''
    missing = round((data.isnull().sum() / len(data) * 100), 2)
    return print(f'% of Missing Data:\n{missing}\n')


def get_type(type):
    '''
    Determines whether dataset is a train or validation set and checks for errors in user input
    :param type: train or validation
    :return: string of type or error
    '''
    if type == 'test' or type == 'validation':
        return 'val'
    elif type == 'train':
        return 'train'
    else:
        return print('Error. Please input train, test, or validation')

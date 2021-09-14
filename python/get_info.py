import matplotlib.pyplot as plt

def plot_hists(data, title):
    '''
    Plots histogram of the data inputted
    :param data: dataset
    :param title: title of the collection of histograms
    :return: None
    '''
    plt.figure(figsize=(20, 20))
    
    for i in range(len(data.columns)):
        ax = plt.subplot(int(len(data.columns)/6), 6, i + 1)
        plt.hist(data.iloc[:, i].dropna())
        plt.title(data.columns[i])
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
        return'val'
    elif type == 'train':
        return 'train'
    else:
        return print('Error. Please input train, test, or validation')
import matplotlib.pyplot as plt

def plot_hists(data):
    '''
    Plots histogram of the data inputted
    :param data: dataset
    :return: None
    '''
    for i in range(len(data.columns)):
        plt.hist(data.iloc[:, i].dropna())
        plt.title(data.columns[i])
        plt.xticks(rotation=90)
        plt.show()
    return None

def get_missing_data(data):
    '''
    Print percentage of data that is missing in the dataset
    :param data: dataset
    :return:
    '''
    return print(f'% of Missing Data:\n{data.isnull().sum() / len(data) * 100}\n')

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
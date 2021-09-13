from get_info import get_type

def create_dataset(type, project_name='capstone-project-320304'):
    '''
    joins true and false transactions into one dataset with labels
    :param project_name: name of project on BigQuery
    :param type: indicate whether test or training data
    :return: visitor id, features from transactions, and labels where transaction = 1 and no transaction = 0
    '''

    type_name = get_type(type)

    query = f'''--CREATE TABLE IF NOT EXISTS `{project_name}.propensity.{type_name}_data` AS
                WITH transactions AS (
                
                SELECT * , 1 as label
                FROM `{project_name}.transactions.{type_name}_true_features` as t
                 
                UNION ALL
                
                SELECT * , 0 as label
                FROM ( SELECT *
                FROM `{project_name}.transactions.{type_name}_false_features` as f
                --limit the number of false transactions to slightly increase the proportion
                --between true and false transactions
                ORDER BY rand() LIMIT 19000)
                )
                SELECT *
                FROM transactions;'''
    return query
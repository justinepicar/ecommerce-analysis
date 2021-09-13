
def get_transactions(start_date, end_date, project_name = 'capstone-project-320304'):
        '''
        This function queries all visitor ids with the earliest known date of transaction
        :param start_date: start date of query
        :param end_date: end date of query
        :param project_name: name of project on BigQuery
        :return: returns fullVisitorId and transaction_date
        '''
        query= f'''
                    CREATE TABLE IF NOT EXISTS `{project_name}.transactions.true_transactions` AS
                    SELECT fullVisitorId, MIN(PARSE_DATE('%Y%m%d', date)) as transaction_date
                    FROM `bigquery-public-data.google_analytics_sample.ga_sessions_*`
                    WHERE _TABLE_SUFFIX BETWEEN '{start_date}' AND '{end_date}'
                    AND totals.transactions >= 1
                    GROUP BY fullVisitorId;
                '''
        return query

def get_true_transactions(start_date, end_date, project_name = 'capstone-project-320304'):
        '''
        This query gets an aggregate of select features that have made transactions >= 1 on a particular date
        :param start_date: start date of query
        :param end_date: end date of query
        :param project_name: name of project on BigQuery
        :return: returns visitor id, transaction date, day difference from transaction, total hits, total pageViews,
                total bounces, total sessions, average session quality, and total time on site in seconds per day
        '''
        query =f''' CREATE TABLE IF NOT EXISTS `{project_name}.transactions.train_true` AS
                    SELECT capstone.fullVisitorId AS visitor_id,
                           MIN(transaction_date) transaction_date,
                           DATE_DIFF(transaction_date, PARSE_DATE('%Y%m%d',date), DAY) day_diff, 
                           SUM(IFNULL(totals.hits, 0)) AS hits,
                           SUM(IFNULL(totals.pageviews, 0)) AS pageViews,
                           SUM(IFNULL(totals.bounces, 0)) AS bounces,
                           SUM(IFNULL(totals.visits, 0)) AS sessions,
                           ROUND(AVG(IFNULL(totals.sessionQualityDim, 0)), 2) AS session_quality,
                           SUM(IFNULL(totals.timeOnSite, 0)) AS time_on_site_seconds
                    FROM `bigquery-public-data.google_analytics_sample.ga_sessions_*` AS bqml
                    JOIN `{project_name}.transactions.true_transactions` AS capstone
                    ON bqml.fullVisitorId = capstone.fullVisitorId
                    WHERE  _TABLE_SUFFIX BETWEEN '{start_date}' AND '{end_date}'
                    AND DATE_DIFF(transaction_date, 
                                  PARSE_DATE('%Y%m%d',date), 
                                  DAY) >= 0
                    AND DATE_DIFF(transaction_date, 
                                  PARSE_DATE('%Y%m%d',date), 
                                  DAY) < 13
                    GROUP BY visitor_id, DATE_DIFF(transaction_date, PARSE_DATE('%Y%m%d',date), DAY);'''
        return query

def get_false_transactions(start_date, end_date, project_name = 'capstone-project-320304'):
        '''
        This query gets an aggregate of select features that have not made transactions on a particular date
        :param start_date: start date of query
        :param end_date: end date of query
        :param project_name: name of project on BigQuery
        :return: returns visitor id, transaction date, day difference from transaction, total hits, total pageViews,
                total bounces, total sessions, average session quality, and total time on site in seconds per day
        '''
        query = f'''CREATE TABLE IF NOT EXISTS `{project_name}.transactions.train_false` AS
                    SELECT fullVisitorId AS visitor_id,
                           MIN(transaction_date) as transaction_date,
                           DATE_DIFF(PARSE_DATE('%Y%m%d',transaction_date),
                                     PARSE_DATE('%Y%m%d',date), DAY) day_diff,
                           SUM(IFNULL(totals.hits, 0)) AS hits,
                           SUM(IFNULL(totals.pageviews, 0)) AS pageViews,
                           SUM(IFNULL(totals.bounces, 0)) AS bounces,
                           SUM(IFNULL(totals.visits, 0)) AS sessions,
                           ROUND(AVG(IFNULL(totals.sessionQualityDim, 0)), 2) AS session_quality,
                           SUM(IFNULL(totals.timeOnSite, 0)) AS time_on_site_seconds
                    FROM `bigquery-public-data.google_analytics_sample.ga_sessions_*` AS bqml
                    JOIN(  SELECT DISTINCT date as transaction_date
                           FROM `bigquery-public-data.google_analytics_sample.ga_sessions_*`
                           WHERE _TABLE_SUFFIX BETWEEN '{start_date}' AND '{end_date}'
                           LIMIT 5)
                    ON TRUE
                    WHERE DATE_DIFF(PARSE_DATE('%Y%m%d',transaction_date),
                                    PARSE_DATE('%Y%m%d',date), 
                                    DAY) >= 0
                    AND DATE_DIFF(PARSE_DATE('%Y%m%d',transaction_date),
                                  PARSE_DATE('%Y%m%d',date), 
                                  DAY) < 13
                    GROUP BY visitor_id, day_diff
                    ORDER BY transaction_date'''
        return query
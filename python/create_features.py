from get_info import get_type

def get_true_features(type, project_name='capstone-project-320304'):
    '''
    Aggregates features from true transactions by day0, day1, day2, day3, day4_6, and week2
    :param project_name: name of project on BigQuery
    :param type: indicate whether test or training data
    :return: features from true transactions by days and week
    '''

    type_name = get_type(type)

    query =f'''CREATE TABLE IF NOT EXISTS `{project_name}.transactions.{type_name}_true_features` AS
               SELECT visitor_id,
               MAX(CASE WHEN day_diff = 0 THEN time_on_site_seconds ELSE NULL END) day0_time_on_site_seconds,
               MAX(CASE WHEN day_diff = 1 THEN time_on_site_seconds ELSE NULL END) day1_time_on_site_seconds,
               MAX(CASE WHEN day_diff = 2 THEN time_on_site_seconds ELSE NULL END) day2_time_on_site_seconds,
               MAX(CASE WHEN day_diff = 3 THEN time_on_site_seconds ELSE NULL END) day3_time_on_site_seconds,
               MAX(CASE WHEN day_diff in (4,6) THEN time_on_site_seconds ELSE NULL END) day4_6_time_on_site_seconds,
               MAX(CASE WHEN day_diff > 6 THEN time_on_site_seconds ELSE NULL END) w2_time_on_site_seconds,
               MAX(CASE WHEN day_diff = 0 THEN hits ELSE NULL END) day0_hits,
               MAX(CASE WHEN day_diff = 1 THEN hits ELSE NULL END) day1_hits,
               MAX(CASE WHEN day_diff = 2 THEN hits ELSE NULL END) day2_hits,
               MAX(CASE WHEN day_diff = 3 THEN hits ELSE NULL END) day3_hits,
               MAX(CASE WHEN day_diff in (4,6) THEN hits ELSE NULL END) day4_6_hits,
               MAX(CASE WHEN day_diff > 6 THEN hits ELSE NULL END) w2_hits,
               MAX(CASE WHEN day_diff = 0 THEN pageViews ELSE NULL END) day0_pageViews,
               MAX(CASE WHEN day_diff = 1 THEN pageViews ELSE NULL END) day1_pageViews,
               MAX(CASE WHEN day_diff = 2 THEN pageViews ELSE NULL END) day2_pageViews,
               MAX(CASE WHEN day_diff = 3 THEN pageViews ELSE NULL END) day3_pageViews,
               MAX(CASE WHEN day_diff in (4,6) THEN pageViews ELSE NULL END) day4_6_pageViews,
               MAX(CASE WHEN day_diff > 6 THEN pageViews ELSE NULL END) w2_pageViews,
               MAX(CASE WHEN day_diff = 0 THEN bounces ELSE NULL END) day0_bounces,
               MAX(CASE WHEN day_diff = 1 THEN bounces ELSE NULL END) day1_bounces,
               MAX(CASE WHEN day_diff = 2 THEN bounces ELSE NULL END) day2_bounces,
               MAX(CASE WHEN day_diff = 3 THEN bounces ELSE NULL END) day3_bounces,
               MAX(CASE WHEN day_diff in (4,6) THEN bounces ELSE NULL END) day4_6_bounces,
               MAX(CASE WHEN day_diff > 6 THEN bounces ELSE NULL END) w2_bounces,
               MAX(CASE WHEN day_diff = 0 THEN sessions ELSE NULL END) day0_sessions,
               MAX(CASE WHEN day_diff = 1 THEN sessions ELSE NULL END) day1_sessions,
               MAX(CASE WHEN day_diff = 2 THEN sessions ELSE NULL END) day2_sessions,
               MAX(CASE WHEN day_diff = 3 THEN sessions ELSE NULL END) day3_sessions,
               MAX(CASE WHEN day_diff in (4,6) THEN sessions ELSE NULL END) day4_6_sessions,
               MAX(CASE WHEN day_diff > 6 THEN sessions ELSE NULL END) w2_sessions,
               MAX(CASE WHEN day_diff = 0 THEN session_quality ELSE NULL END) day0_session_quality,
               MAX(CASE WHEN day_diff = 1 THEN session_quality ELSE NULL END) day1_session_quality,
               MAX(CASE WHEN day_diff = 2 THEN session_quality ELSE NULL END) day2_session_quality,
               MAX(CASE WHEN day_diff = 3 THEN session_quality ELSE NULL END) day3_session_quality,
               MAX(CASE WHEN day_diff in (4,6) THEN session_quality ELSE NULL END) day4_6_session_quality,
               MAX(CASE WHEN day_diff > 6 THEN session_quality ELSE NULL END) w2_session_quality,
               FROM `{project_name}.transactions.{type_name}_true_transactions`
               GROUP BY visitor_id;'''
    return query

def get_false_features(type, project_name='capstone-project-320304'):
    '''
    Aggregates features from false transactions by day0, day1, day2, day3, day4_6, and week2,
    excluding visitors who have made transactions
    :param project_name: name of project on BigQuery
    :param type: indicate whether test or training data
    :return: features from true transactions by days and week
    '''

    type_name = get_type(type)

    query =f'''CREATE TABLE IF NOT EXISTS `{project_name}.transactions.{type_name}_false_features` AS
               SELECT a.visitor_id,
               MAX(CASE WHEN day_diff = 0 THEN time_on_site_seconds ELSE NULL END) day0_time_on_site_seconds,
               MAX(CASE WHEN day_diff = 1 THEN time_on_site_seconds ELSE NULL END) day1_time_on_site_seconds,
               MAX(CASE WHEN day_diff = 2 THEN time_on_site_seconds ELSE NULL END) day2_time_on_site_seconds,
               MAX(CASE WHEN day_diff = 3 THEN time_on_site_seconds ELSE NULL END) day3_time_on_site_seconds,
               MAX(CASE WHEN day_diff in (4,6) THEN time_on_site_seconds ELSE NULL END) day4_6_time_on_site_seconds,
               MAX(CASE WHEN day_diff > 6 THEN time_on_site_seconds ELSE NULL END) w2_time_on_site_seconds,
               MAX(CASE WHEN day_diff = 0 THEN hits ELSE NULL END) day0_hits,
               MAX(CASE WHEN day_diff = 1 THEN hits ELSE NULL END) day1_hits,
               MAX(CASE WHEN day_diff = 2 THEN hits ELSE NULL END) day2_hits,
               MAX(CASE WHEN day_diff = 3 THEN hits ELSE NULL END) day3_hits,
               MAX(CASE WHEN day_diff in (4,6) THEN hits ELSE NULL END) day4_6_hits,
               MAX(CASE WHEN day_diff > 6 THEN hits ELSE NULL END) w2_hits,
               MAX(CASE WHEN day_diff = 0 THEN pageViews ELSE NULL END) day0_pageViews,
               MAX(CASE WHEN day_diff = 1 THEN pageViews ELSE NULL END) day1_pageViews,
               MAX(CASE WHEN day_diff = 2 THEN pageViews ELSE NULL END) day2_pageViews,
               MAX(CASE WHEN day_diff = 3 THEN pageViews ELSE NULL END) day3_pageViews,
               MAX(CASE WHEN day_diff in (4,6) THEN pageViews ELSE NULL END) day4_6_pageViews,
               MAX(CASE WHEN day_diff > 6 THEN pageViews ELSE NULL END) w2_pageViews,
               MAX(CASE WHEN day_diff = 0 THEN bounces ELSE NULL END) day0_bounces,
               MAX(CASE WHEN day_diff = 1 THEN bounces ELSE NULL END) day1_bounces,
               MAX(CASE WHEN day_diff = 2 THEN bounces ELSE NULL END) day2_bounces,
               MAX(CASE WHEN day_diff = 3 THEN bounces ELSE NULL END) day3_bounces,
               MAX(CASE WHEN day_diff in (4,6) THEN bounces ELSE NULL END) day4_6_bounces,
               MAX(CASE WHEN day_diff > 6 THEN bounces ELSE NULL END) w2_bounces,
               MAX(CASE WHEN day_diff = 0 THEN sessions ELSE NULL END) day0_sessions,
               MAX(CASE WHEN day_diff = 1 THEN sessions ELSE NULL END) day1_sessions,
               MAX(CASE WHEN day_diff = 2 THEN sessions ELSE NULL END) day2_sessions,
               MAX(CASE WHEN day_diff = 3 THEN sessions ELSE NULL END) day3_sessions,
               MAX(CASE WHEN day_diff in (4,6) THEN sessions ELSE NULL END) day4_6_sessions,
               MAX(CASE WHEN day_diff > 6 THEN sessions ELSE NULL END) w2_sessions,
               MAX(CASE WHEN day_diff = 0 THEN session_quality ELSE NULL END) day0_session_quality,
               MAX(CASE WHEN day_diff = 1 THEN session_quality ELSE NULL END) day1_session_quality,
               MAX(CASE WHEN day_diff = 2 THEN session_quality ELSE NULL END) day2_session_quality,
               MAX(CASE WHEN day_diff = 3 THEN session_quality ELSE NULL END) day3_session_quality,
               MAX(CASE WHEN day_diff in (4,6) THEN session_quality ELSE NULL END) day4_6_session_quality,
               MAX(CASE WHEN day_diff > 6 THEN session_quality ELSE NULL END) w2_session_quality,
               FROM`capstone-project-320304.transactions.{type_name}_false_transactions` AS a
               LEFT JOIN (SELECT DISTINCT visitor_id 
                          FROM  `{project_name}.transactions.{type_name}_true_features`) AS b
               ON a.visitor_id=b.visitor_id
               WHERE b.visitor_id IS NULL
               GROUP BY a.visitor_id;'''
    return query

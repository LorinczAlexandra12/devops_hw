from operator import itemgetter

import pyodbc
from github import Github
import os
from pprint import pprint

if __name__ == '__main__':
    g = Github("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")
    repo = g.get_repo(full_name_or_id='LorinczAlexandra12/selenium_test')
    views = repo.get_views_traffic(per="day")

    conn = pyodbc.connect('Driver={SQL Server};'
                          'Server=DESKTOP-8G83ASS;'
                          'Database=DevOps;'
                          'Trusted_Connection=yes;')

    cursor = conn.cursor()
    #[UniquesNum],[TimeStamp],[Count]
    for v in views['views']:
        sql = "insert into GithubData(UniquesNum, TimeStamp, Count) values (?,?,?)"
        cursor.execute(sql, (v.uniques,v.timestamp,v.count))
        conn.commit()




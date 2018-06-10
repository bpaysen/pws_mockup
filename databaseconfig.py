import pymysql.cursors

import yaml

with open("config.yml", 'r') as ymlfile:
    cfg = yaml.load(ymlfile)

print(">>>>>>>>>>>>>>>>>>>>>>>>>>>> " + cfg["host"])

connection = pymysql.connect(host=cfg["host"],
							user=cfg["user"],
							password=cfg["password"],
							db=cfg["db"],
							charset=cfg["charset"],
							cursorclass=pymysql.cursors.DictCursor)

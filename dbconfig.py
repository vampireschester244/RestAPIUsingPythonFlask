# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 17:58:25 2019

@author: anush jain
"""
from application import application
from flaskext.mysql import MySQL
MySql = MySQL()
application.config['DATABASE_USER'] = 'sqoopuser'
application.config['DATABASE_PASSWORD'] = '*******'
application.config['DATABASE_DB'] = 'sqoopex'
application.config['DATABASE_HOST'] = 'cxln2.c.thelab-240901.internal'
MySql.init_app(application)
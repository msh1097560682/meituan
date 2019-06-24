# -*- coding: utf-8 -*- 
# @Time : 2019/6/24 15:06


from dao import BaseDao
from logger import api_logger

class UserDao(BaseDao):

    def save(self, **values):
        api_logger.info('db insert app_user: <%s>' % values['user_name'])
        super(UserDao, self).save('app_user', **values)
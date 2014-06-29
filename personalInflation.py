'''
Created on 10 Mar 2013

@author: eidahil
'''

class InflationData(object):

    def __init__(self, annual_inflation):
        self.set_my_annual_inflation(annual_inflation)

    def set_my_annual_inflation(self, my_annual_inflation):
        self.annual_inflation = my_annual_inflation

    def get_my_annual_inflation(self):
        return self.annual_inflation

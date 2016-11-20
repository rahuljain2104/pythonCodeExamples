from mlbase import MLBase
import configparser as cp
import matplotlib as mplot
import datetime as dt


class USPollsPrediction(MLBase):
    def get_data(self, params_file_path="params.ini"):
        ml = MLBase(params_file_path)
        data = ml.read_csv_data()
        return data

    def plot_time_versus_value(self, data):
        datetimes = data['startdate']
        list_of_datetimes = dt.strptime(datetimes)
        rawpoll_clinton = data['rawpoll_clinton']
        dates = mplot.dates.date2num(list_of_datetimes)
        mplot.pyplot.plot_date(dates, rawpoll_clinton)


us_polls = USPollsPrediction()
data = us_polls.get_data()
us_polls.plot_time_versus_value(data)

from datetime import datetime as dt
from datetime import timedelta
import pandas as pd
import lightgbm as lgb

class House:
    use_df=[]
    gen_df=[]
    def __init__(self,battery,datetime=dt.now()):
        datetime = datetime - timedelta(days=365)
        self.battery=battery
        self.datetime=datetime.replace(microsecond=0).replace(second=0)
        self.use_df=pd.read_csv('cac_code/csv_data/use_HO.csv')
        self.gen_df=pd.read_csv('cac_code/csv_data/gen_sol.csv')
        self.use_model=lgb.Booster(model_file='cac_code/ml_models/use_HO_model.txt')
        self.gen_model=lgb.Booster(model_file='cac_code/ml_models/gen_sol_model.txt')
    def date_time(self):
        return self.datetime
    def time_stamp(self):
        return dt.timestamp(self.datetime)
    def pred_cons(self,datetime): #predicted consumption
        cons_data = self.use_df.loc[self.use_df['time'] == str(datetime)]
        cons_data = cons_data.values.flatten().tolist()[1:-1]
        return self.use_model.predict([cons_data])
    def act_cons(self,datetimes): #actual consumption
        if type(datetimes) == str:
            datetimes = [datetimes]
        act_use_list = [self.use_df.loc[self.use_df['time'] == i].use_HO.values.flatten().tolist()[0] for i in datetimes]
        return act_use_list
    def pred_gen(self,datetime): #predicted generation
        weather_data=self.gen_df.loc[self.gen_df['time']==str(datetime)]
        weather_data=weather_data.values.flatten().tolist()[1:-1]
        return self.gen_model.predict([weather_data])
    def act_gen(self,datetimes): #actual generation
        if type(datetimes)==str:
            datetimes=[datetimes]
        act_gen_list=[self.gen_df.loc[self.gen_df['time'] == i].gen_Sol.values.flatten().tolist()[0] for i in datetimes]
        return act_gen_list
    def weather_list(self): #list of all the weather stuff
        return self.gen_df.drop(columns=["month","hour","gen_sol"])
    def use_HO(self): #returns pandas df
        return self.use_df
    def gen_sol(self): #returns pandas df
        return self.gen_df
    def update_battery(self):
        now=self.datetime
    def last_12(self,datetime,exception=False): #actual
        before_12_hr = (datetime - timedelta(hours=12)).strftime("%Y-%m-%d %H:%M:%S")[:-2]+'00'
        now = datetime.strftime("%Y-%m-%d %H:%M:%S")[:-2]+'00'
        mask_before = (self.gen_df['time'] <= now) & (self.gen_df['time'] >= before_12_hr)
        if exception:
            return mask_before
        return self.gen_df.loc[mask_before].time.values.tolist()
    def last_24(self,datetime,exception=False): #actual
        before_24_hr = (datetime - timedelta(hours=24)).strftime("%Y-%m-%d %H:%M:%S")[:-2]+'00'
        now = datetime.strftime("%Y-%m-%d %H:%M:%S")[:-2]+'00'
        mask_before = (self.gen_df['time'] <= now) & (self.gen_df['time'] >= before_24_hr)
        if exception:
            return mask_before
        return self.gen_df.loc[mask_before].time.values.tolist()
        
    def next_12(self,exception=False): #predicted
        now = self.datetime.strftime("%Y-%m-%d %H:%M:%S")[:-2]+'00'
        next_12_hr = (self.datetime + timedelta(hours=12)).strftime("%Y-%m-%d %H:%M:%S")[:-2]+'00'
        mask_after = (self.gen_df['time'] >= now) & (self.gen_df['time'] <= next_12_hr)
        if exception:
            return mask_after
        return self.gen_df.loc[mask_after].time.values.tolist()
        
    

    def next_days(self,days,exception=False): #predicted hourly
        now = self.datetime.strftime("%Y-%m-%d %H:%M:%S")[:-5]+'00:00'
        next_x_days = (self.datetime + timedelta(days=days)).strftime("%Y-%m-%d %H:%M:%S")[:-5]+'00:00'
        mask_after = (self.use_df['time'] >= now) & (self.use_df['time'] <= next_x_days)
        if exception:
            return mask_after
        times = self.use_df.loc[mask_after].time.values.tolist()
        return times[0::30]
    def next_hour(self,time,exception=False): # predicted hour
        time_dt = dt.strptime(time,"%Y-%m-%d %H:%M:%S")
        next_1_hour = (time_dt + timedelta(minutes=59)).strftime("%Y-%m-%d %H:%M:%S")[:-2]+'00'
        mask_after = (self.use_df['time'] >= time) & (self.use_df['time'] <= next_1_hour)
        if exception:
            return mask_after
        times = self.use_df.loc[mask_after].time.values.tolist()
        return times
    
house=House(0)
now = dt.now().replace(microsecond=0).replace(second=0)
now = now - timedelta(days=365)

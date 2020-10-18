from datetime import datetime

utc_time = datetime.strptime("15-08-2020 15:20:20", "%d-%m-%Y %H:%M:%S")
epoch_time = (utc_time - datetime(1970, 1, 1)).total_seconds()
print(epoch_time)

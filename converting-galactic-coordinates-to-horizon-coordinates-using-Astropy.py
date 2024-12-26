import astropy.units as u
from astropy.coordinates import SkyCoord, AltAz, EarthLocation
from astropy.time import Time
from datetime import datetime, timedelta

local_time = datetime.now()  
utc_time = local_time - timedelta(hours=7)  
current_time = Time(utc_time)  

latitude = 20.51  # vĩ độ Hà Nội
longitude = 106.4  # kinh độ Hà Nội
elevation = 10  # độ cao so với mực nước biển (mét)

location = EarthLocation(lat=latitude*u.deg, lon=longitude*u.deg, height=elevation*u.m)

altaz_frame = AltAz(obstime=current_time, location=location)

# Nhập tọa độ Galactic từ người dùng
l = float(input("Nhập kinh độ thiên hà (l) tính bằng độ: ")) * u.deg
b = float(input("Nhập vĩ độ thiên hà (b) tính bằng độ: ")) * u.deg

# Tạo đối tượng tọa độ thiên hà
galactic_coords = SkyCoord(l=l, b=b, frame='galactic')

# Chuyển đổi sang tọa độ Chân trời (Horizon coordinates)
horizon_coords = galactic_coords.transform_to(altaz_frame)

# In kết quả tọa độ Chân trời (góc phương vị và độ cao)
print(f"Thời gian địa phương hiện tại (UTC+7): {local_time}")
print(f"Thời gian UTC hiện tại: {utc_time}")
print(f"Góc phương vị (Azimuth): {horizon_coords.az:.2f}")
print(f"Độ cao (Altitude): {horizon_coords.alt:.2f}")

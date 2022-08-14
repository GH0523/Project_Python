# 모듈
import theater_module
theater_module.price(3)
theater_module.price_morning(4)

import theater_module as mv
mv.price_soldier(4)

from theater_module import *
price(3)
price_morning(5)
price_soldier(4)

from theater_module import price_morning as aaa
aaa(3)

# 패키지
import travel.thailand
trip_to = travel.thailand.ThailandPackage()
trip_to.detail()

# 패키지, 모듈 위치
from travel import *
import inspect
print(inspect.getfile(thailand))

import byme
byme.sign()
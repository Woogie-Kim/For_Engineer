
print(
'Homework #1\n\
----------------------------------\n\
My name is (Jong-Wook Kim)\n\
Student\'s ID is (20160768)\n\
Used program is (Python==3.9.5)\n\
Date: 2022년 3월 9일\n\
----------------------------------'
)
import datetime
d = datetime.datetime.now()

print(
'Homework #1\n\
----------------------------------\n\
My name is (Jong-Wook Kim)\n\
Student\'s ID is (20160768)\n\
Used program is (Python==3.9.5)\n\
Date: (%d년 %d월 %d일)\n\
----------------------------------'
%(d.year,d.month, d.day))
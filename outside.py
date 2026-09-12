"""
Sophia Babayev, Section 10
Use a long exuation to see what the temp calculating feels like.
"""

c1 = -42.379
c2 = 2.04901523
c3 = 10.14333127
c4 = -0.22475541
c5 = -0.00683783
c6 = -0.05481717
c7 = 0.00122874
c8 = 0.00085282
c9 = -0.00000199

T = float(input())
R = float(input())
   
hi = (c1 + c2 * T + c3 * R + c4 * T * R + c5 * (T ** 2) + c6 * (R ** 2) + c7 * (T ** 2) * R + c8 * T * (R ** 2) + c9 * (T ** 2) * (R ** 2))
    

if hi > 100:
  print("too hot?!")
elif 80 <= hi <= 100:
  print("frolic in the fields!")
else:
  print("too cold")
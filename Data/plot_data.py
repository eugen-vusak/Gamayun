import matplotlib.pyplot as plt
from data import Data


fileName = ""
data = Data(fileName, 3000,4);

input, output = data.data_set[0];

i1 = input[::6]
i2 = input[1::6]
i3 = input[2::6]
i4 = input[3::6]
i5 = input[4::6]
i6 = input[5::6]

#print(len(i1),len(i2),len(i3),len(i4),len(i5),len(i6));

#plt.ylim([-20,20])
#	plt.plot(	[x for x in range(len(i1))],
#			i1,
#			label = "x_ac")

#plt.plot(	[x for x in range(len(i2))],
#			i2,
#			label = "y_ac")

#plt.plot(	[x for x in range(len(i3))],
#			i3,
#			label = "z_ac")

plt.plot(	[x for x in range(len(i4))],
			i4,
			label = "x_gy")

#plt.plot(	[x for x in range(len(i5))],
#			i5,
#			label = "y_gy")

#plt.plot(	[x for x in range(len(i6))],
#			i6,
#			label = "z_gy")
plt.legend()
plt.show()
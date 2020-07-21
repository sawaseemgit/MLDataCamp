import matplotlib.pyplot as plt

year = [1960, 1970, 1980, 1990, 2000, 2010, 2020, 2030, 2040, 2050]
pop = [2.615, 3.712, 5.522, 6.345, 7.45, 8.11, 9.87, 10.65, 11.04, 12.85]
# plt.plot(year, pop)
# plt.scatter(year,pop)

# plt.scatter(year, pop )
plt.scatter(x=year, y=pop,   alpha=0.8)
# plt.hist(pop)  # plt.hist(life_exp,bins=20), bins if empty, default=10
plt.xscale('log')
plt.xlabel("Year")
plt.ylabel("Pop")
plt.title("Matplot")

# plt.yticks(['2', '6', '12'], ['2B', '6B', '12B'])
t_val = ['1000', '10000', '100000']
t_lab = ['2B', '6B', '12B']
# plt.xticks(t_val, t_lab)
plt.show()

#!/usr/bin/env python
# coding: utf-8

# In[ ]:


sample_data2 = pd.read_csv("countries.csv")
US = sample_data2[sample_data2.country == 'United States']
South_Africa = sample_data2[sample_data2.country=='South Africa']
plt.plot(US.year,US.population)
plt.plot(South_Africa.year,South_Africa.population)
plt.legend(["This is US's population ","This is South Africa's population"])
plt.xlabel('Year')
plt.ylabel('Population')
plt.show()


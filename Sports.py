#!/usr/bin/env python
# coding: utf-8

# In[16]:


import pandas as pd
import matplotlib.pyplot as plt
# 读取数据集
data = pd.read_csv('athlete_events.csv')
# 输出数据集前5行
display(data.head())


# In[17]:


# 统计各年份参加奥运会的运动员人数
athlete_count = data.groupby('Year')['ID'].nunique()
# 可视化结果
plt.figure(figsize=(10, 6))
plt.plot(athlete_count.index, athlete_count.values)
plt.title('Number of Athletes at the Olympics by Year')
plt.xlabel('Year')
plt.ylabel('Number of Athletes')
plt.show()


# In[18]:


# 统计男女比例
male_count = data[data['Sex'] == 'M'].shape[0]
female_count = data[data['Sex'] == 'F'].shape[0]
labels = ['Male', 'Female']
sizes = [male_count, female_count]
explode = (0, 0.1)
plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
plt.axis('equal')
plt.title('Male vs Female Athletes')
plt.show()


# In[19]:


# 统计历年男性和女性的平均年龄
male_data = data[data['Sex'] == 'M']
female_data = data[data['Sex'] == 'F']
male_age = male_data.groupby('Year')['Age'].mean()
female_age = female_data.groupby('Year')['Age'].mean()
# 绘制折线图
plt.plot(male_age.index, male_age.values, label='Male')
plt.plot(female_age.index, female_age.values, label='Female')
plt.title('Average Age of Male and Female Athletes Over the Years')
plt.xlabel('Year')
plt.ylabel('Average Age')
plt.legend()
plt.show()


# In[20]:


# 统计各国金牌数
gold_medals = data[data['Medal'] == 'Gold']
country_medals = gold_medals.groupby('NOC')['Medal'].count().reset_index(name='Count').sort_values(['Count'], ascending=False).head(10)
plt.bar(country_medals['NOC'], country_medals['Count'])
plt.xticks(rotation=90)
plt.title('Countries with the Most Gold Medals')
plt.xlabel('Country')
plt.ylabel('Gold Medal Count')
plt.show()


# In[21]:


import pandas as pd
import matplotlib.pyplot as plt
# 读取数据集
data = pd.read_csv('athlete_events.csv')
# 统计每个国家的奖牌数
medal_counts = data.groupby('NOC')['Medal'].count().reset_index(name='MedalCount')
# 按奖牌数降序排序并只选择前20名
medal_counts = medal_counts.sort_values(by='MedalCount', ascending=False).head(20)
# 将剩下的国家合并为"Others"
others = pd.DataFrame({
    'NOC': ['Others'],
    'MedalCount': [medal_counts['MedalCount'][20:].sum()]
})
medal_counts = pd.concat([medal_counts.head(20), others])
# 绘制饼图
plt.figure(figsize=(8, 8))
plt.pie(medal_counts['MedalCount'], labels=medal_counts['NOC'], autopct='%1.1f%%')
plt.title('Distribution of Medals by Country (Top 20)')
plt.show()


# In[22]:


# 统计中国历届奥运会获奖数
china_data = data[data['NOC'] == 'CHN']
medal_count = china_data.groupby('Year')['Medal'].value_counts().unstack(fill_value=0)
medal_count.plot(kind='bar', color=['gold', 'silver', 'brown'])
plt.title('Medal Count for China at the Olympics')
plt.xlabel('Year')
plt.ylabel('Medal Count')
plt.legend(['Gold', 'Silver', 'Bronze'])
plt.show()


# In[23]:


# 筛选出中国运动员获奖数据
china_medals = data[(data['NOC'] == 'CHN') & (data['Medal'].notnull())]
# 计算各项目奖牌总数并按降序排列
summer_sports = china_medals[china_medals['Season'] == 'Summer'].groupby('Sport')['Medal'].count().sort_values(ascending=False)[:10]
winter_sports = china_medals[china_medals['Season'] == 'Winter'].groupby('Sport')['Medal'].count().sort_values(ascending=False)[:4]
# 绘制夏季奥运会数据的柱状图
plt.figure(figsize=(10, 6))
plt.bar(summer_sports.index, summer_sports.values)
plt.title('China Olympic Medals in Summer Sports')
plt.xlabel('Sports')
plt.ylabel('Medals')
plt.show()
# 绘制冬季奥运会数据的柱状图
plt.figure(figsize=(6, 6))
plt.bar(winter_sports.index, winter_sports.values)
plt.title('China Olympic Medals in Winter Sports')
plt.xlabel('Sports')
plt.ylabel('Medals')
plt.show()


# In[ ]:





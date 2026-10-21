'''
import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# Load Dataset
# -----------------------------
df = pd.read_csv('Instagram_Analytics.csv')

# -----------------------------
# Create Engagement Column
# -----------------------------
df['engagement'] = df['likes'] + df['comments'] + df['shares'] + df['saves']

# -----------------------------
# Instagram Colors
# -----------------------------
colors = ['#833AB4', '#FD1D1D', '#FCAF45', '#C13584']

# -----------------------------
# Data Preparation
# -----------------------------
bar_data = df.groupby('media_type')['engagement'].mean()
posts_count = df['media_type'].value_counts()

reach = df['reach']
likes = df['likes']
sizes = df['engagement'] / 10

# -----------------------------
# Create Figure
# -----------------------------
plt.figure(figsize=(10, 8))

# -----------------------------
# 1. Bar Chart
# -----------------------------
plt.subplot(2, 2, 1)
plt.bar(bar_data.index, bar_data.values, color=colors)

plt.title("Engagement by Content Type", fontsize=10)
plt.xlabel("Media Type", fontsize=8)
plt.ylabel("Avg Engagement", fontsize=8)

# -----------------------------
# 2. Scatter Plot
# -----------------------------
plt.subplot(2, 2, 2)
plt.scatter(reach, likes, s=sizes, c='#833AB4', alpha=0.7)

plt.title("Reach vs Likes", fontsize=10)
plt.xlabel("Reach", fontsize=8)
plt.ylabel("Likes", fontsize=8)

# -----------------------------
# 3. Pie Chart (WITH LEGEND + SHADOW)
# -----------------------------
plt.subplot(2, 2, 3)
wedges, texts, autotexts = plt.pie(
    posts_count.values,
    labels=None,                 # remove labels from pie
    autopct='%1.1f%%',
    colors=colors,
    shadow=True                 # shadow added
)

# Legend on the right
plt.legend(
    wedges,
    posts_count.index,
    title="Content Type",
    loc="center left",
    bbox_to_anchor=(1, 0.5),
    fontsize=8
)

plt.title("Content Type Distribution", fontsize=10)

# -----------------------------
# 4. Line Chart
# -----------------------------
plt.subplot(2, 2, 4)
plt.plot(df['engagement'].values, color='#FD1D1D')

plt.title("Engagement Trend Over Posts", fontsize=10)
plt.xlabel("Post Index", fontsize=8)
plt.ylabel("Engagement", fontsize=8)

# -----------------------------
# Main Title
# -----------------------------
plt.suptitle("Social Media Trends Analysis (Instagram Case Study)", fontsize=14)

# Adjust layout (extra space for legend)
plt.tight_layout(rect=[0, 0, 0.85, 0.95])

# -----------------------------
# Show Plot
# -----------------------------
plt.show()'''
#

import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# Load Dataset
# -----------------------------
df = pd.read_csv('Instagram_Analytics.csv')

# -----------------------------
# Create Engagement Column
# -----------------------------
df['engagement'] = df['likes'] + df['comments'] + df['shares'] + df['saves']

# -----------------------------
# KPI Calculations
# -----------------------------
total_posts = len(df)
avg_engagement = int(df['engagement'].mean())
max_engagement = int(df['engagement'].max())
avg_reach = int(df['reach'].mean())

# -----------------------------
# Colors (Instagram Theme)
# -----------------------------
colors = ['#833AB4', '#FD1D1D', '#FCAF45', '#C13584']

# -----------------------------
# Data Preparation
# -----------------------------
bar_data = df.groupby('media_type')['engagement'].mean()
posts_count = df['media_type'].value_counts()

reach = df['reach']
likes = df['likes']
sizes = df['engagement'] / 10

top_posts = df.sort_values(by='engagement', ascending=False).head(5)

# -----------------------------
# Create Figure
# -----------------------------
plt.figure(figsize=(14, 10))

# -----------------------------
# KPI TEXT (Top Section)
# -----------------------------
plt.figtext(0.1, 0.95, f"Total Posts: {total_posts}", fontsize=10)
plt.figtext(0.3, 0.95, f"Avg Engagement: {avg_engagement}", fontsize=10)
plt.figtext(0.55, 0.95, f"Max Engagement: {max_engagement}", fontsize=10)
plt.figtext(0.8, 0.95, f"Avg Reach: {avg_reach}", fontsize=10)

# -----------------------------
# 1. Bar Chart
# -----------------------------
plt.subplot(2, 3, 1)
plt.bar(bar_data.index, bar_data.values, color=colors)
plt.title("Avg Engagement by Media Type", fontsize=10)
plt.xlabel("Media Type", fontsize=8)
plt.ylabel("Engagement", fontsize=8)

# -----------------------------
# 2. Scatter Plot
# -----------------------------
plt.subplot(2, 3, 2)
plt.scatter(reach, likes, s=sizes, c='#833AB4', alpha=0.6)
plt.title("Reach vs Likes", fontsize=10)
plt.xlabel("Reach", fontsize=8)
plt.ylabel("Likes", fontsize=8)

# -----------------------------
# 3. Pie Chart
# -----------------------------
plt.subplot(2, 3, 3)
wedges, texts, autotexts = plt.pie(
    posts_count.values,
    labels=None,
    autopct='%1.1f%%',
    colors=colors,
    shadow=True
)

plt.legend(
    wedges,
    posts_count.index,
    loc="center left",
    bbox_to_anchor=(1, 0.5),
    fontsize=8
)

plt.title("Content Distribution", fontsize=10)

# -----------------------------
# 4. Line Chart
# -----------------------------
plt.subplot(2, 3, 4)
plt.plot(df['engagement'].values, color='#FD1D1D')
plt.title("Engagement Trend", fontsize=10)
plt.xlabel("Post Index", fontsize=8)
plt.ylabel("Engagement", fontsize=8)

# -----------------------------
# 5. Horizontal Bar (Top Posts)
# -----------------------------
plt.subplot(2, 3, 5)
plt.barh(top_posts.index.astype(str), top_posts['engagement'], color='#FCAF45')
plt.title("Top 5 Posts by Engagement", fontsize=10)
plt.xlabel("Engagement", fontsize=8)

# -----------------------------
# 6. Histogram
# -----------------------------
plt.subplot(2, 3, 6)
plt.hist(df['engagement'], bins=10, color='#C13584')
plt.title("Engagement Distribution", fontsize=10)
plt.xlabel("Engagement", fontsize=8)
plt.ylabel("Frequency", fontsize=8)

# -----------------------------
# Main Title
# -----------------------------
plt.suptitle("Social Media Trends Dashboard (Instagram Case Study)", fontsize=14)

# Layout Fix
plt.tight_layout(rect=[0, 0, 1, 0.93])

# -----------------------------
# Show Plot
# -----------------------------
plt.show()

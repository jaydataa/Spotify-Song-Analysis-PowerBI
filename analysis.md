# Spotify Song Analysis: Project Overview and Insights

## 1. Project Overview:
In this project, I analysed a Spotify dataset containing various attributes of songs, including audio features, popularity, and genre classification. The primary goal was to explore and gain insights into the characteristics of songs and their relationships with factors such as mood, energy, and tempo.

I used **Power BI** for data visualisation, which allowed me to interact with the data in real-time and uncover trends, patterns, and correlations in a user-friendly and dynamic way.

---

## 2. Data Exploration and Cleaning:

### Data Overview:
The dataset includes the following features for each song:
- **Track Information**: Song name, artist, album, release year, genre, and popularity score.
- **Audio Features**: Danceability, energy, loudness, speechiness, acousticness, instrumentalness, liveness, valence, tempo, and key.
  
### Data Cleaning Steps:
Before starting the analysis, I performed several data cleaning steps:
- **Missing Data**: I handled missing values by either filling them in with the mean or removing rows with critical missing information.
- **Duplicates**: I removed duplicate songs to avoid any biased analysis.
- **Data Types**: I ensured that all columns had the correct data types (e.g., numerical columns, categorical columns).
- **Feature Scaling**: Some features, like energy or tempo, had vastly different ranges, so I scaled them for more consistent comparison.

---

## 3. Feature Engineering and Categorisation:

### Mood and Time of Day Categorisation:
I created **mood categories** for each song based on the `valence` (happiness/positivity) feature:
- **Happy**: Songs with a valence above 0.7, which indicate high positivity and energy.
- **Relaxed**: Songs with valence between 0.3 and 0.7.
- **Sad**: Songs with valence below 0.3, indicating lower energy or more melancholic mood.

Additionally, I created a **Time of Day** classification based on the `tempo` and `energy` features:
- **Morning**: Low to medium energy songs (for relaxed or start-of-day vibes).
- **Afternoon**: High-energy, upbeat songs to match peak productivity hours.
- **Evening**: Mellow songs with medium to low energy for winding down.

These categories allowed me to create a dynamic and interactive visualisation where users could see how different songs fit different times of the day and moods.

---

## 4. Data Visualisation Insights:

### Visualisations Created:
Here are the key visualisations I created to support my analysis:

- **Scatter Plot of Energy vs. Tempo**:
   - This visualisation shows how the **energy** and **tempo** of songs relate to each other. By looking at this graph, we can quickly see that high-energy songs tend to have faster tempos, while more relaxed or sad songs often have slower tempos. 

- **Mood Distribution**:
   - A bar chart that categorises songs into different moods: **Happy**, **Relaxed**, and **Sad** based on their **valence** scores. This helps in understanding which mood is more prevalent in the dataset and how it correlates with other features like energy and tempo.

- **Interactive Time of Day Scatter Plot**:
   - An interactive scatter plot that categorises songs into **Morning**, **Afternoon**, and **Evening**. This allows the user to explore how various features (e.g., loudness, danceability) change throughout the day. The plot also lets users filter and view how songs fit into different time slots.

- **Popularity vs. Features Analysis**:
   - A scatter plot that shows how **track popularity** correlates with other features like **danceability**, **energy**, and **tempo**. From this analysis, we can see if there’s a pattern that certain features (e.g., high danceability or energy) are more likely to result in songs being highly popular on Spotify.

---

## 5. Key Insights and Takeaways:

Here are some of the key insights I discovered from the analysis:

- **Mood and Energy**:
  - High-energy songs are typically categorised as **Happy** and are more commonly associated with **Afternoon** or **Evening** listening times.
  - **Sad** songs, on the other hand, tend to have lower energy and tempo and are often categorised as **Morning** songs.
  
- **Tempo and Time of Day**:
  - Fast-tempo songs are more likely to be categorised as **Afternoon** songs, where people are typically more active and productive.
  - Slow-tempo songs fit more into the **Morning** and **Evening** categories, offering a more relaxed and soothing experience.

- **Track Popularity and Mood**:
  - Popular songs tend to have higher **danceability** and **energy**, suggesting that listeners prefer upbeat songs when engaging with popular music.
  - Surprisingly, **sad** songs with a lower energy level can also achieve high popularity, likely due to their emotional resonance and appeal to specific listeners.

- **Trends Over Time**:
  - From the **Release Year** feature, I observed trends in music over time, such as the increasing popularity of more energetic tracks in recent years, reflecting current music trends.

---

## 6. Conclusion and Future Steps:

This analysis provides valuable insights into the types of songs that are played during different times of the day and their associated moods. The Power BI visualisations I created make this analysis interactive and easily accessible for users who want to explore the data on their own.

### Potential Future Improvements:
- **More Data**: The analysis could be expanded with additional data, such as genre-specific mood analysis or additional features like song length or danceability trends across genres.
- **Machine Learning**: I could explore machine learning techniques to predict the mood of a song or its popularity based on its audio features.
- **User Interaction**: I could improve the interactivity of the Power BI report by adding features such as user input for song recommendations based on selected moods and times of day.

---

## 7. View the Demo:
To see how the visualisations look and interact with the data in real-time, watch the demo video below:
- [Link to Demo Video]

---


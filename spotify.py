import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Drop unnecessary columns
df.drop(columns=['Unnamed: 0', 'image_url', 'spotify_url', 'track_artist_merged', 'tags_tokenized', 'doc_vector', 'combined_vector'], inplace=True)

def classify_time_of_day(row):
    """Classifies a song into Morning, Afternoon, or Evening based on normalized tempo, energy, loudness, and danceability."""
    
    tempo = row['tempo']
    energy = row['energy']
    loudness = row['loudness']
    danceability = row['danceability']

    # MORNING: High-energy, upbeat songs
    if (tempo > 0.6 and energy > 0.6) or (danceability > 0.7 and energy > 0.5):
        return 'Morning'

    # EVENING: Slow, calm, and relaxing songs
    elif (tempo < 0.5 and energy < 0.5) or (loudness < 0.2 and danceability < 0.4):
        return 'Evening'

    # AFTERNOON: Balanced, mid-energy songs
    else:
        return 'Afternoon'

# Apply function
df['time_of_day'] = df.apply(classify_time_of_day, axis=1)

# Check distribution
df['time_of_day'].value_counts()

def classify_mood(row):
    if row['valence'] > 0.7:
        return 'Happy'
    elif row['valence'] < 0.3:
        return 'Sad'
    elif row['valence'] >= 0.3 and row['valence'] <= 0.7:
        return 'Relaxed'

df['Mood'] = df.apply(classify_mood, axis=1)

def classify_popularity(row):
    if row['track_popularity'] < 0.4:
        return 'Low'
    elif row['track_popularity'] < 0.7:
        return 'Medium'
    else:
        return 'High'

df['popularity'] = df.apply(classify_popularity, axis=1)


df.to_csv('enhanced_spotify_songs_with_time_and_mood.csv', index=False)

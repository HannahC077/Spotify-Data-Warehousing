import numpy as np

def min_max_scaling(data):
    min_val = np.min(data)
    max_val = np.max(data)
    normalized_data = (data - min_val) / (max_val - min_val)
    return normalized_data

def z_score_normalization(data):
    mean_val = np.mean(data)
    std_dev = np.std(data)
    normalized_data = (data - mean_val) / std_dev
    return normalized_data

# Example usage
spotify_streams = np.array([100000, 50000, 200000, 30000, 80000])

# Min-Max scaling
min_max_normalized_streams = min_max_scaling(spotify_streams)

# Z-Score normalization
z_score_normalized_streams = z_score_normalization(spotify_streams)

print("Original Spotify Streams:", spotify_streams)
print("Min-Max Normalized Streams:", min_max_normalized_streams)
print("Z-Score Normalized Streams:", z_score_normalized_streams)

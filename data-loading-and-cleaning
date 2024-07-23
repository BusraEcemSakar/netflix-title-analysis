# Load dataset
df = pd.read_csv('data/netflix_titles.csv')

# Handle missing values
df = df.dropna(subset=['title', 'release_year'])
df['title'] = df['title'].fillna('unknown')

# Convert release_year to integer
df['release_year'] = df['release_year'].astype(int)

# Function to clean text
def clean_text(text):
    text = re.sub(r'\d+', '', text)  # Remove numbers
    text = text.lower()  # Convert to lowercase
    text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation
    names_to_remove = ['john', 'jane', 'doe']  # Example names to remove
    text = ' '.join(word for word in text.split() if word not in names_to_remove)
    return text

# Apply text cleaning
df['title'] = df['title'].apply(clean_text)

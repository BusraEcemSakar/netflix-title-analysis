def get_top_words_by_year(df):
    top_words_by_year = {}
    for year in sorted(df['release_year'].unique()):
        titles = df[df['release_year'] == year]['title']
        text = ' '.join(titles)
        
        vectorizer = TfidfVectorizer(stop_words='english', max_features=1000)
        X = vectorizer.fit_transform([text])
        feature_names = vectorizer.get_feature_names_out()
        scores = np.asarray(X.sum(axis=0)).flatten()
        
        word_scores = dict(zip(feature_names, scores))
        top_words_by_year[year] = dict(sorted(word_scores.items(), key=lambda item: item[1], reverse=True)[:10])
    
    return top_words_by_year

top_words_by_year = get_top_words_by_year(df)

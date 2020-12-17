import pandas as pd


def last_support(entry):
    """
    This function returns the last season of friendship. The code is inspired by the provided code from
    the authors
    """
    last_support = None
    for season in entry[:-1]:
        if 'support' in season['interaction'].values():
            last_support = season['season']
    return last_support


def get_first_support(entry):
    """
    This function returns the first season of friendship. 
    """
    for season in entry[:-1]:
        if 'support' in season['interaction'].values():
            return season['season']

    return None


def treat_msg_season(df):
    """
    This function loops over the whole dataset and creates a dictionnary with the set of features for each season 
    with its associated boolean (betrayal or not )
    """
    data_victim = {'features': [], 'betrayed': []}  # data of the (potential) victim
    data_betrayer = {'features': [], 'betrayed': []}  # data of the (potential) betrayer
    for i in range(len(df.seasons.values)):
        entry = df['seasons'][i]  # pick each entry
        for j in range(len(entry)):  # pick each season
            season = entry[j]
            tab_vi = []
            tab_be = []
            if season['season'] <= last_support(entry):  # check if the season is below the last season of friendship
                tab_vi.append(season['messages']['victim'])
                tab_be.append(season['messages']['betrayer'])
                if len(tab_be) != 0 and len(tab_vi) != 0:  # keep only cases where both players have sent messages
                    data_victim['features'].append(tab_vi)
                    data_victim['betrayed'].append(df.betrayal.values[i])
                    data_betrayer['features'].append(tab_be)
                    data_betrayer['betrayed'].append(df.betrayal.values[i])
    return data_victim, data_betrayer


def collect_all_unique_words(message):
    words = message['frequent_words']
    for _, value in message['lexicon_words'].items():
        words += value

    return list(set(words))


def collect_all_disc_words(message):
    words = []
    for _, value in message['lexicon_words'].items():
        words += value
    return words


def to_dict(message):
    sentiment_positive = message['sentiment']['positive']
    sentiment_neutral = message['sentiment']['neutral']
    sentiment_negative = message['sentiment']['negative']
    n_requests = message['n_requests']
    frequent_words = message['frequent_words']
    all_words = collect_all_unique_words(message)
    disc_words = collect_all_disc_words(message)
    n_disc_words = len(collect_all_disc_words(message))
    n_words = message['n_words']
    politeness = message['politeness']
    n_sentences = message['n_sentences']
    return {"sentiment_positive": sentiment_positive,
            "sentiment_neutral": sentiment_neutral,
            'sentiment_negative': sentiment_negative,
            'n_requests': n_requests,
            'frequent_words': frequent_words,
            'n_words': n_words,
            'politeness': politeness,
            'n_sentences': n_sentences,
            'n_disc_words': n_disc_words,
            'disc_words': disc_words,
            'all_words': all_words}


def preprocessing(df):
    result = []
    for row in df.iterrows():
        row = row[1]
        betrayal = row['betrayal']
        idx = row['idx']
        for season in row['seasons']:
            s = season['season']

            last_s = last_support(row['seasons']) + 0.5  # the betrayal occurs one season after the last support
            first_support = get_first_support(row['seasons'])
            if s <= last_support(row['seasons']) and len(season['messages']['betrayer']) and len(
                    season['messages']['victim']):  # here we also have to consider the last season before betrayal
                for m_vic in season['messages']['victim']:
                    data = to_dict(m_vic)
                    data['role'] = 'victim'
                    data['season'] = s
                    data['betrayal'] = betrayal
                    data['season_betrayal'] = last_s
                    data['season_before_betrayal'] = (last_s - s) / 0.5
                    data['idx'] = idx
                    data['friendship_length'] = (last_s - first_support) if first_support else 0
                    result.append(data)
                for m_bet in season['messages']['betrayer']:
                    data = to_dict(m_bet)
                    data['role'] = 'betrayer'
                    data['season'] = s
                    data['betrayal'] = betrayal
                    data['season_betrayal'] = last_s
                    data['season_before_betrayal'] = (last_s - s) / 0.5
                    data['friendship_length'] = (last_s - first_support) if first_support else 0
                    data['idx'] = idx
                    result.append(data)

    return pd.DataFrame(result).set_index(['idx', 'season'])


def get_nb_msg(data):
    """
    Get the mean number of messages sent per season
    """
    tab = []
    for features in data["features"]:
        tab.append(len(features[0]))
    return tab

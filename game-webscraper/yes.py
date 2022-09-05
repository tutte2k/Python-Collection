import pandas as pd

data = pd.read_csv('names.csv',names=['name', 'Age','Gender','Online','time','Timespan','Batch'])
names = data[['name', 'time', 'Batch']].copy()

df_dict = names.groupby(names.Batch.values).agg(list).to_dict('records')

scrapes = [pd.DataFrame(df) for df in df_dict]
sessions = pd.DataFrame(columns=['session', 'name', 'login', 'logout'])
for i in range(len(scrapes) - 1):
    prev_scrape = scrapes[i]
    current_scrape = scrapes[i+1]    
    # Add a new sessions for all users that where not online last scrape
    for _, current_name in current_scrape['name'].iteritems():
        if prev_scrape[prev_scrape['name'] == current_name].empty:
            # Find at which batch the user went offline
            for scrape_to_check_if_still_online in scrapes[i+1:]:   
                if scrape_to_check_if_still_online[scrape_to_check_if_still_online['name'] == current_name].empty:
                    new_entry = {
                        'session': len(sessions[sessions['name'] == current_name].index),
                        'name': current_name,
                        'login': current_scrape['time'].iloc[0],
                        'logout': scrape_to_check_if_still_online['time'].iloc[0]
                    }
                    sessions = sessions.append(new_entry, ignore_index=True)
                    break
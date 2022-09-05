import pandas as pd


def main():
    wanted_data_sessions = pd.DataFrame({
        "session": [    0,      0,       0,       0,     1],
        "name":    ["tom", "linn", "sigge", "selma", "tom"],
        "login":   [   10,     10,      20,      30,    50],
        "logout":  [   30,     50,      30,      50,    60],
    })

    scrapes = [
        pd.DataFrame({
            "name": ["tom", "linn"],
            "time": [10, 10],
        }),
        pd.DataFrame({
            "name": ["tom", "linn", "sigge"],
            "time": [20, 20, 20],
        }),
        pd.DataFrame({
            "name": ["tom", "linn", "sigge", "selma"],
            "time": [30, 30, 30, 30],
        }),
        pd.DataFrame({
            "name": ["linn", "selma"],
            "time": [40, 40],
        }),
        pd.DataFrame({
            "name": ["tom", "linn", "selma"],
            "time": [50, 50, 50],
        }),
        pd.DataFrame({
            "name": ["tom"],
            "time": [60],
        }),
    ]

    sessions = pd.DataFrame(columns=['session', 'name', 'login', 'logout'])
    previous_time = 0
    for scrape in scrapes:
        for index, row in scrape.iterrows():
            name = row['name']
            time = row['time']

            current_session_for_name_filter = (sessions['name'] == name) & (sessions['logout'] == previous_time)
            matching_row = sessions[current_session_for_name_filter]
            if not matching_row.empty:
                # Update logout time, the user has not logged out yet
                sessions.loc[current_session_for_name_filter, 'logout'] = time
            else:
                # Create a new session, the user was not logged in previous scrape
                new_entry = {
                    'session': len(sessions[sessions['name'] == name].index),
                    'name': name,
                    'login': time,
                    'logout': time
                }
                sessions = sessions.append(new_entry, ignore_index=True)
        previous_time = scrape['time'].iloc[0]

    print("###")
    print("## Result")
    print("###")
    print(sessions)
    print("\n")

    print("###")
    print("## Wanted result")
    print("###")
    print(wanted_data_sessions)


if __name__ == '__main__':
    main()
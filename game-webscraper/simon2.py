import pandas as pd


def main():
    wanted_data_sessions = pd.DataFrame({
        "session": [    0,      0,       0,       0,     1],
        "name":    ["tom", "linn", "sigge", "selma", "tom"],
        "login":   [   10,     10,      20,      30,    50],
        "logout":  [   30,     50,      30,      50,    60],
    })

    scrapes = [
        # Add empty scrape to beginning of scrapes for the algorithm to work
        pd.DataFrame(columns=['name', 'time']),
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
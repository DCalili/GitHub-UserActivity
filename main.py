import sys
import requests


def main():
    get_user_events(sys.argv[1])

def get_user_events(username):
    url = f"https://api.github.com/users/{username}/events"
    
    response = requests.get(url)
    
    events = []

    data = response.json()
    
    for event in data:
        eventName = event["type"]
        if eventName == "CreateEvent":
           if event["payload"]["ref_type"] == "repository":
               events.append(f"Created the repo {event['repo']['name']}")
           else:
               events.append(f"Created a {event['payload']['ref_type']} in the repo {event['repo']['name']}")
        elif eventName == "DeleteEvent":
            if event["payload"]["ref_type"] == "repository":
                events.append(f"Deleted the repo {event['repo']['name']}")
            else:
                events.append(f"Deleted a {event['payload']['ref_type']} in the repo {event['repo']['name']}")
        elif eventName == "ForkEvent":
            events.append(f"Created a fork of {event['payload']['forkee']['name']}")

 
    for event in events:
        print(event)
if __name__ == "__main__":
    main()

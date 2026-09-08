import requests

def get_global_news(topic):
    api_key = 'cac9a9a79956423e81f1f13a49dde7b2'  # using the API key
    url = (
        f'https://newsapi.org/v2/everything?'#breaks the url into key value pairs which is easier to read
        f'q={topic}&'
        f'sortBy=publishedAt&'
        f'language=en&'
        f'apiKey={api_key}'
    )

    try:#try to get a response
        response = requests.get(url)#response code of the GET request
        response.raise_for_status()
        data = response.json()#data from the JSON will be used

        articles = data.get('articles', [])
        if not articles:#if no artciles can be found for the topic in question then it will infrom the user
            print(f"No global news found for topic: {topic}")
            return
        if topic=='general':# if topic is, which is the default in taskhub it will print this message instead
            print(f"\nTop global news today:\n")
        else:
            print(f"\nTop Global News on '{topic.capitalize()}':\n")
        for i, article in enumerate(articles[:5], start=1):#enumerates the dictionary whcih is like a numerical loop
            title = article.get('title', 'No title')# - try to get the title key from the article dictionary and if the title is missing, default to No title.
            source = article.get('source', {}).get('name', 'Unknown source')#same for ech case
            published = article.get('publishedAt', 'Unknown date')
            print(f"{i}. {title} ({source}, {published})")#prints all info found for each article

    except requests.exceptions.RequestException as e:
        print(f"Network error: {e}")#Handles network errors (connection problems, timeouts).
    except ValueError:
        print("Failed to parse response.")# checks for errors during response parsing such as JSON decoding failing.
    except Exception as e: # catches any other unexpected exceptions that may occur.
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    topic = input("Enter a topic to search global news for: ")
    get_global_news(topic)
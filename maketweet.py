# importing tweepy
import tweepy
# importing time module
import time
# input the list of profiles for citations
citations = ["ticapsoriginal", "wallarm", "gptchats", "riaa", "macports"]


# input the twitter dev Credintials
client = tweepy.Client(
    consumer_key="INPUT YOUR CONSUMER KEY",
    consumer_secret="INPUT YOUR CONSUMER SECRET",
    access_token="INPUT YOUR ACESS TOKEN",
    access_token_secret="INPUT YOUR TOKEN SECRET"
    )


# start loop for many posts
for item in citations:
    networkpage = item
    up = f"🧢  {networkpage} Ticapsoriginal Networking page" \
        f" 🧢  🆙  @{networkpage} 🆙 " \
        f"🧢 @ticapsoriginal #Professional #networking #software #{networkpage}"
    linktosite = f"https://www.ticapsoriginal.com/en/{networkpage}/"
    # make tweet
    response = client.create_tweet(text=up+linktosite)
    # awaiting time for next tweet
    time.sleep(80)

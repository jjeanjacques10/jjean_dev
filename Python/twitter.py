# Author: Jean J Barros
# Github: https://github.com/jjeanjacques10/

# --- Pesquisando usuários no Twitter ---
import tweepy

# Para ter acesso as keys entre em: https://dev.twitter.com/apps
consumer_key=""
consumer_secret=""

access_token=""
access_token_secret=""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# Coletando informações da conta do twitter
print(api.get_user('jeanjacques1999'))
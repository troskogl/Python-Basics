# PublishTwitter.py

# Consumer Key (API Key) n7iOpF4AkVGbNyC31NcK0JqGg
# Consumer Secret (API Secret) H5GkAegZwHZztjPu4gM1STbUDpLaKzCY8z3lFk1M4Dw9iyqGTF

# Access Token 786244434530676740-MEQwTPn6dkCuAehzMtyKKPFJZCOyGw7
# Access Token Secret 8ZVpMbwKzhSjPLXjgkmXoVCnKWwQ4yAotWHZCc6HbMDxn
# Access Level Read and write
# Owner NwbieProgrmr
# Owner ID 786244434530676740

import tweepy

def get_api(cfg):
  auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
  auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
  return tweepy.API(auth)

def main():
  # Fill in the values noted in previous step here
  cfg = { 
    "consumer_key"        : "n7iOpF4AkVGbNyC31NcK0JqGg",
    "consumer_secret"     : "H5GkAegZwHZztjPu4gM1STbUDpLaKzCY8z3lFk1M4Dw9iyqGTF",
    "access_token"        : "786244434530676740-MEQwTPn6dkCuAehzMtyKKPFJZCOyGw7",
    "access_token_secret" : "8ZVpMbwKzhSjPLXjgkmXoVCnKWwQ4yAotWHZCc6HbMDxn" 
    }

  api = get_api(cfg)
  tweet = "Second Python Tweet"
  status = api.update_status(status=tweet) 
  # Yes, tweet is called 'status' rather confusing


if __name__ == "__main__":
  main()
else:
  print("I do understand, it is always false")
# message = raw_input("Tast inn melding: ")
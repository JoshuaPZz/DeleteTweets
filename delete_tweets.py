import json
import tweepy
from omegaconf import DictConfig
import hydra
from datetime import datetime

@hydra.main(config_path="conf", config_name="config", version_base=None)
def delete_tweets(cfg: DictConfig):
    # 1) Autenticación clásica OAuth 1.0a (API v1.1)
    creds = cfg.twitter
    auth = tweepy.OAuth1UserHandler(
        creds.api_key,
        creds.api_secret,
        creds.access_token,
        creds.access_token_secret
    )
    api = tweepy.API(auth)

    # 2) Leer el archivo JS con JSON dentro
    with open("tweet-headers.js", "r", encoding="utf-8") as f:
        raw = f.read()
    start = raw.find('[')
    end = raw.rfind(']') + 1
    if start == -1 or end == 0:
        raise ValueError("No se encontró contenido JSON válido.")
    json_text = raw[start:end]
    tweets_wrapped = json.loads(json_text)

    # 3) Fecha límite: solo eliminar antes de esta fecha
    cutoff_date = datetime.strptime("2024-06-06", "%Y-%m-%d")

    # 4) Iterar y eliminar
    for entry in tweets_wrapped:
        tweet_obj = entry.get("tweet", {})
        tweet_id = tweet_obj.get("tweet_id")
        
        if not tweet_id:
            print("⚠️  Entrada sin tweet_id, skip:", entry)
            continue

        # Fecha de creación
        created_at_str = tweet_obj.get("created_at")
        is_retweet = "retweeted_status" in tweet_obj or tweet_obj.get("text", "").startswith("RT @")

        if not created_at_str:
            print(f"⚠️  Sin fecha en {tweet_id}, skip.")
            continue

        try:
            created_at = datetime.strptime(created_at_str, "%a %b %d %H:%M:%S +0000 %Y")
        except ValueError as e:
            print(f"⚠️  Fecha inválida en {tweet_id}: {e}")
            continue

        # Filtro de eliminación
        if not is_retweet and created_at < cutoff_date:
            try:
                api.destroy_status(tweet_id)
                print(f"✅ Tweet {tweet_id} eliminado (API v1.1).")
            except Exception as e:
                print(f"❌ Error eliminando {tweet_id}: {e}")
        else:
            print(f"⏩ Skip {tweet_id}: {'retweet' if is_retweet else 'fecha posterior'}")

if __name__ == "__main__":
    delete_tweets()

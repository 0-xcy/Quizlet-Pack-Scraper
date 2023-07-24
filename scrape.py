import threading
import requests
import json
from concurrent.futures import ThreadPoolExecutor

bearertoken = ''
cfbm = ""

def scrape_pack(packID):
    try:
        url = f"https://api.quizlet.com/3.9/terms?filters%5BsetId%5D={packID}&include%5Bterm%5D%5B%5D=definitionImage&include%5Bterm%5D%5B%5D=wordCustomAudio&include%5Bterm%5D%5B%5D=definitionCustomAudio&include%5Bterm%5D%5Bset%5D%5B%5D=creator&perPage=100"
        payload = {}
        headers = {
            'accept': '*/*',
            'x-quizlet-device-id': '593728E2-8831-4C3E-B267-ADF5CC34D564',
            'cookie': f'__cf_bm={cfbm}',
            'user-agent': 'QuizletIOS/7.40 (QuizletBuild/2; iPhone11,2; iOS 16.3; Scale/3.0)',
            'accept-language': 'en-us',
            'authorization': bearertoken,
        }

        response = requests.get(url, headers=headers, data=payload)

        if response.status_code == 200:
            data = response.json()
            with open(f"./scrapedpacks/{packID}.json", "w") as f:
                json.dump(data, f)
            print(f"{response.status_code} | Successfully scraped pack {packID}")
        else:
            print("Request failed with status code:", response.status_code)

    except Exception as e:
        print(f"Error occurred while processing pack {packID}: {e}")

def main(num_threads):
    with open("packlist.txt", "r") as f:
        pack_ids = [line.split("https://quizlet.com/")[1].split("/")[0] for line in f]

    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        executor.map(scrape_pack, pack_ids)

if __name__ == "__main__":
    num_threads_to_run = 3 
    main(num_threads_to_run)
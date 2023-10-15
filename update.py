import requests
import yaml

def get_version_from_url(url):
    # URL에서 데이터 가져오기
    response = requests.get(url)
    if response.status_code != 200:
        raise ValueError(f"Failed to get data from the URL. Status code: {response.status_code}")

    # YAML 데이터 파싱하기
    data = yaml.safe_load(response.text)

    # data 양식
    #   - arasaka:
    #     - version: 1.0
    #     - release_date: 2023-10-15
    
    # 버전 정보 가져오기
    version_info = data[0]["arasaka"][0]["version"]
    return version_info

if __name__ == "__main__":
    url = "https://raw.githubusercontent.com/gzgr/arasaka/main/version.yml"

    version_info = get_version_from_url(url)
    if version_info:
        print(f"Version: {version_info}")
    else:
        print("Version information not found.")


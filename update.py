import requests
import yaml

def get_content_from_url(url):
    # URL에서 데이터 가져오기
    response = requests.get(url)
    if response.status_code != 200:
        raise ValueError(f"Failed to get data from the URL. Status code: {response.status_code}")
    return response.text

def get_version_from_url(url):
    # URL에서 데이터 가져오기
    response = requests.get(url)
    if response.status_code != 200:
        raise ValueError(f"Failed to get data from the URL. Status code: {response.status_code}")

    # YAML 데이터 파싱하기
    data = yaml.safe_load(response.text)

    # version 정보 반환하기
    return data.get('arasaka', {}).get('version')

if __name__ == "__main__":
    url = "https://raw.githubusercontent.com/gzgr/arasaka/main/version.yml"
    content = get_content_from_url(url)
    print(content)
    
    version_info = get_version_from_url(url)
    if version_info:
        print(f"Version: {version_info}")
    else:
        print("Version information not found.")


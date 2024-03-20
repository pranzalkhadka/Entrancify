import requests

class Extract:
    def extract(self, url, html_file_path):
        r = requests.get(url, verify=False)
        with open(html_file_path, "wb") as f:
            f.write(r.content)
        print(f"Data extracted successfully from {url} to {html_file_path}")

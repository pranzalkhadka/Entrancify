from bs4 import BeautifulSoup
import csv

class Transform:
    def transform(self, html_file_path, csv_file_path):
        with open(html_file_path, "r", encoding="utf-8") as f:
            html_content = f.read()

        soup = BeautifulSoup(html_content, "html.parser")

        notices = []
        for li in soup.find_all("li"):
            topic = li.find("h5", class_="topic")
            if topic:
                title = topic.text.strip()
                link = li.find("a")["href"] if li.find("a") else "No link available"
                img_src = li.find("img")["src"] if li.find("img") else "No image available"
                notices.append({"Title": title, "Link": link, "Image Source": img_src})

        with open(csv_file_path, "w", newline="", encoding="utf-8") as csvfile:
            fieldnames = ["Title", "Link", "Image Source"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for notice in notices:
                writer.writerow(notice)

        print(f"Data transformed and saved to CSV successfully at {csv_file_path}")

import requests, json,os,time
with open("Download/newfile.json","r") as file:
	api=json.load(file)
chapters=api["volumes"]["none"]["chapters"]

for num,chapter in chapters.items():
	print(f"Opening Chapter {num}..........")
	os.makedirs(f"comics/Nan_Hao_and_Shang_Feng/ Chapter-{num}",exist_ok=True)
	chapter_id=chapter["id"]
	request=requests.get(f"https://api.mangadex.org/at-home/server/{chapter_id}?forcePort443=false")
	request.raise_for_status
	json=request.json()
	base_url=json["baseUrl"]
	hash=json["chapter"]["hash"]
	pages=json["chapter"]["data"]
	n=1
	for page in pages:
		url=base_url + "/data/" + hash + "/"+ page
		print(f"Downloading Chapter {num} page {n}..........")
		image=requests.get(url)
		image.raise_for_status				
		with open(f"comics/Nan_Hao_and_Shang_Feng/ Chapter-{num}/page-{n}.jpg","wb") as file:
			for chunk in image.iter_content(100000):
				file.write(chunk)
		print(f"Chapter {num} page {n} download successful")
		n+=1
	print(f"Chapter {num} completely downloaded")
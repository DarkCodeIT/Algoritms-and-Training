# import requests, aiohttp
# link = "https://gas-kvas.com/uploads/posts/2023-02/1675609610_gas-kvas-com-p-raduzhnoe-zhivotnoe-risunok-49.jpg"
# def down(url: str):

#     try:
#         response = requests.get(url=url, stream=True)

#         with open("res.png", 'wb') as pic:
#             for chunk in response.iter_content(chunk_size= 1024 * 1024):
#                 if chunk:
#                     pic.write(response.content)
#         return "Done"
    
#     except Exception as ex:
#         return f"Some problem {ex}"
    
# print(down(link))

import requests

def download_image_url(url, filename):
    response = requests.get(url)

    #extension = get_file_extension(filename)
    #if not extension:
        #filename += ".png"

    file = open(filename+".png", "wb")
    file.write(response.content)
    file.close()


def get_file_extension(filename):
    return filename.split(".")[-1] if "." in filename else False
    
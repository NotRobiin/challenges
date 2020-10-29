import requests
import os
import time

def get_file_name(out: str, idx: int, fmt: str) -> str:
    return f'{out}{str(idx)}.{fmt}'

def download(file: str) -> None:
    URL = "https://thispersondoesnotexist.com/image"

    with open(file, "wb") as f:
        res = requests.get(URL)
        f.write(res.content)

def cls() -> None:
    os.system('cls')

def get_fake_face(**kwargs) -> None:
    amt = kwargs["amount"]
    out = kwargs["output"]
    fmt = kwargs["format"]
    d = kwargs["delay"]

    for i in range(1, amt + 1):
        cls()

        file_name = get_file_name(out, i, fmt)

        print(f'Downloading: {i}/{amt} ({file_name})...')

        download(file_name)

        if d:
            time.sleep(d)

    cls()
    print("Download completed successfully.")


if __name__ == "__main__":
    get_fake_face(amount = 10,
        output = "C:/users/robertt/desktop/pics/",
        format = "jpg",
        delay = 0.1)

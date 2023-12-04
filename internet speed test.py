import speedtest

def test_internet_speed():

    st_object = speedtest.Speedtest()

    print("testing downloading speed...")
    download_speed = st_object.download()/10**6
    print(f"download speed is {download_speed:.2f} Mbps\n")

    print("testing upload speed...")
    upload_speed = st_object.upload()/10**6
    print(f"upload speed is {upload_speed:.2f} Mbps")

if __name__ == "__main__":
    test_internet_speed()
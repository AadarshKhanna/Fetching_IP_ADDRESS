import socket

def get_ip_address(url):
    try:
        ip_address = socket.gethostbyname(url)
        return ip_address
    except socket.error as e:
        return f"Error: {e}"

def main():
    website_url = "www.xyz.com" 
    ip_address = get_ip_address(website_url)

    if not ip_address.startswith("Error"):
        print(f"The IP address of {website_url} is: {ip_address}")
    else:
        print(f"Failed to retrieve IP address. {ip_address}")

if __name__ == "__main__":
    main()

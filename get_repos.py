import re

def extract_repo_urls(bitbucket_url):
    # Regular expression pattern for Bitbucket repository URLs
    pattern = r"https?://bitbucket\.org/([a-zA-Z0-9_\-]+)/([a-zA-Z0-9_\-]+)"
    
    # Find all matches in the provided URL
    matches = re.findall(pattern, bitbucket_url)
    
    # Construct repository URLs from matches
    repo_urls = [f"https://bitbucket.org/{match[0]}/{match[1]}" for match in matches]

    return repo_urls

# Example usage
bitbucket_url = "Some text containing https://bitbucket.org/username/repo_name and other URLs"
print(extract_repo_urls(bitbucket_url))

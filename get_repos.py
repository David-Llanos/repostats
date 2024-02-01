import re

def extract_repo_urls(text):
    # Regular expression pattern for your custom Bitbucket repository URLs
    pattern = r"https?://bitbucket\.mycompany\.org/scm/([a-zA-Z0-9_\-]+)/([a-zA-Z0-9_\-]+)\.git"
    
    # Find all matches in the provided text
    matches = re.findall(pattern, text)
    
    # Construct repository URLs from matches
    repo_urls = [f"https://bitbucket.mycompany.org/scm/{match[0]}/{match[1]}.git" for match in matches]

    return repo_urls

# Example usage
text = "Some text containing https://bitbucket.mycompany.org/scm/myoffice/project1.git and other URLs"
print(extract_repo_urls(text))

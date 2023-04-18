import random

def generate_user_agent(os='all', browser='all'):
    os_choices = {
        'windows': ['Windows NT 6.1', 'Windows NT 6.2', 'Windows NT 10.0'],
        'mac': ['Macintosh; Intel Mac OS X 10_15_7', 'Macintosh; Intel Mac OS X 10_14_6'],
        'linux': ['X11; Linux x86_64', 'X11; Ubuntu; Linux i686']
    }

    browser_choices = {
        'chrome': 'Mozilla/5.0 ({os}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_version} Safari/537.36',
        'firefox': 'Mozilla/5.0 ({os}; rv:{firefox_version}) Gecko/20100101 Firefox/{firefox_version}',
        'safari': 'Mozilla/5.0 ({os}) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/{safari_version} Safari/605.1.15'
    }

    if os == 'all':
        os = random.choice(list(os_choices.keys()))

    if browser == 'all':
        browser = random.choice(list(browser_choices.keys()))

    os_choice = random.choice(os_choices[os])

    if browser == 'chrome':
        chrome_version = f"{random.randint(64, 90)}.0.{random.randint(1000, 9999)}.0"
        return browser_choices['chrome'].format(os=os_choice, chrome_version=chrome_version)

    if browser == 'firefox':
        firefox_version = f"{random.randint(50, 90)}.0"
        return browser_choices['firefox'].format(os=os_choice, firefox_version=firefox_version)

    if browser == 'safari':
        safari_version = f"{random.randint(12, 15)}.0.{random.randint(1, 7)}"
        return browser_choices['safari'].format(os=os_choice, safari_version=safari_version)

# Example usage
user_agent = generate_user_agent(os='windows', browser='chrome')
print(user_agent)

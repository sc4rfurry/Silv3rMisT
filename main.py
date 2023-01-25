#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
from dotenv import load_dotenv
import os
from platform import system
from sys import exit as ext
from time import sleep
import email_validator
import ipaddress
import curses
import openai


# Load environment variables
# Safely load environment variables from .env file
load_dotenv()
# Suppress insecure request warning from requests module
requests.packages.urllib3.disable_warnings()
# Initialize curses library and create a window
stdscr = curses.initscr()
# Show the cursor on the screen and make it blink (if possible)
curses.curs_set(1)
# enable the keypad
stdscr.keypad(True)



def ctrl_c_exception(stdscr):
    curses.endwin()
    ext()


def check_api_keys():
    not_set_api_keys = []
    api_keys = ["HUNTER_API_KEY", "CLEARBIT_API_KEY", "OPENAI_API_KEY"]
    try:
        for api_key in api_keys:
            if os.getenv(api_key) == None:
                not_set_api_keys.append(api_key)
        
        if len(not_set_api_keys) > 0:
            print(f"Error: {', '.join(not_set_api_keys)} are not set.")
            ext("Please set the API keys in the .env file.")
        else:
            return True
    except KeyboardInterrupt:
        ctrl_c_exception(stdscr)
    except Exception as e:
        ext(f"Error: {e}")


def mail_validator(email):
    try:
        email_validator.validate_email(email)
        return True
    except KeyboardInterrupt:
        ctrl_c_exception(stdscr)
    except email_validator.EmailNotValidError as e:
        return False
    except Exception as e:
        ext("Error: Unable to validate email address. \nReason: ", e)


def gather_info_email(email):
    if email_validator.validate_email(email) == None:
        ext("Error: Invalid email address.")
    else:
        try:
            api_key = os.getenv("HUNTER_API_KEY")
            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {api_key}"
            }
            response = requests.get("https://api.hunter.io/v2/email-verifier", headers=headers, params={"email":email, "api_key": api_key})
            rate_limit_remaining = response.headers.get('x-rate-limit-remaining')
            if rate_limit_remaining and int(rate_limit_remaining) < 5:
                print(f'Warning: Only {rate_limit_remaining} requests remaining in your rate limit.')
            stdscr.addstr(0, 0, f"Email: {email}")
            stdscr.addstr(2, 0, f"\t\tStatus: {response.json()['data']['status']}")
            stdscr.addstr(3, 0, f"\t\tScore: {response.json()['data']['score']}")
            stdscr.addstr(4, 0, f"\t\tResult: {response.json()['data']['result']}")
            stdscr.addstr(5, 0, f"\t\tDisposable: {response.json()['data']['disposable']}")
            stdscr.addstr(6, 0, f"\t\tWebmail: {response.json()['data']['webmail']}")
            stdscr.addstr(7, 0, f"\t\tSMTP Server: {response.json()['data']['smtp_server']}")
            stdscr.addstr(8, 0, f"\t\tSMTP Check: {response.json()['data']['smtp_check']}")
            stdscr.addstr(8, 0, f"\t\tAccept All: {response.json()['data']['accept_all']}")
            stdscr.addstr(11, 0, f"Press any key to continue...")
            stdscr.refresh()
            stdscr.getkey()
            stdscr.clear()
        except KeyboardInterrupt:
            ctrl_c_exception(stdscr)
        except Exception as e:
            ext(f"Error: {e}")




def gather_info_website(website):
    if "http://" not in website and "https://" not in website:
        website = "https://" + website
        try:
            api_key = os.getenv("CLEARBIT_API_KEY")
            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {api_key}"
            }
            response = requests.get(f"https://company.clearbit.com/v2/companies/find?domain={website}", headers=headers)
            rate_limit_remaining = response.headers.get('x-rate-limit-remaining')
            if rate_limit_remaining and int(rate_limit_remaining) < 5:
                print(f'Warning: Only {rate_limit_remaining} requests remaining in your rate limit.')
            stdscr.addstr(0, 0, f"Website: {website}")
            stdscr.addstr(2, 0, f"\t\tName: {response.json()['name']}")
            stdscr.addstr(3, 0, f"\t\tDescription: {response.json()['description']}")
            stdscr.addstr(5, 0, f"\t\tLocation: {response.json()['location']}")
            stdscr.addstr(7, 0, f"\t\tPhone: {response.json()['phone']}")
            stdscr.addstr(8, 0, f"\t\tTwitter: {response.json()['twitter']}")
            stdscr.addstr(9, 0, f"\t\tFacebook: {response.json()['facebook']}")
            stdscr.addstr(10, 0, f"\t\tLinkedIn: {response.json()['linkedin']}")
            stdscr.addstr(11, 0, f"\t\tCrunchbase: {response.json()['crunchbase']}")
            stdscr.addstr(15, 0, f"\t\tTags: {response.json()['tags']}")
            stdscr.addstr(16, 0, f"\t\tTech: {response.json()['tech']}")
            stdscr.addstr(17, 0, f"\t\tMetrics: {response.json()['metrics']}")
            stdscr.refresh()
            stdscr.getkey()
            stdscr.clear()
        except KeyboardInterrupt:
            ctrl_c_exception(stdscr)
        except Exception as e:
            ext(f"Error: {e}")
    else:
        try:
            api_key = os.getenv("CLEARBIT_API_KEY")
            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {api_key}"
            }
            response = requests.get(f"https://company.clearbit.com/v2/companies/find?domain={website}", headers=headers)
            rate_limit_remaining = response.headers.get('x-rate-limit-remaining')
            if rate_limit_remaining and int(rate_limit_remaining) < 5:
                print(f'Warning: Only {rate_limit_remaining} requests remaining in your rate limit.')
            stdscr.addstr(0, 0, f"Website: {website}")
            stdscr.addstr(2, 0, f"\t\tName: {response.json()['name']}")
            stdscr.addstr(3, 0, f"\t\tDescription: {response.json()['description']}")
            stdscr.addstr(5, 0, f"\t\tLocation: {response.json()['location']}")
            stdscr.addstr(7, 0, f"\t\tPhone: {response.json()['phone']}")
            stdscr.addstr(8, 0, f"\t\tTwitter: {response.json()['twitter']}")
            stdscr.addstr(9, 0, f"\t\tFacebook: {response.json()['facebook']}")
            stdscr.addstr(10, 0, f"\t\tLinkedIn: {response.json()['linkedin']}")
            stdscr.addstr(11, 0, f"\t\tCrunchbase: {response.json()['crunchbase']}")
            stdscr.addstr(15, 0, f"\t\tTags: {response.json()['tags']}")
            stdscr.addstr(16, 0, f"\t\tTech: {response.json()['tech']}")
            stdscr.addstr(17, 0, f"\t\tMetrics: {response.json()['metrics']}")
            stdscr.refresh()
            stdscr.getkey()
            stdscr.clear()
        except KeyboardInterrupt:
            ctrl_c_exception(stdscr)
        except Exception as e:
            ext(f"Error: {e}")


def gather_info_ip(ip):
    if ipaddress.ip_address(ip) == None:
        ext("Error: Invalid IP address.")
    else:
        try:
            response = requests.get(f"http://ip-api.com/json/{ip}")
            stdscr.addstr(0, 0, f"IP: {ip}")
            stdscr.addstr(2, 0, f"\t\tStatus: {response.json()['status']}")
            stdscr.addstr(3, 0, f"\t\tCountry: {response.json()['country']}")
            stdscr.addstr(4, 0, f"\t\tCountry Code: {response.json()['countryCode']}")
            stdscr.addstr(5, 0, f"\t\tRegion: {response.json()['region']}")
            stdscr.addstr(6, 0, f"\t\tRegion Name: {response.json()['regionName']}")
            stdscr.addstr(7, 0, f"\t\tCity: {response.json()['city']}")
            stdscr.addstr(8, 0, f"\t\tZip: {response.json()['zip']}")
            stdscr.addstr(9, 0, f"\t\tLat: {response.json()['lat']}")
            stdscr.addstr(10, 0, f"\t\tLon: {response.json()['lon']}")
            stdscr.addstr(11, 0, f"\t\tTimezone: {response.json()['timezone']}")
            stdscr.addstr(12, 0, f"\t\tISP: {response.json()['isp']}")
            stdscr.addstr(13, 0, f"\t\tOrg: {response.json()['org']}")
            stdscr.addstr(14, 0, f"\t\tAS: {response.json()['as']}")
            stdscr.addstr(18, 0, f"Press any key to continue...")
            stdscr.refresh()
            stdscr.getkey()
            stdscr.clear()
        except KeyboardInterrupt:
            ctrl_c_exception(stdscr)
        except Exception as e:
            ext(f"Error: {e}")
    


def gather_info(query):
    try:
        api_key = os.getenv("OPENAI_API_KEY")
        openai.api_key = api_key
        model = "text-davinci-003"
        response = openai.Completion.create(
            engine=model,
            prompt=str(query),
            max_tokens=3000,
            temperature=0.5,
        )
        stdscr.addstr(0, 0, f"\tQuery: {query}")
        stdscr.addstr(2, 0, f"\t\tResponse: {response['choices'][0]['text']}")
        stdscr.addstr(18, 0, f"Press any key to continue...")
        stdscr.refresh()
        stdscr.getkey()
        stdscr.clear()
    except openai.APIError as e:
        ext(f"OpenAI Error: {e}")
    except KeyboardInterrupt:
        ctrl_c_exception(stdscr)
    except Exception as e:
        ext(f"Error: {e}")




def stdscr_api_keys(stdscr):
    stdscr.clear()
    try:
        stdscr.addstr(0, 1, "   _____ _ _      ____       __  __ _  _______ ") 
        stdscr.addstr(1, 1, "  / ____(_) |    |___ \     |  \/  (_)|__   __|")
        stdscr.addstr(2, 1, " | (___  _| |_   ____) |_ __| \  / |_ ___| |   ")
        stdscr.addstr(3, 1, "  \___ \| | \ \ / /__ <| '__| |\/| | / __| |   ")
        stdscr.addstr(4, 1, "  ____) | | |\ V /___) | |  | |  | | \__ \ |   ")
        stdscr.addstr(5, 1, " |_____/|_|_| \_/|____/|_|  |_|  |_|_|___/_|   ")
        stdscr.addstr(6, 1, "")
        stdscr.addstr(8, 1, "Checking API keys...")
        progress = "|"
        for i in range(20):
            stdscr.addstr(9, 1, progress)
            stdscr.refresh()
            progress += "="
            sleep(0.1)
        
        if check_api_keys():
            stdscr.addstr(9, 1, "All API keys are valid.")
            stdscr.addstr(10, 1, "Press any key to continue...")
            stdscr.getch()
            curses_menu(stdscr)
        else:
            stdscr.addstr(9, 1, "One or more API keys are invalid.")
            stdscr.addstr(10, 1, "Press any key to Exit...")
            stdscr.getch()
            ext()
    except KeyboardInterrupt:
        ctrl_c_exception(stdscr)
    except Exception as e:
        ext(f"Error: {e}")



def curses_menu(stdscr):
    stdscr.clear()
    try:
        while True:
            stdscr.addstr(0, 1, "   _____ _ _      ____       __  __ _  _______ ") 
            stdscr.addstr(1, 1, "  / ____(_) |    |___ \     |  \/  (_)|__   __|")
            stdscr.addstr(2, 1, " | (___  _| |_   ____) |_ __| \  / |_ ___| |   ")
            stdscr.addstr(3, 1, "  \___ \| | \ \ / /__ <| '__| |\/| | / __| |   ")
            stdscr.addstr(4, 1, "  ____) | | |\ V /___) | |  | |  | | \__ \ |   ")
            stdscr.addstr(5, 1, " |_____/|_|_| \_/|____/|_|  |_|  |_|_|___/_|   ")
            stdscr.addstr(6, 1, "")
            stdscr.addstr(8, 1, "Name: Silv3rMisT - Information Gathering Suite")
            stdscr.addstr(9, 1, "Version: 1.0")
            stdscr.addstr(10, 1, "Author: @sc4rfurry")
            stdscr.addstr(11, 1, "Github: https://github.com/sc4rfurry/silv3rmist")
            stdscr.addstr(12, 1, "Description: Silv3rMisT gathers information about a person, organization, email address, website, company, or IP address.")
            stdscr.addstr(15, 1, "=" * 120 + "")
            stdscr.addstr(16, 1, "\t1. Gather information about an email address")
            stdscr.addstr(17, 1, "\t2. Gather information about a website")
            stdscr.addstr(18, 1, "\t3. Gather information about a company - (Not yet implemented)")
            stdscr.addstr(19, 1, "\t4. Gather information about an IP address")
            stdscr.addstr(20, 1, "\t5. Gather information about a person or organization")
            stdscr.addstr(21, 1, "\t6. Exit")
            stdscr.addstr(24    , 1, "\t\tEnter your choice: ")
            stdscr.refresh()
            choice = stdscr.getstr().decode()
            if choice == "1":
                stdscr.clear()
                stdscr.addstr(1, 1, "Enter an email address to gather information about: ")
                stdscr.refresh()
                email = stdscr.getstr().decode()
                stdscr.clear()
                if mail_validator(email):
                    stdscr.refresh()
                    stdscr.clear()
                    gather_info_email(email)
                else:
                    stdscr.addstr(1, 1, "Email address is invalid.")
                    stdscr.refresh()
                    stdscr.getch()
                    stdscr.clear()
            elif choice == "2":
                stdscr.clear()
                stdscr.addstr(1, 1, "Enter a website to gather information about: ")
                website = stdscr.getstr().decode()
                stdscr.clear()
                if website:
                    gather_info_website(website)
                else:
                    stdscr.addstr(1, 1, "Website is invalid.")
                    stdscr.refresh()
                    stdscr.getch()
                    stdscr.clear()
            elif choice == "3":
                stdscr.clear()
                stdscr.addstr(1, 1, "Enter a company to gather information about: ")
                stdscr.refresh()
                company = stdscr.getstr().decode()
                stdscr.clear()
                if company:
                    stdscr.addstr(1, 1, "Not implemented yet.")
                    stdscr.refresh()
                    stdscr.getch()
                    stdscr.clear()
                else:
                    stdscr.addstr(1, 1, "Company is invalid.")
                    stdscr.refresh()
                    stdscr.getch()
                    stdscr.clear()
            elif choice == "4":
                stdscr.clear()
                stdscr.addstr(1, 1, "Enter an IP address to gather information about: ")
                stdscr.refresh()
                ip = stdscr.getstr().decode()
                stdscr.clear()
                try:
                    ipaddress.ip_address(ip)
                    gather_info_ip(ip)
                except ValueError:
                    stdscr.addstr(1, 1, "IP address is invalid.")
                    stdscr.refresh()
                    stdscr.getch()
                    stdscr.clear()
            elif choice == "5":
                stdscr.clear()
                stdscr.addstr(1, 1, "Enter a query to gather information about: ")
                stdscr.refresh()
                query = stdscr.getstr().decode()
                stdscr.clear()
                if query:
                    gather_info(query)
                    stdscr.refresh()
                    stdscr.getch()
                    stdscr.clear()
                else:
                    stdscr.addstr(1, 1, "Person or organization is invalid.")
                    stdscr.refresh()
                    stdscr.getch()
                    stdscr.clear()
            elif choice == "6":
                stdscr.clear()
                stdscr.addstr(1, 1, "Are you sure you want to exit? (y/n): ")
                stdscr.refresh()
                exit = stdscr.getstr().decode()
                if exit == "y" or exit == "Y":
                    ext()
                elif exit == "n" or exit == "N":
                    stdscr.clear()
                    stdscr.refresh()
                else:
                    stdscr.clear()
                    stdscr.addstr(1, 1, "Invalid Option: Choice y/n.")
                    sleep(1)
                    stdscr.clear()
                    stdscr.refresh()
            else:
                stdscr.clear()
                stdscr.addstr(1, 1, "Invalid choice.")
                stdscr.addstr(2, 1, "Press Enter to continue...")
                stdscr.refresh()
                stdscr.getch()
                stdscr.clear()
        
            curses.endwin()
    except KeyboardInterrupt:
        ctrl_c_exception(stdscr)
    except Exception as e:
        print(e)
        curses.endwin()
        ext()


def main():
    try:
        stdscr_api_keys(stdscr)
    except KeyboardInterrupt:
        ctrl_c_exception(stdscr)
    except Exception as e:
        ext(f"Error: {e}")


if __name__ == '__main__':
    main()
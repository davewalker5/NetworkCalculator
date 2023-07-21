import sys
from cli.user_input import prompt_for_option
from cli.ipv4_network_details import network_details_main
from cli.ipv4_subnetting import subnetting_main
from cli.ipv4_same_subnet import same_subnet_main

OPTIONS = ["Calculate Network Details", "Subnetting", "Same Subnet"]
PROMPT = "Which calculation do you want to do"


def main():
    if len(sys.argv) == 2:
        while True:
            print()
            print(f"API URL: {sys.argv[1]}")
            print()
            option = prompt_for_option(OPTIONS, PROMPT)
            print()

            if option == 1:
                network_details_main(sys.argv[1])
            elif option == 2:
                subnetting_main(sys.argv[1])
            elif option == 3:
                same_subnet_main(sys.argv[1])
            else:
                break
    else:
        print(f"Usage {sys.argv[0]} api_url")

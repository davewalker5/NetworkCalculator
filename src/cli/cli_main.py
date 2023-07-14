import sys
from cli.user_input import prompt_for_option
from cli.ipv4_network_details import network_details_main
from cli.ipv4_subnetting import subnetting_main

OPTIONS = ["Calculate Network Details", "Subnetting"]
PROMPT = "Which calculation do you want to do"

def main():
    if len(sys.argv) == 3:
        while True:
            print()
            print(f"API Host: {sys.argv[1]}")
            print(f"API Port: {sys.argv[2]}")
            print()
            option = prompt_for_option(OPTIONS, PROMPT)
            print()

            if option == 1:
                network_details_main(sys.argv[1], sys.argv[2])
            elif option == 2:
                subnetting_main(sys.argv[1], sys.argv[2])
            else:
                break
    else:
        print(f"Usage {sys.argv[0]} api_host api_port")

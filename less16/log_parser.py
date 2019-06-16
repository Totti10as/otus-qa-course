"""
Parser
"""
import re
import os
import json
import argparse
from collections import Counter

# ------ GET USER ARGUMENTS FROM THE COMMAND LINE -----------------------------------


def parse_arguments():
    """
    GET USER ARGUMENTS FROM THE COMMAND LINE
    """
    # Initialize the parser
    parser = argparse.ArgumentParser(
        description='Process command line arguments.')
    parser.add_argument(
        '-p', '--path', help='Please indicate the path to the file', type=dir_path)
    parser.add_argument(
        '-f', '--file', help='Please indicate the file name', type=file_name)

    # Parse the arguments and return
    return parser.parse_args()


def dir_path(path):
    """
    Verify is Path
    """
    if os.path.isdir(path):
        return path
    else:
        raise argparse.ArgumentTypeError(
            f"readable_dir:{path} is not a valid path")


def file_name(file):
    """
    Verify is File
    """

    if os.path.isfile(file):
        return file
    else:
        raise argparse.ArgumentTypeError(
            f"readable_file:{file} is not a valid file")

# ------------- GET ALL REQUESTS SUCH AS GET AND POST ------------------------------------------


def get_all_req(filename):
    """
    GET ALL REQUESTS SUCH AS GET AND POST
    """
    regexp_req_type = r'GET|POST|PUT'

    with open(filename) as file:
        log = file.read()
        get_list = re.findall(regexp_req_type, log)
        return get_list

# --------- GET TOP 10 IP'S REQUESTS -------------------------------------------------------


def get_ip_list(filename):
    """
    GET TOP 10 IP'S REQUESTS
    """
    regexp_ip = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'

    with open(filename) as file:
        log = file.read()
        get_list = re.findall(regexp_ip, log)
        return get_list

# --------- GET LIST OF CLIENT ERRORS  ---------------------------------------------------------


def get_all_4xx_err(filename):
    """
     GET LIST OF CLIENT ERRORS
    """
    regexp_req_type = r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})+.*(POST|GET)+.*(400|401|403|404)" \
                      r"+.*(http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+)"

    with open(filename) as file:
        log = file.read()
        get_list = re.findall(regexp_req_type, log)
        return get_list

# --------- GET LIST OF SERVER ERRORS  ---------------------------------------------------------


def get_all_5xx_err(filename):
    """
     GET LIST OF SERVER ERRORS
    """
    regexp_req_type = r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})+.*(POST|GET)+.*(500|503|509|598)' \
                      r'+.*(http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+)'

    with open(filename) as file:
        log = file.read()
        get_list = re.findall(regexp_req_type, log)
        return get_list


# --------- Counter - All entities -------------------------------------------------------------


def count_all_ip(get_list):
    """
    Counter - All entities
    """
    count = Counter(get_list)
    return count

# --------- Counter Top 10 entities ------------------------------------------------------------


def count_top10_ip(get_list):
    """
    Counter Top 10 entities
    """
    count = Counter(get_list)
    return count.most_common(10)

# --------- MAIN -------------------------------------------------------------------------------


def main():
    """ Main"""
    log = {}
    parsed_args = parse_arguments()
    res_top_ip = count_top10_ip(get_ip_list(parsed_args.file))
    res_get_post = count_all_ip(get_all_req(parsed_args.file))
    res_all_ent = len(get_ip_list(parsed_args.file))
    res_client_err = count_top10_ip(get_all_4xx_err(parsed_args.file))
    res_server_err = count_top10_ip(get_all_5xx_err(parsed_args.file))

    with open('output.json', 'w') as json_file:
        log['Parsed_log'] = {'Top 10 IPs list': res_top_ip,
                             'Top 10 client errors': res_client_err,
                             'Top 10 server errors': res_server_err,
                             'All GET and POST requests': res_get_post,
                             'All log entities': res_all_ent

                             }
        json.dump(log, json_file, indent=4)


# --------- STRAT ------------------------------------------------------------------------------

if __name__ == "__main__":
    main()

import sys
import getopt
from launchers import config_launcher, query_launcher


def show_usage():
    print('Usage:\n\'main.py -q <query>\' to run with query\n\'main.py -q <config>\' to run with config file')
    print('Without params app runs with \'application.conf\' file as config')
    sys.exit()


def run_application_by_params(argv):
    query = None
    config_file_path = 'application.conf'
    excel_output = False

    opts, args = getopt.getopt(argv, "hxq:c:", ["help", "excel", "query=", "config="])

    for opt, arg in opts:
        if opt in ('-h', '--help'):
            show_usage()
        elif opt in ('-q', '--query'):
            query = arg
        elif opt in ('-c', '--config'):
            config_file_path = arg
        elif opt in ('-x', '--excel'):
            excel_output = True

    if query:
        query_launcher.start_app_with_query(query, excel_output)
    else:
        config_launcher.start_app_with_config(config_file_path, excel_output)


if __name__ == "__main__":
    run_application_by_params(sys.argv[1:])

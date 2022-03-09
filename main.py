import argparse

from project0 import downloader, parser, storer


def main(url):
    # Download data
    incident_data = downloader.fetch_incidents(url)
    if(incident_data is None):
        print('Something unexpected hapenned!')
        return
    
    # Extract data
    incidents = parser.extract_incidents(incident_data)

    # Create new database
    db = storer.create_db()
    inserted_count = db.add_incidents(incidents)

    if(inserted_count == -1):
        print('Something unexpected hapenned!')
        return

    print(f'\n{db.get_stats()}')


if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("--incidents", type=str, required=True,
                            help="Incident summary url.")

    args = arg_parser.parse_args()
    if args.incidents:
        main(args.incidents)

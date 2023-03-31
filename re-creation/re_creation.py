from subprocess import call

#Web Scraper for general player data
call(["python", "helper_py/general_webscraper.py"])
#Web Scraper for stat-leader data
call(["python", "helper_py/leader_webscraper.py"])
#Web Scraper for HoF condition
call(["python", "helper_py/hof_webscraper.py"])
#File Formatter for all_def csv
call(["python", "helper_py/alldef_formatter.py"])
#File Cleaner for data csv's
call(["python", "helper_py/file_cleaner.py"])
#Data Consolidator into one csv
call(["python", "helper_py/data_consolidator.py"])



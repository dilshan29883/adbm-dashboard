def format_date(date):
    return date.strftime("%Y-%m-%d")

def log_error(error_message):
    with open("error.log", "a") as log_file:
        log_file.write(f"{error_message}\n")
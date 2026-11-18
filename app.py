import csv

input_file = "Sales.csv"
error_log = "errors.log"
summary_file = "sales_summary.csv"


def save_summary(summary_dic):
    #writes the summary to the summary file
    pass

def log_error(record, line, error_message):
    #open the error log and record whatever error it is
    pass


def validate_transaction(line_num, record) ->bool:
   #check the record for valid fields
   #if an invalid field is found, call log error with the record, line num and message and return false
   #if no error is found, return true
   pass

def update_summary(rec, dict):
    # assuming record is valid at this point, update or create a record in the dictionary for the product
    pass

def read_sales() -> tuple[dict, int]:
    #loop through file, validate each record
    #if valid, update the product sales dictionary appropriately (update summary)
    #if invalid add one to invalid_records 
    product_sales = {}
    invalid_records = 0
    with open(filepath, "r", newline="") as file:
        reader = csv.reader(file)
        header = next(reader)

def display_totals(summary_recs):
    pass

def main():
    summary_recs, error_count = read_sales()
    #save the summary file of products sold
    #print the summary lines (display totals)





if __name__ == "__main__":
    main()
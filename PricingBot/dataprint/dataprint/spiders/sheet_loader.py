import time
import gspread
from datetime import datetime
from oauth2client.service_account import ServiceAccountCredentials


def sheet_loader (data_info, sheet_idx):

    # Get access to Google API
    scope = ['https://www.googleapis.com/auth/spreadsheets',
             "https://www.googleapis.com/auth/drive.file",
             "https://www.googleapis.com/auth/drive"
             ]

    # This credential key is created by Ze
    # If a new Google Sheet file is created, please share to:
    # sheetconnerction@sheetsconnection-354213.iam.gserviceaccount.com

    creds = ServiceAccountCredentials.from_json_keyfile_name('ProductData/creds.json', scope)

    client = gspread.authorize(creds)

    # get access to Google sheet by the id of the product
    sheet = client.open('DataPrint Web Scraper Data Storage ').worksheet(str(sheet_idx))

    # writing to google sheets

    # data_info is our data set, including time, link, title, producer, description and price

    #data_info = [str(product['time']), str(product['link']), str(product['titles']),
                # str(product['producers']), str(product['description']), str(product['prices'])]
    #print(data_info)

    """
    :param data_info: [time, link, title, producer, description, price]
    :param sheet_idx: sheet of this product
    :return: void
    """

    # Get name and url list for adding new products and time cell to update the date
    product_name = data_info[2]
    name_list = sheet.col_values(3)
    product_time = datetime.strptime(data_info[0][0:10], "%m/%d/%Y")
    product_url = data_info[1]
    url_list = sheet.col_values(2)

    # Update to current time
    # for time = '07/05/2022 15:48:1234'
    # time[0:10] = '07/05/2022'
    if (sheet.acell("F1").value is None) or (product_time != datetime.strptime(sheet.acell("F1").value[0:10], "%m/%d/%Y")):
        sheet.insert_cols([['test']], 6)
        sheet.update("F1", data_info[0][0:10])

    # If the product is already in our list, then we do not show it
    if product_url not in url_list or product_name not in name_list:
        sheet.insert_row(data_info, 2)

    # Else we need to add this product to our sheet
    else:
        for i in range(0, len(url_list)):
            if (product_url in url_list[i]):
                print("Find" + product_url + "at")
                # print(i)
                insert_position = "F" + str(i + 1)
                sheet.update(insert_position, data_info[5])
                print("update" + insert_position + "to" + data_info[5])

    print("Updating happens at page " + sheet_idx)
    time.sleep(4)
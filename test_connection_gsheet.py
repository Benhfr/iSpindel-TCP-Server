import gspread
from gspread_formatting import *


# d'ici.....
import configparser
import os
config = configparser.ConfigParser()
config_path = './config/'
config_path = config_path.replace('\\', '/')

try:
    with open(os.path.join(os.path.expanduser(config_path), 'iSpindle_config.ini')) as f:
        config.read_file(f)
except IOError:
    config.read_file(os.path.join(os.path.expanduser(config_path), 'iSpindle_default.ini'))

# ...à la ça sera à supprimer : déjà dans iSpindel.py





# retrieve Gsheet properties
# retrieve Gsheet properties
GSHEET_JSON_KEY_LOCATION = config.get('GSHEET', 'GSHEET_JSON_KEY_LOCATION')
GSPREADSHEET_NAME = config.get('GSHEET', 'GSPREADSHEET_NAME')

ISPINDEL_VERT_NAME = config.get('GSHEET', 'ISPINDEL_VERT_NAME')
ISPINDEL_BLEU_NAME = config.get('GSHEET', 'ISPINDEL_BLEU_NAME')

RECIPE_NAME = 'IPA ANGLAISE_FERMENTATION'


sa = gspread.service_account(filename=GSHEET_JSON_KEY_LOCATION)
sh = sa.open(GSPREADSHEET_NAME)
try:
    wks = sh.worksheet('IPA ANGLAISE_FERMENTATION')
except gspread.exceptions.WorksheetNotFound:
    wks = sh.add_worksheet(RECIPE_NAME + "_FERMENTATION", 1500, 5)
    wks.update('A1:E1', [['TIME', 'DENSITE', 'TEMPERATURE (°C)', 'BATTERIE (Volt)', 'ISPINDEL']])


fmt = cellFormat(
    backgroundColor=color(34.218, 112.86, 246.96),
    textFormat=textFormat(bold=True, foregroundColor=color(1,1,1)),
    horizontalAlignment='CENTER',
    verticalAlignment='MIDDLE'
    )

format_cell_range(wks, 'A1:E1', fmt)
set_frozen(wks, rows=1)


wks.append_row(['30/12/2022 22:13:43', float('1.010'), float('21.5'),float('4.5'), 'titi'])

#print(wks.acell('A2').value)


#wks.update('A6','Benjamin')
#wks.update('A7:C8',[['7A','7B','7C'],['8A','8B','8C']])
##−∗−coding :  utf−8−∗−

import sqlite3 
import logging
import sys
from collections import OrderedDict

import conf

LogFormat = "%(levelname)s >  Line:%(lineno)s - %(message)s"
logging.basicConfig(filename="debug.log", level=logging.DEBUG, format=LogFormat, filemode="w")
logger = logging.getLogger(__name__)

# encode: string -> byte
# unicode.encode() -> bytes
# decode: bytes -> string
# bytes.decode() -> unicode

# no need to encoding or decode
def decode_to_text(text):
    if isinstance(text, str): #check if text is string
        #print(text)
        if "时间" == text:
            logger.debug(str(text.encode('utf-8')))
            logger.debug(str("时间".encode('utf-8')))
            logger.debug(str("时间".encode('utf-8')))
        # decode_text = text.encode('utf-8').decode('utf-8')
        decode_text = text
    else:
        decode_text = text

    return decode_text


def convert_into_dic(columns, rows):
    """
    Return query value into dictionary
    :type columns: list
    :type rows: tuple
    """
    column_name = None
    row_val = None

    query_val = OrderedDict()
    length_c = len(columns)

    for c in range(0,length_c):
        column_name = columns[c]
        query_val[column_name] = [] # create key name with empty list value
        for r in range(0,len(rows)):
            row_val = decode_to_text(rows[r][c])
            query_val[column_name].append(row_val) 
            
    #print(query_val)
    return query_val


def run_query(query):
        """
        Return query result 
        sql: rawstring of sql
        """
        con = None
        data = None

        try:
            con = sqlite3.connect('VoiceCommand.db') 
            cur = con.cursor()
            
            cur.execute(query)

            # TODO: Simplified it
            if True in map(lambda x: x.lower() in query.lower(),['update','insert','delete']):
                conf.NEW_COMMAND = True

            data = cur.fetchall()
            print(data)

            if cur.description:
                column_name = [c[0] for c in cur.description]

            if data:
                data = convert_into_dic(column_name, data)
            
            con.commit()

        except sqlite3.Error as e:
            print("Error {}:".format(e.args[0]))
            sys.exit(1)

        finally:
            if con:
                con.close()
        return data


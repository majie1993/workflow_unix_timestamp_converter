# encoding: utf-8

import sys
import time
import datetime
from workflow import Workflow


def timestamp_with_offset(offset):
    current_timestamp = int(time.time()) + offset
    readable_time = datetime.datetime.fromtimestamp(current_timestamp).strftime('%Y-%m-%d %H:%M:%S')
    return (str(current_timestamp), str(readable_time))


def readable_string_with_offset(offset):
    return str(timestamp_with_offset(offset)[0]) + " " + str(timestamp_with_offset(offset)[1])


def main(wf):
    if len(wf.args):
        query = str(wf.args[0])

        if query.startswith('+') or query.startswith('-'):
            real_num = query[1:]
            if real_num.isdigit():
               wf.add_item(title="Current unix timestamp",
                        subtitle=readable_string_with_offset(int(query)),
                        arg=timestamp_with_offset(int(query))[0],
                        valid=True)

        elif query.isdigit():
            result = datetime.datetime.fromtimestamp(int(query)).strftime('%Y-%m-%d %H:%M:%S')
            wf.add_item(title="Current unix timestamp",
                        subtitle=query + " " + result,
                        arg=result,
                        valid=True)

        try:
            current_timestamp = int(time.mktime(time.strptime(query, "%Y-%m-%d %H:%M:%S")))
            wf.add_item(title="Current unix timestamp",
                        subtitle=str(current_timestamp) + " " + query,
                        arg=str(current_timestamp),
                        valid=True)
        except:
            pass


    else:
        query = None
        wf.add_item(title="Current unix timestamp",
                    subtitle=readable_string_with_offset(0),
                    arg=timestamp_with_offset(0)[0],
                    valid=True)

    wf.add_item(title="Current unix timestamp",
                subtitle=readable_string_with_offset(0),
                arg=timestamp_with_offset(0)[0],
                valid=True)
    wf.send_feedback()


if __name__ == u"__main__":
    wf = Workflow()
    sys.exit(wf.run(main))

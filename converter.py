import csv
import json
import re
import sys

# reg exps
reg_artist = re.compile('artists_')
reg_colors = re.compile('color_')

# initialize
result = []
header = []

# ref file name
fname  = sys.argv[1]
with open(fname) as f:
    for r in csv.reader(f):
        if len(header) == 0:
            header = r
        else:
            tmp = {}
            for i in range(len(header)):
                if reg_artist.match(header[i]):
                    if not 'artists' in tmp:
                        tmp['artists'] = []
                    tmp['artists'].append(r[i])
                elif reg_colors.match(header[i]):
                    if not 'color' in tmp:
                        tmp['color'] = {}
                    tmp['color'][re.sub(reg_colors, '', header[i])] = r[i]
                else:
                    tmp[header[i]] = r[i]
            result.append(tmp)

print(json.dumps(result, ensure_ascii=False))

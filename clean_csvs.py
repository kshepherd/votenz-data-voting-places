import code

def clean_data():
    """
    Add electorate name as new first col, fill out col header with address 1, address 2
    skip blank lines or lines that just have totals or other labels
    give non-place rows a special non-place address 1 so they dont pick up previous address 1 when we fill down
    :return:
    """
    for i in range(1, 73):
        filename = f"party-votes-by-voting-place-{i}.csv"
        print(f"Cleaning csv {filename}")
        csv = open(f"input/{filename}", 'r')
        cleaned = open(f"input/cleaned/{filename}", 'w')
        cleaned_no_totals = open(f"input/cleaned_no_totals/{filename}", 'w')
        lines = csv.readlines()
        electorate = lines[1].split(',')[0]
        print(electorate)
        for line in lines:
            if line is None:
                continue
            commas = line.count(',')
            if commas >= 20:
                # this is either the party header or the special lines where there isn't a voting place
                # eg overseas votes, rest home teams, etc.
                # most other cols are 21
                # over 21 is fine too, it means there is one or more comma in the place name but encapsulated in quotes
                # anyway so a proper csv parser will read it as a single column
                if commas == 20:
                    cleaned_line = ''
                    if line.startswith(',,ACT'):
                        cleaned_line = 'Electorate,Address 1, Address 2,' + line[2:]
                    else:
                        cleaned_line = f"{electorate},Non-place{line}"
                else:
                    cleaned_line = f"{electorate},{line}"
                # print to stdout
                print(cleaned_line)
                if ' Total,' not in cleaned_line:
                    # this file won't have the per-electorate totals so it is probably more useful in analysis
                    cleaned_no_totals.write(cleaned_line)
                # this file will have per-electorate totals which will help validate that i haven't messed
                # any data up
                cleaned.write(cleaned_line)

        #code.interact(local=locals())


if __name__ == '__main__':
    clean_data()

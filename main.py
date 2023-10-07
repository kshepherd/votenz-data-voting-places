import code

import pandas as pd

def read_data():
    """
    Read data and output as frames
    :return:
    """
    frames = list()
    frames_no_totals = list()

    for i in range(1, 73):
        filename = f"party-votes-by-voting-place-{i}.csv"
        print(f"Reading csv {filename}")
        df = pd.read_csv(f"input/cleaned/{filename}")
        df_no_totals = pd.read_csv(f"input/cleaned_no_totals/{filename}")
        # fill nulls in teh first city col with prev vals
        df = df.fillna(method='ffill')
        df_no_totals = df_no_totals.fillna(method='ffill')
        # append to list for concatenation
        frames.append(df)
        frames_no_totals.append(df_no_totals)

    all_frames = pd.concat(frames)
    all_frames_no_totals = pd.concat(frames_no_totals)
    #code.interact(local=locals())
    output_filename = 'voting-places-party-votes'
    all_frames.to_csv(f"output/{output_filename}_with_totals.csv")
    all_frames.to_html(f"output/{output_filename}_with_totals.html")
    all_frames_no_totals.to_csv(f"output/{output_filename}.csv")
    all_frames_no_totals.to_html(f"output/{output_filename}.html")

if __name__ == '__main__':
    read_data()


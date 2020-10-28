import pandas as pd
import numpy as np 

def read_csv(file_name, num_rows):
    import pandas as pd 
    return pd.read_csv(file_name, nrows=num_rows)


# reduce memory
def reduce_mem_usage(df, verbose=True):
    start_mem = df.memory_usage().sum() / 1024**2
    numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']

    for col in df.columns:
        col_type = df[col].dtypes
        if col_type in numerics:
            c_min = df[col].min()
            c_max = df[col].max()
            if str(col_type)[:3] == 'int':
                if c_min > np.iinfo(np.int8).min and c_max < np.iinfo(np.int8).max:
                    df[col] = df[col].astype(np.int8)
                elif c_min > np.iinfo(np.int16).min and c_max < np.iinfo(np.int16).max:
                    df[col] = df[col].astype(np.int16)
                elif c_min > np.iinfo(np.int32).min and c_max < np.iinfo(np.int32).max:
                    df[col] = df[col].astype(np.int32)
                elif c_min > np.iinfo(np.int64).min and c_max < np.iinfo(np.int64).max:
                    df[col] = df[col].astype(np.int64)
            else:
                if c_min > np.finfo(np.float16).min and c_max < np.finfo(np.float16).max:
                    df[col] = df[col].astype(np.float16)
                elif c_min > np.finfo(np.float32).min and c_max < np.finfo(np.float32).max:
                    df[col] = df[col].astype(np.float32)
                else:
                    df[col] = df[col].astype(np.float64)
                    
    end_mem = df.memory_usage().sum() / 1024**2
    print('Memory usage after optimization is: {:.2f} MB'.format(end_mem))
    print('Decreased by {:.1f}%'.format(100 * (start_mem - end_mem) / start_mem))
    return df


# Utility functions to help extract features

# Number of data
def cnt_(x):
    try:
        return len(x.split(' '))
    except:
        return -1

# Number of Unique data
def nunique_(x):
    try:
        return len(set(x.split(' ')))
    except:
        return -1

# Max of data
def max_(x):
    try:
        return np.max([int(i) for i in x.split(' ')])
    except:
        return -1

# Min of data
def min_(x):
    try:
        return np.min([int(i) for i in x.split(' ')])
    except:
        return -1  

# Standard Deviation of data
def std_(x):
    try:
        return np.std([float(i) for i in x.split(' ')])
    except:
        return -1 

# Top n of data
def most_n(x, n):
    try:
        return Counter(x.split(' ')).most_common(n)[n-1][0]
    except:
        return -1

# Number of top n data
def most_n_cnt(x, n):
    try:
        return Counter(x.split(' ')).most_common(n)[n-1][1]
    except:
        return -1   

# count number of other features in case of action_type
def col_cnt_(df_data, columns_list, action_type):
    try:
        data_dict = {}

        col_list = copy.deepcopy(columns_list)
        if action_type != None:
            data_dict['action_type_path'] = df_data['action_type_path'].split(' ')

        for col in col_list:
            data_dict[col] = df_data[col].split(' ')

            path_len = len(data_dict[col])

            data_out = []
            for i_ in range(path_len):
                data_txt = ''

                if data_dict['action_type_path'][i_] == action_type:
                    data_txt += '_' + data_dict[col][i_]
                    data_out.append(data_txt)

            return len(data_out)  
    except:
        return -1


# count unqiue number of other features in case of action_type
def col_nuique_(df_data, columns_list, action_type):
    try:
        data_dict = {}

        col_list = copy.deepcopy(columns_list)
        if action_type != None:
            data_dict['action_type_path'] = df_data['action_type_path'].split(' ')


        for col in col_list:
            data_dict[col] = df_data[col].split(' ')

            path_len = len(data_dict[col])

            data_out = []
            for i_ in range(path_len):
                data_txt = ''
           
                if data_dict['action_type_path'][i_] == action_type:
                    data_txt += '_' + data_dict[col][i_]
                    data_out.append(data_txt)

            return len(set(data_out))
    except:
        return -1

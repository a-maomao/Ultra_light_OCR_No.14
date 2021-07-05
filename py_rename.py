def read_ori(ori_path='/home/aistudio/work/output/rec/predicts_chinese_mv3_v2.0.txt'):
    with open(ori_path, 'r') as fread:
        a = fread.readlines()
    fread.close()
    return a

def write_res(res_list, res_path='/home/aistudio/work/output/rec/baseline_mv3_b.txt'):
    with open(res_path, 'w') as fwrite:
        for each in res_list:
            print(each)
            info_ = each.split('\t')
            print(info_[0].split('/')[-1]+'\t'+info_[1])
            fwrite.write(info_[0].split('/')[-1]+'\t'+info_[1]+'\n')
    fwrite.close()

if __name__ == "__main__":
    res_list = read_ori()
    write_res(res_list)
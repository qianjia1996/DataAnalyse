book_dict = [{'书名':'无声告白', '作者':'伍绮诗'}, {'书名':'我不是潘金莲', '作者':'刘震云'}, {'书名':'沉默的大多数 (王小波集)', '作者':'王小波'}]

filename = './files/json_output.json'
with open(filename, 'w', encoding='utf-8') as f_obj:
    f_obj.write(json.dumps(book_dict, ensure_ascii=False))
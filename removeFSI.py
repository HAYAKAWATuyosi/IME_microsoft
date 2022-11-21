################################################################
# 定数
################################################################
ENCODING="UTF-16"

KEYWORD_CREDENTIAL="fsixxxx\n"
FILENAME="dict.txt"
FILENAME_SAFE="dict_safe.txt"

################################################################
# 処理
################################################################
whileCredentialBlock = False
with ( open(FILENAME,      "r", encoding=ENCODING) as fp1,
       open(FILENAME_SAFE, "w", encoding=ENCODING) as fp2
      ):
    for line_no, line in enumerate(fp1):
        if line.endswith(KEYWORD_CREDENTIAL):
            print("at the line {:05d}, finding credential item.".format(line_no))
            continue

        fp2.write(line)
################################################################
# THE END OF THIS FILE
################################################################

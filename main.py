from art import text2art # pip install art > https://pypi.org/project/art/
import datetime
import time

def main() :
    
    target_h_int = 21
    target_m_int = 58

    target_h_word = "CH"
    target_m_word = "OM"

    while(True) : 
        curr_time = datetime.datetime.now()
        curr_h_int = curr_time.hour
        curr_m_int = curr_time.minute
        curr_s_int = curr_time.second

        clock_str = ''
        if target_h_int == curr_h_int and target_m_int == curr_m_int : # 타켓 시간에 맞는 경우
            # 2글자씩 표기되도록 준비 (초만)
            curr_s_str = str(curr_s_int).zfill(2)

            clock_str = f'{target_h_word}:{target_m_word}:{curr_s_int}'
        else : # 타겟 시간과 맞지 않는 경우

            # 2글자씩 표기되도록 준비 (시, 분, 초 전부)
            curr_h_str = str(curr_h_int).zfill(2)
            curr_m_str = str(curr_m_int).zfill(2)
            curr_s_str = str(curr_s_int).zfill(2)

            clock_str = f'{curr_h_str}:{curr_m_str}:{curr_s_str}'

        # print(clock_str)
        art_str = text2art(clock_str, font = "block", chr_ignore=True)
        print(art_str) 
        time.sleep(1)
            
if __name__ == '__main__' :
    main()
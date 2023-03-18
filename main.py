from src.utils.intro import *
from src.SSDVS_Checker.SSDVS_Checker import SSDVS_Checker


file_path = 'test-files/test_requirement.txt'

if __name__ == '__main__':

    printIntro()
    ssdvs_res = SSDVS_Checker(filename=file_path)


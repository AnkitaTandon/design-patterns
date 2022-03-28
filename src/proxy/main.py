from proxi import *
from college import *

if __name__ == "__main__":
      
    collegeProxy = CollegeProxy()
    collegeProxy.studyingInCollege()
  
    collegeProxy.feeBalance = 100
    collegeProxy.studyingInCollege()
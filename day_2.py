from util import read_file

input = "inputs/day2.txt"

def is_report_safe(report):
    """Checks if the given report is safe """
    if(report != sorted(report) and report != sorted(report, reverse=True)):
        return False
    
    for index, value in enumerate(report[1:]):

        distance = abs(report[index]- value)
        if distance < 1 or distance > 3:
             return False

    return True

def problem_dampener(report):
    """Checks if the given report is safe when tuning it a bit"""
    
    # Check if unaltered report is safe
    if is_report_safe(report=report):
        return 1

    #Check if the report can be fixed
    for index, _ in enumerate(report):
        modified_report = report[:index] + report[index + 1:]
        if is_report_safe(modified_report):
            return 1
    
    return 0

def test():
    report = [1, 3, 2, 4, 5]
    
    for index in range(len(report)):
        print(report[:index] + report[index+1:])

if __name__ == '__main__':

    reports = read_file(input).split("\n")
    safe_reports = 0
    for report in [report.split(' ') for report in reports]:
        safe_reports += problem_dampener([int(value) for value in report])

    print(f"Safe reports: {safe_reports}")    


import csv

def main():
    with open('output.csv', 'r') as f:
        reader = csv.reader(f)    
        for row in reader:
            str1 = ''.join(row)
            print str1  

if __name__ == '__main__':
    main() 

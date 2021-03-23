import pandas as pd

class FoodInspections():

    def __init__(self, file1, file2):

        df1 = pd.read_csv(file1)
        df2 = pd.read_csv(file2)
        self.inspections = pd.merge(df1, df2, how='left', on='Establishment_id')

    def analyze(self, distance):
        self.df = self.inspections[self.inspections['Distance_to_McKeldin'] <= distance]
        self.counts = self.df['Name'].value_counts()
        self.max = self.counts.max
        self.violations = list(zip(self.counts.index,self.counts))
        return self.violations
        
    def mask(self, distance):

        dfm = self.inspections
        self.dfmask = dfm[(dfm['Distance_to_McKeldin'] < 10) & (dfm['Inspection_results'] == "Critical Violations observed") & (dfm['Inspection_type'].str.contains("Monitoring", "Comprehensive"))]
        return self.dfmask

def main(filea, fileb, distance):

    food = FoodInspections(filea, fileb)
    print('This is a list of all resturants in the area with multiple health violations:')
    for tup in food.analyze(distance)[0:25]:
        print(tup[0], tup[1])

if __name__ == "__main__":

    import sys
    main(sys.argv[1:], sys.argv[2:], sys.argv[3:])

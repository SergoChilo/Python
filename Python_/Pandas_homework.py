import numpy as np
import pandas as pd
from pandas import merge


""" Pandas """
# !!! Տնայինի համար անհրաժեշտ բոլոր csv ֆայլերը կցված են

# 1. Պիտոնի պահատական գեներացված թվային լիստերից կամ np զանգվածներից ստեղծել երկու pandas series: Այնուհետև ստեղծել
# երրորդ series, որը կպարունակի երկրորդի այն տարրերը, որոնք մեծ են առաջինի տարրերից։

# a = pd.Series(np.random.randint(1, 20, 10))
# b = pd.Series(np.random.randint(1, 20, 10))
# c = b - a
# d = []
# print(c)
# for i in c:
#     if i > 0:
#         d = np.array(i)
#         print(d)

# 2. Ստեղծել հեռախոսային գրքույկ ներկայացնող DataFrame: Այն պետք է ունենա առնվազն հինգ մարդու տվյալ։ Առաջին սյան մեջ
# լինելու է մարդու անունը և ազգանունը, իսկ երկրորդ սյան մեջ նրա հեռախոսահամարը։

# l = [('Arustamyan Mariam', '091186208'),
#      ('Chobanyan Mher', '093274365'),
#      ('Artazyan Garnik', '043659476'),
#      ('Ghukasyan Gagik', '033367586'),
#      ('Chilingaryan Sergey', '098183208')]

# df = pd.DataFrame(l, columns=['Names', 'Numbers'], index=['1', '2', '3', '4', '5'])
# print(df)

# 3. Ստեղծել 1-100 պատահական ամբողջ թվերից լիստ և այն վերածեք Series-ի։ Այնուհետև սորտավորել այն։

# n = pd.Series(np.random.randint(1, 100, 10))
# n = pd.Series(sorted(n))
# print(n)

# 4. Ստեղծել փոքրատառով սկսվող բառերից բաղկացած լիստ։ Դրանից ստանալ Series: Այնուհետև Series-ի միջի բոլոր բառերի վերջին
# և առաջին տառերը վերածել մեծատառերի։
#
# Կարելի է անել ցիկլով, սակայն փորձեք գտնել հենց pandas.Series-ին պատկանող համապտասխան մեթոդ։

# l = pd.Series(['apple', 'break', 'down', 'world', 'orange'])
# s = l.map(lambda x: x[0].upper() + x[1:-1] + x[-1].upper())
# print(s)

# 5. Ունենք dictionary, որը պարունակում է ուսանողների անունները և նրանց ավարտական քննության գնահատականը։ Դրանից ստեղծել
# Dataframe։ Ինդեքսավորումը փոխել և թվայինից դարձնել տառային, այսինքն Jack-ը լինելու է a ինդեքսով տողում, John-ը b և
# այլն։
# Այնուհետև DataFrame-ին ավելացնել ևս մեկ սյուն, որը կկոչվի 'passed'։ Այն ուսանողը, ով հավաքել է 8 կամ բարձր, անցնում է,
# այսինքն 'passed' արժեքը True է, իսկ հակառակ դեպքում՝ False:

# d = [
#     {'Name': 'Jack', 'Grade': 5},
#      {'Name': 'John', 'Grade': 9},
#      {'Name': 'Anna', 'Grade': 8},
#      {'Name': 'Kim', 'Grade': 7},
#      {'Name': 'Leo', 'Grade': 8}]
# d1 = pd.DataFrame(d, columns=['Name', 'Grade'], index=['a', 'b', 'c', 'd', 'e'])
# #########Tarberak_1
# d1['Passed'] = np.where(d1['Grade'] >= 8, True, False)
# #########Tarberak_2
# d1.loc[d1['Grade'] < 8, ['Pass']] = False
# d1.loc[d1['Grade'] >= 8, ['Pass']] = True
# print(d1)

# 6. Կարդալ այդ world_religions.csv-ն և պահել փոփոխականի մեջ։
#   ```
#   ա) Ստուգել առաջին տաս տողը
#   բ) Գտնել երկրների սյան մեջ չկրկնվող անունների քանակը
#   գ) Ջնջել այն բոլոր տողերը, որտեղ Country-ն All Countries է
#   դ) Ստուգել, արդյոք կան բացակայող/nan արժեքներ դատասեթի մեջ
#   ե) Փոխարինել այդ բացակայող արժեքները կամ սյան միջին արժեքով, կամ, ցանկության դեպքում կարող եք այդ արժեքները լցնել
#   նորմալ բաշխումից պատահական կերպով գեներացված արժեքներով։ Նորմալ բաշխման միջին արժեքը պետք է հավասար լինի սյան միջին
#   արժեքին, լայնությունը (սիգման) լինի 0,5
#   զ) Փոփոխությունից հետո հաստատել, որ դատասեթում այլևս վատ արժեքներ չկան
#   է) Վերջապես գումարել բոլոր սյուները, համեմատել արժեքները սորտավորելով։ Արդյունքը պետք է ներկայացվի այսպես, կրոնի
#   անունը որպես ինդեքս կամ key, իսկ տոկոսը որպես արժեք (value)։ Կարող եք արդյունքը ներկայացնել պիտոնական dict-ով կամ
#   pd.Series-ով


##   ա) Ստուգել առաջին տաս տողը
# df = pd.read_csv('./world_religions.csv')
# print(df[:11])

##   բ) Գտնել երկրների սյան մեջ չկրկնվող անունների քանակը
# df = pd.read_csv('./world_religions.csv')
# s = df['Country']
# seen = set()
# count = 0
# for n in s:
#     if n in seen:
#         continue
#     else:
#         seen.add(n)
#         count += 1
# print(count)

##   գ) Ջնջել այն բոլոր տողերը, որտեղ Country-ն All Countries է
# df = pd.read_csv('./world_religions.csv')
# df = df.drop(df[df["Country"] == ' All Countries'].index)
# print(df["Country"])

##   դ) Ստուգել, արդյոք կան բացակայող/nan արժեքներ դատասեթի մեջ
# df = pd.read_csv('./world_religions.csv')
# print(df.isna().sum())

##   ե) Փոխարինել այդ բացակայող արժեքները կամ սյան միջին արժեքով, կամ, ցանկության դեպքում կարող եք այդ արժեքները լցնել
##   նորմալ բաշխումից պատահական կերպով գեներացված արժեքներով։ Նորմալ բաշխման միջին արժեքը պետք է հավասար լինի սյան միջին
##   արժեքին, լայնությունը (սիգման) լինի 0,5
# df = pd.read_csv('./world_religions.csv')
# df = df.fillna(df.mean())
# print(df)

##   զ) Փոփոխությունից հետո հաստատել, որ դատասեթում այլևս վատ արժեքներ չկան
# df = pd.read_csv('./world_religions.csv')
# df = df.fillna(df.mean())
# print(df)
# print(df.isna().sum())

##   է) Վերջապես գումարել բոլոր սյուները, համեմատել արժեքները սորտավորելով։ Արդյունքը պետք է ներկայացվի այսպես, կրոնի
##   անունը որպես ինդեքս կամ key, իսկ տոկոսը որպես արժեք (value)։ Կարող եք արդյունքը ներկայացնել պիտոնական dict-ով կամ
##   pd.Series-ով
# df = pd.read_csv('./world_religions.csv')
# religions = [
#     df['Buddhists'].mean(),
#     df['Christians'].mean(),
#     df['Folk Religions'].mean(),
#     df['Hindus'].mean(),
#     df['Jews'].mean(),
#     df['Muslims'].mean(),
#     df['Other Religions'].mean(),
#     df['Unaffiliated'].mean()]
# re = pd.DataFrame(religions, index=['Buddhists', 'Christians', 'Folk Religions', 'Hindus', 'Jews', 'Muslims', 'Other Religions', 'Unaffiliated'])
# re.columns = ['Procent']
# print(re)

# 7. Կարդալ laptops.csv ֆայլը։ Գտնել՝
#
#    1. 5 ամենաթանկ laptop-ները f’{brand}։ {model}։ {price}’ այս ֆորմատով
#    2. 5 ամենամատչելի laptop-ները f’{brand} {model} {price}’ այս ֆորմատով
#    3. բոլոր օպերացիոն համակարգերը և իրենց մոդելների քանակը(օրինակ՝ windows: 456, macOS:46, Linux: 876...)
#    4. 5 ամենածանր laptop-ները f’{brand} {model} {weight}’ այս ֆորմատով
#    5. 5 ամենահզոր RAM ունեցող laptop-ները f’{brand} {model} {ram}’ այս ֆորմատով
#    բոլոր չափի RAM-երը և իրենց մոդելների քանակը(օրինակ՝ 4GB: 456, 8GB:46, 10GB: 876...)
#    բոլոր brand-երը և իրենց մոդելների քանակը(օրինակ՝ apple: 11, Dell:80...)

##    1. 5 ամենաթանկ laptop-ները f’{brand}։ {model}։ {price}’ այս ֆորմատով
# df = pd.read_csv('./laptops.csv')
# print((df[['Manufacturer', 'Model Name', 'Price (Euros)']]).sort_values('Price (Euros)', ascending=True).head())

##    2. 5 ամենամատչելի laptop-ները f’{brand} {model} {price}’ այս ֆորմատով
# df = pd.read_csv('./laptops.csv')
# df = df.sort_values(by=['Price (Euros)'])
# print(df[['Manufacturer', 'Model Name', 'Price (Euros)']].head())

##    3. բոլոր օպերացիոն համակարգերը և իրենց մոդելների քանակը(օրինակ՝ windows: 456, macOS:46, Linux: 876...)
# df = pd.read_csv('./laptops.csv')
# ds = df['Operating System']
# dl = pd.DataFrame({'Operating System': ds})
# dx = dl.groupby('Operating System').size().reset_index(name='Repetition Count')
# print(dx)


##    4. 5 ամենածանր laptop-ները f’{brand} {model} {weight}’ այս ֆորմատով
# df = pd.read_csv('./laptops.csv')
# df = df.sort_values(by=['Weight'], ascending=False)
# print(df[['Manufacturer', 'Model Name', 'Weight']].head())

#    5. 5 ամենահզոր RAM ունեցող laptop-ները f’{brand} {model} {ram}’ այս ֆորմատով
# df = pd.read_csv('./laptops.csv')
# df = df.sort_values(by=['RAM'])
# print(df[['Manufacturer', 'Model Name', 'RAM']].head())

##    բոլոր չափի RAM-երը և իրենց մոդելների քանակը(օրինակ՝ 4GB: 456, 8GB:46, 10GB: 876...)
# df = pd.read_csv('./laptops.csv')
# ds = df['RAM']
# dl = pd.DataFrame({'Value': ds})
# dx = dl.groupby('Value').size().reset_index(name='Repetition Count')
# print(dx)

##    բոլոր brand-երը և իրենց մոդելների քանակը(օրինակ՝ apple: 11, Dell:80...)
# df = pd.read_csv('./laptops.csv')
# ds = df['Manufacturer']
# dl = pd.DataFrame({'Value': ds})
# dx = dl.groupby('Value').size().reset_index(name='Repetition Count')
# print(dx)



# 8. Կարդալ imdb_top_1000.csv ֆայլը։ Այստեղ կտեսնենք IMDB կայքի տվյալների բազայի լավագույն 1000 ֆիլմերի ցանկը։
#
#     1. Ստուգել դատասեթի առաջին 8 տողը
#     2. Գտնել բազայում ներառված ամենահին ֆիլմը և տպել դրա ռեժիսորին և ժանրը
#     3. Գտնել ամենամեծ քանակությամբ ֆիլմեր ունեցող ռեժիսորին (կարող եք խմբավորել ըստ ռեժիսորների)
#     4. Հաշվել այդ ռեժիսորի ֆիլմերի միջին, առավելագույն և նվազագույն ռեյտինգները։
#     5․ Գտնել այն ռեժիսորներին, ովքեր դատասեթում ունեն 1-ից ավել ֆիլմ և գտնել նվազագույն միջին ռեյտինգ ունեցողին։
#     6. Տպել Meta score սյան միջին և միջին քառակուսային շեղման արժեքները բոլոր ռեժիսորների համար
#     7. Դատասեթում բացակայող արժեքները լրացնել այդ սյան միջին արժեքով։ Եթե սյունը թվային տիպ չունի, պարզապես ջնջել
#     այդտեղ բացակայող արժեքներին համապատասխան տողերը
#     8. Սորտավորել դատասեթը ըստ տարեթվերի և այն պահել նոր ֆայլի մեջ


##     1. Ստուգել դատասեթի առաջին 8 տողը
# df = pd.read_csv('./imdb_top_1000.csv')
# print(df[:9])

##     2. Գտնել բազայում ներառված ամենահին ֆիլմը և տպել դրա ռեժիսորին և ժանրը
# df = pd.read_csv('./imdb_top_1000.csv')
# print((df[['Director','Genre','Released_Year']]).sort_values('Released_Year').head(1))

##     3. Գտնել ամենամեծ քանակությամբ ֆիլմեր ունեցող ռեժիսորին (կարող եք խմբավորել ըստ ռեժիսորների)
# df = pd.read_csv('./imdb_top_1000.csv')
# ds = df['Director']
# dl = pd.DataFrame({'Director': ds})
# dx = dl.groupby('Director').size().reset_index(name='Film Count')
# a = dx.sort_values('Film Count', ascending=False).head()
# print(a)


##     4. Հաշվել այդ ռեժիսորի ֆիլմերի միջին, առավելագույն և նվազագույն ռեյտինգները։

# df = pd.read_csv('./imdb_top_1000.csv')
# dr = df.loc[df['Director'] == 'Alfred Hitchcock']
# group = dr.groupby('Director')
# ag = group.agg({'IMDB_Rating': ['min', 'mean', 'max'], 'No_of_Votes': ['max', 'std']})
# ag['Count'] = group.size()
# print(ag)

##     5․ Գտնել այն ռեժիսորներին, ովքեր դատասեթում ունեն 1-ից
##     ավել ֆիլմ և գտնել նվազագույն միջին ռեյտինգ ունեցողին։

# df = pd.read_csv('./imdb_top_1000.csv')
# dx = df.groupby('Director').size().reset_index(name='Repetition Count')
# dy = dx.loc[(dx['Repetition Count'] > 1)]
# group = df.groupby('Director')
# print(group.mean())

##     6. Տպել Meta score սյան միջին և միջին քառակուսային շեղման արժեքները բոլոր ռեժիսորների համար

# df = pd.read_csv('./imdb_top_1000.csv')
# group = df.groupby('Director')
# ag = group.agg({'IMDB_Rating': ['mean', 'std']})
# print(ag)

#     7. Դատասեթում բացակայող արժեքները լրացնել այդ սյան միջին արժեքով։ Եթե սյունը թվային տիպ չունի, պարզապես ջնջել
#     այդտեղ բացակայող արժեքներին համապատասխան տողերը

df = pd.read_csv('./imdb_top_1000.csv')
ds = df.fillna(method='ffill').fillna(method='bfill')
# All ' ' -> to NaN
df['Poster_Link'].replace('', np.nan, inplace=True)
df['Released_Year'].replace('', np.nan, inplace=True)
df['Certificate'].replace('', np.nan, inplace=True)
df['Genre'].replace('', np.nan, inplace=True)
df['IMDB_Rating'].replace('', np.nan, inplace=True)
df['Overview'].replace('', np.nan, inplace=True)
df['Meta_score'].replace('', np.nan, inplace=True)
df['Director'].replace('', np.nan, inplace=True)
df['Star1'].replace('', np.nan, inplace=True)
df['Star2'].replace('', np.nan, inplace=True)
df['Star3'].replace('', np.nan, inplace=True)
df['Star4'].replace('', np.nan, inplace=True)
df['No_of_Votes'].replace('', np.nan, inplace=True)
df['Gross'].replace('', np.nan, inplace=True)
df['Series_Title'].replace('', np.nan, inplace=True)
# Delete All NaN
df.dropna(inplace=True)
print(df)

##     8. Սորտավորել դատասեթը ըստ տարեթվերի և այն պահել նոր ֆայլի մեջ
#df = pd.read_csv('./imdb_top_1000.csv')
#print((df.sort_values('Released_Year').to_csv('saved_ratings.csv', index=False)))

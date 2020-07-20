#adriana ku
#pandas
#example:  steps of data manipulation
import pandas as pd
series =pd.Series([1,2,3])
print(series)
print("1 table creation-------------------------------\n")
df=pd.DataFrame({'Matricula':['001','002','003','004'],'Nombre':['Adriana','Juan','Luis','Miguel']})#table creation
print("\n",df)
print("2 get table size-------------------------------\n")
tamaño=df.shape #get table size
print("tamaño de la matriz es\n",tamaño)
print("3 first item-------------------------------\n")
first=df.head(1)#first item
print("4 el primer dato de la tabla es es: \n",first)
last=df.tail(1)
print("5 last element-------------------------------\n")
print("el ultimo dato  de la tabla es es: \n",last)
print("6 rename headers-------------------------------\n")
df=df.rename(columns = {'Matricula':'Registration Number','Nombre':'Name'})
print("\n",df)
print("7 swap columns-------------------------------\n")
sort=df[sorted(df.columns)]
print("/n",sort)
print("8 add columns-------------------------------\n")
#new values
df['Semester']=['1','3','5','7']
df['Career']=['ISC','IFN','DATA','ARQ']

print("/n",df)
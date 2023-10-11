import pandas as pd
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
print(f'первые пять строк\n {data.head()}')
# Получение уникальных значений в столбце 'whoAmI'
uniq_columns =set(data['whoAmI'])
# Создаем новые столбцы
for i in uniq_columns:
    data[i]=(data['whoAmI']==i).astype(int)
# удаляем столбец 'whoAmI'
del data['whoAmI']
print(f"После приведения в вид One Hot \n {data}")

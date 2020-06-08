import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data/data.csv')
df = df.set_index('Час t')
color_dict = {'Вразливі': 'Blue', 'Заражені': 'Red', 'Одужали': 'Green'}
ax = df.plot(color=[color_dict.get(x, 'Grey') for x in df.columns])
ax.set_ylabel('Кількість')
ax.yaxis.set_tick_params(length=0)
ax.xaxis.set_tick_params(length=0)
for spine in ('top', 'right', 'bottom', 'left'):
    ax.spines[spine].set_visible(False)
plt.savefig('data/plot.png')

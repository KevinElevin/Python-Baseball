from .data import games
import pandas as pd
import matplotlib.pyplot as plt
import sys
import os
sys.path.append(os.path.abspath("/d/git/Python-Baseball/stats"))

attendance = games.loc[(games['type'] == 'info') & (
    games['multi2'] == 'attendance'), ['year', 'multi3']]
attendance.columns = ['year', 'attendance']
attendance.loc[:, 'attendance'] = pd.to_numeric(
    attendance.loc[:, 'attendance'])
attendance.plot(kind='bar', x='year', y='attendance', figsize=(15, 7))

plt.xlabel('Year')
plt.ylabel('Attendance')
plt.axhline(y=attendance['attendance'].mean(), label='Mean',
            linestyle='--', color='green')
plt.show()

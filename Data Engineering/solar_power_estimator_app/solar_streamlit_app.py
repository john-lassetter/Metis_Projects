'''
To run this app, run `streamlit run solar_streamlit_app.py` from inside this directory
'''

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


st.write('''
# Solar Power Performance Estimator
This app uses publically available climate data and solar panel specs
to estimate monthly performance of solar panels in US counties.
**Warning:  This is a prototype and this analysis has not been imperically verified.**
''')

from sqlalchemy import create_engine

engine = create_engine('sqlite:///data/processed_solar_panel.db', echo=False)

df_processed = pd.read_sql(
    "SELECT * FROM processed_solar_data",
    con=engine, index_col='index'
)


st.write(
'''
### County/State Comparison
Fill out county/state 1 and county/state 2 to see how potential solar power production compares
between the two.
'''
)

# plot data automatically grouping at different scopes
calibration = 3000

# state1 = st.selectbox(label: 'State1')
col1, col2 = st.columns(2)

with col1:
    county_or_state1 = st.radio('Location 1 is a...', options=['County', 'State'], index=0)

    state1 = st.selectbox('State 1', options = df_processed.state.unique())
    mask1 = (df_processed.state==state1)
    if county_or_state1=='County':
        county1 = st.selectbox('County 1', options = df_processed[df_processed.state==state1].county.unique())
        mask1 = ((df_processed.county==county1) & (df_processed.state==state1))

with col2:
    county_or_state2 = st.radio('Location 2 is a...', options=['County', 'State'], index=1)

    state2 = st.selectbox('State 2', options = df_processed.state.unique(), index=1)
    mask2 = (df_processed.state==state2)
    if county_or_state2=='County':
        county2 = st.selectbox('County 2', options = df_processed[df_processed.state==state2].county.unique())
        mask2 = ((df_processed.county==county2) & (df_processed.state==state2))


grain = ['month', 'week']

y = df_processed[mask1].groupby(['month']).agg('mean').solar_power_per_sq_m*60*60*24*30.4/1000/calibration
x = np.linspace(0, 1, 12)
y2 = df_processed[mask2].groupby(['month']).agg('mean').solar_power_per_sq_m*60*60*24*30.4/1000/calibration
x2 = x



fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, sharey=True)

plt.rcParams.update({'font.size': 12})
ax1.plot(x, y, label='monthly ave.');
ax2.plot(x2, y2, c='g', label='monthly ave.')

ax1.set_ylabel('Ave. Solar Energy Production (kWh/m^2/month)')
ax1.set_ylim(0)
ax2.set_ylim(0)
if county_or_state1=='County':
    ax1.set_title('{} county, {}'.format(county1, state1))

else:
    ax1.set_title('{}'.format(state1))

if county_or_state2=='County':
    ax2.set_title('{} county, {}'.format(county2, state2))

else:
    ax2.set_title('{}'.format(state2))

ax1.set_xticks(ticks=np.linspace(min(x), max(x), 12))
ax1.set_xticklabels(labels=['Jan.', 'Feb.', 'March', 'April', 'May', 'June', 'July', 'Aug.', 'Sep.', 'Oct.', 'Nov.', 'Dec.'], rotation=90);
ax2.set_xticks(ticks=np.linspace(min(x), max(x), 12))
ax2.set_xticklabels(labels=['Jan.', 'Feb.', 'March', 'April', 'May', 'June', 'July', 'Aug.', 'Sep.', 'Oct.', 'Nov.', 'Dec.'], rotation=90);


col1, col2 = st.columns(2)

with col1:
    if county_or_state1=='County':
        st.metric(label='Approximate Production in {} county (per m^2)'.format(county1), value='{:.0f} kWh/year'.format(np.mean(y)*12))

    else:
        st.metric(label='Approximate Production in {} (per m^2)'.format(state1), value='{:.0f} kWh/year'.format(np.mean(y)*12))

with col2:
    if county_or_state2=='County':
        st.metric(label='Approximate Production in {} county (per m^2)'.format(county2), value='{:.0f} kWh/year'.format(np.mean(y2)*12))

    else:
        st.metric(label='Approximate Production in {} (per m^2)'.format(state2), value='{:.0f} kWh/year'.format(np.mean(y2)*12))


st.pyplot(fig)


with st.expander(label='About the calculation', expanded = False):
    st.write("""
        All analysis on this webpage is derived from global horizontal irradiance and temperature from the [National Renewable Energy Laboratory](https://www.nrel.gov/).
        Only 2020 data has been used in the analysis. Solar panel performance is estimated using
        the performance metrics of a First Solar series 6445. These metrics can be found here:
        [First Solar series 6](https://www.firstsolar.com/-/media/First-Solar/Technical-Documents/Series-6-Datasheets/Series-6-Datasheet.ashx)
    """)

import pandas as pd
import matplotlib.pyplot as plt


def plot_scatter(preds, obs):
    plt.scatter(preds, obs, s=2)
    plt.xlabel('Predictions [cfs]')
    plt.ylabel('Observations [cfs]')
    plt.plot([0, 1e6], [0, 1e6], lw=1, c='gray', ls="--")
    plt.xlim(0, preds.max() + 1000)
    plt.ylim(0, obs.max() + 1000)
    plt.tight_layout()
    plt.savefig('../out/montague_scatter.png', dpi=300)
    plt.clf()


def plot_ts(preds, obs):
    ax = preds.plot(label='predictions', legend=True)
    obs.plot(ax=ax, label='observations', legend=True, grid=True)
    ax.set_ylabel('Discharge at Montague [cfs]')
    ax.set_xlabel('Date')
    plt.tight_layout()
    plt.savefig('../out/montague_ts.png', dpi=300)
    plt.show()
    plt.clf()


montague_seg_id = 1659
montague_site_code = '01438500'

df_preds = pd.read_feather('../../3_predictions/in/rgcn_v2_preds_flow.feather')
df_obs = pd.read_csv('../../2_observations/out/drb_discharge_daily_dv.csv',
                     index_col='datetime', parse_dates=['datetime'])

df_preds = df_preds[df_preds['seg_id_nat'] == montague_seg_id]
df_preds.set_index('date', inplace=True)
# convert to cfs
df_preds = df_preds['discharge_cms'] * 35.315
df_obs = df_obs[montague_site_code]
df_obs = df_obs.loc[df_preds.index]

plot_scatter(df_preds, df_obs)
plot_ts(df_preds, df_obs)





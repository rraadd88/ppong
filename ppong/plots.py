from rohan.global_imports import *
from rohan.dandage.io_dict import read_dict,to_dict

def plot_peaks(df1):
    plt.figure(figsize=[60*(len(df1)//10000),3])
    ax=plt.subplot()
    df1.plot(x='time (ms)',y='db (log-scale) mean',ax=ax,legend=None)
    df1.plot.scatter(x='time (ms)',y='db (log-scale) mean peak',ax=ax,color='b')
    # df1.plot.scatter(x='time (ms)',y='db (log-scale) mean peak delay',ax=ax,color='g')
    ymax=ax.get_ylim()[1]
    def annot_rally(ax,x,y):
        ax.plot([x[('time (ms)', 'amin')],x[('time (ms)', 'amax')]],[y,y],color='lime')
        ax.text(np.mean([x[('time (ms)', 'amin')],x[('time (ms)', 'amax')]]),y,f"#{int(x.name)}",ha='center',va='bottom')
    _=df1.loc[~df1['db (log-scale) mean peak'].isnull(),:].groupby('rally #').agg({'time (ms)':[np.min,np.max,]}).apply(lambda x: annot_rally(ax,x,ymax),axis=1)
    # ax.legend(bbox_to_anchor=[1,1.2],loc='upper right')
    # ax.get_legend().remove()
    ymin,ymax=ax.get_ylim()
    _=ax.set_ylim(ymin,ymin+(ymax-ymin)*1.1)
    return ax
force=False
for k in dn2dp:
    outp=f'plot/line_time_db (log-scale) mean peak {k}.png'
    if not exists(outp):
        df1=read_table(f'data_analysed/data02_peaks/{k}.pqt')
        ax=plot_peaks(df1)
        savefig(outp,dpi=90)
        
        
lim_quantile=0.05
fig,axs=plt.subplots(ncols=3,nrows=2,figsize=[12,8])
for ax,(colx,coly) in zip(np.ravel(axs),itertools.product(colxs,colys)):
    sns.regplot(x=colx, y=coly, data=df2,lowess=True,
            scatter_kws={"color":"gray",'alpha':0.5},line_kws={"color":'r'},
            ax=ax)
    ax.set_ylim(df2[coly].quantile(lim_quantile),df2[coly].quantile(1-lim_quantile))
plt.tight_layout()
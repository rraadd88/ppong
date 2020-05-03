
def run_all(input_audio_path,output_directory,test=False,force=False,cores=4):
    """
    runs the analysis.
    
    :param path: path to audio file/s (ext:.m4a) e.g. 'drive/*.m4a'
    """
    from glob import glob
    from os.path import basename,dirname
    packagen=basename(dirname(__file__))
    
    cfgp=f"{basename(output_directory).replace('/','')}.json"
    cfg={}
    cfg['date2pathm4a']={basename(p).replace('.m4a',''):p for p in sorted(glob(input_audio_path))}
    to_dict(cfg,cfgp)
    
    from rohan.dandage.io_fun import run_package
    cfg=run_package(cfgp,packagen=packagen,test=test,force=force,cores=cores)
    

## begin
import argh
import sys
parser = argh.ArghParser()
parser.add_commands([run_all,])

if __name__ == '__main__':
    parser.dispatch()

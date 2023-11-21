from pytracking.evaluation.environment import EnvSettings

def local_env_settings():
    settings = EnvSettings()

    # Set your local paths here.

    settings.cdtb_path = '/mnt/data0-nfs/sl53/det/results/CDTB/seqs'
    settings.cdtb_st_path = '/mnt/data0-nfs/sl53/det/results/CDTB-ST/seqs'
    settings.davis_dir = ''
    settings.depthtrack_path = '/mnt/data0-nfs/sl53/det_dataset/test'
    settings.depthtrack_st_path = '/mnt/data0-nfs/sl53/det/results/DepthTrack-ST/sequences/'
    settings.got10k_path = ''
    settings.got_packed_results_path = ''
    settings.got_reports_path = ''
    settings.lasot_path = ''
    settings.network_path = '/mnt/data0-nfs/sl53/det_networks'    # Where tracking networks are stored.
    settings.nfs_path = ''
    settings.otb_path = ''
    settings.result_plot_path = '//mnt/data0-nfs/sl53/det/results/pytracking/result_plots/'
    settings.results_path = '/mnt/data0-nfs/sl53/det/results/tracking_results/'   # Where to store tracking results
    settings.segmentation_path = '/mnt/data0-nfs/sl53/det/results/segmentation_results/'
    settings.tn_packed_results_path = ''
    settings.tpl_path = ''
    settings.trackingnet_path = ''
    settings.uav_path = ''
    settings.vot_path = ''
    settings.youtubevos_dir = ''

    return settings

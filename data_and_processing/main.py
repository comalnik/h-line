import virgo

#Observation parameters
DURATION_HRS = 6
RF_GAIN = 45
FREQUENCY = 1420e6
TSAMPLE = 2
LOCATION = '46.60, 14.95, 473.0'
AZALT = '0.0, 90.0'
RADEC = ''
CHANNELS = 2048

#calibration
CALIBRATION = False
CAL_DURATION_S = 300

#plotting
F_REST = 1420.4057517667e6
N_FILTER = 8



DURATION = DURATION_HRS * 3600

obs = {
    'dev_args': 'rtl=0,bias=1',
    'rf_gain': RF_GAIN,
    'if_gain': 20,
    'bb_gain': 20,
    'frequency': FREQUENCY,
    'bandwidth': 2.4e6,
    'channels': CHANNELS,
    't_sample': TSAMPLE,
    'duration': DURATION,
    'loc': LOCATION,
    'az_alt': AZALT,
    'ra_dec': RADEC
}


cal_obs = obs.copy()
cal_obs['duration'] = CAL_DURATION_S

if CALIBRATION:
  print(f'Calibrating for {CAL_DURATION_S} seconds...')
  virgo.observe(obs_parameters=cal_obs, spectrometer='wola', obs_file='calibration.dat')
  input("Calibration run finished. Press ENTER to start observation.")
  CALFILE = 'calibration.dat'
else:
  CALFILE = ''

  
print(f'Collecting data for {DURATION_HRS} hours...')
virgo.observe(obs_parameters=obs, spectrometer='wola', obs_file='observation.dat')

print('processing data...')
virgo.plot(
    obs_parameters=obs,
    obs_file='observation.dat',
    cal_file=CALFILE,
    f_rest=F_REST,
    slope_correction=True,
    dB=True,
    n=N_FILTER,
    m=0,
    spectra_csv='spectra.csv',
    waterfall_fits='waterfall.fits',
    power_csv='power.csv',
    plot_file='plot.png'
)

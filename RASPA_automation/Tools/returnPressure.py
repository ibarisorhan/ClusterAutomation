if __name__ == '__main__':
    import sys
    sys.path.append('..')
    sys.path.append('../..')
    from RASPA_automation import Settings
    pressure = str(Settings.Settings['ExternalPressure'])
    sys.stdout.write(pressure)
    sys.exit(0)


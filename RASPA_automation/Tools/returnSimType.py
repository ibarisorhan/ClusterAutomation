if __name__ == '__main__':
    import sys
    sys.path.append("..")
    sys.path.append("../..")
    from RASPA_automation import Settings
    SimulationType = Settings.Settings['SimulationType']
    sys.stdout.write(SimulationType)
    sys.exit(0)

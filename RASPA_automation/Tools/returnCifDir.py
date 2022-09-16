if __name__ == '__main__':
    import sys
    sys.path.append("..")
    sys.path.append("../..")
    from RASPA_automation import Settings
    cifDirectory = Settings.Structures['Directory']
    sys.stdout.write(cifDirectory)
    sys.exit(0)
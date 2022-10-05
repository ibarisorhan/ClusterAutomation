if __name__ == '__main__':
    import sys
    sys.path.append("..")
    sys.path.append("../..")
    from RASPA_automation import Settings
    doc = Settings.Structures['ListOfStructures']
    queue = "./" + doc.strip('.txt') + Settings.Structures['currentSuffix']  
    sys.stdout.write(queue)
    sys.exit(0)

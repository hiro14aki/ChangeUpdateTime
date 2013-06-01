#!/usr/bin/python

import sys
import os
import time

class FileUtil:
    """ Change file update time.
    Excecure changeupdatefile.py with argument about filepath.
    """
    def change_updatetime(self):
        argvs = sys.argv
        argc = len(argvs)
        if argc != 2:
            print 'Argument ERROR'
            sys.exit()
        else:
            path = argvs[1]
            print path

        files = self.get_file_list(path)
        self.get_update_time(files, path)

    def get_file_list(self, path):
        files = os.listdir(path)
        return files

    def get_update_time(self, files, path):
        mod_hour = 11
        mod_minute = 0
        for file in files:
            file_ext = os.path.splitext(file)[-1].lower()[1:]
            if "jpg" == file_ext or "avi" == file_ext:
                fullpath = path + file
                updtime = os.stat(fullpath).st_mtime
                # mtime = time.gmtime(updtime)
                mtime = time.localtime(updtime)

                year = str(mtime[0])
                month = str(mtime[1]).rjust(2, "0")
                day = str(mtime[2]).rjust(2, "0")
                hour = str(mtime[3])
                minute = str(mtime[4])

                # For incremental modify.
                # If you want to change some parameter, comment outed about following two lines;
                month = 10
                day = 11
                hour = mod_hour
                minute = mod_minute

                self.update_time_info(fullpath, year, month, day, hour, minute)

                if 59 == mod_minute:
                    mod_hour += 1
                    mod_minute = 0
                else:
                    mod_minute += 1

    def update_time_info(self, fullpath, y, m, d, h, mi):
        # If you want to change some parameters, change parameter in this method.
        mtime = time.mktime((2011, int(m), int(d), int(h), int(mi), 0, 0, 0, 0,))
        atime = mtime
        os.utime(fullpath, (atime, mtime))

if __name__ == "__main__":
    targetfile = FileUtil()
    targetfile.change_updatetime()

    # atime = time.mktime((2010, 10, 8, 12, 10, 0, 0, 0, 0))
    # print atime

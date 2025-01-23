import os


class ReusableMethods:

    def __init__(self, driver):
        self.driver = driver

    def get_current_win_tab(self):
       return self.driver.current_window_handle


    def get_all_win_tabs(self):
        window_handles = self.driver.window_handles
        return  window_handles
    def switching_tabs(self, window_handles, main_window_handle ):
        for handle in window_handles:
            if handle !=main_window_handle:
                self.driver.switch_to.window(handle)

                break
    def get_external_file(self):
        # Reading data from external file
        project_dir = os.getcwd()
        root_dir = os.path.dirname(project_dir)
        file_path = os.path.join(root_dir, "files", "keywords.txt")
        return file_path

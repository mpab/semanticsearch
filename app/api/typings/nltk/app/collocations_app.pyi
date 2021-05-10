"""
This type stub file was generated by pyright.
"""

import threading

CORPUS_LOADED_EVENT = ...
ERROR_LOADING_CORPUS_EVENT = ...
POLL_INTERVAL = ...
_DEFAULT = ...
_CORPORA = ...
class CollocationsView:
    _BACKGROUND_COLOUR = ...
    def __init__(self) -> None:
        ...
    
    def set_result_size(self, **kwargs):
        ...
    
    def reset_current_page(self):
        ...
    
    def handle_error_loading_corpus(self, event):
        ...
    
    def handle_corpus_loaded(self, event):
        ...
    
    def corpus_selected(self, *args):
        ...
    
    def previous(self):
        ...
    
    def __next__(self):
        ...
    
    def load_corpus(self, selection):
        ...
    
    def freeze_editable(self):
        ...
    
    def clear_results_box(self):
        ...
    
    def fire_event(self, event):
        ...
    
    def destroy(self, *e):
        ...
    
    def mainloop(self, *args, **kwargs):
        ...
    
    def unfreeze_editable(self):
        ...
    
    def set_paging_button_states(self):
        ...
    
    def write_results(self, results):
        ...
    


class CollocationsModel:
    def __init__(self, queue) -> None:
        ...
    
    def reset_results(self):
        ...
    
    def load_corpus(self, name):
        ...
    
    def non_default_corpora(self):
        ...
    
    def is_last_page(self, number):
        ...
    
    def next(self, page):
        ...
    
    def prev(self, page):
        ...
    
    class LoadCorpus(threading.Thread):
        def __init__(self, name, model) -> None:
            ...
        
        def run(self):
            ...
        
    
    


def app():
    ...

if __name__ == "__main__":
    ...

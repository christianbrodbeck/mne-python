"""Convenience functions for opening guis."""

import os as _os

from .transforms.coreg import trans_fname as _trans


def combine_markers(mrk1='', mrk2=''):
    """Create a new KIT marker file by interpolating two marker files

    Parameters
    ----------
    mrk1, mrk2 : str
        Path to source marker files (*.sqd; can be empty str, in which case the
        files can be loaded in GUI)
    """
    from .transforms.marker_gui import MainWindow
    gui = MainWindow(mrk1=mrk1, mrk2=mrk2)
    gui.configure_traits()
    return gui


def coregistration(raw, subject=None, trans_fname=_trans, subjects_dir=None):
    """Open a gui for scaling an mri to fit a subject's head shape

    Parameters
    ----------
    raw : str(path)
        path to a raw file containing the digitizer data.
    subject : str
        name of the mri subject.
        Can be None if the raw file-name starts with "{subject}_".
    trans_fname : str
        Filename pattern for the trans file. "{raw_dir}" will be formatted to
        the directory containing the raw file, and "{subject}" will be
        formatted to the subject name.
    subjects_dir : None | path
        Override the SUBJECTS_DIR environment variable
        (sys.environ['SUBJECTS_DIR'])
    """
    from .transforms.coreg_gui import HeadMriCoreg
    gui = HeadMriCoreg(raw, subject, trans_fname, subjects_dir)
    gui.configure_traits()
    return gui


def headshape(hsp=None):
    """GUI for decimating the number of points in a headshape file

    Parameters
    ----------
    hsp : None | str
        Path to the source hsp file.
    """
    from .transforms.headshape_gui import MainWindow
    gui = MainWindow()
    gui.configure_traits()
    if (hsp is not None) and _os.path.exists(hsp):
        gui.headshape.file = hsp
    return gui


def fit_mri_to_head(raw, s_from='fsaverage', s_to=None, trans_fname=_trans,
                    subjects_dir=None):
    """Open a gui for head-mri coregistration

    Parameters
    ----------
    raw : str(path)
        path to a raw file containing the digitizer data.
    s_from : str
        name of the source subject (e.g., 'fsaverage').
    s_to : str | None
        Name of the the subject for which the MRI is destined (used to
        save MRI and in the trans file's file name).
        Can be None if the raw file-name starts with "{subject}_".
    trans_fname : str
        Filename pattern for the trans file. "{raw_dir}" will be formatted to
        the directory containing the raw file, and "{subject}" will be
        formatted to s_to.
    subjects_dir : None | path
        Override the SUBJECTS_DIR environment variable
        (sys.environ['SUBJECTS_DIR'])
    """
    from .transforms.coreg_gui import MriHeadCoreg
    gui = MriHeadCoreg(raw, s_from, s_to, trans_fname, subjects_dir)
    gui.configure_traits()
    return gui


def kit2fiff():
    from .transforms.kit2fiff_gui import MainWindow
    gui = MainWindow()
    gui.configure_traits()
    return gui


def set_fiducials(subject, fid=None, subjects_dir=None):
    """Open a gui for creating a fiducials file for an mri

    Parameters
    ----------
    subject : str
        The mri subject.
    fid : None | str
        Fiducials file for initial positions.
    subjects_dir : None | str
        Overrule the subjects_dir environment variable.
    """
    from .transforms.coreg_gui import Fiducials
    gui = Fiducials(subject, fid, subjects_dir)
    gui.configure_traits()
    return gui

"""Set up the main qcodes namespace."""
# flake8: noqa (we don't need the "<...> imported but unused" error)
# config and logging
import logging
# TODO(giulioungaretti) remove this import
from multiprocessing import active_children

from qcodes.config import Config
config = Config()

from qcodes.utils.zmqlogger import check_broker
haz_broker = check_broker()
if haz_broker:
    from qcodes.utils.zmqlogger import QPUBHandler
    import logging.config
    import pkg_resources as pkgr
    logger_config = pkgr.resource_filename(__name__, "./config/logging.conf")
    logging.config.fileConfig(logger_config)
else:
    logging.warning("Can't publish logs, did you star the server?")


# name space
from qcodes.version import __version__
from qcodes.process.helpers import set_mp_method
from qcodes.utils.helpers import in_notebook

# code that should only be imported into the main (notebook) thread
# in particular, importing matplotlib in the side processes takes a long
# time and spins up other processes in order to try and get a front end
if in_notebook():  # pragma: no cover
    try:
        from qcodes.plots.qcmatplotlib import MatPlot
    except Exception:
        print('matplotlib plotting not supported, '
              'try "from qcodes.plots.qcmatplotlib import MatPlot" '
              'to see the full error')

    try:
        from qcodes.plots.pyqtgraph import QtPlot
    except Exception:
        print('pyqtgraph plotting not supported, '
              'try "from qcodes.plots.pyqtgraph import QtPlot" '
              'to see the full error')

# only import in name space if the gui is set to noebook
# and there is multiprocessing
if config['gui']['notebook'] and config['core']['legacy_mp']:
    from qcodes.widgets.widgets import show_subprocess_widget

from qcodes.station import Station
from qcodes.loops import get_bg, halt_bg, Loop
from qcodes.measure import Measure
from qcodes.actions import Task, Wait, BreakIf

from qcodes.data.manager import get_data_manager
from qcodes.data.data_set import DataMode, DataSet, new_data, load_data
from qcodes.data.location import FormatLocation
from qcodes.data.data_array import DataArray
from qcodes.data.format import Formatter
from qcodes.data.gnuplot_format import GNUPlotFormat
from qcodes.data.hdf5_format import HDF5Format
from qcodes.data.io import DiskIO

from qcodes.instrument.base import Instrument
from qcodes.instrument.ip import IPInstrument
from qcodes.instrument.visa import VisaInstrument
from qcodes.instrument.mock import MockInstrument, MockModel

from qcodes.instrument.function import Function
from qcodes.instrument.parameter import Parameter, StandardParameter, combine, CombinedParameter
from qcodes.instrument.sweep_values import SweepFixedValues, SweepValues

from qcodes.utils import validators

from qcodes.instrument_drivers.test import test_instruments, test_instrument
from qcodes.test import test_core, test_part

import os, ResultObjs, GetDistPlots, sys, batchJob
from matplotlib import rcParams, rc, pylab

# common setup for matplotlib
params = {'backend': 'pdf',
          'axes.labelsize': 10,
          'font.size': 10,
          'legend.fontsize': 9,
          'xtick.labelsize': 9,
          'ytick.labelsize': 9,
          'ytick.major.pad': 6,
          'xtick.major.pad': 6,
          'text.usetex': True,
          'font.family':'sans-serif',
          # free font similar to Helvetica
          'font.sans-serif':'FreeSans'}

sfmath = os.path.dirname(os.path.abspath(__file__)) + os.sep + 'sfmath'
# use of Sans Serif also in math mode
rc('text.latex', preamble=r'\usepackage{' + sfmath + '}')

rcParams.update(params)

non_final = True
version = 'clik9.0'
defdata_root = 'plik'
defdata_TT = defdata_root + '_TT_lowTEB'
defdata_TE = defdata_root + '_TE_lowTEB'
defdata_EE = defdata_root + '_EE_lowTEB'

defdata_all = defdata_root + '_TTTEEE_lowTEB'
defdata_TTonly = defdata_root + '_TT_lowl'
defdata_allNoLowE = defdata_root + '_TTTEEE_lowl'


planck = r'\textit{Planck}'
planckTT = r'\textit{Planck} TT'
planckTTlowEE = r'\textit{Planck} TT$+$lowE'
planckall = planck
WP = r'\textit{Planck}+WP'
WPhighL = r'\textit{Planck}+WP+highL'
lensing = r'\textit{Planck}+lensing'
WPhighLlensing = r'\textit{Planck}+lensing+WP+highL'
NoLowL = r'\textit{Planck}$-$lowL'
NoLowLhighL = r'\textit{Planck}$-$lowL+highL'
NoLowLtau = r'\textit{Planck}$-$lowL+$\tau$prior'
NoLowLhighLtau = r'\textit{Planck}$-$lowL+highL+$\tau$prior'
NoLowLE = r'\textit{Planck}$-$lowE'
lensonly = 'lensing'
HST = r'$H_0$'
BAO = 'BAO'

LCDM = r'$\Lambda$CDM'

s = GetDistPlots.defaultSettings
s.legend_frame = False
s.figure_legend_frame = False
s.prob_label = r'$P/P_{\rm max}$'
s.prob_y_ticks = True
s.param_names_for_labels = 'clik_units.paramnames'
s.alpha_filled_add = 0.85
# s.solid_colors = ['#006FED', '#E03424', 'gray', '#009966' ]
s.solid_contour_palefactor = 0.6

s.solid_colors = [('#8CD3F5', '#006FED'), ('#F7BAA6', '#E03424'), ('#D1D1D1', '#A1A1A1'), 'g', 'c']
s.axis_marker_lw = 0.6
s.lw_contour = 1

rootdir = 'main'

# various Omegam sigma8 constraints for plots
def PLSZ(s8, sigma):
    # from Anna 18/7/2014
    return  ((0.757 + 0.013 * sigma) / s8) ** (1 / 0.3) * 0.32

def CFTHlens(s8, sigma):
    return  ((0.79 + 0.03 * sigma) / s8) ** (1 / 0.6) * 0.27

def galaxygalaxy(s8, sigma):  # mandelbaum
    return  ((0.8 + 0.05 * sigma) / s8) ** (1 / 0.57) * 0.25

def planck_lensing(s8, sigma):  # mandelbaum
    # g60_full
    return  ((0.572 + 0.019 * sigma) / s8) ** (1 / 0.25)


def plotBounds(s8, data, c='gray'):
    pylab.fill_between(s8, data(-2), data(2), facecolor=c, alpha=0.15, edgecolor=c, lw=0)
    pylab.fill_between(s8, data(-1), data(1), facecolor=c, alpha=0.25, edgecolor=c, lw=0)


class planckPlotter(GetDistPlots.GetDistPlotter):

    def doExport(self, fname, adir=None, watermark=None):
        if fname is None: fname = os.path.basename(sys.argv[0]).replace('.py', '')
        if not '.' in fname: fname += '.pdf'
        if adir is not None and not os.sep in fname: fname = os.path.join(adir, fname)
        if not os.path.exists(os.path.dirname(fname)): os.makedirs(os.path.dirname(fname))
        if watermark is not None and watermark or watermark is None and non_final:
            # #watermark with version tag so we know it's old
            pylab.gcf().text(0.45, 0.5, version.replace('_', '{\\textunderscore}'), fontsize=30, color='gray', ha='center', va='center', alpha=0.2)
        GetDistPlots.GetDistPlotter.export(self, fname)

    def export(self, fname=None):
        self.doExport(fname, 'outputs')

    def exportExtra(self, fname=None):
        self.doExport(fname, 'plots')

    def getRoot(self, paramtag, datatag):
        batch = batchJob.readobject(rootdir)
        return batch.resolveName(paramtag, datatag)

plotter = planckPlotter(rootdir + '/plot_data')


def getSubplotPlotter(plot_data=None):
    global plotter
    s.setWithSubplotSize(2)
    s.axes_fontsize += 2
    s.colorbar_axes_fontsize += 2
#    s.lab_fontsize += 2
    s.legend_fontsize = s.lab_fontsize + 1
    if plot_data is not None: plotter = planckPlotter(plot_data)
    return plotter

def getPlotterWidth(size=1, **kwargs):  # size in mm
    inch_mm = 0.0393700787
    if size == 1:
        width = 88 * inch_mm
    elif size == 2: width = 120 * inch_mm
    elif size == 3: width = 180 * inch_mm
    else: width = size * inch_mm
    s.fig_width_inch = width
    s.setWithSubplotSize(2)
    s.rcSizes(**kwargs)
    return plotter

def getSinglePlotter(ratio=3 / 4., plot_data=None):
    global plotter
    s.setWithSubplotSize(3.5)
    s.rcSizes()
    if plot_data is not None: plotter = planckPlotter(plot_data)
    plotter.make_figure(1, ystretch=ratio)
    return plotter


class planckStyleTableFormatter(ResultObjs.noLineTableFormatter):
    """Planck style guide compliant formatter
    
    Andrea Zonca (edits by AL for consistent class structure)"""

    tableOpen = r"""
\begingroup
\openup 5pt
\newdimen\tblskip \tblskip=5pt
\nointerlineskip
\vskip -3mm
\scriptsize
\setbox\tablebox=\vbox{
    \newdimen\digitwidth
    \setbox0=\hbox{\rm 0}
    \digitwidth=\wd0
    \catcode`"=\active
    \def"{\kern\digitwidth}
%
    \newdimen\signwidth
    \setbox0=\hbox{+}
    \signwidth=\wd0
    \catcode`!=\active
    \def!{\kern\signwidth}
%
\halign{"""

    tableClose = r"""} % close halign
} % close vbox
\endPlancktable
\endgroup
"""

    def __init__(self):
        super(planckStyleTableFormatter, self).__init__()
        self.aboveHeader = None
        self.belowHeader = r'\noalign{\vskip 3pt\hrule\vskip 5pt}'
        self.aboveTitles = r'\noalign{\doubleline}'
        self.belowTitles = ''
        self.minorDividor = ''
        self.majorDividor = ''
        self.endofrow = r'\cr'
        self.hline = r'\noalign{\vskip 5pt\hrule\vskip 3pt}'
        self.belowFinalRow = self.hline
        self.belowBlockRow = self.hline
        self.belowRow = None
        self.colDividor = '|'
        self.headerWrapper = "\\omit\\hfil %s\\hfil"
        self.noConstraint = r'\dots'
        self.colSeparator = '&'
        self.spacer = ''

    def formatTitle(self, title):
        return ResultObjs.texEscapeText(title)

    def belowTitleLine(self, colsPerParam, numResults):
        out = r'\noalign{\vskip -3pt}'
        if colsPerParam > 1:
            out += "\n"
            out += r"\omit"
            out += (r"&\multispan" + str(colsPerParam) + r"\hrulefill") * numResults
            out += r"\cr"
        out += self.getLine("belowTitles")
        return out

    def startTable(self, ncol, colsPerResult, numResults):
        tableOpen = self.tableOpen + "\n"
        tableOpen += r"""\hbox to 0.9in{$#$\leaderfil}\tabskip=1.5em&"""
        if numResults > 3 and colsPerResult == 2:
            for res in range(numResults):
                tableOpen += r"\hfil$#$\hfil\tabskip=0.5em&" + "\n"
                if res < numResults - 1:
                    tableOpen += r"\hfil$#$\hfil\tabskip=1.7em&" + "\n"
        else:
            tableOpen += r"$#$\hfil&" * (colsPerResult * numResults - 1)
        tableOpen += r"\hfil$#$\hfil\tabskip=0pt\cr"
        return tableOpen

    def endTable(self):
        return self.tableClose

    def titleSubColumn(self, colsPerResult, title):
        return '\\multispan' + str(colsPerResult) + '\hfil ' + self.formatTitle(title) + '\hfil'

    def textAsColumn(self, txt, latex=False, separator=False, bold=False):
        bold = False
        if latex:
            res = txt  # there should be NO SPACE after a number in latex AZ
        else:
            wid = len(txt)
            res = txt + self.spacer * max(0, 28 - wid)
        if latex:
            if bold: res = '{\\boldmath$' + res + '$}'
            else:  res = res
        if separator:
            if latex:
                res += self.colSeparator  # there should be NO SPACE after a number in latex AZ
            else:
                res += self.colSeparator
        return res

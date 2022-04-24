# script-version: 2.0
# Catalyst state generated using paraview version 5.9.1

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# ----------------------------------------------------------------
# setup views used in the visualization
# ----------------------------------------------------------------

# get the material library
materialLibrary1 = GetMaterialLibrary()

# Create a new 'Render View'
renderView1 = CreateView('RenderView')
renderView1.ViewSize = [1605, 1156]
renderView1.AxesGrid = 'GridAxes3DActor'
renderView1.CenterOfRotation = [11.0, 11.0, 21.0]
renderView1.StereoType = 'Crystal Eyes'
renderView1.CameraPosition = [115.96553408247446, 65.763290178971, 113.94635940544958]
renderView1.CameraFocalPoint = [11.0, 10.999999999999991, 21.00000000000001]
renderView1.CameraViewUp = [-0.22823463463465377, 0.9294514707896202, -0.28987741374622167]
renderView1.CameraFocalDisk = 1.0
renderView1.CameraParallelScale = 5.790716398685054
renderView1.BackEnd = 'OSPRay raycaster'
renderView1.OSPRayMaterialLibrary = materialLibrary1

SetActiveView(None)

# ----------------------------------------------------------------
# setup view layouts
# ----------------------------------------------------------------

# create new layout object 'Layout #1'
layout1 = CreateLayout(name='Layout #1')
layout1.AssignView(0, renderView1)
layout1.SetSize(1605, 1156)

# ----------------------------------------------------------------
# restore active view
SetActiveView(renderView1)
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

# create a new 'PVD Reader'
fluidpvd = PVDReader(registrationName='fluid', FileName='C:\\Users\\Connor\\Documents\\post3\\fluid.pvd')
fluidpvd.CellArrays = ['vtkTestType']
fluidpvd.PointArrays = ['velocity', 'vorticity', 'velocityNorm']

# create a new 'PVD Reader'
cellspvd = PVDReader(registrationName='cells', FileName='C:\\Users\\Connor\\Documents\\post3\\cells.pvd')

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from cellspvd
cellspvdDisplay = Show(cellspvd, renderView1, 'GeometryRepresentation')

# get color transfer function/color map for 'vtkBlockColors'
vtkBlockColorsLUT = GetColorTransferFunction('vtkBlockColors')
vtkBlockColorsLUT.InterpretValuesAsCategories = 1
vtkBlockColorsLUT.AnnotationsInitialized = 1
vtkBlockColorsLUT.RGBPoints = [7.579073974147171e-06, 0.301961, 0.047059, 0.090196, 0.008828778147533358, 0.396078431372549, 0.0392156862745098, 0.058823529411764705, 0.017649977221092537, 0.49411764705882355, 0.054901960784313725, 0.03529411764705882, 0.026471176294651778, 0.5882352941176471, 0.11372549019607843, 0.023529411764705882, 0.035292375368210956, 0.6627450980392157, 0.16862745098039217, 0.01568627450980392, 0.04411357444177017, 0.7411764705882353, 0.22745098039215686, 0.00392156862745098, 0.05293477351532938, 0.788235294117647, 0.2901960784313726, 0.0, 0.061755972588888576, 0.8627450980392157, 0.3803921568627451, 0.011764705882352941, 0.07057717166244779, 0.9019607843137255, 0.4588235294117647, 0.027450980392156862, 0.07939837073600699, 0.9176470588235294, 0.5215686274509804, 0.047058823529411764, 0.0882195698095662, 0.9254901960784314, 0.5803921568627451, 0.0784313725490196, 0.09704076888312539, 0.9372549019607843, 0.6431372549019608, 0.12156862745098039, 0.10586196795668461, 0.9450980392156862, 0.7098039215686275, 0.1843137254901961, 0.11468316703024381, 0.9529411764705882, 0.7686274509803922, 0.24705882352941178, 0.12350436610380301, 0.9647058823529412, 0.8274509803921568, 0.3254901960784314, 0.13232556517736221, 0.9686274509803922, 0.8784313725490196, 0.4235294117647059, 0.1411467642509214, 0.9725490196078431, 0.9176470588235294, 0.5137254901960784, 0.14996796332448062, 0.9803921568627451, 0.9490196078431372, 0.596078431372549, 0.1587891623980398, 0.9803921568627451, 0.9725490196078431, 0.6705882352941176, 0.16761036147159902, 0.9882352941176471, 0.9882352941176471, 0.7568627450980392, 0.17607871258221586, 0.984313725490196, 0.9882352941176471, 0.8549019607843137, 0.17643156054515824, 0.9882352941176471, 0.9882352941176471, 0.8588235294117647, 0.17643694252599687, 0.9529411764705882, 0.9529411764705882, 0.8941176470588236, 0.17643694252599687, 0.9529411764705882, 0.9529411764705882, 0.8941176470588236, 0.18559749198663758, 0.8901960784313725, 0.8901960784313725, 0.807843137254902, 0.19475804144727826, 0.8274509803921568, 0.8235294117647058, 0.7372549019607844, 0.20391859090791895, 0.7764705882352941, 0.7647058823529411, 0.6784313725490196, 0.21307914036855963, 0.7254901960784313, 0.7137254901960784, 0.6274509803921569, 0.2222396898292003, 0.6784313725490196, 0.6627450980392157, 0.5803921568627451, 0.231400239289841, 0.6313725490196078, 0.6078431372549019, 0.5333333333333333, 0.24056078875048167, 0.5803921568627451, 0.5568627450980392, 0.48627450980392156, 0.24972133821112238, 0.5372549019607843, 0.5058823529411764, 0.44313725490196076, 0.25888188767176307, 0.4980392156862745, 0.4588235294117647, 0.40784313725490196, 0.2680424371324038, 0.4627450980392157, 0.4196078431372549, 0.37254901960784315, 0.27720298659304443, 0.43137254901960786, 0.38823529411764707, 0.34509803921568627, 0.28636353605368514, 0.403921568627451, 0.3568627450980392, 0.3176470588235294, 0.2955240855143258, 0.37254901960784315, 0.3215686274509804, 0.29411764705882354, 0.3046846349749665, 0.34509803921568627, 0.29411764705882354, 0.26666666666666666, 0.31384518443560716, 0.3176470588235294, 0.2627450980392157, 0.23921568627450981, 0.32300573389624787, 0.28627450980392155, 0.23137254901960785, 0.21176470588235294, 0.3321662833568886, 0.2549019607843137, 0.2, 0.1843137254901961, 0.34132683281752924, 0.23137254901960785, 0.17254901960784313, 0.16470588235294117, 0.35048738227816995, 0.2, 0.1450980392156863, 0.13725490196078433, 0.3596533137196493, 0.14902, 0.196078, 0.278431, 0.3775085486416103, 0.2, 0.2549019607843137, 0.34509803921568627, 0.3953637835635713, 0.24705882352941178, 0.3176470588235294, 0.41568627450980394, 0.4132190184855324, 0.3058823529411765, 0.38823529411764707, 0.49411764705882355, 0.43107425340749345, 0.37254901960784315, 0.4588235294117647, 0.5686274509803921, 0.4489294883294545, 0.44313725490196076, 0.5333333333333333, 0.6431372549019608, 0.4667847232514155, 0.5176470588235295, 0.615686274509804, 0.7254901960784313, 0.48463995817337663, 0.6, 0.6980392156862745, 0.8, 0.5024951930953376, 0.6862745098039216, 0.7843137254901961, 0.8705882352941177, 0.5203504280172987, 0.7607843137254902, 0.8588235294117647, 0.9294117647058824, 0.5292780454782793, 0.807843137254902, 0.9019607843137255, 0.9607843137254902, 0.5382056629392598, 0.8901960784313725, 0.9568627450980393, 0.984313725490196]
vtkBlockColorsLUT.ColorSpace = 'Lab'
vtkBlockColorsLUT.Annotations = ['0', '0', '1', '1', '2', '2', '3', '3', '4', '4', '5', '5', '6', '6', '7', '7', '8', '8', '9', '9', '10', '10', '11', '11']
vtkBlockColorsLUT.ActiveAnnotatedValues = ['0', '1', '2', '3']
vtkBlockColorsLUT.IndexedColors = [1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 0.0, 1.0, 0.0, 1.0, 0.0, 1.0, 1.0, 0.63, 0.63, 1.0, 0.67, 0.5, 0.33, 1.0, 0.5, 0.75, 0.53, 0.35, 0.7, 1.0, 0.75, 0.5]

# trace defaults for the display properties.
cellspvdDisplay.Representation = 'Surface'
cellspvdDisplay.ColorArrayName = ['FIELD', 'vtkBlockColors']
cellspvdDisplay.LookupTable = vtkBlockColorsLUT
cellspvdDisplay.SelectTCoordArray = 'None'
cellspvdDisplay.SelectNormalArray = 'None'
cellspvdDisplay.SelectTangentArray = 'None'
cellspvdDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
cellspvdDisplay.SelectOrientationVectors = 'None'
cellspvdDisplay.ScaleFactor = 0.8
cellspvdDisplay.SelectScaleArray = 'None'
cellspvdDisplay.GlyphType = 'Arrow'
cellspvdDisplay.GlyphTableIndexArray = 'None'
cellspvdDisplay.GaussianRadius = 0.04
cellspvdDisplay.SetScaleArray = [None, '']
cellspvdDisplay.ScaleTransferFunction = 'PiecewiseFunction'
cellspvdDisplay.OpacityArray = [None, '']
cellspvdDisplay.OpacityTransferFunction = 'PiecewiseFunction'
cellspvdDisplay.DataAxesGrid = 'GridAxesRepresentation'
cellspvdDisplay.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
cellspvdDisplay.OSPRayScaleFunction.Points = [7.579073974147171e-06, 0.0, 0.5, 0.0, 0.5382056629392598, 1.0, 0.5, 0.0]

# show data from fluidpvd
fluidpvdDisplay = Show(fluidpvd, renderView1, 'UniformGridRepresentation')

# get opacity transfer function/opacity map for 'vtkBlockColors'
vtkBlockColorsPWF = GetOpacityTransferFunction('vtkBlockColors')
vtkBlockColorsPWF.Points = [7.579073974147171e-06, 0.0, 0.5, 0.0, 0.5382056629392598, 1.0, 0.5, 0.0]

# trace defaults for the display properties.
fluidpvdDisplay.Representation = 'Outline'
fluidpvdDisplay.ColorArrayName = ['FIELD', 'vtkBlockColors']
fluidpvdDisplay.LookupTable = vtkBlockColorsLUT
fluidpvdDisplay.SelectTCoordArray = 'None'
fluidpvdDisplay.SelectNormalArray = 'None'
fluidpvdDisplay.SelectTangentArray = 'None'
fluidpvdDisplay.OSPRayScaleArray = 'velocity'
fluidpvdDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
fluidpvdDisplay.SelectOrientationVectors = 'None'
fluidpvdDisplay.ScaleFactor = 4.6000000000000005
fluidpvdDisplay.SelectScaleArray = 'None'
fluidpvdDisplay.GlyphType = 'Arrow'
fluidpvdDisplay.GlyphTableIndexArray = 'None'
fluidpvdDisplay.GaussianRadius = 0.23
fluidpvdDisplay.SetScaleArray = ['POINTS', 'velocity']
fluidpvdDisplay.ScaleTransferFunction = 'PiecewiseFunction'
fluidpvdDisplay.OpacityArray = ['POINTS', 'velocity']
fluidpvdDisplay.OpacityTransferFunction = 'PiecewiseFunction'
fluidpvdDisplay.DataAxesGrid = 'GridAxesRepresentation'
fluidpvdDisplay.PolarAxes = 'PolarAxesRepresentation'
fluidpvdDisplay.ScalarOpacityUnitDistance = 1.6089203037013018
fluidpvdDisplay.ScalarOpacityFunction = vtkBlockColorsPWF
fluidpvdDisplay.OpacityArrayName = ['POINTS', 'velocity']
fluidpvdDisplay.SliceFunction = 'Plane'
fluidpvdDisplay.Slice = 23

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
fluidpvdDisplay.OSPRayScaleFunction.Points = [7.579073974147171e-06, 0.0, 0.5, 0.0, 0.5382056629392598, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
fluidpvdDisplay.ScaleTransferFunction.Points = [-2.0718339164222184e-06, 0.0, 0.5, 0.0, 2.071833916422222e-06, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
fluidpvdDisplay.OpacityTransferFunction.Points = [-2.0718339164222184e-06, 0.0, 0.5, 0.0, 2.071833916422222e-06, 1.0, 0.5, 0.0]

# init the 'Plane' selected for 'SliceFunction'
fluidpvdDisplay.SliceFunction.Origin = [10.0, 10.0, 20.0]

# setup the color legend parameters for each legend in this view

# get color legend/bar for vtkBlockColorsLUT in view renderView1
vtkBlockColorsLUTColorBar = GetScalarBar(vtkBlockColorsLUT, renderView1)
vtkBlockColorsLUTColorBar.Title = 'vtkBlockColors'
vtkBlockColorsLUTColorBar.ComponentTitle = ''

# set color bar visibility
vtkBlockColorsLUTColorBar.Visibility = 1

# show color legend
cellspvdDisplay.SetScalarBarVisibility(renderView1, True)

# show color legend
fluidpvdDisplay.SetScalarBarVisibility(renderView1, True)

# ----------------------------------------------------------------
# setup color maps and opacity mapes used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# setup extractors
# ----------------------------------------------------------------

# create extractor
jPG1 = CreateExtractor('JPG', renderView1, registrationName='JPG1')
# trace defaults for the extractor.
# init the 'JPG' selected for 'Writer'
jPG1.Writer.FileName = 'RenderView1_%.6ts%cm.jpg'
jPG1.Writer.ImageResolution = [1605, 1156]
jPG1.Writer.Format = 'JPEG'

# ----------------------------------------------------------------
# restore active source
SetActiveSource(jPG1)
# ----------------------------------------------------------------

# ------------------------------------------------------------------------------
# Catalyst options
from paraview import catalyst
options = catalyst.Options()
options.GenerateCinemaSpecification = 1
options.GlobalTrigger = 'TimeStep'
options.CatalystLiveTrigger = 'TimeStep'

# ------------------------------------------------------------------------------
if __name__ == '__main__':
    from paraview.simple import SaveExtractsUsingCatalystOptions
    # Code for non in-situ environments; if executing in post-processing
    # i.e. non-Catalyst mode, let's generate extracts using Catalyst options
    SaveExtractsUsingCatalystOptions(options)

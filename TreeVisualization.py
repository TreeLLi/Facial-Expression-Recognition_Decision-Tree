import matplotlib.pyplot as plt
from DecisionTree import *
from config import *

INTERNAL_NODE = dict(boxstyle = "square", fc = "0.8")
LEAF_NODE = dict(boxstyle = "circle", fc = "0.8")

def getTreeWidth(tree):
    width = 0
    for key in tree.branchs.keys():
        if isinstance(tree.branchs[key], DecisionTree):
            width += getTreeWidth(tree.branchs[key])
        else:
            width += 1
    return width

def getTreeDepth(tree):
    maxDepth = 0
    for key in tree.branchs.keys():
        if isinstance(tree.branchs[key], DecisionTree):
            depth = getTreeDepth(tree.branchs[key]) + 1
        else:
            depth = 1
        if depth > maxDepth:
            maxDepth = depth
    return maxDepth

def plotNode(nodeAttribute, nodeX, nodeY, nodeType):
    visualise.ax.text(nodeX, nodeY, nodeAttribute, ha = "center", va = "center", size = 12, bbox = nodeType)

def plotArrow(startX, startY, endX, endY):
    visualise.ax.annotate("",
                            xy = (endX, endY), xycoords = 'data',
                            xytext = (startX, startY), textcoords = 'data',
                            size = 12, ha = "center", va = "center",
                            arrowprops = dict(arrowstyle = "->", connectionstyle = "arc3"),
                        )

# key = 1 left tree, key = 0 right tree
def plotTree(tree, xlim, rootX, rootY, isLeft):
    l = [0,0]
    for key in tree.branchs.keys():
        if isinstance(tree.branchs[key], DecisionTree):
            l[key] = getTreeWidth(tree.branchs[key])
        else:
            l[key] = 1

    if isLeft:
        currX = rootX - xlim * (float(l[0]) / (l[0] + l[1]))
    else:
        currX = rootX + xlim * (float(l[1]) / (l[0] + l[1]))

    currY = rootY - plotTree.yOff
    plotNode(str(tree.op()), currX, currY, INTERNAL_NODE)
    plotArrow(rootX, rootY, currX, currY)

    for key in tree.branchs.keys():
        if isinstance(tree.branchs[key], DecisionTree):
            xlim = getTreeWidth(tree.branchs[key])
            if key == 1:
                plotTree(tree.branchs[key], xlim, currX, currY, True)
            else:
                plotTree(tree.branchs[key], xlim, currX, currY, False)

        else:
            if key == 1:
                arrowX = currX - plotTree.xOff
            else:
                arrowX = currX + plotTree.xOff
            arrowY = currY - plotTree.yOff
            plotNode(str(tree.branchs[key]), arrowX, arrowY, LEAF_NODE)
            plotArrow(currX, currY, arrowX, arrowY)

def visualise(tree):
    fig = plt.figure(1, facecolor = 'white', figsize = (30,10))
    fig.clf()
    visualise.ax = plt.subplot(111)
    plotTree.totalW = float(getTreeWidth(tree))
    plotTree.totalD = float(getTreeDepth(tree))
    visualise.ax.set_xlim(0, plotTree.totalW)
    visualise.ax.set_ylim(0, plotTree.totalD)
    visualise.ax.text(5, 0, "Left Arrow: YES; Right Arrow: NO\n Square: ATTRIBUTE; Circle: LEAF NODE",
                        ha = "center", va = "center", size = 20,
                        bbox = dict(boxstyle = "round", fc = "w", ec = "0.5", alpha = 0.9))
    plotTree.xOff = 0.5
    plotTree.yOff = 1.0
    plotTree(tree, plotTree.totalW, plotTree.totalW, 1.1 + plotTree.totalD, True)
    figName = labelToStr(tree.emotion())
    plt.axis('off')
    plt.savefig(figName + '.png')
#    plt.show()

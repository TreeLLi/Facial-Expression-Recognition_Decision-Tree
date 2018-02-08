import matplotlib.pyplot as plt
import DecisionTree as DT
from config import *

INTERNAL_NODE = dict(boxstyle = "square", fc = "0.8")
LEAF_NODE = dict(boxstyle = "circle", fc = "0.8")


def plotNode(nodeAttribute, nodeX, nodeY, nodeType):
    visualise.ax.text(nodeX, nodeY, nodeAttribute, ha = "center", va = "center", size = 12, bbox = nodeType)

def plotArrow(startX, startY, endX, endY):
    visualise.ax.annotate("",
                            xy = (endX, endY), xycoords = 'data',
                            xytext = (startX, startY), textcoords = 'data',
                            size = 6, ha = "center", va = "center",
                            arrowprops = dict(arrowstyle = "->", connectionstyle = "arc3"),
                        )

# key = 1 left tree, key = 0 right tree
def plotTree(tree, xlim, rootX, rootY, isLeft):
    l = [0,0]
    for key in tree.branchs.keys():
        if isinstance(tree.branchs[key], DT.DecisionTree):
            l[key] = tree.branchs[key].getTreeWidth()
        else:
            l[key] = 1
# calculate the x coordinate of the root node of the current subtree based on the size of its branchs and the x coordinate of its parent tree's root node
    if isLeft:
        currX = rootX - xlim * (float(l[0]) / (l[0] + l[1]))
    else:
        currX = rootX + xlim * (float(l[1]) / (l[0] + l[1]))

# adjust the y coordinate of the root node of the current subtree
    currY = rootY - plotTree.yOff
    plotNode(str(tree.op()), currX, currY, INTERNAL_NODE)
    plotArrow(rootX, rootY, currX, currY)

# plot current subtree's branchs
    for key in tree.branchs.keys():
        # if the branch is another subtree
        if isinstance(tree.branchs[key], DT.DecisionTree):
            xlim = tree.branchs[key].getTreeWidth()
            if key == 1:
                plotTree(tree.branchs[key], xlim, currX, currY, True)
            else:
                plotTree(tree.branchs[key], xlim, currX, currY, False)
        # if the branch is a leaf node
        else:
            if key == 1:
                arrowX = currX - plotTree.xOff
            else:
                arrowX = currX + plotTree.xOff
            arrowY = currY - plotTree.yOff
            plotNode(str(tree.branchs[key]), arrowX, arrowY, LEAF_NODE)
            plotArrow(currX, currY, arrowX, arrowY)

def visualise(tree):
# please adjust the figsize if overlap occurs, and then zoom in to observe the tree structure
    fig = plt.figure(1, facecolor = 'white', figsize = (36,20))
    fig.clf()
    visualise.ax = plt.subplot(111)
    plotTree.totalW = tree.getTreeWidth()
    plotTree.totalD = tree.getTreeDepth()
    visualise.ax.set_xlim(0, plotTree.totalW)
    visualise.ax.set_ylim(0, plotTree.totalD)
    visualise.ax.text(5, 0, "Left Arrow: YES; Right Arrow: NO\n Square: ATTRIBUTE; Circle: LEAF NODE",
                        ha = "center", va = "center", size = 30,
                        bbox = dict(boxstyle = "round", fc = "w", ec = "0.5", alpha = 0.9))
    plotTree.xOff = 0.5 # adjust the x coordinate of the leaf nodes
    plotTree.yOff = 1.0 # adjust the y coordinate of all nodes
    plotTree(tree, plotTree.totalW, plotTree.totalW, 1.1 + plotTree.totalD, True)
    figName = labelToStr(tree.emotion())
    plt.axis('off')
    plt.savefig(figName + '.png')
#    plt.show()

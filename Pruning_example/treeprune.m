function Tree = treeprune(Tree,varargin)
%TREEPRUNE Obsolete function
%   
%   TREEPRUNE will be removed in a future release. Use the PRUNE method of an
%   object returned by FITCTREE or FITRTREE instead.
%
%   See also fitctree, fitrtree.

%   Copyright 1993-2014 The MathWorks, Inc. 

%error(message('stats:obsolete:ReplaceThisWithMethodOfObjectReturnedByEitherOr','treefit',...
 %   'prune','fitctree','fitrtree'));

if isa(Tree,'struct')
    Tree = classregtree(Tree);
end

Tree = prune(Tree,varargin{:});

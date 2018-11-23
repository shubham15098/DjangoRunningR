from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from . import serializers
from rest_framework import status
from . import models

from rest_framework import status, viewsets

# rpy2
import rpy2.robjects as robjects
import rpy2.robjects.packages as rpackages
from rpy2.robjects.vectors import StrVector
from rpy2.robjects.packages import SignatureTranslatedAnonymousPackage


# Create your views here.

class TryViewset(viewsets.ModelViewSet):
    serializer_class = serializers.TrySerializer
    setMe = 0

    queryset = models.Try.objects.all()


    def perform_create(self, serializer):
        """Sets the users profile to logged in user"""

        # serializer1 = serializer(data=)
        a = serializer.validated_data['minCells']
        b = serializer.validated_data['minGenes']
        print("fucking a")
        print(a)

        string = '''
        square <- function(x1,x2) {
            library(Seurat)
            library(dplyr)
            i <- 1
            
            pbmc.data <- Read10X(data.dir = "filtered_gene_bc_matrices/hg19/")
            dense.size <- object.size(x = as.matrix(x = pbmc.data))
            dense.size
            
            ans <- dense.size
            i <- i+1
            
            sparse.size <- object.size(x = pbmc.data)
            sparse.size
            
            ans[i] <- sparse.size
            i <- i+1
            
            ans[i] <- dense.size/sparse.size
            i <- i+1
            
            pbmc <- CreateSeuratObject(raw.data = pbmc.data, min.cells = x1, min.genes = x2,project = "10X_PBMC")
            mito.genes <- grep(pattern = "^MT-", x = rownames(x = pbmc@data), value = TRUE)
            percent.mito <- Matrix::colSums(pbmc@raw.data[mito.genes, ])/Matrix::colSums(pbmc@raw.data)
            pbmc <- AddMetaData(object = pbmc, metadata = percent.mito, col.name = "percent.mito")
            png("plot1.png")
            plot1 <- VlnPlot(object = pbmc, features.plot = c("nGene", "nUMI", "percent.mito"), nCol = 3)
            print(plot1)
            dev.off() 
            return(ans)
        }
        '''
        powerpack = SignatureTranslatedAnonymousPackage(string, "powerpack")
        pp = robjects.Vector(powerpack.square(a, b))
        print(pp)
        self.setMe = pp[2]

        # save it to our database
        print("in bc")
        print(self.setMe)
        serializer.save(checkIt=self.setMe)









    # # get
    # def list(self, request):
    #     """Return a hello message."""
    #     # same as get of apiview
    #
    #     return Response({'message': 'Hello viewset'})

    # same as post
    # def create(self, request):
    #     """Create a new hello message."""
    #
    # #     # get data from request and pass it in serializer
    #     serializer = serializers.TrySerializer(data=request.data)
    #
    #     # if it is valid, print the string message
    #     if serializer.is_valid():
    #         # receive from the post
    #         a = serializer.data.get('minCells')
    #         b = serializer.data.get('minGenes')
    #         c = int(a) + int(b)
    #
    #         string = '''
    #         square <- function(ini,inj) {
    #             ans <- c(1,2,3)
    #             return(ans)
    #         }
    #         '''
    #
    #         powerpack = SignatureTranslatedAnonymousPackage(string, "powerpack")
    #         pp = robjects.Vector(powerpack.square(a, b))
    #         print("booooooyeahhhhhhhhhhh")
    #         print(pp)
    #         self.setMe = pp[1]
    #         models.Try.checkIt = self.setMe
    #
    #         return Response({'message': 'hogya bc'})
    #     else:
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
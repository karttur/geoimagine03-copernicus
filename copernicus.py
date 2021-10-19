'''
Created on 23 Mar 2021

@author: thomasgumbricht
'''

import os

from sys import exit

# Third party imports

# Package application imports

from geoimagine.params import Composition, LayerCommon, RegionLayer, VectorLayer, RasterLayer

#from ancillary import ancillary_import

import geoimagine.support.karttur_dt as mj_dt 

from geoimagine.gis import GetVectorProjection, GetRasterMetaData, MjProj, Geometry, ESRIOpenGetLayer

from ..assets.httpsdataaccess import AccessCopernicusDEM
         
class ProcessCopernicus(AccessCopernicusDEM):
    'class for modis specific processing' 
      
    def __init__(self, pp, session):
        '''
        '''
        
        # Initiate the package for Online data access
        AccessCopernicusDEM.__init__(self, pp)
        
        self.session = session
                
        self.pp = pp  
        
        self.verbose = self.pp.process.verbose 
        
        self.session._SetVerbosity(self.verbose)
        
        print ('        ProcessCopernicus',self.pp.process.processid) 
               
        #direct to subprocess
        
        if self.pp.process.processid.lower() == 'searchcopernicusproducts':
            
            # Redirect to assets
            self._SearchOnlineProducts(self.pp.process.parameters.product)
            
        elif self.pp.process.processid.lower() == 'downloadcopernicus':
            
            # Redirect to assets
            self._SearchToListFile(self.pp.process.parameters.product)
            
        elif self.pp.process.processid.lower() == 'boundboxtilescopernicus':
            
            # Redirect to assets
            Snulle
            
        else:
            
            exitstr = 'Exiting, processid %(p)s missing in ProcessCopernicus' %{'p':self.pp.process.processid}
            
            exit(exitstr)
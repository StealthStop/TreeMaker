import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_1.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_10.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_100.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_101.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_102.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_103.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_104.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_105.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_106.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_107.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_108.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_109.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_11.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_110.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_111.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_112.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_113.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_114.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_115.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_116.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_117.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_118.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_119.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_12.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_120.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_121.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_122.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_123.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_124.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_125.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_126.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_127.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_128.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_129.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_13.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_130.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_131.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_132.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_133.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_134.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_135.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_136.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_137.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_138.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_139.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_14.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_140.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_141.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_142.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_143.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_144.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_145.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_146.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_147.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_148.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_149.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_15.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_150.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_151.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_152.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_153.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_154.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_155.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_156.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_157.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_158.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_159.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_16.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_160.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_161.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_162.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_163.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_164.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_165.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_166.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_167.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_168.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_169.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_17.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_170.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_171.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_172.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_173.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_174.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_175.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_176.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_177.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_178.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_179.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_18.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_180.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_181.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_182.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_183.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_184.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_185.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_186.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_187.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_188.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_189.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_19.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_190.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_191.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_192.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_193.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_194.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_195.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_196.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_197.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_198.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_199.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_2.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_20.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_200.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_201.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_202.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_203.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_204.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_205.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_206.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_207.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_208.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_209.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_21.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_210.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_211.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_212.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_213.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_214.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_215.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_216.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_217.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_218.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_219.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_22.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_220.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_221.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_222.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_223.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_224.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_225.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_226.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_227.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_228.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_229.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_23.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_230.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_231.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_232.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_233.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_234.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_235.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_236.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_237.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_238.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_239.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_24.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_240.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_241.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_242.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_243.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_244.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_245.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_246.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_247.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_248.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_249.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_25.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_250.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_251.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_252.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_253.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_254.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_255.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_256.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_257.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_258.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_259.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_26.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_260.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_27.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_28.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_29.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_3.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_30.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_31.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_32.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_33.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_34.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_35.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_36.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_37.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_38.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_39.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_4.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_40.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_41.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_42.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_43.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_44.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_45.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_46.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_47.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_48.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_49.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_5.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_50.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_51.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_52.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_53.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_54.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_55.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_56.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_57.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_58.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_59.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_6.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_60.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_61.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_62.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_63.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_64.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_65.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_66.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_67.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_68.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_69.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_7.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_70.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_71.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_72.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_73.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_74.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_75.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_76.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_77.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_78.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_79.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_8.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_80.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_81.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_82.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_83.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_84.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_85.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_86.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_87.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_88.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_89.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_9.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_90.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_91.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_92.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_93.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_94.root' ] );

readFiles.extend( [
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_95.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_96.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_97.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_98.root',
'/store/user/soha/rpv/rpv_stop_550_t3j_uds_GENSIM/rpv_stop_550_t3j_uds_MINIAOD/170918_213944/0000/rpv_stop_550_t3j_uds_MINIAOD_99.root' ] );


secFiles.extend( [
               ] )

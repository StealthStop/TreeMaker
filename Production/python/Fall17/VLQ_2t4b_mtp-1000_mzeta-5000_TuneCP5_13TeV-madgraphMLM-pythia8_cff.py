import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       	'/store/user/bcrossma/exoticVLQtbb_events_1TeV_GS/exoticVLQtbb_1TeV_MiniAOD/200407_130606/0000/exoticVLQtbb_MiniAOD_1TeV_1.root',
	'/store/user/bcrossma/exoticVLQtbb_events_1TeV_GS/exoticVLQtbb_1TeV_MiniAOD/200407_130606/0000/exoticVLQtbb_MiniAOD_1TeV_2.root',
	'/store/user/bcrossma/exoticVLQtbb_events_1TeV_GS/exoticVLQtbb_1TeV_MiniAOD/200407_130606/0000/exoticVLQtbb_MiniAOD_1TeV_3.root',
	'/store/user/bcrossma/exoticVLQtbb_events_1TeV_GS/exoticVLQtbb_1TeV_MiniAOD/200407_130606/0000/exoticVLQtbb_MiniAOD_1TeV_4.root',
	'/store/user/bcrossma/exoticVLQtbb_events_1TeV_GS/exoticVLQtbb_1TeV_MiniAOD/200407_130606/0000/exoticVLQtbb_MiniAOD_1TeV_5.root',
	'/store/user/bcrossma/exoticVLQtbb_events_1TeV_GS/exoticVLQtbb_1TeV_MiniAOD/200407_130606/0000/exoticVLQtbb_MiniAOD_1TeV_6.root',
	'/store/user/bcrossma/exoticVLQtbb_events_1TeV_GS/exoticVLQtbb_1TeV_MiniAOD/200407_130606/0000/exoticVLQtbb_MiniAOD_1TeV_7.root',
] )

import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/0C10D0C9-E2E0-E811-82F5-0025905AC804.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/4A45DD8B-26E2-E811-B1EB-3464A9B95F50.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/869FA643-8EE0-E811-90D4-5CB901C2A510.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/B6B35FAE-A8E0-E811-9F66-D0BF9C033BB0.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/0080A835-4DE2-E811-945A-70106F42AFF8.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/08F57789-EFE0-E811-84BC-D0BF9C039BA0.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/0AAE38F9-C7E0-E811-BBC2-D0BF9C033BB0.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/0EDDCB51-A2E2-E811-A7A0-B05ADA036C70.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/10FA70D7-49E2-E811-822F-3464A9B95F70.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/12F8803F-4FE2-E811-9422-5CB901C2A510.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/1631508A-EFE0-E811-A50F-0025905C445A.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/1E64C007-17E1-E811-BCBB-0025905C4328.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/2ACE26A3-A2E2-E811-84D6-3464A9B95F50.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/2E5F1F2E-B2E2-E811-B18F-70106F421A38.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/2EB70E0C-16E1-E811-B79A-3464A9B95FF0.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/383628AF-13E4-E811-BDCB-308D99304920.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/3E6E797D-91E0-E811-B4CC-0025905C4474.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/44583087-EFE0-E811-8CDC-0025905C42D4.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/4615F689-EFE0-E811-9D51-0025905C445A.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/4A1C334A-92E0-E811-9720-0025905C4474.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/50185D89-EFE0-E811-8F86-D0BF9C039BA0.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/56F47809-17E1-E811-96A4-0025905AC960.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/6A0B70F8-8BE2-E811-9CA1-D0BF9C039BA0.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/6C348D9E-C7E0-E811-8CE8-3464A9B96F00.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/6C417A2D-16E1-E811-981A-0025905C445A.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/74AB229E-C7E0-E811-AEF5-3464A9B96F00.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/76B40DDA-90E0-E811-83A4-3464A9B95F70.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/78A81531-F0E0-E811-9D5B-0025905C445A.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/7E9E050B-16E1-E811-9367-0025905C445A.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/80A5BA9A-36E1-E811-A47E-0025905C22B0.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/84EB7B3E-4FE2-E811-AF67-5CB901C2A510.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/8A9591A9-4BE2-E811-B16F-3464A9B95F70.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/92466F78-92E0-E811-A1CC-D0BF9C036BE0.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/969B8B17-4AE2-E811-8107-D0BF9C036BE0.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/9C167F16-92E0-E811-B510-3464A9B95FF0.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/9EE0A94B-93E0-E811-9F69-3464A9B95F70.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/A47F473B-F4E3-E811-945F-70106F42AFF8.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/A6225EAB-C1E0-E811-81EF-B05ADA036C70.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/AC493B01-4CE2-E811-BEA5-D0BF9C039BA0.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/B2841D4D-9DE0-E811-9E55-0025905C4328.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/BED847A8-CEE2-E811-AD78-5CB901C2A510.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/C43438A5-89E2-E811-B9BE-D0BF9C039BA0.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/C4DBD146-D1E0-E811-94AE-3464A9B95F70.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/C855D881-92E2-E811-A2C5-5CB901C2A510.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/D4765616-EBE0-E811-8AC7-0025905C42D4.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/D6DBD9EA-F4E0-E811-A5A3-0025905C4328.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/DCC5628B-A2E2-E811-AC6B-5CB901C34160.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/E8C9F04E-CFE0-E811-83F2-D0BF9C036BE0.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/E8E4D43B-64E2-E811-B4B6-70106F421A38.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/ECE77B1E-16E1-E811-84AF-B05ADA036C70.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/F28ECC31-B0E0-E811-8AB7-70106F421A38.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/110000/F64C0AB1-C7E0-E811-8718-0025905C4474.root',
] )

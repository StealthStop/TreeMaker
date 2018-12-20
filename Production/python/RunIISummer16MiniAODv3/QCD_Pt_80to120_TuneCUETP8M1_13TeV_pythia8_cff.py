import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_80to120_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/110000/280DF6F8-7AD0-E811-884A-0025905AC97A.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_80to120_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/110000/3A8373E0-30D3-E811-BB36-5CB901C2A510.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_80to120_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/110000/4A870E50-46D1-E811-8F9A-B05ADA036C70.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_80to120_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/110000/A414A398-7FD3-E811-8D9F-D0BF9C039BA0.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_80to120_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/120000/4ABB6C52-8CD3-E811-A423-3464A9B96F00.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_80to120_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/120000/5A9D98D2-E5D1-E811-AA01-D0BF9C033BB0.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_80to120_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/120000/5C7E66B1-70D0-E811-A909-0025905AC960.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_80to120_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/120000/6A02244F-46D1-E811-BBDA-308D99304920.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_80to120_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/120000/945BD266-71D0-E811-9334-0025905AC822.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_80to120_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/120000/9E43F36D-19D2-E811-963C-D0BF9C033BB0.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_80to120_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/120000/A65097C8-70D0-E811-88A0-0025905AC878.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_80to120_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/270000/20058975-71D0-E811-90A1-0025905AC822.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_80to120_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/270000/46642371-8DD0-E811-A385-5CB901C39220.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_80to120_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/04FAC2F3-85D0-E811-A1D3-0025905AC804.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_80to120_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/12074C68-77D0-E811-BB2C-308D99304920.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_80to120_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/16417F20-E8D1-E811-8DD5-70106F421A38.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_80to120_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/188DBE42-7BD0-E811-BC13-0025905AC95E.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_80to120_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/1A1CFF47-66D2-E811-B1A8-5CB901C39220.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_80to120_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/2491B0B8-EDD1-E811-A921-0025905AC878.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_80to120_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/265F7031-17D2-E811-A3CD-B05ADA036C70.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_80to120_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/2E1F2B37-EED1-E811-AEB8-0025905AC97A.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_80to120_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/3057A8F6-2BD7-E811-8A21-0025905AC960.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_80to120_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/36777B9F-16D2-E811-85E2-308D99304920.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_80to120_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/38089DBD-77D0-E811-BD2A-3464A9B96F00.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_80to120_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/38AD82A6-77D0-E811-87BA-0025905AC97A.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_80to120_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/38B410CF-02D3-E811-BBBE-0025905AC97A.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_80to120_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/3E3C6740-78D0-E811-9589-70106F421A38.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_80to120_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/4247B8DC-76D0-E811-8446-D0BF9C033BB0.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_80to120_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/465CD2A8-77D0-E811-9CB2-0025905AC984.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_80to120_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/4849DDDD-28D2-E811-873F-5CB901C34160.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_80to120_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/4C1E7B4B-52D3-E811-AB67-5CB901C39220.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_80to120_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/5CD3B066-5CD1-E811-BD7D-3464A9B95F50.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_80to120_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/6231669A-8DD0-E811-ACAC-0025905C4432.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_80to120_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/6CB63142-EED1-E811-88FB-3464A9B95F50.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_80to120_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/6EEC0D29-EED1-E811-B5B9-5CB901C34160.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_80to120_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/7262D733-18D2-E811-A1B7-5CB901C39220.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_80to120_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/84746DF9-EDD1-E811-AD9E-0025905C22B0.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_80to120_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/8A40163D-EED1-E811-9FD0-0025905AC97A.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_80to120_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/8A4D8549-7ED2-E811-BD85-5CB901C2A510.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_80to120_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/8CDC2043-78D0-E811-B968-70106F421A38.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_80to120_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/94CC1A77-E7D1-E811-B258-70106F421A38.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_80to120_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/963B5C2A-56D5-E811-BC02-0025905C22B0.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_80to120_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/9AF7C401-22D2-E811-B004-70106F421A38.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_80to120_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/A2F7AA92-8BD0-E811-A224-5CB901C39220.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_80to120_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/A400A9FD-EDD1-E811-ABBA-0025905AC878.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_80to120_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/B2374305-EED1-E811-957F-0025905AF57E.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_80to120_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/B2ED5B9B-EDD1-E811-9E41-3464A9B95F70.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_80to120_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/B80039B5-84D0-E811-A240-0025905AC984.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_80to120_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/BE9FBDEA-64D2-E811-ACC8-70106F42AFF8.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_80to120_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/C4733248-18D2-E811-BEE4-5CB901C39220.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_80to120_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/C668A9E1-EDD1-E811-85B1-3464A9B95F70.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_80to120_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/CA2BA0C8-77D0-E811-BA4F-3464A9B96F00.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_80to120_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/D2FBC84E-80D2-E811-B5ED-3464A9B96F00.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_80to120_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/E829D498-75D0-E811-8BFB-0025905C42D2.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_80to120_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/E87999BD-77D0-E811-9AE7-3464A9B96F00.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_80to120_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/FAD546B8-ECD1-E811-9C16-3464A9B95F70.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_80to120_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/FE444634-17D2-E811-82EF-B05ADA036C70.root',
] )

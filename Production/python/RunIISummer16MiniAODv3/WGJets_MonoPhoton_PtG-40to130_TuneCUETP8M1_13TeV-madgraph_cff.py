import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/WGJets_MonoPhoton_PtG-40to130_TuneCUETP8M1_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/0062FDEE-07F1-E811-BB58-001E67DDBFF7.root',
       '/store/mc/RunIISummer16MiniAODv3/WGJets_MonoPhoton_PtG-40to130_TuneCUETP8M1_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/14B07AD7-0DF1-E811-9CAC-001E675A6653.root',
       '/store/mc/RunIISummer16MiniAODv3/WGJets_MonoPhoton_PtG-40to130_TuneCUETP8M1_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/1843EDD5-83F0-E811-8A7A-001E67DDBEDA.root',
       '/store/mc/RunIISummer16MiniAODv3/WGJets_MonoPhoton_PtG-40to130_TuneCUETP8M1_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/1ACE6CF8-A9F0-E811-959C-001E67A3FEAC.root',
       '/store/mc/RunIISummer16MiniAODv3/WGJets_MonoPhoton_PtG-40to130_TuneCUETP8M1_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/1C64E60F-08F1-E811-A6D3-001E67A4061D.root',
       '/store/mc/RunIISummer16MiniAODv3/WGJets_MonoPhoton_PtG-40to130_TuneCUETP8M1_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/32BD984B-0AF1-E811-8289-001E67D89532.root',
       '/store/mc/RunIISummer16MiniAODv3/WGJets_MonoPhoton_PtG-40to130_TuneCUETP8M1_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/441B5092-0AF1-E811-B8A6-A4BF01025568.root',
       '/store/mc/RunIISummer16MiniAODv3/WGJets_MonoPhoton_PtG-40to130_TuneCUETP8M1_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/46103203-85F0-E811-B7F4-001E67A3EC2D.root',
       '/store/mc/RunIISummer16MiniAODv3/WGJets_MonoPhoton_PtG-40to130_TuneCUETP8M1_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/46FAD9DA-06F1-E811-8C73-EC0D9A0B3080.root',
       '/store/mc/RunIISummer16MiniAODv3/WGJets_MonoPhoton_PtG-40to130_TuneCUETP8M1_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/48E64D85-09F1-E811-BE62-A4BF0102A5F9.root',
       '/store/mc/RunIISummer16MiniAODv3/WGJets_MonoPhoton_PtG-40to130_TuneCUETP8M1_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/4A2C0280-86F0-E811-85DA-001E67A402C1.root',
       '/store/mc/RunIISummer16MiniAODv3/WGJets_MonoPhoton_PtG-40to130_TuneCUETP8M1_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/5073B8CC-0DF1-E811-ACCA-001E67DFFB31.root',
       '/store/mc/RunIISummer16MiniAODv3/WGJets_MonoPhoton_PtG-40to130_TuneCUETP8M1_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/5C1A7D30-9CF0-E811-950D-EC0D9A0B3360.root',
       '/store/mc/RunIISummer16MiniAODv3/WGJets_MonoPhoton_PtG-40to130_TuneCUETP8M1_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/5E9BD31D-0CF1-E811-B0F9-001E675A5244.root',
       '/store/mc/RunIISummer16MiniAODv3/WGJets_MonoPhoton_PtG-40to130_TuneCUETP8M1_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/5EA28D50-A5F0-E811-BDEA-001E675A69DC.root',
       '/store/mc/RunIISummer16MiniAODv3/WGJets_MonoPhoton_PtG-40to130_TuneCUETP8M1_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/60F617FF-06F1-E811-9EC5-EC0D9A0B3370.root',
       '/store/mc/RunIISummer16MiniAODv3/WGJets_MonoPhoton_PtG-40to130_TuneCUETP8M1_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/64F775AB-84F0-E811-BFFF-001E675A6AB8.root',
       '/store/mc/RunIISummer16MiniAODv3/WGJets_MonoPhoton_PtG-40to130_TuneCUETP8M1_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/664E1847-06F1-E811-9D21-001E67DDC0FB.root',
       '/store/mc/RunIISummer16MiniAODv3/WGJets_MonoPhoton_PtG-40to130_TuneCUETP8M1_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/6854BD6F-08F1-E811-AA9E-EC0D9A0B3380.root',
       '/store/mc/RunIISummer16MiniAODv3/WGJets_MonoPhoton_PtG-40to130_TuneCUETP8M1_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/6E2633C3-02F1-E811-BA69-EC0D9A0B3320.root',
       '/store/mc/RunIISummer16MiniAODv3/WGJets_MonoPhoton_PtG-40to130_TuneCUETP8M1_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/72AE0A02-84F0-E811-93B1-001E675A5244.root',
       '/store/mc/RunIISummer16MiniAODv3/WGJets_MonoPhoton_PtG-40to130_TuneCUETP8M1_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/80FB5E11-A2F0-E811-9DEA-001E67A3EC2D.root',
       '/store/mc/RunIISummer16MiniAODv3/WGJets_MonoPhoton_PtG-40to130_TuneCUETP8M1_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/82894822-03F1-E811-9293-001E67A406E0.root',
       '/store/mc/RunIISummer16MiniAODv3/WGJets_MonoPhoton_PtG-40to130_TuneCUETP8M1_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/8CB59C59-83F0-E811-94F3-001E675A69DC.root',
       '/store/mc/RunIISummer16MiniAODv3/WGJets_MonoPhoton_PtG-40to130_TuneCUETP8M1_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/9284D9F9-07F1-E811-A86A-A4BF0102A4F5.root',
       '/store/mc/RunIISummer16MiniAODv3/WGJets_MonoPhoton_PtG-40to130_TuneCUETP8M1_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/9A7BEF5E-06F1-E811-B590-001E67DFF609.root',
       '/store/mc/RunIISummer16MiniAODv3/WGJets_MonoPhoton_PtG-40to130_TuneCUETP8M1_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/D4270455-06F1-E811-8F4F-A4BF01025C02.root',
       '/store/mc/RunIISummer16MiniAODv3/WGJets_MonoPhoton_PtG-40to130_TuneCUETP8M1_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/D48705C0-07F1-E811-91D3-90B11C094A7E.root',
       '/store/mc/RunIISummer16MiniAODv3/WGJets_MonoPhoton_PtG-40to130_TuneCUETP8M1_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/D66867E8-08F1-E811-9078-A4BF01013D80.root',
       '/store/mc/RunIISummer16MiniAODv3/WGJets_MonoPhoton_PtG-40to130_TuneCUETP8M1_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/DE5E404B-84F0-E811-828C-EC0D9A0B3380.root',
       '/store/mc/RunIISummer16MiniAODv3/WGJets_MonoPhoton_PtG-40to130_TuneCUETP8M1_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/DE95363D-83F0-E811-AEEA-A4BF0102A5F4.root',
       '/store/mc/RunIISummer16MiniAODv3/WGJets_MonoPhoton_PtG-40to130_TuneCUETP8M1_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/E63B0126-86F0-E811-A3A5-EC0D9A0B3370.root',
       '/store/mc/RunIISummer16MiniAODv3/WGJets_MonoPhoton_PtG-40to130_TuneCUETP8M1_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/EA9533B0-84F0-E811-91AE-001E675A5262.root',
       '/store/mc/RunIISummer16MiniAODv3/WGJets_MonoPhoton_PtG-40to130_TuneCUETP8M1_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/F24E00D7-06F1-E811-A1E0-A4BF0101DB3E.root',
       '/store/mc/RunIISummer16MiniAODv3/WGJets_MonoPhoton_PtG-40to130_TuneCUETP8M1_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/F2E7ABC0-9CF0-E811-AC65-001E67A42A71.root',
       '/store/mc/RunIISummer16MiniAODv3/WGJets_MonoPhoton_PtG-40to130_TuneCUETP8M1_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/F8405B74-85F0-E811-AFBE-001E67A3F49D.root',
       '/store/mc/RunIISummer16MiniAODv3/WGJets_MonoPhoton_PtG-40to130_TuneCUETP8M1_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/FA777AAB-9BF0-E811-B0B5-A4BF01025630.root',
       '/store/mc/RunIISummer16MiniAODv3/WGJets_MonoPhoton_PtG-40to130_TuneCUETP8M1_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/FAFCAAC0-A3F0-E811-954A-A4BF0102A5F4.root',
] )
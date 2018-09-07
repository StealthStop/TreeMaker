import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/00316E5B-AD8B-E811-8BFB-A0369FE2C21A.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/00A004CC-AA8B-E811-AC59-A0369FE2C084.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/02D70D02-AB8B-E811-A316-AC1F6B0DE4A2.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/02DF30BF-9F8B-E811-BDE5-0CC47A4DEDFC.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/04809A78-C08B-E811-8806-0CC47A4DEE12.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/0486A7AA-AD8B-E811-AD8D-A0369FE2C216.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/04975367-C08B-E811-AA1C-AC1F6B0DE338.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/049EB2B6-B08B-E811-8E64-0090FAA57B10.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/063F426B-D38B-E811-AC5F-AC1F6B0F7B16.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/083086B6-B08B-E811-889E-0090FAA57B10.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/08441F62-AD8B-E811-878D-0CC47A4DED4E.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/0A0F4CF8-A48B-E811-973A-0090FAA58C54.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/0A7F381C-B18B-E811-B40B-0090FAA57FA4.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/0E05E85E-AD8B-E811-8BF2-0CC47A4D99B0.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/0E0BC3AA-AD8B-E811-AAD1-A0369FE2C084.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/0E115F59-AD8B-E811-86DC-0CC47A412A7A.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/0E959EA0-7E8C-E811-BFA2-0090FAA584D4.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/10324DE5-B08B-E811-ACF2-AC1F6B0DE33A.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/10B92767-A58B-E811-A54F-0090FAA57F14.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/140B73D4-AA8B-E811-94C8-0090FAA57760.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/14F97098-778C-E811-BF69-A0369FE2C228.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/169E2BAC-AD8B-E811-85A1-AC1F6B0DE4A2.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/16A5F099-AD8B-E811-B224-A0369FD0B300.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/1A09C289-B68B-E811-9BFC-AC1F6B0F6752.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/1CC5A234-9F8B-E811-BF4A-06FDAA0000B2.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/1E64D08F-B68B-E811-958C-A0369FD0B148.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/1EC549F7-B08B-E811-87E3-0682FA0002F5.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/2269B2CE-AA8B-E811-B458-0CC47A4DED92.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/22780209-B78B-E811-B83F-0CC47A4DEE10.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/227E7A2F-9F8B-E811-B52F-0090FAA57F14.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/22EC5178-C08B-E811-AE8E-0CC47A4DEE12.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/22EE9BBE-D38B-E811-8928-0CC47A4DEF54.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/24E95296-7E8C-E811-830A-002590D60488.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/28C850F9-A48B-E811-B580-0090FAA58124.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/2A224758-AD8B-E811-BFDC-A0369FE2C166.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/2A3D7734-9F8B-E811-B767-0090FAA587C4.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/2A441CBA-9F8B-E811-A3DA-0090FAA58D24.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/2AB2261C-B18B-E811-93C4-AC1F6B0DE2A2.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/2AE98403-B78B-E811-931F-A0369FE2C1A6.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/2AEA3438-9F8B-E811-B2DA-0090FAA58D64.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/2C46E86A-D38B-E811-A5DA-AC1F6B0F7B16.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/2CF48190-B68B-E811-A855-0090FAA57CE4.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/2EC2C5B8-7E8C-E811-89CE-A0369FD0B3A0.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/30ECD9F8-A48B-E811-813F-0090FAA58124.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/30FA3A6A-D38B-E811-B72A-0CC47A4DEE00.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/32298F94-788C-E811-A55B-A0369FD0B3FC.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/326286BB-9F8B-E811-B702-AC1F6B0DE4A2.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/32E7DE33-9F8B-E811-9882-0090FAA58B64.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/34103C59-AB8B-E811-B5AA-A0369FD0B180.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/3689A91F-B18B-E811-BF49-0090FAA577A0.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/3C912AFC-A48B-E811-B7CE-06FDAA0000B2.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/3C9A3F95-7E8C-E811-97D5-0CC47A4DEEDC.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/3CB3FEB3-B08B-E811-B54B-A0369FE2C11C.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/3CBE7EFB-6E8C-E811-BFD9-0CC47A4DED0A.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/3E958F06-B78B-E811-BA28-0090FAA577A0.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/3ECB60A0-B68B-E811-A97F-0090FAA57CE4.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/40CCCFFC-6E8C-E811-BECB-0090FAA58BF4.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/42BDAD8D-9F8B-E811-8AC9-0CC47A4D99B2.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/44066B78-C08B-E811-951D-0CC47A4DEE12.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/46663200-AB8B-E811-BA7C-0090FAA59864.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/466D37AC-7E8C-E811-ABFD-A0369FE2C1E8.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/46A8787C-EC8B-E811-9DA0-AC1F6B0DE33A.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/46FD5502-B78B-E811-A51B-A0369FE2C020.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/489914F9-A48B-E811-AA62-AC1F6B0DE2F4.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/48AC5F6F-AD8B-E811-9773-AC1F6B0DE33A.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/4A6A5178-C08B-E811-A43E-0CC47A4DEE12.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/4AB3239E-B68B-E811-8EA8-A0369FD0B2A8.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/4AD41022-B18B-E811-83F1-0090FAA577A0.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/4AE4E466-D38B-E811-BDEB-A0369FD0B334.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/4C1DE303-B78B-E811-9B0F-A0369FE2C1A6.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/4CA81A67-BE8B-E811-8A4C-0090FAA57CE4.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/5010A997-B68B-E811-9D9A-A0369FD0B148.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/509E9C03-AB8B-E811-A931-A0369FD0B20C.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/50FA0000-B78B-E811-ACD9-A0369FD0B242.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/540375E1-DB8B-E811-8A24-A0369FE2C068.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/56115C05-B78B-E811-9F1B-AC1F6B0F6758.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/5691E27B-AD8B-E811-AE9D-A0369FD0B3A0.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/581DD604-B78B-E811-AB0D-0CC47A412A7A.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/5836E564-C08B-E811-8ABC-A0369FD0B198.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/586FEBEA-AA8B-E811-8561-0090FAA582E4.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/58D094F6-AD8B-E811-8EC9-0090FAA57400.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/5C49DFAC-AD8B-E811-933E-0090FAA58C54.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/5CD24D37-9F8B-E811-833D-0090FAA58D64.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/5CFB411C-B18B-E811-B7AC-AC1F6B0DE2A2.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/5E3D38AE-AD8B-E811-9BA7-0090FAA582E4.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/5EB856C0-B68B-E811-9E04-A0369FD0B2A0.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/5EC7D268-D38B-E811-A7F5-0090FAA577A0.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/609A1CBA-9F8B-E811-BAB9-0090FAA58D24.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/6203D032-9F8B-E811-BF06-0090FAA58D64.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/62288445-AE8B-E811-88A4-A0369FD0B20C.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/62436DAB-AD8B-E811-91D3-A0369FE2C084.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/625B61AE-AD8B-E811-B2BE-0CC47A4DEDE6.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/629F8604-B78B-E811-BFBA-A0369FE2C14A.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/62A1B6B9-7E8C-E811-A979-0CC47A4D9A5E.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/62E4CD66-A58B-E811-BE85-A0369FE2C0DE.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/6481DE04-B78B-E811-92F7-0090FAA57FA4.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/64D62943-788C-E811-B9AD-0090FAA58224.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/66114EAD-AD8B-E811-B055-0090FAA58D64.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/662133C5-AA8B-E811-8630-AC1F6B0DE2F4.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/66221BA6-9F8B-E811-BD5B-0090FAA57AF0.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/686669F8-A48B-E811-8117-AC1F6B0DE2F4.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/687C4A03-B78B-E811-ABC3-A0369FE2C228.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/68D63467-A58B-E811-A5CA-0090FAA58D84.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/6AC01EEB-778C-E811-9A4D-A0369FE2C1FC.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/6C773164-C08B-E811-8C21-A0369FD0B180.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/6E5EF4B3-B08B-E811-9434-A0369FE2C11C.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/6EA17CF7-6E8C-E811-BD69-0CC47A4DEF06.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/6ED6FE24-DB8B-E811-A141-AC1F6B0DE49C.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/6EE49203-AB8B-E811-905C-A0369FD0B316.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/703CE664-AB8B-E811-A73B-A0369FE2C020.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/70FC277F-DA8B-E811-ACD7-A0369FE2C216.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/727F2C5C-AB8B-E811-934B-0CC47A4DEEF0.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/747AF8A9-AD8B-E811-A8AB-0090FAA569C4.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/7612558A-9F8B-E811-AEA3-0090FAA58D24.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/763F486B-AD8B-E811-88E0-AC1F6B0DE45C.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/76F29F60-AD8B-E811-8656-0CC47A412A7A.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/781C6D68-C08B-E811-AE1F-0CC47A4D99B0.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/7870E431-9F8B-E811-BA83-A0369FD0B374.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/78C07648-AB8B-E811-846D-0CC47A4DED42.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/78CF54BB-AA8B-E811-AFA1-A0369FE2C216.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/7A2B0989-B68B-E811-9A18-AC1F6B0F7B08.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/7A6F65E4-B08B-E811-9954-0CC47A4DED4E.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/7AAD04DC-DB8B-E811-B0C3-0090FAA57CD4.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/7AC1C867-A58B-E811-8561-0CC47A4DEEF0.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/7C395ACA-AA8B-E811-9B53-A0369FD0B1FE.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/7C91B0B6-B08B-E811-B373-0CC47A4D9A08.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/7E2801B4-B08B-E811-94F9-A0369FE2C11C.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/7E8741E3-AA8B-E811-90D0-0682FA0002F5.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/80C39904-B78B-E811-A3E0-0090FAA57B20.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/84DD0968-C08B-E811-95F2-0090FAA57D64.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/864AF743-AB8B-E811-A7D0-A0369FE2C006.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/8888E465-C08B-E811-86FD-A0369FD0B2A4.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/88A892B6-B08B-E811-BBE3-0090FAA57B10.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/88AB9202-B78B-E811-85C7-AC1F6B0DE462.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/8AD36FB6-B08B-E811-A8B4-AC1F6B0DE2E6.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/8C468B12-AB8B-E811-B300-0090FAA58194.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/8C4CBE66-A58B-E811-9773-A0369FE2C22E.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/8E3DA3B5-B08B-E811-9757-A0369FD0B1FE.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/8E711887-9F8B-E811-9C50-0CC47A4DEDFC.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/8E8332BA-9F8B-E811-A721-0CC47A4D99B2.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/8EFBDF78-C08B-E811-9D59-0CC47A4DEE12.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/9006A203-B78B-E811-82EE-AC1F6B0DE4A2.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/9020F320-B18B-E811-AEA6-0090FAA577A0.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/90B85A67-C08B-E811-AE8B-A0369FE2C208.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/90CFFD4E-788C-E811-9BCE-A0369FD0B130.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/9248E447-AB8B-E811-8E3E-0090FAA573E0.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/92E54E57-AD8B-E811-8C45-AC1F6B0DE4A2.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/92F5DD8B-B68B-E811-AA78-0090FAA57B20.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/94E3C478-C08B-E811-A3B1-0CC47A4DEE12.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/963E6007-B78B-E811-AA91-0090FAA57B20.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/982D111B-B18B-E811-9D60-A0369FD0B1F4.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/98B6BBA9-AD8B-E811-A89A-A0369FE2C084.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/9AB13868-C08B-E811-8A9C-0090FAA57D64.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/9C5AD520-B18B-E811-9CDB-0090FAA577A0.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/9E4F3079-C08B-E811-AFC0-0CC47A4DEE12.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/A0858AF8-A48B-E811-AE04-0090FAA58C54.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/A0B1DEB7-B08B-E811-AEDF-0CC47A4DED4E.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/A0B71037-9F8B-E811-9AB1-A0369FD0B374.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/A254C132-9F8B-E811-BAFA-A0369FD0B1FE.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/A29B49F9-A48B-E811-B7CC-AC1F6B0DE30C.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/A2D70701-B78B-E811-BB6A-0090FAA58544.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/A4447105-B78B-E811-AA21-AC1F6B0DE462.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/A695F2F7-A48B-E811-B01A-A0369FE2C042.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/A6A3ECCB-AA8B-E811-8876-0090FAA57260.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/A6EECF51-AB8B-E811-86C7-062CF6000156.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/A84185F8-A48B-E811-B8D0-0090FAA58C54.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/A863A74B-DB8B-E811-B027-AC1F6B0DE33A.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/A8A00E69-D38B-E811-B6CF-062CF6000156.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/A8CB9768-C08B-E811-ACFF-0CC47A4DECD6.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/AA5561BE-D38B-E811-9AA0-0CC47A4DED0A.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/AA8E36DF-DB8B-E811-867E-AC1F6B0DE45C.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/AAB86638-AB8B-E811-B763-A0369FD0B268.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/AC0E2736-9F8B-E811-BB66-0090FAA58D64.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/AC96695D-AD8B-E811-9AB3-0CC47A412A7A.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/B0460DAB-AD8B-E811-AF71-A0369FD0B12C.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/B054D16C-D38B-E811-8C70-A0369FD0B2AA.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/B0A37B68-C08B-E811-AC1F-0090FAA57D64.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/B2314860-AD8B-E811-9F57-AC1F6B0DE33A.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/B2E0485D-AB8B-E811-9F66-0090FAA57760.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/B43D1EB5-B08B-E811-9EC8-AC1F6B0DE33A.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/B4643279-C08B-E811-A398-0CC47A4DEE12.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/B6700F37-9F8B-E811-B4C0-A0369FD0B374.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/B6ECB8F7-A48B-E811-87A9-A0369FE2C042.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/B81616BA-9F8B-E811-B905-0CC47A4D99B2.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/BA17D9F8-A48B-E811-A348-0090FAA58124.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/BA3FB8EA-B08B-E811-B3E3-0CC47A412A7A.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/BA8DF0F7-A48B-E811-AF1F-A0369FE2C042.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/BC2180E0-AA8B-E811-AEC5-0090FAA57B10.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/BCFE856B-D38B-E811-A1E5-AC1F6B0F7B16.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/BE666BD0-B08B-E811-9E69-AC1F6B0DE3A4.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/BEEF20B5-B08B-E811-9A63-A0369FD0B1FE.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/C0239FE4-DB8B-E811-8E40-AC1F6B0DE3F8.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/C0DDBD34-9F8B-E811-B5B7-0648CA000185.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/C22EAFBF-B68B-E811-99DB-A0369FD0B2A0.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/C2C83064-AB8B-E811-9602-0CC47A4D99EE.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/C2FB466B-D38B-E811-BA65-AC1F6B0F7B16.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/C4071B04-DB8B-E811-BB85-A0369FD0B3A0.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/C4F47058-AD8B-E811-844D-AC1F6B0DE30C.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/C60A61F9-A48B-E811-B069-0090FAA58124.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/C65DF902-AB8B-E811-9D73-A0369FE2C0DE.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/C813F204-B78B-E811-9AD2-0090FAA57C74.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/C8140E8A-AB8B-E811-BCDE-0CC47A4DEF06.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/CAB3CF8F-B68B-E811-B115-A0369FD0B148.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/CC247DE6-AD8B-E811-B12E-A0369FD0B2A0.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/CC33B77C-EC8B-E811-8D60-0090FAA57E44.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/CCE074AB-AD8B-E811-8770-A0369FE2C084.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/D0A3DB55-AD8B-E811-9E9E-A0369FD0B2A4.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/D0C3CC7B-AD8B-E811-814C-AC1F6B0DE4A2.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/D229580D-788C-E811-9B7A-A0369FE2C21A.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/D2639E1D-B18B-E811-8E27-0090FAA57FA4.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/D2952392-AD8B-E811-8012-A0369FD0B1FE.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/D4A963B6-B08B-E811-8284-0090FAA57B10.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/D4AB1A66-C08B-E811-B6BB-0090FAA57AF0.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/D61D6E68-D38B-E811-8AC9-AC1F6B0F6758.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/D634DC74-D38B-E811-A369-A0369FD0B306.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/D87ADD68-A58B-E811-AEAF-06FDAA0000B2.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/D8E82536-9F8B-E811-ACF7-A0369FD0B374.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/DAC98C1B-838C-E811-B5AC-0CC47A4D99EE.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/DC564466-C08B-E811-B551-A0369FE2C18E.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/DE2AD18F-B68B-E811-8729-A0369FD0B148.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/DE4BC7F8-A48B-E811-B620-0090FAA58C54.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/DE6B9D47-AB8B-E811-B2DC-0090FAA572C0.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/DEF1B5B9-9F8B-E811-B329-0CC47A4DEEA2.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/E00ADA68-C08B-E811-A553-0090FAA57D64.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/E09A5667-D38B-E811-ABFA-0CC47A4D99EE.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/E0BB4EC0-B68B-E811-BB1C-A0369FD0B2A0.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/E2917C1A-B18B-E811-9724-AC1F6B0DE49C.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/E2A9D830-9F8B-E811-8C4C-0CC47A4DED58.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/E4555EB4-B08B-E811-8553-A0369FD0B3B0.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/E6A6BF69-D38B-E811-8349-0CC47A4DEDE6.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/E8B7EF89-B68B-E811-AF2E-AC1F6B0DE4A2.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/E8DB8F1B-B18B-E811-A02D-0CC47A4D9A5E.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/E8EE41F9-A48B-E811-8210-AC1F6B0DE30C.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/EA3E5C4F-788C-E811-80F6-A0369FD0B35A.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/EA5D15B8-B08B-E811-8A37-0CC47A4DED4E.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/EC5BE367-D38B-E811-92DB-A0369FE2C094.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/EE5EACEF-AA8B-E811-BFB4-0CC47A4DEDF2.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/EE850A72-AD8B-E811-ABC8-A0369FE2C0D2.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/F053B364-D38B-E811-B257-A0369FD0B3C4.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/F0E3D258-AD8B-E811-AB3D-0CC47A412A7A.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/F24EB6B4-B08B-E811-8F57-A0369FD0B1FE.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/F2C7B11C-B18B-E811-8C9B-0090FAA57FA4.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/F2DD324A-AB8B-E811-B7EA-A0369FD0B300.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/F437D168-D38B-E811-882C-0090FAA577A0.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/F4D37B8F-B68B-E811-81FE-0090FAA57CE4.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/F86BD5BD-D38B-E811-B1EC-0090FAA56994.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/F8732AF9-A48B-E811-AF4B-AC1F6B0DE30C.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/F884E57B-EC8B-E811-B4AF-0090FAA57D64.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/F8E7D400-6F8C-E811-B5C3-0090FAA575E0.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/FC0F17F9-A48B-E811-A183-AC1F6B0DE2F4.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/FC7547FC-6E8C-E811-83CA-0090FAA57B20.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/FE33A166-A58B-E811-8911-A0369FE2C042.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50000/FE4456DC-AA8B-E811-B505-A0369FD0B3A0.root',
       '/store/data/Run2016G/HTMHT/MINIAOD/17Jul2018-v1/50001/BC63A2EC-7B8B-E811-B517-A0369FD0B1F4.root',
] )

# -*- coding: utf-8 -*-

datas={1001: {'name': '新手接待员', 'dialogID': 10001001, 'runSpeed': 65, 'moveSpeed': 50, 'entityType': 'NPC', 'etype': 1, 'id': 1001, 'modelID': 1001}, 1002: {'name': '传送员', 'dialogID': 10001001, 'runSpeed': 65, 'moveSpeed': 50, 'entityType': 'NPC', 'etype': 1, 'id': 1002, 'modelID': 1001}, 1003: {'name': '怪物1', 'dialogID': 0, 'runSpeed': 65, 'moveSpeed': 50, 'entityType': 'Monster', 'etype': 1, 'id': 1003, 'modelID': 1002}, 1004: {'name': '怪物2', 'dialogID': 0, 'runSpeed': 65, 'moveSpeed': 50, 'entityType': 'Monster', 'etype': 1, 'id': 1004, 'modelID': 1003}, 2001: {'name': '怪物1', 'dialogID': 0, 'runSpeed': 65, 'moveSpeed': 50, 'entityType': 'Monster', 'etype': 1, 'id': 2001, 'modelID': 1001}, 2002: {'name': '怪物2', 'dialogID': 0, 'runSpeed': 65, 'moveSpeed': 50, 'entityType': 'Monster', 'etype': 1, 'id': 2002, 'modelID': 1002}, 2003: {'name': '怪物3', 'dialogID': 0, 'runSpeed': 65, 'moveSpeed': 50, 'entityType': 'Monster', 'etype': 1, 'id': 2003, 'modelID': 1003}}

# warring
datas.update({10004001: {'name': '怪物2', 'dialogID': 0, 'runSpeed': 65, 'entityType': 'Monster', 'moveSpeed': 50, 'etype': 1, 'id': 10004001, 'modelID': 10004001}, 10002001: {'name': '传送员', 'dialogID': 10001001, 'runSpeed': 65, 'entityType': 'NPC', 'moveSpeed': 50, 'etype': 1, 'id': 10002001, 'modelID': 10001001}, 10001001: {'name': '新手接待员', 'dialogID': 10001001, 'runSpeed': 65, 'entityType': 'NPC', 'moveSpeed': 50, 'etype': 1, 'id': 10001001, 'modelID': 10001001}, 20003001: {'name': '怪物3', 'dialogID': 0, 'runSpeed': 65, 'entityType': 'Monster', 'moveSpeed': 50, 'etype': 1, 'id': 20003001, 'modelID': 20001001}, 20002001: {'name': '压力山大巨龙', 'dialogID': 0, 'runSpeed': 65, 'entityType': 'Monster', 'moveSpeed': 50, 'etype': 1, 'id': 20002001, 'modelID': 20002001}, 20001001: {'name': '艾克斯球', 'dialogID': 0, 'runSpeed': 65, 'entityType': 'Monster', 'moveSpeed': 50, 'etype': 1, 'id': 20001001, 'modelID': 20001001}, 10003001: {'name': '怪物1', 'dialogID': 0, 'runSpeed': 65, 'entityType': 'Monster', 'moveSpeed': 50, 'etype': 1, 'id': 10003001, 'modelID': 10001001}})
datas.update({40001001: {'name': 'teleport(传送)', 'dialogID': 0, 'runSpeed': 0, 'entityType': 'Gate', 'moveSpeed': 0, 'etype': 1, 'id': 40001001, 'modelID': 40001001}})
datas.update({40001002: {'name': 'teleport-back(传送回去)', 'dialogID': 0, 'runSpeed': 0, 'entityType': 'Gate', 'moveSpeed': 0, 'etype': 1, 'id': 40001002, 'modelID': 40001001}})
allDatas = {
	'NPC表':datas,
}

csf = {
    'cw1-weight': 0.4,
    'cw1-mark':79,
    'exam-weight':0.6,
    'exam-mark':65
}


cw1Weight = csf.get('cw1-weight')
cw1Mark= csf.get('cw1-mark')
examWeight = csf.get(('exam-weight'))
examMark = csf.get(('exam-mark'))

averageMark = cw1Mark * cw1Weight + examMark * examWeight
print(averageMark)

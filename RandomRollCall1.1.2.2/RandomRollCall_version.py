# UTF-8
#
# For more details about fixed file info 'ffi' see:
# http://msdn.microsoft.com/en-us/library/ms646997.aspx
VSVersionInfo(
  ffi=FixedFileInfo(
    # filevers and prodvers should be always a tuple with four items: (1, 2, 3, 4)
    # Set not needed items to zero 0.
    filevers=(1, 1, 2, 2),# 文件版本
    prodvers=(1, 1, 2, 2),
    # Contains a bitmask that specifies the valid bits 'flags'r
    mask=0x3f,
    # Contains a bitmask that specifies the Boolean attributes of the file.
    flags=0x0,
    # The operating system for which this file was designed.
    # 0x4 - NT and there is no need to change it.
    OS=0x4,
    # The general type of file.
    # 0x1 - the file is an application.
    fileType=0x1,
    # The function of the file.
    # 0x0 - the function is not defined for this fileType
    subtype=0x0,
    # Creation date and time stamp.
    date=(0, 0)
    ),
  kids=[
    StringFileInfo(
      [
      StringTable(
        u'000004b0',
        [StringStruct(u'CompanyName', u'Python Software Foundation'),
        StringStruct(u'FileDescription', u'随机点名'),#文件说明
        StringStruct(u'FileVersion', u'1.1.2.2'),
        StringStruct(u'InternalName', u'RandomRollCall'),# 产品名称
        StringStruct(u'LegalCopyright', u'小喾苦'),#版权
        StringStruct(u'OriginalFilename', u'RandomRollCall.exe'),# 原始文件名
        StringStruct(u'ProductName', u'RandomRollCall'),
        StringStruct(u'ProductVersion', u'1.1.2.2')])
      ]), 
    VarFileInfo([VarStruct(u'Translation', [0, 1200])])
  ]
)

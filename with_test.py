class With_Test():
    def __enter__(self):
        print('enter')
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_tb is None:
            print('正常结束')
        else:
            print('has error %s' %exc_tb)

with With_Test():
    print('I am running...')
    raise NameError('testNameError')
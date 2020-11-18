import logging
"""

@Created:  2020/11/15 12:08
@Author: Tong Chu
@Summary:日志级别，日志器名称，日志内容
日志默认输出位置为sys.stderr


@Environment:

"""
# logging.debug("This is a debug log.")
# logging.info("This is a info log.")
# logging.warning("This is a warning log.")
# logging.error("This is a error log.")
# logging.critical("This is a critical log.")

# logging.log(logging.DEBUG, "This is a debug log.")
# logging.log(logging.INFO, "This is a info log.")
# logging.log(logging.WARNING, "This is a warning log.")
# logging.log(logging.ERROR, "This is a error log.")
# logging.log(logging.CRITICAL, "This is a critical log.")

# logging.basicConfig(filename='example.log', level=logging.DEBUG)
# logging.debug('this message should go to the log file')
# logging.info('so should this')
# logging.warning('and this, too')
import test_module
test_module.print_name('Nicole')
test_module.print_name('Duoduo')
test_module.print_name('Dabao')
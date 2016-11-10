__author__ = 'alipirani'
import os
from log_modules import keep_logging
from logging_subprocess import *

#################################################### BWA Alignment ############################################
def align_bwa(base_cmd,forward_clean, reverse_clean, out_path, reference, split_field, analysis, files_to_delete, logger, Config):
    cmd = "%s mem -M -R %s -t 8 %s %s %s > %s/%s_aln.sam" % (base_cmd,split_field, reference, forward_clean, reverse_clean, out_path, analysis)
    keep_logging(cmd, cmd, logger, 'debug')
    try:
        #call(cmd, logger)
        print ""
    except sp.CalledProcessError:
        keep_logging('Error in Alignment step. Exiting.', 'Error in Alignment step. Exiting.', logger, 'exception')
        sys.exit(1)
    out_sam = "%s/%s_aln.sam" % (out_path, analysis)
    files_to_delete.append(out_sam)
    if not os.path.isfile(out_sam):
        keep_logging('Problem in BWA alignment. SAM file was not generated.', 'Problem in BWA alignment. SAM file was not generated', logger, 'exception')
        exit()
    else:
        return out_sam
#################################################### END: BWA Alignment #######################################



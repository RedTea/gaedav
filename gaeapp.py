import sys
import logging 
from pyfileserver.mainappwrapper import PyFileApp
from google.appengine.ext.webapp.util import run_wsgi_app

def real_main():
    app = PyFileApp('PyFileServer.conf')
    run_wsgi_app(app)

def profile_main():
    # This is the main function for profiling 
    # We've renamed our original main() above to real_main()
    import cProfile, pstats, StringIO
    prof = cProfile.Profile()
    prof = prof.runctx("real_main()", globals(), locals())
    stream = StringIO.StringIO()
    stats = pstats.Stats(prof, stream=stream)
    stats.sort_stats("time")  # Or cumulative
    stats.print_stats(80)  # 80 = how many to print
    # The rest is optional.
    # stats.print_callees()
    # stats.print_callers()
    logging.info("Profile data:\n%s", stream.getvalue())

main = profile_main

if __name__ == "__main__":
    main()

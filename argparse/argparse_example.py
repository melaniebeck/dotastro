import argparse
from astropy.io import fits

def write_fits_extention(infile, ext, outfile):
    fits.open(infile)[ext].writeto(outfile)




if __name__=='__main__':
    parser = argparse.ArgumentParser(description='tool that does something')
    parser.add_argument('filename')
    parser.add_argument('extention')

    group = parser.add_mutually_exclusive_group()
    group.add_argument('--verbose',action='store_true')
    group.add_argument('--quiet',action='store_true')
    
    args = parser.parse_args()

    outfile = '{}-ext{}.fits'.format(args.filename, args.extention)
    print "writing "+outfile

    write_fits_extention(infile=args.filename,
                         ext=args.extention,
                         outfile=outfile)
    

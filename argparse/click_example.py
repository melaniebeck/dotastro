import click
from astropy.io import fits

def write_fits_extention(infile, ext, outfile):
    fits.open(infile)[ext].writeto(outfile)


@click.command(help='write some shit')
@click.argument('filename')
@click.argument('extention', type=int)
@click.option('-c','-clobber', is_flag=True)

def fitsextract_click(filename, extention, clobber):
    outfile = '{}-ext{}.fits'.format(args.filename, args.extention)
    print "writing "+outfile

    write_fits_extention(infile=args.filename,
                         ext=args.extention,
                         outfile=outfile)
    

if __name__=='__main__':
    fitsextract_click()

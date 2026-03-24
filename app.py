#!/usr/bin/env python3
"""Apply watermark overlays to videos, including batch use."""
import argparse, shutil, subprocess

def require(x):
    if shutil.which(x) is None: raise SystemExit(f'Missing required binary: {x}')

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('input'); p.add_argument('watermark'); p.add_argument('output'); p.add_argument('--position',default='10:10'); p.add_argument('--opacity',type=float,default=0.8); p.add_argument('--dry-run',action='store_true')
    a=p.parse_args(); require('ffmpeg')
    fc=f'[1:v]format=rgba,colorchannelmixer=aa={a.opacity}[wm];[0:v][wm]overlay={a.position}'
    cmd=['ffmpeg','-y','-i',a.input,'-i',a.watermark,'-filter_complex',fc,'-codec:a','copy',a.output]
    print(' '.join(cmd))
    if not a.dry_run: subprocess.check_call(cmd)
if __name__ == '__main__': main()

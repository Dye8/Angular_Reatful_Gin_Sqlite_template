#! /usr/bin/env python

import os
import shutil
import logging
from urllib.request import urlopen
import urllib.error

# set logger
LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.DEBUG)

FILE_HANDLER = logging.FileHandler('./temp/fetch_file_logger.txt')
FILE_HANDLER.setLevel(logging.DEBUG)
FILE_HANDLER.setFormatter(
    logging.Formatter('%(asctime)s - %(name)s - %(message)s'))

LOGGER.addHandler(FILE_HANDLER)

TISSUES = [
    "Bladder",
    "Bone-Marrow",
    "Brain",
    "Bone-Marrow-c-kit",
    "Embryonic-Mesenchyme",
    "Embryonic-Stem-Cell",
    "Fetal-Liver",
    "Kidney",
    "Liver",
    "Lung",
    "Mammary-Gland-Involution",
    "Mammary-Gland-Lactation",
    "Mammary-Gland-Pregnancy",
    "Mammary-Gland-Virgin",
    "Muscle",
    "Neonatal-Calvaria",
    "Neonatal-Muscle",
    "Neonatal-Heart",
    "Neonatal-Rib",
    "Neonatal-Skin",
    "E18-Brain",
    "Ovary",
    "Pancreas",
    "Peripheral-Blood",
    "Placenta",
    "Preimplantation-Embryo",
    "Prostate",
    "Retina",
    "Small-Intestine",
    "Spleen",
    "Stomach",
    "Testis",
    "Thymus",
    "Trophoblast-Stem-Cell",
    "Uterus",
    "Lung-Mesenchyme",
    "Fetal-Brain",
    "Female-Fetal-Gonad",
    "Fetal-Intestine",
    "Fetal-Lung",
    "Fetal-Kidney",
    "Male-Fetal-Gonad",
    "Fetal-Stomache",
    "Bone-Marrow-Mesenchyme",
    "Neonatal-Brain",
    "Mesenchymal-Stem-Cell-Cultured",
    "E8.25-embryo",
    "Figure2-98Clusters",
    "Arcuate-hypothalamus-and-median-eminence",
]

OUTPUT_DIR = "./temp/MCA"


def downlaod_link(link, outdir=OUTPUT_DIR):
    """download link into dir, and keep the filename in the link"""
    os.makedirs(outdir, exist_ok=True)
    out_file_fullname = os.path.join(OUTPUT_DIR, link.split("/")[-1])
    if os.path.exists(
            out_file_fullname) and os.path.getsize(out_file_fullname) > 0:
        return 0
    try:
        with urlopen(link) as in_stream, open(out_file_fullname,
                                              'wb') as out_file:
            shutil.copyfileobj(in_stream, out_file)
            LOGGER.info("Success: %s", link)
            return 1
    except urllib.error.HTTPError:
        LOGGER.debug("FAILED: %s", link)
        return 0


for tissue in TISSUES:
    cell_tsne = "http://bis.zju.edu.cn/MCA/data/tissues/{}/tsne_{}.csv".format(
        tissue, tissue)
    marker_mca = "http://bis.zju.edu.cn/MCA/data/tissues/{}/mca_top_markers_{}.json".format(
        tissue, tissue)
    downlaod_link(cell_tsne)
    downlaod_link(marker_mca)

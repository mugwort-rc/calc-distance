#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import csv
import os
import sys

from geopy.distance import vincenty
from progressbar import ProgressBar


def main(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument("points1", type=argparse.FileType("r", encoding="utf-8"))
    parser.add_argument("points2", type=argparse.FileType("r", encoding="utf-8"))
    #parser.add_argument("--max_radius")

    args = parser.parse_args(argv)

    reader1 = csv.reader(args.points1)
    for header1 in reader1:
        break
    reader2 = csv.reader(args.points2)
    for header2 in reader2:
        break

    lat_idx1, lon_idx1, id_idx1 = get_index(header1)
    lat_idx2, lon_idx2, id_idx2 = get_index(header2)

    error = False
    if lat_idx1 is None:
        error = True
        print("Latitude not in", args.points1.name, file=sys.stderr)
    if lon_idx1 is None:
        error = True
        print("Longitude not in", args.points1.name, file=sys.stderr)
    if id_idx1 is None:
        error = True
        print("ID not in", args.points1.name, file=sys.stderr)
    if lat_idx2 is None:
        error = True
        print("Latitude not in", args.points2.name, file=sys.stderr)
    if lon_idx2 is None:
        error = True
        print("Longitude not in", args.points2.name, file=sys.stderr)
    if id_idx2 is None:
        error = True
        print("ID not in", args.points2.name, file=sys.stderr)

    if error:
        return 1

    points2 = []
    for row in reader2:
        points2.append((
            row[id_idx2],
            row[lat_idx2],
            row[lon_idx2],
        ))

    count = 0
    for row in open(args.points1.name, encoding="utf-8"):
        count += 1
    count -= 1

    bar = ProgressBar(max_value=count)
    with open("output.csv", "w", encoding="utf-8", newline="") as fp:
        writer = csv.writer(fp)
        writer.writerow(header1 + ["Station", "Distance"])
        for i, row in enumerate(reader1, 1):
            id1 = row[id_idx1]
            lat1 = row[lat_idx1]
            lon1 = row[lon_idx1]
            id = None
            distance = 999999.0
            for id2, lat2, lon2 in points2:
                d = vincenty((lat1, lon1), (lat2, lon2)).meters
                if distance > d:
                    distance = d
                    id = id2
            writer.writerow(row + [id, distance])
            bar.update(i)

    return 0


def get_index(header):
    lat, lon, id = None, None, None
    if "Latitude" in header:
        lat = header.index("Latitude")
    if "Longitude" in header:
        lon = header.index("Longitude")
    if "ID" in header:
        id = header.index("ID")
    return lat, lon, id


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

# TODO find a nicer way to do this
import argparse
from foosballapi import create_all_players

parser = argparse.ArgumentParser()
parser.add_argument('--year', required = True, type = int)
parser.add_argument('--kind', required = True, type = str)
parser.add_argument('--host', required = True, type = str)
parser.add_argument('--port', required = True, type = int)
ns = parser.parse_args()

create_all_players(
	ns.host,
	ns.port,
	ns.year if ns.kind == "REG" else ns.year - 1,
	"PRE" if ns.kind == "REG" else "REG",
	range(1, 5 if ns.kind == "REG" else 18)
)
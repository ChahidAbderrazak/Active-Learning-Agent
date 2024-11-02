import gc

gc.collect()
from utils import agent


def prepare_parser():
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument(
        "--cfg",
        default="config/config.yml",
        metavar="FILE",
        help="path to config file",
        type=str,
    )
    return parser


def main(file=""):
    parser = prepare_parser()
    args = parser.parse_args()
    try:
        config_file = args.cfg
    except:
        config_file = file
    agent1 = agent.AcliveLearningAgent(config_file=config_file, verbose=1)


if __name__ == "__main__":
    main()

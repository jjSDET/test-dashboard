import argparse
import sys

from testrail import TestRailHelpers


PROJECTS_ABBREV = [
    'fenix',
    'focus-android',
    'reference-browser',
    'firefox-ios',
    'focus-ios',
]

REPORT_TYPES = [
    'test-cases',
    'test-runs',
    'issue-regression',
]


def parse_args(cmdln_args):
    parser = argparse.ArgumentParser(
        description="Retrieve and update mobile project test data"
    )

    parser.add_argument(
        "--project",
        help="Indicate project",
        required=True,
        choices=PROJECTS_ABBREV
    )

    parser.add_argument(
        "--report-type",
        help="Indicate report type",
        required=True,
        choices=REPORT_TYPES
    )

    parser.add_argument(
        "--start-date",
        help="Indicate data range start date: YYYY-MM-DD",
        required=False
    )

    parser.add_argument(
        "--end-date",
        help="Indicate data range end date: YYYY-MM-DD",
        required=False
    )
    return parser.parse_args(args=cmdln_args)


def main():
    args = parse_args(sys.argv[1:])

    if args.report_type == 'test-cases':
        h = TestRailHelpers()
        h.testrail_coverage_update(args.project)
    if args.report_type == 'test-runs':
        h = TestRailHelpers()
        h.testrail_run_update(args.project, args.start_date, args.end_date)
    if args.report_type == 'issue-regression':
        """
        h = GithubHelpers()
        h.github_issue_regression(args.project)
        h = GithubHelpers()
        """
        pass


if __name__ == '__main__':
    main()

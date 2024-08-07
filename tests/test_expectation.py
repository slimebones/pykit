from ryz.check import check
from ryz.condition import ComparisonCondition, ComparisonMark
from ryz.expectation import (
    ExpectationErr,
    ListExpectation,
    UnsupportedExpectationTypeErr,
)


def test_count():
    expectation: ListExpectation = ListExpectation(count=ComparisonCondition(
        mark=ComparisonMark.MoreEqual,
        value=3,
    ))

    check.expect(
        expectation.check,
        ExpectationErr,
        [1, 2],
    )
    expectation.check([1, 2, 3])
    expectation.check([1, 2, 3, 4])


def test_unsupported_type():
    expectation: ListExpectation = ListExpectation(count=ComparisonCondition(
        mark=ComparisonMark.MoreEqual,
        value=2,
    ))

    check.expect(
        expectation.check,
        UnsupportedExpectationTypeErr,
        # only list should be expected as a target
        2,
    )

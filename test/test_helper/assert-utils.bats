#!/usr/bin/env bats

load "bats-support/load"
load "bats-assert/load"
load "assert-utils"

@test "assert not equal" {
    assert_not_equal 'a' 'b'
    run assert_not_equal 'a' 'a' ; assert_failure
}

@test "assert contain" {
    assert_contain 'ab' 'ab'
    assert_contain 'abcd' 'ab'
    assert_contain 'abcd' 'bc'
    assert_contain 'abcd' 'cd'
    run assert_contain 'ab' 'abcd' ; assert_failure
    run assert_contain 'bc' 'abcd' ; assert_failure
    run assert_contain 'cd' 'abcd' ; assert_failure
}

@test "assert start with" {
    assert_start_with 'ab' 'ab'
    assert_start_with 'abcd' 'ab'
    run assert_start_with 'abcd' 'bd' ; assert_failure
    run assert_start_with 'abcd' 'cd' ; assert_failure
}

@test "assert ends with" {
    assert_end_with 'ab' 'ab'
    assert_end_with 'abcd' 'cd'
    run assert_end_with 'abcd' 'ab' ; assert_failure
    run assert_end_with 'abcd' 'bc' ; assert_failure
}

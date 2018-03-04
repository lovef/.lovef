#!/usr/bin/env bats

load "../../test/test_helper/bats-support/load"
load "../../test/test_helper/bats-assert/load"
load "../../test/test_helper/assert-utils"

setup() {
    source windows/.bash_profile
}

@test "pathsToWin: no path as input gives no output" {
    assert_equal `pathsToWin` ""
}

@test "pathsToWin: paths are processed in cygpath, commands are not" {
    assert_equal "$(pathsToWin .. --path ~)" "$(cygpath -w ..) --path $(cygpath -w ~)"
}

# group11

Collaborative software development lab for group11: student discount feature implementation.

## Student discount

`checkout.py` applies a 10% discount to eligible students and leaves non-student totals unchanged. Totals are rounded to two decimal places; negative totals are rejected.

Run the automated checks with `python -m unittest -v`.

## Assessment answers

1. `git clone` downloads a repository and its history to a local machine, creating a working copy connected to the remote.
2. A repository stores project files and their version history. A branch is a movable reference to a line of development within that repository.
3. `git switch -c add-discount` creates a branch named `add-discount` from the current commit and switches to it.
4. `git add` stages selected changes so they can be included in the next commit.
5. `git commit` records a snapshot of staged changes in the repository history with an author and message.
6. `git push` sends local commits to a remote repository; `git pull` fetches remote commits and integrates them into the current local branch.
7. A Pull Request proposes merging changes from one branch into another and provides a place for discussion and review.
8. Code review can catch defects, improve clarity and consistency, share knowledge, and check that changes meet project requirements before integration.
9. Simultaneous edits can conflict when Git cannot automatically combine them. Even when changes merge cleanly, one edit may unintentionally overwrite or break another, so the combined result should be reviewed and tested.
10. Branches let developers work on features independently, keep unfinished work separate from the stable branch, and make changes easier to review and integrate.

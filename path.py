# !/usr/bin/env python
# coding=utf-8

# Given an absolute path for a file (Unix-style), simplify it.
# eg: "/home/", => "/home",  "/a/./b/../../c/", => "/c"

def simplify_path(path):
    folds = path.split("/")
    stack = []
    for fold in folds:
        if fold == "..":
           if stack: stack.pop()  # path = "/.."
        elif fold != "." and fold != "":
            stack.append(fold)

    return "/" + "/".join(stack)

if __name__ == "__main__":
    # path = "/"
    # path = "/root"
    path = "/root/.."
    print simplify_path(path)

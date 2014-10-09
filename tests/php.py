syntax = "Packages/PHP/PHP.tmLanguage"

def test_for_issue_292_php_args_pass_by_reference_missing_ampersand_char(helper):
    "PHP pass by reference https://github.com/spadgos/sublime-jsdocs/issues/292"

    helper.insert("/**|\nfunction function_name($a1,  $a2 = 'x', array $a3, &$b1, &$b2 = 'x', array &$b3) {}")
    helper.run()

    return [
        "/**",
        " * |[function_name description]|",
        " * @param  {[type]} $a1  [description]",
        " * @param  string $a2  [description]",
        " * @param  array  $a3  [description]",
        " * @param  {[type]} &$b1 [description]",
        " * @param  string &$b2 [description]",
        " * @param  array  &$b3 [description]",
        " * @return {[type]}      [description]",
        " */",
        "function function_name($a1,  $a2 = 'x', array $a3, &$b1, &$b2 = 'x', array &$b3) {}"
    ]

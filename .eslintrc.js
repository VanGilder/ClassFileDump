{
    "root": true,
    "rules": {
        "arrow-parens": [
            2,
            "always"
        ],
        "max-len": [
            1,
            {
                "code": 100
            }
        ],
        "indent": [
            2,
            4,
            {
                "SwitchCase": 1,
                "MemberExpression": "off",
                "flatTernaryExpressions": true
            }
        ],
        "no-unused-vars": [
            1,
            {
                "args": "all",
                "argsIgnorePattern": "(^.+_$)",
                "varsIgnorePattern": "(^.+_$)"
            }
        ],
        "comma-spacing": [
            1,
            {
                "before": false,
                "after": true
            }
        ],
        "comma-dangle": [
            1,
            "always-multiline"
        ],
        "eol-last": 2,
        "eqeqeq": 2,
        "linebreak-style": [
            2,
            "unix"
        ],
        "radix": [
            2,
            "as-needed"
        ],
        "semi": [
            2,
            "always"
        ]
    },
    "env": {
        "browser": true,
        "node": true,
        "es2021": true
    },
    "parserOptions": {
        "ecmaVersion": 2021,
        "sourceType": "script",
        "ecmaFeatures": {
            "impliedStrict": true
        }
    },
    "extends": [
        "eslint:recommended"
    ]
}

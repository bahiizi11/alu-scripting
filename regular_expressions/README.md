# alu-scripting

Scripting projects for the ALU/Holberton-style curriculum.

## regular_expressions

Ruby scripts exploring regular expression basics: literal matches,
repetition tokens, anchors, character classes, and log-line parsing.
Each script reads its input from a single command-line argument
(`ARGV[0]`) and prints only the matched portion of the string.

| File | Description |
| --- | --- |
| `0-simply_match_school.rb` | Matches the literal word `School` |
| `0-simply_match_holberton.rb` | Same as above, alternate filename |
| `1-repetition_token_0.rb` | Repetition token: `*` (0 or more) |
| `2-repetition_token_1.rb` | Repetition token: `+` (1 or more) |
| `3-repetition_token_2.rb` | Repetition token: `?` (0 or 1) |
| `4-repetition_token_3.rb` | Repetition token: `{m,n}` (specific range, no `[]`) |
| `5-beginning_and_end.rb` | Matches strings starting with `h`, ending with `n`, one char between |
| `6-phone_number.rb` | Matches a plain 10-digit phone number |
| `7-OMG_WHY_ARE_YOU_SHOUTING.rb` | Extracts only capital letters from a string |
| `8-textme.rb` | Parses TextMe log lines into `sender,receiver,flags` |

### Usage

```bash
./0-simply_match_school.rb "Best School"
```

### Requirements

- Ruby 3.x
- Scripts are executable (`chmod +x`) and start with `#!/usr/bin/env ruby`

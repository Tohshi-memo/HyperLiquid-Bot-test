# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-12T17:22:30.986288+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8954`

## Conditions

- `news_risk_high`: News Risk is elevated.
- `macro_risk_high`: Macro Risk is elevated.
- `risk_on_high`: Risk-On score is elevated.
- `market_context_high`: Market Context is supportive.
- `polymarket_volume_spike`: Polymarket 24h volume z-score is elevated.
- `flow_alert_high`: Flow Alert score is elevated.
- `news_and_polymarket`: News Risk and Polymarket volume spike happen together.
- `risk_on_and_context`: Risk-On and Market Context are both supportive.
- `macro_and_flow`: Macro Risk and Flow Alert are elevated together.

## Top Patterns

- `market_context_high->crypto_major_24h` score `11.4164` n `55` status `ready` deltaP `32.358` edge `1.4965` maxDD `-15.8859`
- `market_context_high->crypto_alt_24h` score `8.6046` n `55` status `ready` deltaP `20.3788` edge `1.3431` maxDD `-25.7309`
- `risk_on_high->crypto_alt_4h` score `4.2148` n `48` status `ready` deltaP `18.496` edge `0.2727` maxDD `-1.9151`
- `risk_on_and_context->crypto_alt_4h` score `4.2148` n `48` status `ready` deltaP `18.496` edge `0.2727` maxDD `-1.9151`
- `risk_on_high->crypto_major_4h` score `3.6583` n `48` status `ready` deltaP `33.2826` edge `0.3324` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `3.6583` n `48` status `ready` deltaP `33.2826` edge `0.3324` maxDD `-4.1548`
- `market_context_high->crypto_alt_4h` score `3.5129` n `100` status `ready` deltaP `13.5793` edge `0.3471` maxDD `-9.2574`
- `market_context_high->crypto_major_4h` score `3.2376` n `100` status `ready` deltaP `17.1159` edge `0.3116` maxDD `-7.4722`
- `market_context_high->crypto_alt_1h` score `1.6292` n `100` status `ready` deltaP `12.3533` edge `0.1485` maxDD `-4.9401`
- `risk_on_high->crypto_alt_1h` score `1.0078` n `48` status `ready` deltaP `6.6866` edge `0.0991` maxDD `-2.4421`
- `risk_on_and_context->crypto_alt_1h` score `1.0078` n `48` status `ready` deltaP `6.6866` edge `0.0991` maxDD `-2.4421`
- `market_context_high->crypto_major_1h` score `0.6704` n `100` status `ready` deltaP `4.3473` edge `0.1032` maxDD `-3.4384`
- `risk_on_high->crypto_major_1h` score `0.4241` n `48` status `ready` deltaP `5.514` edge `0.0829` maxDD `-3.2233`
- `risk_on_and_context->crypto_major_1h` score `0.4241` n `48` status `ready` deltaP `5.514` edge `0.0829` maxDD `-3.2233`
- `market_context_high->unknown_4h` score `0.2135` n `100` status `ready` deltaP `-3.9268` edge `0.1086` maxDD `-1.8373`
- `market_context_high->index_1h` score `-0.0156` n `100` status `ready` deltaP `4.1502` edge `0.0034` maxDD `-0.3122`
- `market_context_high->metal_24h` score `-0.1171` n `55` status `ready` deltaP `7.642` edge `0.0383` maxDD `-2.341`
- `market_context_high->metal_1h` score `-0.1201` n `100` status `ready` deltaP `6.2515` edge `0.0044` maxDD `-0.4868`
- `risk_on_high->metal_1h` score `-0.3028` n `48` status `ready` deltaP `3.4182` edge `0.0039` maxDD `-0.4868`
- `risk_on_and_context->metal_1h` score `-0.3028` n `48` status `ready` deltaP `3.4182` edge `0.0039` maxDD `-0.4868`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-12T23:07:28.061229+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8774`

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

- `risk_on_high->crypto_alt_4h` score `4.9629` n `48` status `ready` deltaP `20.7826` edge `0.3198` maxDD `-1.9151`
- `risk_on_and_context->crypto_alt_4h` score `4.9629` n `48` status `ready` deltaP `20.7826` edge `0.3198` maxDD `-1.9151`
- `market_context_high->crypto_alt_4h` score `4.2611` n `100` status `ready` deltaP `15.8659` edge `0.3942` maxDD `-9.2574`
- `risk_on_high->crypto_major_4h` score `4.0244` n `48` status `ready` deltaP `35.4167` edge `0.3651` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `4.0244` n `48` status `ready` deltaP `35.4167` edge `0.3651` maxDD `-4.1548`
- `market_context_high->crypto_major_4h` score `3.8008` n `100` status `ready` deltaP `19.25` edge `0.3443` maxDD `-7.4722`
- `market_context_high->crypto_alt_1h` score `1.8715` n `100` status `ready` deltaP `13.4012` edge `0.1617` maxDD `-4.9401`
- `risk_on_high->crypto_alt_1h` score `1.25` n `48` status `ready` deltaP `7.7345` edge `0.1123` maxDD `-2.4421`
- `risk_on_and_context->crypto_alt_1h` score `1.25` n `48` status `ready` deltaP `7.7345` edge `0.1123` maxDD `-2.4421`
- `market_context_high->crypto_major_1h` score `0.897` n `100` status `ready` deltaP `5.6946` edge `0.1131` maxDD `-3.4384`
- `risk_on_high->crypto_major_1h` score `0.5714` n `48` status `ready` deltaP `6.8613` edge `0.0928` maxDD `-3.2233`
- `risk_on_and_context->crypto_major_1h` score `0.5714` n `48` status `ready` deltaP `6.8613` edge `0.0928` maxDD `-3.2233`
- `market_context_high->unknown_4h` score `0.4971` n `100` status `ready` deltaP `-4.5366` edge `0.1363` maxDD `-1.8373`
- `market_context_high->index_1h` score `0.0429` n `100` status `ready` deltaP `5.2012` edge `0.0039` maxDD `-0.3122`
- `market_context_high->metal_1h` score `-0.1453` n `100` status `ready` deltaP `5.9521` edge `0.0043` maxDD `-0.4868`
- `market_context_high->metal_4h` score `-0.297` n `100` status `ready` deltaP `9.0671` edge `0.0101` maxDD `-1.624`
- `risk_on_high->metal_1h` score `-0.3279` n `48` status `ready` deltaP `3.1188` edge `0.0038` maxDD `-0.4868`
- `risk_on_and_context->metal_1h` score `-0.3279` n `48` status `ready` deltaP `3.1188` edge `0.0038` maxDD `-0.4868`
- `market_context_high->fx_1h` score `-0.3346` n `100` status `ready` deltaP `-0.5526` edge `-0.0012` maxDD `-0.3742`
- `market_context_high->crypto_major_24h` score `-0.3956` n `78` status `ready` deltaP `11.9391` edge `0.7974` maxDD `-62.5501`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

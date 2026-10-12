# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-12T14:52:32.780707+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `7550`

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

- `market_context_high->crypto_alt_24h` score `27.1828` n `45` status `ready` deltaP `36.5972` edge `2.0665` maxDD `-2.6199`
- `market_context_high->crypto_major_24h` score `26.739` n `45` status `ready` deltaP `48.2292` edge `1.9301` maxDD `-1.2036`
- `risk_on_high->crypto_alt_4h` score `4.0128` n `48` status `ready` deltaP `18.1911` edge `0.2579` maxDD `-1.9151`
- `risk_on_and_context->crypto_alt_4h` score `4.0128` n `48` status `ready` deltaP `18.1911` edge `0.2579` maxDD `-1.9151`
- `risk_on_high->crypto_major_4h` score `3.5872` n `48` status `ready` deltaP `33.1301` edge `0.3243` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `3.5872` n `48` status `ready` deltaP `33.1301` edge `0.3243` maxDD `-4.1548`
- `market_context_high->crypto_alt_4h` score `3.3109` n `100` status `ready` deltaP `13.2744` edge `0.3323` maxDD `-9.2574`
- `market_context_high->crypto_major_4h` score `3.1282` n `100` status `ready` deltaP `16.9634` edge `0.3035` maxDD `-7.4722`
- `market_context_high->crypto_alt_1h` score `1.6113` n `100` status `ready` deltaP `12.2036` edge `0.148` maxDD `-4.9401`
- `market_context_high->metal_24h` score `1.4196` n `45` status `ready` deltaP `22.1875` edge `0.079` maxDD `-0.9265`
- `risk_on_high->crypto_alt_1h` score `0.9898` n `48` status `ready` deltaP `6.5369` edge `0.0986` maxDD `-2.4421`
- `risk_on_and_context->crypto_alt_1h` score `0.9898` n `48` status `ready` deltaP `6.5369` edge `0.0986` maxDD `-2.4421`
- `market_context_high->crypto_major_1h` score `0.6488` n `100` status `ready` deltaP `4.1976` edge `0.1024` maxDD `-3.4384`
- `risk_on_high->crypto_major_1h` score `0.4101` n `48` status `ready` deltaP `5.3643` edge `0.0821` maxDD `-3.2233`
- `risk_on_and_context->crypto_major_1h` score `0.4101` n `48` status `ready` deltaP `5.3643` edge `0.0821` maxDD `-3.2233`
- `market_context_high->index_1h` score `-0.0476` n `100` status `ready` deltaP `3.6252` edge `0.0028` maxDD `-0.3122`
- `market_context_high->metal_1h` score `-0.1033` n `100` status `ready` deltaP `6.4012` edge `0.0048` maxDD `-0.4868`
- `market_context_high->unknown_4h` score `-0.1407` n `100` status `ready` deltaP `-4.9939` edge `0.0862` maxDD `-1.8373`
- `risk_on_high->metal_1h` score `-0.286` n `48` status `ready` deltaP `3.5679` edge `0.0043` maxDD `-0.4868`
- `risk_on_and_context->metal_1h` score `-0.286` n `48` status `ready` deltaP `3.5679` edge `0.0043` maxDD `-0.4868`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

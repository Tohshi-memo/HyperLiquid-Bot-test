# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-13T16:22:31.639538+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13440`

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

- `market_context_high->unknown_24h` score `17793.0756` n `56` status `ready` deltaP `10.2093` edge `1482.7084` maxDD `-0.613`
- `risk_on_high->unknown_24h` score `8516.9474` n `36` status `ready` deltaP `13.5823` edge `709.6608` maxDD `-0.1252`
- `risk_on_and_context->unknown_24h` score `8516.9474` n `36` status `ready` deltaP `13.5823` edge `709.6608` maxDD `-0.1252`
- `news_risk_high->unknown_1h` score `422.2587` n `82` status `ready` deltaP `-4.9511` edge `35.2634` maxDD `-1.7068`
- `news_risk_high->crypto_alt_24h` score `18.5809` n `82` status `ready` deltaP `35.6854` edge `1.3593` maxDD `-2.2369`
- `news_risk_high->crypto_major_24h` score `18.406` n `82` status `ready` deltaP `38.0236` edge `1.4274` maxDD `-9.098`
- `news_risk_high->equity_24h` score `8.8458` n `82` status `ready` deltaP `25.7191` edge `0.7437` maxDD `-6.5742`
- `news_risk_high->index_24h` score `6.9393` n `82` status `ready` deltaP `49.4911` edge `0.266` maxDD `-0.0797`
- `news_risk_high->metal_24h` score `4.6074` n `82` status `ready` deltaP `24.7603` edge `0.2643` maxDD `-0.6334`
- `risk_on_high->commodity_24h` score `4.2806` n `36` status `ready` deltaP `39.8276` edge `0.0912` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `4.2806` n `36` status `ready` deltaP `39.8276` edge `0.0912` maxDD `0.0`
- `market_context_high->commodity_24h` score `4.2422` n `56` status `ready` deltaP `39.8276` edge `0.088` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `3.9316` n `36` status `ready` deltaP `13.8697` edge `0.5048` maxDD `-5.4574`
- `risk_on_and_context->crypto_alt_24h` score `3.9316` n `36` status `ready` deltaP `13.8697` edge `0.5048` maxDD `-5.4574`
- `market_context_high->crypto_alt_24h` score `3.3472` n `56` status `ready` deltaP `9.9015` edge `0.4972` maxDD `-8.0596`
- `market_context_high->metal_24h` score `1.0092` n `56` status `ready` deltaP `12.2167` edge `0.1258` maxDD `-1.2288`
- `risk_on_high->index_24h` score `0.8123` n `36` status `ready` deltaP `29.2337` edge `0.0073` maxDD `-3.5102`
- `risk_on_and_context->index_24h` score `0.8123` n `36` status `ready` deltaP `29.2337` edge `0.0073` maxDD `-3.5102`
- `market_context_high->index_24h` score `0.5562` n `56` status `ready` deltaP `29.6305` edge `0.0174` maxDD `-4.8234`
- `news_risk_high->index_4h` score `0.3982` n `82` status `ready` deltaP `12.0427` edge `0.0336` maxDD `-0.6935`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

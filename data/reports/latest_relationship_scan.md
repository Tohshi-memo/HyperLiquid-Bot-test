# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-07T19:52:10.701679+00:00`
- Price records: `579`
- Market context records: `678`
- Flow alert records: `1922`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `901`

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

- `market_context_high->crypto_major_24h` score `9.2881` n `146` status `ready` deltaP `23.2508` edge `0.6524` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `6.5117` n `146` status `ready` deltaP `8.6319` edge `0.4899` maxDD `-0.0508`
- `market_context_high->fx_4h` score `-0.2222` n `147` status `ready` deltaP `6.9828` edge `0.0121` maxDD `-1.6381`
- `market_context_high->fx_1h` score `-0.2971` n `149` status `ready` deltaP `2.5517` edge `0.0027` maxDD `-0.291`
- `market_context_high->commodity_1h` score `-0.4735` n `149` status `ready` deltaP `2.2332` edge `0.0431` maxDD `-3.7959`
- `market_context_high->index_1h` score `-0.5876` n `149` status `ready` deltaP `0.858` edge `0.0043` maxDD `-2.8282`
- `market_context_high->equity_1h` score `-1.154` n `149` status `ready` deltaP `-1.5645` edge `-0.0047` maxDD `-4.4826`
- `market_context_high->unknown_1h` score `-1.3204` n `149` status `ready` deltaP `-5.0692` edge `-0.0159` maxDD `-2.1602`
- `market_context_high->crypto_alt_1h` score `-1.4169` n `149` status `ready` deltaP `4.3046` edge `-0.0153` maxDD `-8.1842`
- `market_context_high->index_4h` score `-1.6389` n `147` status `ready` deltaP `2.7297` edge `-0.0025` maxDD `-6.5149`
- `market_context_high->crypto_major_1h` score `-1.6908` n `149` status `ready` deltaP `5.5197` edge `-0.0054` maxDD `-11.4508`
- `market_context_high->crypto_major_4h` score `-1.7229` n `147` status `ready` deltaP `16.1888` edge `0.1191` maxDD `-22.648`
- `market_context_high->crypto_alt_4h` score `-1.7422` n `147` status `ready` deltaP `5.3237` edge `0.0763` maxDD `-15.2248`
- `market_context_high->index_24h` score `-2.1597` n `146` status `ready` deltaP `-6.5791` edge `0.0634` maxDD `-5.9609`
- `market_context_high->equity_4h` score `-2.6237` n `147` status `ready` deltaP `-1.3848` edge `0.0058` maxDD `-10.5498`
- `market_context_high->metal_1h` score `-3.3526` n `149` status `ready` deltaP `-5.0178` edge `-0.05` maxDD `-9.0076`
- `market_context_high->commodity_4h` score `-3.6857` n `147` status `ready` deltaP `-5.5565` edge `0.08` maxDD `-13.0076`
- `market_context_high->equity_24h` score `-3.7018` n `146` status `ready` deltaP `-8.7911` edge `0.0106` maxDD `-10.5047`
- `market_context_high->unknown_4h` score `-4.5633` n `147` status `ready` deltaP `1.9864` edge `-0.2057` maxDD `-8.3588`
- `market_context_high->fx_24h` score `-4.7995` n `146` status `ready` deltaP `-9.02` edge `-0.038` maxDD `-21.0414`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

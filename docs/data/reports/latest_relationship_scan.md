# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-06T07:07:21.567859+00:00`
- Price records: `672`
- Market context records: `3049`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6969`

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

- `market_context_high->crypto_alt_24h` score `25.313` n `99` status `ready` deltaP `13.589` edge `2.4105` maxDD `-22.6673`
- `market_context_high->unknown_24h` score `13.4867` n `99` status `ready` deltaP `24.6686` edge `1.0059` maxDD `-1.7175`
- `market_context_high->commodity_24h` score `13.3929` n `99` status `ready` deltaP `44.2866` edge `0.8449` maxDD `-1.2589`
- `market_context_high->equity_24h` score `9.7586` n `99` status `ready` deltaP `24.7633` edge `1.3612` maxDD `-18.3486`
- `market_context_high->index_24h` score `9.304` n `99` status `ready` deltaP `23.8321` edge `0.742` maxDD `-4.7103`
- `market_context_high->commodity_4h` score `2.7061` n `129` status `ready` deltaP `18.1686` edge `0.1691` maxDD `-2.8438`
- `market_context_high->commodity_1h` score `-0.0996` n `133` status `ready` deltaP `1.5837` edge `0.0234` maxDD `-1.7142`
- `market_context_high->unknown_4h` score `-0.4634` n `129` status `ready` deltaP `1.6981` edge `0.0554` maxDD `-3.7602`
- `market_context_high->index_1h` score `-0.4723` n `133` status `ready` deltaP `4.1286` edge `0.0182` maxDD `-4.5023`
- `market_context_high->fx_1h` score `-0.5187` n `133` status `ready` deltaP `-4.4415` edge `0.0001` maxDD `-0.2921`
- `market_context_high->crypto_alt_1h` score `-0.5842` n `133` status `ready` deltaP `6.2345` edge `0.0965` maxDD `-14.7034`
- `market_context_high->equity_1h` score `-0.6671` n `133` status `ready` deltaP `3.5399` edge `0.0322` maxDD `-8.3065`
- `market_context_high->crypto_major_1h` score `-0.9083` n `133` status `ready` deltaP `4.8669` edge `0.0774` maxDD `-15.1032`
- `market_context_high->index_4h` score `-0.9613` n `129` status `ready` deltaP `12.5602` edge `0.0623` maxDD `-16.8761`
- `market_context_high->unknown_1h` score `-1.038` n `133` status `ready` deltaP `4.1522` edge `-0.0411` maxDD `-3.1801`
- `market_context_high->fx_4h` score `-1.1046` n `129` status `ready` deltaP `-8.1785` edge `-0.0036` maxDD `-1.0127`
- `market_context_high->metal_1h` score `-1.1973` n `133` status `ready` deltaP `-2.0531` edge `-0.003` maxDD `-7.278`
- `market_context_high->fx_24h` score `-1.2332` n `99` status `ready` deltaP `-0.2367` edge `-0.014` maxDD `-0.6418`
- `market_context_high->equity_4h` score `-2.9306` n `129` status `ready` deltaP `9.8423` edge `0.0514` maxDD `-34.4188`
- `market_context_high->crypto_alt_4h` score `-3.1693` n `129` status `ready` deltaP `18.1745` edge `0.277` maxDD `-58.6918`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

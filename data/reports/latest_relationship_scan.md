# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-12T22:52:24.602032+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11760`

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

- `market_context_high->unknown_24h` score `308.9581` n `84` status `ready` deltaP `6.2996` edge `25.7186` maxDD `-0.4606`
- `market_context_high->unknown_4h` score `75.897` n `94` status `ready` deltaP `8.1053` edge `6.3155` maxDD `-0.9162`
- `news_risk_high->equity_24h` score `29.7294` n `53` status `ready` deltaP `24.9869` edge `2.3815` maxDD `-3.6503`
- `market_context_high->equity_24h` score `21.712` n `84` status `ready` deltaP `22.7182` edge `1.7285` maxDD `-1.983`
- `news_risk_high->crypto_major_24h` score `11.8145` n `53` status `ready` deltaP `37.3559` edge `1.4622` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `9.2473` n `53` status `ready` deltaP `32.7341` edge `0.6654` maxDD `-7.0416`
- `market_context_high->crypto_alt_24h` score `8.8151` n `84` status `ready` deltaP `42.7828` edge `1.2545` maxDD `-25.4331`
- `news_risk_high->commodity_24h` score `7.2719` n `53` status `ready` deltaP `43.2292` edge `0.3178` maxDD `0.0`
- `market_context_high->metal_24h` score `6.3714` n `84` status `ready` deltaP `39.0377` edge `0.312` maxDD `-0.3044`
- `news_risk_high->metal_4h` score `4.6324` n `53` status `ready` deltaP `44.1096` edge `0.1296` maxDD `-1.0104`
- `market_context_high->index_24h` score `4.2758` n `84` status `ready` deltaP `24.6776` edge `0.2013` maxDD `-0.0934`
- `news_risk_high->index_24h` score `3.8675` n `53` status `ready` deltaP `22.8806` edge `0.2001` maxDD `-0.4279`
- `news_risk_high->equity_1h` score `2.9999` n `53` status `ready` deltaP `16.967` edge `0.1999` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `2.9187` n `53` status `ready` deltaP `26.7114` edge `0.0905` maxDD `-0.3611`
- `news_risk_high->crypto_major_4h` score `2.6811` n `53` status `ready` deltaP `19.6762` edge `0.241` maxDD `-9.2335`
- `news_risk_high->metal_1h` score `2.1822` n `53` status `ready` deltaP `25.74` edge `0.0357` maxDD `-0.3692`
- `news_risk_high->index_4h` score `1.6559` n `53` status `ready` deltaP `18.0022` edge `0.0616` maxDD `-0.8235`
- `news_risk_high->crypto_alt_24h` score `1.3775` n `53` status `ready` deltaP `12.8636` edge `0.5414` maxDD `-29.0448`
- `news_risk_high->crypto_alt_4h` score `1.3345` n `53` status `ready` deltaP `24.5168` edge `0.1715` maxDD `-10.1088`
- `news_risk_high->index_1h` score `1.1543` n `53` status `ready` deltaP `16.2778` edge `0.0178` maxDD `-0.4103`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

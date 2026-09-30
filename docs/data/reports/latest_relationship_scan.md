# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-30T11:37:30.716725+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7492`

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

- `market_context_high->unknown_1h` score `400.231` n `51` status `ready` deltaP `7.9194` edge `33.3047` maxDD `-0.0597`
- `market_context_high->unknown_4h` score `337.4361` n `40` status `ready` deltaP `8.2317` edge `28.0648` maxDD `0.0`
- `news_risk_high->unknown_24h` score `249.1576` n `135` status `ready` deltaP `1.9097` edge `20.7504` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `16.4675` n `135` status `ready` deltaP `26.9907` edge `1.2133` maxDD `-1.0093`
- `news_risk_high->equity_24h` score `7.0499` n `135` status `ready` deltaP `25.6019` edge `0.6517` maxDD `-9.4579`
- `news_risk_high->crypto_major_24h` score `6.6177` n `135` status `ready` deltaP `23.9931` edge `0.7069` maxDD `-15.8971`
- `market_context_high->crypto_major_4h` score `3.8639` n `40` status `ready` deltaP `11.5244` edge `0.3155` maxDD `-3.294`
- `news_risk_high->index_24h` score `3.4422` n `135` status `ready` deltaP `31.794` edge `0.1227` maxDD `-0.4916`
- `market_context_high->fx_4h` score `3.1893` n `40` status `ready` deltaP `35.9756` edge `0.039` maxDD `-0.0449`
- `news_risk_high->metal_24h` score `3.001` n `135` status `ready` deltaP `23.6227` edge `0.22` maxDD `-2.192`
- `news_risk_high->equity_4h` score `2.6017` n `135` status `ready` deltaP `27.7992` edge `0.1916` maxDD `-9.143`
- `market_context_high->crypto_major_1h` score `2.3885` n `51` status `ready` deltaP `15.29` edge `0.1581` maxDD `-3.546`
- `market_context_high->crypto_alt_1h` score `2.1257` n `51` status `ready` deltaP `13.2089` edge `0.1554` maxDD `-3.6387`
- `market_context_high->fx_1h` score `1.4658` n `51` status `ready` deltaP `20.5589` edge `0.0115` maxDD `-0.113`
- `news_risk_high->crypto_alt_4h` score `0.9513` n `135` status `ready` deltaP `8.8257` edge `0.2864` maxDD `-15.9436`
- `news_risk_high->crypto_alt_1h` score `0.9207` n `135` status `ready` deltaP `8.503` edge `0.1111` maxDD `-4.2849`
- `news_risk_high->equity_1h` score `0.8984` n `135` status `ready` deltaP `9.5509` edge `0.0735` maxDD `-1.6514`
- `market_context_high->crypto_alt_4h` score `0.7409` n `40` status `ready` deltaP `7.622` edge `0.1735` maxDD `-7.6792`
- `news_risk_high->index_1h` score `0.4933` n `135` status `ready` deltaP `8.8179` edge `0.0111` maxDD `-0.302`
- `market_context_high->commodity_1h` score `-0.0096` n `51` status `ready` deltaP `9.1229` edge `-0.0074` maxDD `-2.3717`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

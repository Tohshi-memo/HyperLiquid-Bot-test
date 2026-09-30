# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-30T11:07:37.933899+00:00`
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

- `market_context_high->unknown_1h` score `405.6375` n `50` status `ready` deltaP `7.8802` edge `33.7555` maxDD `-0.0597`
- `market_context_high->unknown_4h` score `350.2089` n `38` status `ready` deltaP `8.2317` edge `29.1292` maxDD `0.0`
- `news_risk_high->unknown_24h` score `341.4976` n `135` status `ready` deltaP `1.9097` edge `28.4454` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `16.6223` n `135` status `ready` deltaP `26.9907` edge `1.2262` maxDD `-1.0093`
- `news_risk_high->equity_24h` score `7.1231` n `135` status `ready` deltaP `25.6019` edge `0.6578` maxDD `-9.4579`
- `news_risk_high->crypto_major_24h` score `6.7473` n `135` status `ready` deltaP `23.9931` edge `0.7177` maxDD `-15.8971`
- `news_risk_high->index_24h` score `3.4566` n `135` status `ready` deltaP `31.794` edge `0.1239` maxDD `-0.4916`
- `market_context_high->crypto_major_4h` score `3.4534` n `38` status `ready` deltaP `9.724` edge `0.2933` maxDD `-3.294`
- `market_context_high->fx_4h` score `3.0614` n `38` status `ready` deltaP `34.8122` edge `0.0361` maxDD `-0.0449`
- `news_risk_high->metal_24h` score `3.0281` n `135` status `ready` deltaP `23.7963` edge `0.2211` maxDD `-2.192`
- `news_risk_high->equity_4h` score `2.6029` n `135` status `ready` deltaP `27.7992` edge `0.1917` maxDD `-9.143`
- `market_context_high->crypto_major_1h` score `2.3469` n `50` status `ready` deltaP `14.6946` edge `0.1586` maxDD `-3.546`
- `market_context_high->crypto_alt_1h` score `2.2329` n `50` status `ready` deltaP `14.2036` edge `0.1577` maxDD `-3.6387`
- `market_context_high->fx_1h` score `1.4244` n `50` status `ready` deltaP `20.0419` edge `0.0115` maxDD `-0.113`
- `news_risk_high->crypto_alt_4h` score `1.1113` n `135` status `ready` deltaP `9.1305` edge `0.2977` maxDD `-15.9436`
- `news_risk_high->equity_1h` score `0.8828` n `135` status `ready` deltaP `9.4012` edge `0.0732` maxDD `-1.6514`
- `news_risk_high->crypto_alt_1h` score `0.88` n `135` status `ready` deltaP `8.2036` edge `0.1097` maxDD `-4.2849`
- `market_context_high->crypto_alt_4h` score `0.513` n `38` status `ready` deltaP `5.9531` edge `0.1554` maxDD `-7.6792`
- `news_risk_high->index_1h` score `0.4802` n `135` status `ready` deltaP `8.6682` edge `0.011` maxDD `-0.302`
- `market_context_high->commodity_1h` score `-0.0563` n `50` status `ready` deltaP `8.2994` edge `-0.0079` maxDD `-2.3717`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

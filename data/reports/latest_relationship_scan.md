# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-01T21:22:34.666775+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6814`

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

- `market_context_high->unknown_1h` score `337.8398` n `50` status `ready` deltaP `8.479` edge `28.1017` maxDD `-0.0598`
- `market_context_high->unknown_4h` score `286.6192` n `50` status `ready` deltaP `6.8598` edge `23.8392` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `20.2425` n `97` status `ready` deltaP `35.9589` edge `1.4681` maxDD `-1.0093`
- `market_context_high->crypto_major_24h` score `10.3486` n `50` status `ready` deltaP `33.7361` edge `0.7791` maxDD `-9.3299`
- `market_context_high->crypto_major_4h` score `7.2293` n `50` status `ready` deltaP `18.7622` edge `0.5477` maxDD `-3.294`
- `market_context_high->crypto_alt_24h` score `5.7945` n `50` status `ready` deltaP `12.0208` edge `0.5737` maxDD `-11.6768`
- `market_context_high->crypto_alt_4h` score `5.0246` n `50` status `ready` deltaP `16.3415` edge `0.4391` maxDD `-7.6792`
- `news_risk_high->crypto_major_24h` score `4.6199` n `97` status `ready` deltaP `18.7464` edge `0.5754` maxDD `-15.8971`
- `market_context_high->equity_24h` score `3.806` n `50` status `ready` deltaP `19.0417` edge `0.5472` maxDD `-11.8957`
- `news_risk_high->equity_4h` score `3.2195` n `110` status `ready` deltaP `27.1037` edge `0.1572` maxDD `-2.9013`
- `market_context_high->fx_4h` score `3.1026` n `50` status `ready` deltaP `34.6707` edge `0.0409` maxDD `-0.0791`
- `market_context_high->crypto_major_1h` score `3.0239` n `50` status `ready` deltaP `14.5988` edge `0.1997` maxDD `-2.2692`
- `market_context_high->crypto_alt_1h` score `2.959` n `50` status `ready` deltaP `13.7545` edge `0.2212` maxDD `-3.6387`
- `news_risk_high->equity_24h` score `2.667` n `97` status `ready` deltaP `19.0829` edge `0.4496` maxDD `-9.4579`
- `news_risk_high->index_24h` score `2.094` n `97` status `ready` deltaP `22.1113` edge `0.0749` maxDD `-0.4916`
- `news_risk_high->metal_24h` score `2.0252` n `97` status `ready` deltaP `23.2263` edge `0.2322` maxDD `-2.192`
- `news_risk_high->commodity_24h` score `1.6521` n `97` status `ready` deltaP `21.5779` edge `0.1169` maxDD `-4.8459`
- `market_context_high->fx_1h` score `1.5023` n `50` status `ready` deltaP `20.9401` edge `0.012` maxDD `-0.113`
- `market_context_high->index_24h` score `0.9073` n `50` status `ready` deltaP `14.7917` edge `0.0748` maxDD `-1.2338`
- `news_risk_high->equity_1h` score `0.5018` n `110` status `ready` deltaP `7.3163` edge `0.0467` maxDD `-0.9592`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

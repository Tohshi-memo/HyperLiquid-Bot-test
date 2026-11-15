# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-15T21:37:23.729416+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8264`

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

- `market_context_high->unknown_24h` score `723.8913` n `52` status `ready` deltaP `3.9861` edge `60.2977` maxDD `0.0`
- `news_risk_high->equity_24h` score `46.2933` n `50` status `ready` deltaP `50.565` edge `3.5913` maxDD `-3.6503`
- `market_context_high->equity_24h` score `40.4727` n `52` status `ready` deltaP `43.3342` edge `3.238` maxDD `-9.0005`
- `market_context_high->crypto_alt_24h` score `34.3769` n `52` status `ready` deltaP `61.2185` edge `2.5643` maxDD `-6.2814`
- `news_risk_high->crypto_major_24h` score `22.6142` n `50` status `ready` deltaP `44.6551` edge `2.7159` maxDD `-6.8139`
- `market_context_high->crypto_major_24h` score `12.7725` n `52` status `ready` deltaP `17.4243` edge `1.4868` maxDD `-38.4205`
- `news_risk_high->equity_4h` score `11.7964` n `50` status `ready` deltaP `37.2378` edge `0.8478` maxDD `-7.0416`
- `market_context_high->unknown_4h` score `9.4375` n `72` status `ready` deltaP `8.9939` edge `0.7265` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `9.399` n `50` status `ready` deltaP `20.6031` edge `1.5182` maxDD `-29.0448`
- `market_context_high->index_24h` score `8.0476` n `52` status `ready` deltaP `48.4769` edge `0.3561` maxDD `-0.0251`
- `news_risk_high->index_24h` score `6.6779` n `50` status `ready` deltaP `42.2461` edge `0.3052` maxDD `-0.4279`
- `news_risk_high->commodity_24h` score `6.3557` n `50` status `ready` deltaP `41.4211` edge `0.2535` maxDD `0.0`
- `market_context_high->metal_24h` score `6.2436` n `52` status `ready` deltaP `61.5318` edge `0.4794` maxDD `-3.7989`
- `news_risk_high->metal_4h` score `4.8566` n `50` status `ready` deltaP `43.9268` edge `0.1495` maxDD `-1.0104`
- `news_risk_high->crypto_major_4h` score `4.649` n `50` status `ready` deltaP `21.2988` edge `0.383` maxDD `-9.0062`
- `news_risk_high->crypto_alt_4h` score `4.1314` n `50` status `ready` deltaP `25.9268` edge `0.315` maxDD `-9.4848`
- `news_risk_high->equity_1h` score `3.8773` n `50` status `ready` deltaP `20.5988` edge `0.2488` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.6344` n `50` status `ready` deltaP `33.6768` edge `0.1037` maxDD `-0.3611`
- `news_risk_high->index_4h` score `2.414` n `50` status `ready` deltaP `23.2744` edge `0.081` maxDD `-0.7999`
- `news_risk_high->metal_1h` score `2.1574` n `50` status `ready` deltaP `24.6946` edge `0.0406` maxDD `-0.3692`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

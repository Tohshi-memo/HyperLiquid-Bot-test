# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-16T02:22:22.045152+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8676`

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

- `market_context_high->unknown_24h` score `1320.9585` n `33` status `ready` deltaP `3.9861` edge `110.0533` maxDD `0.0`
- `news_risk_high->equity_24h` score `47.5761` n `50` status `ready` deltaP `50.565` edge `3.6982` maxDD `-3.6503`
- `market_context_high->unknown_4h` score `42.5308` n `64` status `ready` deltaP `7.5838` edge `3.4979` maxDD `-0.0048`
- `market_context_high->equity_24h` score `29.9281` n `33` status `ready` deltaP `32.262` edge `2.4331` maxDD `-9.0005`
- `market_context_high->crypto_alt_24h` score `29.2246` n `33` status `ready` deltaP `52.3607` edge `2.194` maxDD `-6.2814`
- `news_risk_high->crypto_major_24h` score `21.4008` n `50` status `ready` deltaP `42.5754` edge `2.5742` maxDD `-6.8139`
- `news_risk_high->equity_4h` score `11.9106` n `50` status `ready` deltaP `37.3902` edge `0.8563` maxDD `-7.0416`
- `market_context_high->crypto_major_24h` score `10.4586` n `33` status `ready` deltaP `11.8481` edge `1.211` maxDD `-28.8081`
- `news_risk_high->crypto_alt_24h` score `9.0675` n `50` status `ready` deltaP `20.6031` edge `1.4757` maxDD `-29.0448`
- `news_risk_high->index_24h` score `6.8447` n `50` status `ready` deltaP `42.2461` edge `0.3191` maxDD `-0.4279`
- `market_context_high->index_24h` score `6.5915` n `33` status `ready` deltaP `45.1552` edge `0.2569` maxDD `-0.0251`
- `news_risk_high->commodity_24h` score `6.262` n `50` status `ready` deltaP `41.0745` edge `0.248` maxDD `0.0`
- `news_risk_high->metal_4h` score `4.9674` n `50` status `ready` deltaP `44.2317` edge `0.1567` maxDD `-1.0104`
- `news_risk_high->crypto_major_4h` score `4.3916` n `50` status `ready` deltaP `20.8415` edge `0.3646` maxDD `-9.0062`
- `news_risk_high->crypto_alt_4h` score `4.201` n `50` status `ready` deltaP `25.9268` edge `0.3208` maxDD `-9.4848`
- `market_context_high->metal_24h` score `3.9526` n `33` status `ready` deltaP `50.4596` edge `0.2595` maxDD `-3.7989`
- `news_risk_high->equity_1h` score `3.9001` n `50` status `ready` deltaP `20.2994` edge `0.2527` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.8461` n `50` status `ready` deltaP `35.0488` edge `0.1122` maxDD `-0.3611`
- `news_risk_high->index_4h` score `2.4588` n `50` status `ready` deltaP `23.5793` edge `0.0827` maxDD `-0.7999`
- `news_risk_high->metal_1h` score `2.2569` n `50` status `ready` deltaP `25.4431` edge `0.0439` maxDD `-0.3692`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

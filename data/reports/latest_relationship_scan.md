# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-16T01:37:23.389588+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8652`

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

- `market_context_high->unknown_24h` score `1183.9833` n `36` status `ready` deltaP `3.9861` edge `98.6387` maxDD `0.0`
- `news_risk_high->equity_24h` score `47.3541` n `50` status `ready` deltaP `50.565` edge `3.6797` maxDD `-3.6503`
- `market_context_high->unknown_4h` score `43.9627` n `64` status `ready` deltaP `8.9939` edge `3.6036` maxDD `0.0`
- `market_context_high->equity_24h` score `32.0693` n `36` status `ready` deltaP `34.7872` edge `2.5947` maxDD `-9.0005`
- `market_context_high->crypto_alt_24h` score `29.7439` n `36` status `ready` deltaP `54.3809` edge `2.2238` maxDD `-6.2814`
- `news_risk_high->crypto_major_24h` score `21.5483` n `50` status `ready` deltaP `42.922` edge `2.5908` maxDD `-6.8139`
- `news_risk_high->equity_4h` score `11.8188` n `50` status `ready` deltaP `36.9329` edge `0.8517` maxDD `-7.0416`
- `market_context_high->crypto_major_24h` score `11.0849` n `36` status `ready` deltaP `12.6998` edge `1.2708` maxDD `-29.8715`
- `news_risk_high->crypto_alt_24h` score `9.1026` n `50` status `ready` deltaP `20.6031` edge `1.4802` maxDD `-29.0448`
- `news_risk_high->index_24h` score `6.8231` n `50` status `ready` deltaP `42.2461` edge `0.3173` maxDD `-0.4279`
- `market_context_high->index_24h` score `6.7961` n `36` status `ready` deltaP `45.9128` edge `0.2689` maxDD `-0.0251`
- `news_risk_high->commodity_24h` score `6.2608` n `50` status `ready` deltaP `41.0745` edge `0.2479` maxDD `0.0`
- `news_risk_high->metal_4h` score `4.948` n `50` status `ready` deltaP `44.0793` edge `0.1561` maxDD `-1.0104`
- `news_risk_high->crypto_major_4h` score `4.3904` n `50` status `ready` deltaP `20.8415` edge `0.3645` maxDD `-9.0062`
- `market_context_high->metal_24h` score `4.2711` n `36` status `ready` deltaP `52.9848` edge `0.2835` maxDD `-3.7989`
- `news_risk_high->crypto_alt_4h` score `4.1926` n `50` status `ready` deltaP `25.9268` edge `0.3201` maxDD `-9.4848`
- `news_risk_high->equity_1h` score `3.7898` n `50` status `ready` deltaP `20.0` edge `0.2455` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.7832` n `50` status `ready` deltaP `34.5915` edge `0.11` maxDD `-0.3611`
- `news_risk_high->index_4h` score `2.4418` n `50` status `ready` deltaP `23.4268` edge `0.0823` maxDD `-0.7999`
- `news_risk_high->metal_1h` score `2.2005` n `50` status `ready` deltaP `24.994` edge `0.0422` maxDD `-0.3692`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

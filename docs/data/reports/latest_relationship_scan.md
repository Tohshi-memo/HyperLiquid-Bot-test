# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-16T02:37:25.406662+00:00`
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

- `market_context_high->unknown_24h` score `1372.5873` n `32` status `ready` deltaP `3.9861` edge `114.3557` maxDD `0.0`
- `news_risk_high->equity_24h` score `47.6457` n `50` status `ready` deltaP `50.565` edge `3.704` maxDD `-3.6503`
- `market_context_high->unknown_4h` score `41.6025` n `64` status `ready` deltaP `6.1738` edge `3.4343` maxDD `-0.02`
- `market_context_high->equity_24h` score `29.1911` n `32` status `ready` deltaP `31.315` edge `2.378` maxDD `-9.0005`
- `market_context_high->crypto_alt_24h` score `29.0188` n `32` status `ready` deltaP `51.6031` edge `2.1819` maxDD `-6.2814`
- `news_risk_high->crypto_major_24h` score `21.3739` n `50` status `ready` deltaP `42.4021` edge `2.5719` maxDD `-6.8139`
- `news_risk_high->equity_4h` score `11.9154` n `50` status `ready` deltaP `37.3902` edge `0.8567` maxDD `-7.0416`
- `market_context_high->crypto_major_24h` score `10.2615` n `32` status `ready` deltaP `12.5271` edge `1.1846` maxDD `-28.7059`
- `news_risk_high->crypto_alt_24h` score `9.0659` n `50` status `ready` deltaP `20.6031` edge `1.4755` maxDD `-29.0448`
- `news_risk_high->index_24h` score `6.8519` n `50` status `ready` deltaP `42.2461` edge `0.3197` maxDD `-0.4279`
- `market_context_high->index_24h` score `6.5291` n `32` status `ready` deltaP `44.8711` edge `0.2536` maxDD `-0.0251`
- `news_risk_high->commodity_24h` score `6.2608` n `50` status `ready` deltaP `41.0745` edge `0.2479` maxDD `0.0`
- `news_risk_high->metal_4h` score `4.9808` n `50` status `ready` deltaP `44.3841` edge `0.1568` maxDD `-1.0104`
- `news_risk_high->crypto_major_4h` score `4.3856` n `50` status `ready` deltaP `20.8415` edge `0.3641` maxDD `-9.0062`
- `news_risk_high->crypto_alt_4h` score `4.1804` n `50` status `ready` deltaP `25.7744` edge `0.3201` maxDD `-9.4848`
- `news_risk_high->equity_1h` score `3.9097` n `50` status `ready` deltaP `20.2994` edge `0.2535` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.8643` n `50` status `ready` deltaP `35.2012` edge `0.1127` maxDD `-0.3611`
- `market_context_high->metal_24h` score `3.8425` n `32` status `ready` deltaP `49.5126` edge `0.2517` maxDD `-3.7989`
- `news_risk_high->index_4h` score `2.4588` n `50` status `ready` deltaP `23.5793` edge `0.0827` maxDD `-0.7999`
- `market_context_high->fx_24h` score `2.3494` n `32` status `ready` deltaP `39.0977` edge `0.0817` maxDD `-0.292`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

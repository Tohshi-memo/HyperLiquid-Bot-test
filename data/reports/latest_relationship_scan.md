# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-24T09:37:18.541482+00:00`
- Price records: `672`
- Market context records: `1722`
- Flow alert records: `6865`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8834`

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

- `market_context_high->metal_24h` score `6.614` n `142` status `ready` deltaP `25.4496` edge `0.6241` maxDD `-12.7414`
- `market_context_high->unknown_24h` score `6.1082` n `142` status `ready` deltaP `17.033` edge `0.9275` maxDD `-35.8966`
- `market_context_high->crypto_alt_4h` score `5.9825` n `196` status `ready` deltaP `21.4286` edge `0.5323` maxDD `-9.1295`
- `market_context_high->crypto_major_4h` score `4.4826` n `196` status `ready` deltaP `23.1769` edge `0.4596` maxDD `-10.9117`
- `market_context_high->index_24h` score `3.8834` n `142` status `ready` deltaP `17.1085` edge `0.3324` maxDD `-4.1604`
- `market_context_high->unknown_4h` score `3.0377` n `196` status `ready` deltaP `13.7941` edge `0.3883` maxDD `-11.1695`
- `market_context_high->equity_4h` score `3.0153` n `196` status `ready` deltaP `16.2643` edge `0.2523` maxDD `-5.0894`
- `market_context_high->equity_24h` score `1.5362` n `142` status `ready` deltaP `15.8487` edge `0.5122` maxDD `-33.1875`
- `market_context_high->crypto_alt_1h` score `0.7321` n `196` status `ready` deltaP `7.4209` edge `0.1139` maxDD `-4.1892`
- `market_context_high->index_4h` score `0.5348` n `196` status `ready` deltaP `8.6642` edge `0.0957` maxDD `-3.7119`
- `market_context_high->crypto_major_1h` score `0.1777` n `196` status `ready` deltaP `4.7477` edge `0.0905` maxDD `-3.9211`
- `market_context_high->equity_1h` score `0.0215` n `196` status `ready` deltaP `4.6713` edge `0.0515` maxDD `-2.8014`
- `market_context_high->crypto_alt_24h` score `-0.1182` n `142` status `ready` deltaP `22.7789` edge `1.0192` maxDD `-88.8062`
- `market_context_high->metal_4h` score `-0.3377` n `196` status `ready` deltaP `11.8343` edge `0.147` maxDD `-12.5349`
- `market_context_high->index_1h` score `-0.424` n `196` status `ready` deltaP `1.5215` edge `0.0177` maxDD `-1.7205`
- `market_context_high->metal_1h` score `-0.5533` n `196` status `ready` deltaP `5.4962` edge `0.026` maxDD `-6.3532`
- `market_context_high->fx_1h` score `-0.6723` n `196` status `ready` deltaP `-3.2659` edge `-0.0012` maxDD `-0.3914`
- `market_context_high->fx_24h` score `-0.7959` n `142` status `ready` deltaP `4.7371` edge `0.007` maxDD `-1.3925`
- `market_context_high->crypto_major_24h` score `-0.9246` n `142` status `ready` deltaP `21.1121` edge `0.5993` maxDD `-62.3533`
- `market_context_high->unknown_1h` score `-1.5121` n `196` status `ready` deltaP `1.6864` edge `0.0097` maxDD `-7.7558`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

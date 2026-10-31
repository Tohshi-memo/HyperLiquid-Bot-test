# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-31T21:37:26.967365+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7559`

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

- `market_context_high->unknown_24h` score `3299.5226` n `92` status `ready` deltaP `-10.6658` edge `275.0743` maxDD `-1.1049`
- `market_context_high->unknown_4h` score `121.9713` n `92` status `ready` deltaP `1.4051` edge `10.1682` maxDD `-0.3966`
- `news_risk_high->unknown_1h` score `77.6548` n `108` status `ready` deltaP `-5.1951` edge `6.5345` maxDD `-0.9571`
- `news_risk_high->crypto_alt_24h` score `18.9749` n `80` status `ready` deltaP `45.0694` edge `1.2859` maxDD `-0.0763`
- `market_context_high->equity_24h` score `10.7107` n `92` status `ready` deltaP `24.0414` edge `1.008` maxDD `-14.0571`
- `news_risk_high->crypto_alt_4h` score `5.4775` n `108` status `ready` deltaP `20.5793` edge `0.4579` maxDD `-7.4246`
- `market_context_high->index_24h` score `4.9531` n `92` status `ready` deltaP `43.9009` edge `0.1384` maxDD `-0.1315`
- `market_context_high->metal_4h` score `1.5868` n `92` status `ready` deltaP `19.6381` edge `0.0438` maxDD `-0.7323`
- `market_context_high->metal_1h` score `0.9219` n `92` status `ready` deltaP `12.9654` edge `0.0194` maxDD `-0.3209`
- `news_risk_high->crypto_alt_1h` score `0.8301` n `108` status `ready` deltaP `8.8767` edge `0.1054` maxDD `-3.9659`
- `market_context_high->commodity_4h` score `0.617` n `92` status `ready` deltaP `15.7476` edge `0.0623` maxDD `-0.7211`
- `market_context_high->equity_4h` score `0.5376` n `92` status `ready` deltaP `2.4987` edge `0.1916` maxDD `-4.48`
- `market_context_high->equity_1h` score `0.4673` n `92` status `ready` deltaP `6.5217` edge `0.104` maxDD `-2.3383`
- `market_context_high->fx_4h` score `0.3959` n `92` status `ready` deltaP `10.6045` edge `0.0014` maxDD `-0.1285`
- `market_context_high->fx_1h` score `0.3667` n `92` status `ready` deltaP `9.8607` edge `-0.0003` maxDD `-0.1407`
- `market_context_high->crypto_major_1h` score `0.3424` n `92` status `ready` deltaP `8.8454` edge `0.0877` maxDD `-5.2213`
- `market_context_high->metal_24h` score `-0.2816` n `92` status `ready` deltaP `9.2844` edge `0.1667` maxDD `-10.5088`
- `market_context_high->crypto_major_4h` score `-0.4271` n `92` status `ready` deltaP `14.7998` edge `0.1206` maxDD `-14.5879`
- `market_context_high->index_1h` score `-0.4344` n `92` status `ready` deltaP `2.6621` edge `0.0019` maxDD `-1.1344`
- `market_context_high->commodity_1h` score `-0.4388` n `92` status `ready` deltaP `-2.7792` edge `0.0137` maxDD `-0.4475`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

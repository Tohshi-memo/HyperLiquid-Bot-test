# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-01T11:22:28.216520+00:00`
- Price records: `672`
- Market context records: `8616`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5898`

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

- `news_risk_high->unknown_24h` score `5192.5206` n `60` status `ready` deltaP `34.2345` edge `432.5239` maxDD `-2.0332`
- `market_context_high->crypto_alt_24h` score `18.3373` n `42` status `ready` deltaP `52.5213` edge `1.2177` maxDD `-2.1786`
- `news_risk_high->equity_4h` score `6.1603` n `60` status `ready` deltaP `20.7991` edge `0.4344` maxDD `-3.4427`
- `news_risk_high->index_4h` score `2.4435` n `60` status `ready` deltaP `20.9513` edge `0.083` maxDD `-0.191`
- `market_context_high->crypto_alt_4h` score `1.7993` n `62` status `ready` deltaP `13.1315` edge `0.1581` maxDD `-5.323`
- `news_risk_high->equity_1h` score `1.6688` n `60` status `ready` deltaP `14.7805` edge `0.0882` maxDD `-2.4803`
- `market_context_high->fx_24h` score `1.4935` n `42` status `ready` deltaP `24.8164` edge `0.0704` maxDD `-0.8832`
- `news_risk_high->crypto_major_4h` score `1.035` n `60` status `ready` deltaP `6.2938` edge `0.1683` maxDD `-3.5385`
- `news_risk_high->crypto_alt_1h` score `0.4568` n `60` status `ready` deltaP `8.6327` edge `0.0537` maxDD `-1.8813`
- `news_risk_high->crypto_major_1h` score `0.3434` n `60` status `ready` deltaP `6.517` edge `0.0518` maxDD `-2.0972`
- `news_risk_high->crypto_alt_4h` score `0.3308` n `60` status `ready` deltaP `10.2283` edge `0.1134` maxDD `-5.8012`
- `news_risk_high->fx_4h` score `0.3073` n `60` status `ready` deltaP `14.6651` edge `0.0236` maxDD `-0.6604`
- `market_context_high->crypto_major_24h` score `0.2985` n `42` status `ready` deltaP `4.0274` edge `0.429` maxDD `-26.7401`
- `news_risk_high->fx_1h` score `0.125` n `60` status `ready` deltaP `5.8982` edge `0.0048` maxDD `-0.2475`
- `news_risk_high->metal_1h` score `0.0679` n `60` status `ready` deltaP `5.6387` edge `0.0084` maxDD `-0.5599`
- `news_risk_high->metal_4h` score `0.0667` n `60` status `ready` deltaP `3.2344` edge `0.0346` maxDD `-0.8085`
- `news_risk_high->index_1h` score `-0.024` n `60` status `ready` deltaP `2.9242` edge `0.0091` maxDD `-0.5338`
- `market_context_high->fx_4h` score `-0.1551` n `62` status `ready` deltaP `8.0522` edge `0.013` maxDD `-1.3685`
- `market_context_high->fx_1h` score `-0.2583` n `62` status `ready` deltaP `2.5111` edge `0.0004` maxDD `-0.6874`
- `market_context_high->commodity_1h` score `-0.3223` n `62` status `ready` deltaP `4.0081` edge `-0.0055` maxDD `-2.0038`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-03T05:37:26.778233+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5935`

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

- `news_risk_high->unknown_24h` score `1958.604` n `40` status `ready` deltaP `20.3819` edge `163.1232` maxDD `-2.0332`
- `market_context_high->crypto_alt_24h` score `13.4055` n `40` status `ready` deltaP `51.4583` edge `0.8138` maxDD `-2.1786`
- `market_context_high->commodity_24h` score `11.0538` n `40` status `ready` deltaP `51.3194` edge `0.5918` maxDD `-0.6889`
- `news_risk_high->equity_4h` score `1.1018` n `40` status `ready` deltaP `-2.5915` edge `0.2349` maxDD `-3.4427`
- `news_risk_high->index_4h` score `0.5961` n `40` status `ready` deltaP `5.061` edge `0.054` maxDD `-0.3783`
- `news_risk_high->commodity_1h` score `0.4719` n `40` status `ready` deltaP `14.8952` edge `-0.008` maxDD `-1.1306`
- `market_context_high->commodity_1h` score `0.3712` n `47` status `ready` deltaP `7.7143` edge `0.0336` maxDD `-1.3282`
- `market_context_high->commodity_4h` score `0.3193` n `47` status `ready` deltaP `5.0338` edge `0.092` maxDD `-2.7703`
- `market_context_high->fx_4h` score `0.0596` n `47` status `ready` deltaP `14.1801` edge `-0.0039` maxDD `-1.8531`
- `market_context_high->fx_1h` score `0.0071` n `47` status `ready` deltaP `7.2652` edge `-0.0086` maxDD `-0.7804`
- `news_risk_high->metal_1h` score `-0.0006` n `40` status `ready` deltaP `3.6527` edge `0.0076` maxDD `-0.5599`
- `market_context_high->crypto_alt_4h` score `-0.2134` n `47` status `ready` deltaP `2.2963` edge `0.0479` maxDD `-4.9116`
- `news_risk_high->fx_1h` score `-0.257` n `40` status `ready` deltaP `-0.5539` edge `0.003` maxDD `-0.2475`
- `news_risk_high->metal_4h` score `-0.3339` n `40` status `ready` deltaP `1.7378` edge `-0.0043` maxDD `-0.8085`
- `news_risk_high->crypto_alt_1h` score `-0.3889` n `40` status `ready` deltaP `3.997` edge `-0.0083` maxDD `-3.1233`
- `news_risk_high->fx_24h` score `-0.415` n `40` status `ready` deltaP `5.6597` edge `0.0295` maxDD `-2.9683`
- `news_risk_high->index_1h` score `-0.5398` n `40` status `ready` deltaP `-1.6467` edge `-0.0017` maxDD `-0.5845`
- `news_risk_high->fx_4h` score `-0.6237` n `40` status `ready` deltaP `-2.2561` edge `0.0265` maxDD `-0.6466`
- `market_context_high->fx_24h` score `-0.6851` n `40` status `ready` deltaP `0.6597` edge `0.0365` maxDD `-2.506`
- `news_risk_high->equity_1h` score `-0.7912` n `40` status `ready` deltaP `-3.4431` edge `0.0393` maxDD `-2.916`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

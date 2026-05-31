# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-31T21:37:17.922745+00:00`
- Price records: `672`
- Market context records: `2498`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9248`

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

- `market_context_high->unknown_24h` score `5.4571` n `124` status `ready` deltaP `19.8869` edge `0.355` maxDD `-1.626`
- `market_context_high->crypto_alt_4h` score `4.1321` n `146` status `ready` deltaP `21.0805` edge `0.4717` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `3.5547` n `146` status `ready` deltaP `16.9688` edge `0.3641` maxDD `-10.1468`
- `market_context_high->crypto_major_24h` score `2.1633` n `124` status `ready` deltaP `12.78` edge `0.5814` maxDD `-25.1408`
- `market_context_high->unknown_4h` score `1.4232` n `146` status `ready` deltaP `9.8208` edge `0.1581` maxDD `-3.7312`
- `market_context_high->crypto_alt_1h` score `0.4692` n `154` status `ready` deltaP `6.546` edge `0.1142` maxDD `-6.1656`
- `market_context_high->crypto_alt_24h` score `0.3899` n `124` status `ready` deltaP `2.8393` edge `0.7268` maxDD `-43.6595`
- `market_context_high->crypto_major_1h` score `0.3866` n `154` status `ready` deltaP `6.8454` edge `0.106` maxDD `-4.2199`
- `market_context_high->index_24h` score `0.124` n `124` status `ready` deltaP `4.3514` edge `0.0794` maxDD `-2.5127`
- `market_context_high->equity_24h` score `-0.1377` n `124` status `ready` deltaP `18.4084` edge `0.0185` maxDD `-6.8828`
- `market_context_high->index_4h` score `-0.1764` n `146` status `ready` deltaP `6.5319` edge `0.0259` maxDD `-2.3986`
- `market_context_high->fx_1h` score `-0.342` n `154` status `ready` deltaP `0.7991` edge `0.0043` maxDD `-0.278`
- `market_context_high->index_1h` score `-0.5376` n `154` status `ready` deltaP `-0.1944` edge `0.0059` maxDD `-1.2855`
- `market_context_high->commodity_1h` score `-0.5401` n `154` status `ready` deltaP `2.8482` edge `-0.0004` maxDD `-4.3601`
- `market_context_high->unknown_1h` score `-0.5891` n `154` status `ready` deltaP `1.7498` edge `0.0112` maxDD `-3.0902`
- `market_context_high->fx_4h` score `-0.6271` n `146` status `ready` deltaP `-0.4553` edge `0.0086` maxDD `-0.8774`
- `market_context_high->metal_1h` score `-0.8008` n `154` status `ready` deltaP `0.4977` edge `0.0059` maxDD `-3.0759`
- `market_context_high->equity_1h` score `-0.8549` n `154` status `ready` deltaP `0.0623` edge `0.0122` maxDD `-2.7085`
- `market_context_high->fx_24h` score `-0.9026` n `124` status `ready` deltaP `2.8506` edge `0.0038` maxDD `-2.7484`
- `market_context_high->metal_4h` score `-1.0731` n `146` status `ready` deltaP `1.6079` edge `0.0386` maxDD `-4.7664`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-04T00:07:31.464132+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `64`

- Symbol pattern count: `7932`

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

- `market_context_high->unknown_24h` score `37.4148` n `46` status `ready` deltaP `26.8192` edge `2.9434` maxDD `-0.0103`
- `market_context_high->unknown_4h` score `11.6938` n `69` status `ready` deltaP `11.2606` edge `0.9468` maxDD `-1.4578`
- `market_context_high->crypto_alt_24h` score `10.3421` n `46` status `ready` deltaP `48.1658` edge `0.5581` maxDD `-0.3889`
- `market_context_high->commodity_24h` score `8.6118` n `46` status `ready` deltaP `41.561` edge `0.4585` maxDD `-0.434`
- `news_risk_high->fx_24h` score `1.0445` n `31` status `ready` deltaP `12.192` edge `0.071` maxDD `-1.5526`
- `news_risk_high->commodity_1h` score `0.8843` n `31` status `ready` deltaP `19.0892` edge `0.0073` maxDD `-0.6947`
- `market_context_high->commodity_4h` score `0.5853` n `69` status `ready` deltaP `9.4954` edge `0.0701` maxDD `-2.7703`
- `market_context_high->fx_4h` score `0.5201` n `69` status `ready` deltaP `21.3105` edge `0.0106` maxDD `-1.8797`
- `market_context_high->fx_1h` score `0.3742` n `81` status `ready` deltaP `12.3642` edge `0.0004` maxDD `-0.7878`
- `market_context_high->commodity_1h` score `0.2182` n `81` status `ready` deltaP `5.6683` edge `0.022` maxDD `-1.3282`
- `news_risk_high->fx_4h` score `0.0805` n `31` status `ready` deltaP `3.8257` edge `0.0351` maxDD `-0.356`
- `news_risk_high->commodity_4h` score `-0.1518` n `31` status `ready` deltaP `9.5889` edge `-0.0265` maxDD `-1.6728`
- `news_risk_high->index_1h` score `-0.1731` n `31` status `ready` deltaP `0.7968` edge `-0.0077` maxDD `-0.5845`
- `news_risk_high->crypto_alt_1h` score `-0.2126` n `31` status `ready` deltaP `9.7933` edge `-0.0285` maxDD `-3.1233`
- `market_context_high->index_1h` score `-0.2201` n `81` status `ready` deltaP `5.2174` edge `-0.0096` maxDD `-1.6054`
- `news_risk_high->index_4h` score `-0.2538` n `31` status `ready` deltaP `-3.4176` edge `0.0397` maxDD `-0.3783`
- `news_risk_high->fx_1h` score `-0.3408` n `31` status `ready` deltaP `-2.2117` edge `0.0022` maxDD `-0.1588`
- `market_context_high->metal_1h` score `-0.4763` n `81` status `ready` deltaP `-0.5433` edge `-0.008` maxDD `-1.6224`
- `news_risk_high->unknown_4h` score `-0.5074` n `31` status `ready` deltaP `-1.3621` edge `-0.0071` maxDD `-1.5766`
- `news_risk_high->equity_4h` score `-0.6806` n `31` status `ready` deltaP `-16.6257` edge `0.1237` maxDD `-2.8999`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

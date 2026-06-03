# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-03T07:52:23.606877+00:00`
- Price records: `672`
- Market context records: `2744`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9237`

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

- `market_context_high->crypto_alt_24h` score `9.9264` n `114` status `ready` deltaP `14.5742` edge `1.0794` maxDD `-19.9486`
- `market_context_high->unknown_24h` score `7.734` n `114` status `ready` deltaP `15.5428` edge `0.5737` maxDD `-1.6255`
- `market_context_high->unknown_4h` score `1.0583` n `143` status `ready` deltaP `6.8587` edge `0.1478` maxDD `-3.7602`
- `market_context_high->index_4h` score `0.1255` n `143` status `ready` deltaP `10.5514` edge `0.0299` maxDD `-2.3986`
- `market_context_high->unknown_1h` score `-0.0956` n `143` status `ready` deltaP `3.4976` edge `0.0418` maxDD `-3.1801`
- `market_context_high->index_1h` score `-0.1853` n `143` status `ready` deltaP `2.7512` edge `0.0073` maxDD `-1.2855`
- `market_context_high->fx_1h` score `-0.5219` n `143` status `ready` deltaP `-0.3475` edge `0.0032` maxDD `-0.2164`
- `market_context_high->crypto_alt_1h` score `-0.6321` n `143` status `ready` deltaP `5.9954` edge `0.055` maxDD `-10.747`
- `market_context_high->crypto_major_24h` score `-0.6388` n `114` status `ready` deltaP `5.0713` edge `0.7833` maxDD `-54.5873`
- `market_context_high->commodity_1h` score `-0.6395` n `143` status `ready` deltaP `-0.247` edge `-0.005` maxDD `-4.3601`
- `market_context_high->metal_1h` score `-0.7551` n `143` status `ready` deltaP `-1.1003` edge `-0.0049` maxDD `-3.0996`
- `market_context_high->crypto_alt_4h` score `-0.8234` n `143` status `ready` deltaP `16.0584` edge `0.2584` maxDD `-28.7261`
- `market_context_high->crypto_major_1h` score `-0.9643` n `143` status `ready` deltaP `3.4976` edge `0.04` maxDD `-9.622`
- `market_context_high->fx_4h` score `-1.1321` n `143` status `ready` deltaP `-3.6405` edge `0.0078` maxDD `-0.5631`
- `market_context_high->fx_24h` score `-1.2391` n `114` status `ready` deltaP `-0.1005` edge `-0.0154` maxDD `-0.6418`
- `market_context_high->equity_1h` score `-1.3034` n `143` status `ready` deltaP `-4.984` edge `0.0079` maxDD `-2.6634`
- `market_context_high->commodity_24h` score `-1.5208` n `114` status `ready` deltaP `3.6001` edge `0.0904` maxDD `-12.4171`
- `market_context_high->commodity_4h` score `-1.5834` n `143` status `ready` deltaP `-0.1631` edge `-0.0099` maxDD `-10.0279`
- `market_context_high->equity_4h` score `-2.0339` n `143` status `ready` deltaP `-1.2493` edge `-0.0232` maxDD `-5.7037`
- `market_context_high->crypto_major_4h` score `-2.3544` n `143` status `ready` deltaP `6.9046` edge `0.1427` maxDD `-32.2466`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

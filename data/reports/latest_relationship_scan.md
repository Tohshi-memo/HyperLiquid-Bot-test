# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-14T09:37:29.267867+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11808`

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

- `market_context_high->unknown_24h` score `90.0286` n `150` status `ready` deltaP `-30.1458` edge `7.9946` maxDD `-9.6329`
- `risk_on_high->unknown_24h` score `32.9779` n `32` status `ready` deltaP `-44.2708` edge `4.5981` maxDD `-1.6689`
- `risk_on_and_context->unknown_24h` score `32.9779` n `32` status `ready` deltaP `-44.2708` edge `4.5981` maxDD `-1.6689`
- `news_risk_high->equity_24h` score `9.9094` n `36` status `ready` deltaP `10.0694` edge `0.7966` maxDD `-1.0358`
- `news_risk_high->equity_4h` score `7.3353` n `36` status `ready` deltaP `39.1768` edge `0.3501` maxDD `0.0`
- `risk_on_high->commodity_24h` score `4.6485` n `32` status `ready` deltaP `31.0764` edge `0.1802` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `4.6485` n `32` status `ready` deltaP `31.0764` edge `0.1802` maxDD `0.0`
- `market_context_high->commodity_24h` score `2.7214` n `150` status `ready` deltaP `21.0764` edge `0.1666` maxDD `-2.4263`
- `risk_on_high->commodity_4h` score `2.5966` n `32` status `ready` deltaP `18.064` edge `0.1142` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.5966` n `32` status `ready` deltaP `18.064` edge `0.1142` maxDD `-0.1258`
- `news_risk_high->index_24h` score `2.2227` n `36` status `ready` deltaP `14.5833` edge `0.088` maxDD `0.0`
- `news_risk_high->index_4h` score `1.7309` n `36` status `ready` deltaP `20.2235` edge `0.0226` maxDD `-0.0546`
- `news_risk_high->equity_1h` score `1.6901` n `36` status `ready` deltaP `8.8823` edge `0.1135` maxDD `-0.5496`
- `risk_on_high->crypto_major_24h` score `1.622` n `32` status `ready` deltaP `14.0625` edge `0.2298` maxDD `-6.2481`
- `risk_on_and_context->crypto_major_24h` score `1.622` n `32` status `ready` deltaP `14.0625` edge `0.2298` maxDD `-6.2481`
- `market_context_high->commodity_4h` score `1.2351` n `150` status `ready` deltaP `14.6057` edge `0.0694` maxDD `-2.1077`
- `risk_on_high->commodity_1h` score `1.2252` n `32` status `ready` deltaP `13.0614` edge `0.0383` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.2252` n `32` status `ready` deltaP `13.0614` edge `0.0383` maxDD `-0.1957`
- `risk_on_high->fx_24h` score `1.1972` n `32` status `ready` deltaP `14.2361` edge `0.0233` maxDD `-0.1418`
- `risk_on_and_context->fx_24h` score `1.1972` n `32` status `ready` deltaP `14.2361` edge `0.0233` maxDD `-0.1418`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

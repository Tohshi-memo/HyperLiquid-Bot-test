# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-16T02:37:28.749873+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11734`

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

- `market_context_high->unknown_24h` score `164.9908` n `94` status `ready` deltaP `-24.1178` edge `21.5818` maxDD `-7.8016`
- `risk_on_high->unknown_24h` score `33.561` n `32` status `ready` deltaP `-39.4768` edge `4.6409` maxDD `-1.6689`
- `risk_on_and_context->unknown_24h` score `33.561` n `32` status `ready` deltaP `-39.4768` edge `4.6409` maxDD `-1.6689`
- `news_risk_high->equity_24h` score `12.7733` n `36` status `ready` deltaP `24.9278` edge `0.9362` maxDD `-1.0358`
- `news_risk_high->equity_4h` score `7.624` n `36` status `ready` deltaP `38.7195` edge `0.3772` maxDD `0.0`
- `market_context_high->commodity_24h` score `7.0284` n `94` status `ready` deltaP `38.9468` edge `0.3318` maxDD `-0.1266`
- `risk_on_high->commodity_24h` score `5.8876` n `32` status `ready` deltaP `41.0745` edge `0.2168` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `5.8876` n `32` status `ready` deltaP `41.0745` edge `0.2168` maxDD `0.0`
- `risk_on_high->crypto_major_24h` score `3.8917` n `32` status `ready` deltaP `26.1211` edge `0.4404` maxDD `-6.2481`
- `risk_on_and_context->crypto_major_24h` score `3.8917` n `32` status `ready` deltaP `26.1211` edge `0.4404` maxDD `-6.2481`
- `news_risk_high->index_24h` score `3.6943` n `36` status `ready` deltaP `30.8492` edge `0.1022` maxDD `0.0`
- `risk_on_high->commodity_4h` score `3.0557` n `32` status `ready` deltaP `22.3323` edge `0.124` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `3.0557` n `32` status `ready` deltaP `22.3323` edge `0.124` maxDD `-0.1258`
- `market_context_high->commodity_4h` score `2.0226` n `103` status `ready` deltaP `17.9937` edge `0.0957` maxDD `-0.7687`
- `news_risk_high->index_4h` score `1.9266` n `36` status `ready` deltaP `22.2053` edge `0.0257` maxDD `-0.0546`
- `news_risk_high->equity_1h` score `1.7598` n `36` status `ready` deltaP `8.4332` edge `0.1223` maxDD `-0.5496`
- `risk_on_high->commodity_1h` score `1.3845` n `32` status `ready` deltaP `14.8578` edge `0.0396` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.3845` n `32` status `ready` deltaP `14.8578` edge `0.0396` maxDD `-0.1957`
- `risk_on_high->fx_4h` score `0.8399` n `32` status `ready` deltaP `10.2896` edge `0.0155` maxDD `-0.1285`
- `risk_on_and_context->fx_4h` score `0.8399` n `32` status `ready` deltaP `10.2896` edge `0.0155` maxDD `-0.1285`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

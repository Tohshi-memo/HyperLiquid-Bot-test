# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-15T23:52:28.348170+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11717`

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

- `market_context_high->unknown_24h` score `134.9606` n `105` status `ready` deltaP `-26.8053` edge `17.7497` maxDD `-7.8016`
- `risk_on_high->unknown_24h` score `33.6857` n `32` status `ready` deltaP `-38.2636` edge `4.6488` maxDD `-1.6689`
- `risk_on_and_context->unknown_24h` score `33.6857` n `32` status `ready` deltaP `-38.2636` edge `4.6488` maxDD `-1.6689`
- `news_risk_high->equity_24h` score `12.9382` n `36` status `ready` deltaP `26.3142` edge `0.9407` maxDD `-1.0358`
- `news_risk_high->equity_4h` score `7.6847` n `36` status `ready` deltaP `39.3293` edge `0.3782` maxDD `0.0`
- `market_context_high->commodity_24h` score `6.7991` n `105` status `ready` deltaP `37.9566` edge `0.3193` maxDD `-0.1266`
- `risk_on_high->commodity_24h` score `5.6729` n `32` status `ready` deltaP `39.8614` edge `0.207` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `5.6729` n `32` status `ready` deltaP `39.8614` edge `0.207` maxDD `0.0`
- `risk_on_high->crypto_major_24h` score `4.0063` n `32` status `ready` deltaP `27.3343` edge `0.447` maxDD `-6.2481`
- `risk_on_and_context->crypto_major_24h` score `4.0063` n `32` status `ready` deltaP `27.3343` edge `0.447` maxDD `-6.2481`
- `news_risk_high->index_24h` score `3.7799` n `36` status `ready` deltaP `31.8891` edge `0.1024` maxDD `0.0`
- `risk_on_high->commodity_4h` score `2.9925` n `32` status `ready` deltaP `21.7226` edge `0.1228` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.9925` n `32` status `ready` deltaP `21.7226` edge `0.1228` maxDD `-0.1258`
- `market_context_high->commodity_4h` score `2.2939` n `105` status `ready` deltaP `20.7405` edge `0.1` maxDD `-0.7687`
- `news_risk_high->index_4h` score `2.029` n `36` status `ready` deltaP `23.4248` edge `0.0261` maxDD `-0.0546`
- `news_risk_high->equity_1h` score `1.773` n `36` status `ready` deltaP `8.5829` edge `0.1224` maxDD `-0.5496`
- `risk_on_high->commodity_1h` score `1.3857` n `32` status `ready` deltaP `14.8578` edge `0.0397` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.3857` n `32` status `ready` deltaP `14.8578` edge `0.0397` maxDD `-0.1957`
- `risk_on_high->fx_4h` score `0.7655` n `32` status `ready` deltaP `9.375` edge `0.0154` maxDD `-0.1285`
- `risk_on_and_context->fx_4h` score `0.7655` n `32` status `ready` deltaP `9.375` edge `0.0154` maxDD `-0.1285`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

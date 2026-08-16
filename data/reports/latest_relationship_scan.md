# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-16T01:22:30.879212+00:00`
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

- `market_context_high->unknown_24h` score `150.5118` n `99` status `ready` deltaP `-25.4784` edge `19.7346` maxDD `-7.8016`
- `risk_on_high->unknown_24h` score `33.6138` n `32` status `ready` deltaP `-38.9569` edge `4.6442` maxDD `-1.6689`
- `risk_on_and_context->unknown_24h` score `33.6138` n `32` status `ready` deltaP `-38.9569` edge `4.6442` maxDD `-1.6689`
- `news_risk_high->equity_24h` score `12.875` n `36` status `ready` deltaP `25.7943` edge `0.9389` maxDD `-1.0358`
- `news_risk_high->equity_4h` score `7.6544` n `36` status `ready` deltaP `39.0244` edge `0.3777` maxDD `0.0`
- `market_context_high->commodity_24h` score `6.9655` n `99` status `ready` deltaP `38.881` edge `0.327` maxDD `-0.1266`
- `risk_on_high->commodity_24h` score `5.8257` n `32` status `ready` deltaP `40.9012` edge `0.2128` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `5.8257` n `32` status `ready` deltaP `40.9012` edge `0.2128` maxDD `0.0`
- `risk_on_high->crypto_major_24h` score `3.9132` n `32` status `ready` deltaP `26.2944` edge `0.442` maxDD `-6.2481`
- `risk_on_and_context->crypto_major_24h` score `3.9132` n `32` status `ready` deltaP `26.2944` edge `0.442` maxDD `-6.2481`
- `news_risk_high->index_24h` score `3.7221` n `36` status `ready` deltaP `31.1958` edge `0.1022` maxDD `0.0`
- `risk_on_high->commodity_4h` score `3.0521` n `32` status `ready` deltaP `22.3323` edge `0.1237` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `3.0521` n `32` status `ready` deltaP `22.3323` edge `0.1237` maxDD `-0.1258`
- `market_context_high->commodity_4h` score `2.0548` n `104` status `ready` deltaP `18.2458` edge `0.0967` maxDD `-0.7687`
- `news_risk_high->index_4h` score `1.9522` n `36` status `ready` deltaP `22.5101` edge `0.0258` maxDD `-0.0546`
- `news_risk_high->equity_1h` score `1.7886` n `36` status `ready` deltaP `8.7326` edge `0.1227` maxDD `-0.5496`
- `risk_on_high->commodity_1h` score `1.3857` n `32` status `ready` deltaP `14.8578` edge `0.0397` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.3857` n `32` status `ready` deltaP `14.8578` edge `0.0397` maxDD `-0.1957`
- `risk_on_high->fx_4h` score `0.8155` n `32` status `ready` deltaP `9.9848` edge `0.0155` maxDD `-0.1285`
- `risk_on_and_context->fx_4h` score `0.8155` n `32` status `ready` deltaP `9.9848` edge `0.0155` maxDD `-0.1285`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

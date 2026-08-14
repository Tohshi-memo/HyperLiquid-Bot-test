# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-14T10:07:35.698048+00:00`
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

- `market_context_high->unknown_24h` score `89.9938` n `150` status `ready` deltaP `-30.1458` edge `7.9917` maxDD `-9.6329`
- `risk_on_high->unknown_24h` score `32.9553` n `32` status `ready` deltaP `-44.2708` edge `4.5952` maxDD `-1.6689`
- `risk_on_and_context->unknown_24h` score `32.9553` n `32` status `ready` deltaP `-44.2708` edge `4.5952` maxDD `-1.6689`
- `news_risk_high->equity_24h` score `9.865` n `36` status `ready` deltaP `10.0694` edge `0.7929` maxDD `-1.0358`
- `news_risk_high->equity_4h` score `7.3389` n `36` status `ready` deltaP `39.1768` edge `0.3504` maxDD `0.0`
- `risk_on_high->commodity_24h` score `4.6358` n `32` status `ready` deltaP `30.9028` edge `0.1803` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `4.6358` n `32` status `ready` deltaP `30.9028` edge `0.1803` maxDD `0.0`
- `market_context_high->commodity_24h` score `2.7087` n `150` status `ready` deltaP `20.9028` edge `0.1667` maxDD `-2.4263`
- `risk_on_high->commodity_4h` score `2.61` n `32` status `ready` deltaP `18.2165` edge `0.1143` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.61` n `32` status `ready` deltaP `18.2165` edge `0.1143` maxDD `-0.1258`
- `news_risk_high->index_24h` score `2.2095` n `36` status `ready` deltaP `14.5833` edge `0.0869` maxDD `0.0`
- `news_risk_high->index_4h` score `1.7333` n `36` status `ready` deltaP `20.2235` edge `0.0228` maxDD `-0.0546`
- `risk_on_high->crypto_major_24h` score `1.6689` n `32` status `ready` deltaP `14.4097` edge `0.2335` maxDD `-6.2481`
- `risk_on_and_context->crypto_major_24h` score `1.6689` n `32` status `ready` deltaP `14.4097` edge `0.2335` maxDD `-6.2481`
- `news_risk_high->equity_1h` score `1.6554` n `36` status `ready` deltaP `8.5829` edge `0.1126` maxDD `-0.5496`
- `market_context_high->commodity_4h` score `1.2485` n `150` status `ready` deltaP `14.7582` edge `0.0695` maxDD `-2.1077`
- `risk_on_high->commodity_1h` score `1.224` n `32` status `ready` deltaP `13.0614` edge `0.0382` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.224` n `32` status `ready` deltaP `13.0614` edge `0.0382` maxDD `-0.1957`
- `risk_on_high->fx_24h` score `1.1984` n `32` status `ready` deltaP `14.2361` edge `0.0234` maxDD `-0.1418`
- `risk_on_and_context->fx_24h` score `1.1984` n `32` status `ready` deltaP `14.2361` edge `0.0234` maxDD `-0.1418`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

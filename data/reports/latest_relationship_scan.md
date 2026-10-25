# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-25T08:07:29.379607+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7906`

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

- `market_context_high->unknown_4h` score `42.9757` n `104` status `ready` deltaP `-0.129` edge `3.6157` maxDD `-1.016`
- `market_context_high->unknown_1h` score `12.7823` n `114` status `ready` deltaP `4.4831` edge `1.0842` maxDD `-1.5781`
- `market_context_high->crypto_alt_24h` score `4.38` n `40` status `ready` deltaP `21.7361` edge `0.5247` maxDD `-6.9786`
- `market_context_high->crypto_major_24h` score `1.7742` n `40` status `ready` deltaP `13.3333` edge `0.1649` maxDD `-5.8084`
- `market_context_high->commodity_24h` score `0.8206` n `40` status `ready` deltaP `16.1111` edge `0.0887` maxDD `-3.6055`
- `market_context_high->fx_4h` score `-0.0508` n `104` status `ready` deltaP `6.6956` edge `0.0087` maxDD `-0.4545`
- `market_context_high->fx_1h` score `-0.0572` n `114` status `ready` deltaP `3.7005` edge `0.0029` maxDD `-0.1258`
- `market_context_high->fx_24h` score `-0.4542` n `40` status `ready` deltaP `4.7917` edge `0.0061` maxDD `-1.0353`
- `market_context_high->commodity_1h` score `-0.5386` n `114` status `ready` deltaP `-0.5121` edge `0.0086` maxDD `-1.0053`
- `market_context_high->metal_1h` score `-0.6323` n `114` status `ready` deltaP `4.6197` edge `-0.0043` maxDD `-1.6682`
- `market_context_high->index_1h` score `-0.6612` n `114` status `ready` deltaP `-2.1405` edge `-0.0053` maxDD `-1.2155`
- `market_context_high->commodity_4h` score `-0.8714` n `104` status `ready` deltaP `-3.213` edge `0.0326` maxDD `-1.165`
- `market_context_high->crypto_major_1h` score `-1.4239` n `114` status `ready` deltaP `1.2633` edge `-0.0329` maxDD `-9.3126`
- `market_context_high->metal_4h` score `-1.7305` n `104` status `ready` deltaP `6.9301` edge `-0.0194` maxDD `-5.3474`
- `market_context_high->index_4h` score `-2.03` n `104` status `ready` deltaP `-5.3588` edge `-0.0371` maxDD `-4.3282`
- `market_context_high->metal_24h` score `-2.6991` n `40` status `ready` deltaP `-5.5208` edge `-0.0237` maxDD `-6.4869`
- `market_context_high->crypto_alt_1h` score `-3.1718` n `114` status `ready` deltaP `-2.4189` edge `-0.0608` maxDD `-11.3243`
- `market_context_high->equity_1h` score `-3.8139` n `114` status `ready` deltaP `-0.4938` edge `-0.0872` maxDD `-12.1865`
- `market_context_high->index_24h` score `-5.8746` n `40` status `ready` deltaP `-26.1458` edge `-0.1851` maxDD `-5.078`
- `market_context_high->crypto_major_4h` score `-5.9598` n `104` status `ready` deltaP `-10.061` edge `-0.1973` maxDD `-33.3092`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

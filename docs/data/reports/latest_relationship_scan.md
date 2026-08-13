# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-13T13:52:24.811406+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11712`

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

- `market_context_high->unknown_24h` score `53.5611` n `161` status `ready` deltaP `-23.6898` edge `4.9126` maxDD `-9.6329`
- `risk_on_high->unknown_24h` score `21.061` n `32` status `ready` deltaP `-42.1875` edge `3.0564` maxDD `-1.6689`
- `risk_on_and_context->unknown_24h` score `21.061` n `32` status `ready` deltaP `-42.1875` edge `3.0564` maxDD `-1.6689`
- `news_risk_high->equity_24h` score `8.4215` n `32` status `ready` deltaP `7.9861` edge `0.6865` maxDD `-1.0358`
- `news_risk_high->equity_4h` score `6.8434` n `36` status `ready` deltaP `36.4329` edge `0.3274` maxDD `0.0`
- `risk_on_high->commodity_24h` score `3.7308` n `32` status `ready` deltaP `26.9097` edge `0.1315` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `3.7308` n `32` status `ready` deltaP `26.9097` edge `0.1315` maxDD `0.0`
- `risk_on_high->commodity_4h` score `2.6214` n `32` status `ready` deltaP `18.6738` edge `0.1122` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.6214` n `32` status `ready` deltaP `18.6738` edge `0.1122` maxDD `-0.1258`
- `news_risk_high->index_24h` score `2.4404` n `32` status `ready` deltaP `15.625` edge `0.0992` maxDD `0.0`
- `risk_on_high->fx_24h` score `2.0036` n `32` status `ready` deltaP `22.3958` edge `0.0361` maxDD `-0.1418`
- `risk_on_and_context->fx_24h` score `2.0036` n `32` status `ready` deltaP `22.3958` edge `0.0361` maxDD `-0.1418`
- `news_risk_high->index_4h` score `1.7961` n `36` status `ready` deltaP `20.5284` edge `0.026` maxDD `-0.0546`
- `market_context_high->commodity_24h` score `1.7618` n `161` status `ready` deltaP `16.9718` edge `0.114` maxDD `-2.4263`
- `news_risk_high->equity_1h` score `1.4828` n `36` status `ready` deltaP `7.2356` edge `0.1072` maxDD `-0.5496`
- `market_context_high->commodity_4h` score `1.4399` n `161` status `ready` deltaP `16.3252` edge `0.075` maxDD `-2.1077`
- `risk_on_high->crypto_major_24h` score `1.2943` n `32` status `ready` deltaP `12.5` edge `0.1982` maxDD `-6.2481`
- `risk_on_and_context->crypto_major_24h` score `1.2943` n `32` status `ready` deltaP `12.5` edge `0.1982` maxDD `-6.2481`
- `risk_on_high->commodity_1h` score `1.218` n `32` status `ready` deltaP `13.0614` edge `0.0377` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.218` n `32` status `ready` deltaP `13.0614` edge `0.0377` maxDD `-0.1957`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

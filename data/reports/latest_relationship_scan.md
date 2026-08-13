# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-13T14:37:54.750657+00:00`
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

- `market_context_high->unknown_24h` score `60.4707` n `161` status `ready` deltaP `-23.6898` edge `5.4884` maxDD `-9.6329`
- `risk_on_high->unknown_24h` score `25.5522` n `32` status `ready` deltaP `-42.1875` edge `3.6322` maxDD `-1.6689`
- `risk_on_and_context->unknown_24h` score `25.5522` n `32` status `ready` deltaP `-42.1875` edge `3.6322` maxDD `-1.6689`
- `news_risk_high->equity_24h` score `8.8913` n `34` status `ready` deltaP `9.089` edge `0.7183` maxDD `-1.0358`
- `news_risk_high->equity_4h` score `6.7084` n `36` status `ready` deltaP `35.9756` edge `0.3192` maxDD `0.0`
- `risk_on_high->commodity_24h` score `3.8396` n `32` status `ready` deltaP `27.4306` edge `0.1371` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `3.8396` n `32` status `ready` deltaP `27.4306` edge `0.1371` maxDD `0.0`
- `risk_on_high->commodity_4h` score `2.6626` n `32` status `ready` deltaP `18.9787` edge `0.1136` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.6626` n `32` status `ready` deltaP `18.9787` edge `0.1136` maxDD `-0.1258`
- `news_risk_high->index_24h` score `2.498` n `34` status `ready` deltaP `15.625` edge `0.104` maxDD `0.0`
- `risk_on_high->fx_24h` score `1.9976` n `32` status `ready` deltaP `22.3958` edge `0.0356` maxDD `-0.1418`
- `risk_on_and_context->fx_24h` score `1.9976` n `32` status `ready` deltaP `22.3958` edge `0.0356` maxDD `-0.1418`
- `market_context_high->commodity_24h` score `1.8707` n `161` status `ready` deltaP `17.4927` edge `0.1196` maxDD `-2.4263`
- `news_risk_high->index_4h` score `1.7427` n `36` status `ready` deltaP `20.0711` edge `0.0246` maxDD `-0.0546`
- `market_context_high->commodity_4h` score `1.4811` n `161` status `ready` deltaP `16.6301` edge `0.0764` maxDD `-2.1077`
- `news_risk_high->equity_1h` score `1.4084` n `36` status `ready` deltaP `7.0859` edge `0.102` maxDD `-0.5496`
- `risk_on_high->commodity_1h` score `1.218` n `32` status `ready` deltaP `13.0614` edge `0.0377` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.218` n `32` status `ready` deltaP `13.0614` edge `0.0377` maxDD `-0.1957`
- `risk_on_high->crypto_major_24h` score `1.2118` n `32` status `ready` deltaP `11.9792` edge `0.1911` maxDD `-6.2481`
- `risk_on_and_context->crypto_major_24h` score `1.2118` n `32` status `ready` deltaP `11.9792` edge `0.1911` maxDD `-6.2481`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

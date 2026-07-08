# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-08T02:07:27.060644+00:00`
- Price records: `672`
- Market context records: `6041`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11125`

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

- `news_risk_high->fx_24h` score `7.9868` n `30` status `ready` deltaP `71.875` edge `0.1864` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.2345` n `30` status `ready` deltaP `43.811` edge `0.0654` maxDD `-0.0345`
- `news_risk_high->commodity_24h` score `2.4771` n `30` status `ready` deltaP `25.5556` edge `0.0566` maxDD `-0.3101`
- `news_risk_high->fx_1h` score `2.2717` n `30` status `ready` deltaP `27.2255` edge `0.0217` maxDD `-0.1113`
- `market_context_high->equity_4h` score `1.5625` n `206` status `ready` deltaP `8.7941` edge `0.1633` maxDD `-2.671`
- `market_context_high->equity_24h` score `1.4517` n `181` status `ready` deltaP `29.3048` edge `0.5654` maxDD `-33.6387`
- `news_risk_high->crypto_major_1h` score `0.9533` n `30` status `ready` deltaP `10.9381` edge `0.096` maxDD `-2.0691`
- `news_risk_high->crypto_alt_24h` score `0.6943` n `30` status `ready` deltaP `24.9305` edge `-0.0936` maxDD `-0.5131`
- `news_risk_high->crypto_alt_1h` score `0.3198` n `30` status `ready` deltaP `5.9182` edge `0.0477` maxDD `-1.6923`
- `news_risk_high->index_24h` score `0.1343` n `30` status `ready` deltaP `9.2361` edge `0.0428` maxDD `-2.3058`
- `market_context_high->metal_1h` score `-0.4158` n `206` status `ready` deltaP `3.43` edge `0.0037` maxDD `-2.0564`
- `news_risk_high->metal_1h` score `-0.4523` n `30` status `ready` deltaP `0.9381` edge `-0.0276` maxDD `-1.2643`
- `market_context_high->index_24h` score `-0.4727` n `181` status `ready` deltaP `5.0741` edge `0.0756` maxDD `-5.6021`
- `market_context_high->fx_1h` score `-0.5606` n `206` status `ready` deltaP `0.0087` edge `-0.0011` maxDD `-0.6538`
- `market_context_high->commodity_1h` score `-0.6727` n `206` status `ready` deltaP `-1.683` edge `-0.0002` maxDD `-0.5708`
- `market_context_high->crypto_major_1h` score `-0.8644` n `206` status `ready` deltaP `4.4009` edge `0.0366` maxDD `-9.807`
- `market_context_high->crypto_alt_1h` score `-0.8867` n `206` status `ready` deltaP `4.1059` edge `0.0342` maxDD `-9.3536`
- `market_context_high->index_4h` score `-0.9773` n `206` status `ready` deltaP `1.8056` edge `0.016` maxDD `-1.9335`
- `market_context_high->metal_4h` score `-0.9879` n `206` status `ready` deltaP `4.6383` edge `0.0055` maxDD `-3.4996`
- `news_risk_high->index_1h` score `-1.0727` n `30` status `ready` deltaP `-9.8503` edge `-0.0204` maxDD `-1.1161`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

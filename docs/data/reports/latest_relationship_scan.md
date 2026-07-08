# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-08T06:07:25.095376+00:00`
- Price records: `672`
- Market context records: `6058`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11073`

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

- `news_risk_high->fx_24h` score `8.1162` n `30` status `ready` deltaP `72.7431` edge `0.1914` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.3087` n `30` status `ready` deltaP `44.5732` edge `0.0665` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.3232` n `30` status `ready` deltaP `27.8243` edge `0.022` maxDD `-0.1113`
- `news_risk_high->crypto_alt_24h` score `2.3217` n `30` status `ready` deltaP `27.7083` edge `0.0235` maxDD `-0.5131`
- `news_risk_high->commodity_24h` score `1.7365` n `30` status `ready` deltaP `22.7778` edge `0.0134` maxDD `-0.3101`
- `market_context_high->equity_4h` score `1.2911` n `206` status `ready` deltaP `7.727` edge `0.1478` maxDD `-2.671`
- `news_risk_high->crypto_major_1h` score `0.9759` n `30` status `ready` deltaP `11.2375` edge `0.0969` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.3448` n `30` status `ready` deltaP `6.0679` edge `0.0499` maxDD `-1.6923`
- `news_risk_high->index_24h` score `0.0961` n `30` status `ready` deltaP `9.2361` edge `0.0379` maxDD `-2.3058`
- `market_context_high->metal_1h` score `-0.5085` n `206` status `ready` deltaP `2.0827` edge `0.0008` maxDD `-2.0564`
- `market_context_high->fx_1h` score `-0.5091` n `206` status `ready` deltaP `0.6075` edge `-0.0008` maxDD `-0.6538`
- `news_risk_high->metal_1h` score `-0.5449` n `30` status `ready` deltaP `-0.4092` edge `-0.0305` maxDD `-1.2643`
- `market_context_high->commodity_1h` score `-0.7673` n `206` status `ready` deltaP `-2.5812` edge `-0.0021` maxDD `-0.5708`
- `market_context_high->crypto_major_1h` score `-0.8418` n `206` status `ready` deltaP `4.7003` edge `0.0375` maxDD `-9.807`
- `market_context_high->crypto_alt_1h` score `-0.8618` n `206` status `ready` deltaP `4.2556` edge `0.0364` maxDD `-9.3536`
- `market_context_high->index_4h` score `-1.021` n `206` status `ready` deltaP `0.891` edge `0.0165` maxDD `-1.9335`
- `news_risk_high->index_1h` score `-1.0314` n `30` status `ready` deltaP `-9.2515` edge `-0.0191` maxDD `-1.1161`
- `market_context_high->equity_1h` score `-1.0697` n `206` status `ready` deltaP `0.6308` edge `0.0195` maxDD `-4.3608`
- `market_context_high->metal_4h` score `-1.2132` n `206` status `ready` deltaP `2.9615` edge `-0.0021` maxDD `-3.4996`
- `market_context_high->commodity_4h` score `-1.2204` n `206` status `ready` deltaP `-4.1884` edge `-0.0216` maxDD `-2.5555`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

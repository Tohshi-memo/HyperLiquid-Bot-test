# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-09T05:37:31.778554+00:00`
- Price records: `672`
- Market context records: `6158`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11131`

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

- `news_risk_high->crypto_alt_24h` score `12.2843` n `30` status `ready` deltaP `42.4712` edge `0.7553` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `7.5387` n `30` status `ready` deltaP `66.3793` edge `0.1857` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.209` n `32` status `ready` deltaP `43.8068` edge `0.0633` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.4204` n `32` status `ready` deltaP `29.0984` edge `0.0216` maxDD `-0.1113`
- `market_context_high->unknown_1h` score `1.6584` n `195` status `ready` deltaP `1.0669` edge `0.2319` maxDD `-3.7317`
- `news_risk_high->crypto_major_1h` score `1.2485` n `32` status `ready` deltaP `13.315` edge `0.118` maxDD `-2.0691`
- `news_risk_high->crypto_major_24h` score `0.9261` n `30` status `ready` deltaP `14.023` edge `0.1032` maxDD `-4.2368`
- `news_risk_high->crypto_alt_1h` score `0.6519` n `32` status `ready` deltaP `8.5553` edge `0.0727` maxDD `-1.6923`
- `market_context_high->equity_4h` score `0.0394` n `195` status `ready` deltaP `3.0303` edge `0.0748` maxDD `-2.671`
- `market_context_high->unknown_4h` score `0.03` n `195` status `ready` deltaP `-1.0606` edge `0.2628` maxDD `-11.925`
- `market_context_high->metal_24h` score `-0.0859` n `195` status `ready` deltaP `19.4607` edge `0.1161` maxDD `-11.8809`
- `news_risk_high->index_24h` score `-0.2223` n `30` status `ready` deltaP `7.6436` edge `0.0077` maxDD `-2.3058`
- `market_context_high->fx_1h` score `-0.2569` n `195` status `ready` deltaP `1.7907` edge `-0.0003` maxDD `-0.5659`
- `market_context_high->metal_4h` score `-0.5745` n `195` status `ready` deltaP `4.1842` edge `0.0172` maxDD `-3.4996`
- `news_risk_high->commodity_24h` score `-0.6051` n `30` status `ready` deltaP `13.9081` edge `-0.1226` maxDD `-0.3101`
- `market_context_high->commodity_1h` score `-0.7229` n `195` status `ready` deltaP `-1.7555` edge `-0.0039` maxDD `-0.5708`
- `news_risk_high->metal_1h` score `-0.7684` n `32` status `ready` deltaP `-3.0551` edge `-0.0284` maxDD `-1.6464`
- `market_context_high->metal_1h` score `-0.8165` n `195` status `ready` deltaP `2.3295` edge `-0.0037` maxDD `-2.0564`
- `market_context_high->equity_1h` score `-0.8682` n `195` status `ready` deltaP `-1.6592` edge `0.0113` maxDD `-4.2573`
- `market_context_high->crypto_alt_1h` score `-0.924` n `195` status `ready` deltaP `3.5393` edge `0.0332` maxDD `-9.3536`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

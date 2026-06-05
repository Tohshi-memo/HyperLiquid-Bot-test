# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-05T02:22:23.401343+00:00`
- Price records: `672`
- Market context records: `2927`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6927`

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

- `market_context_high->crypto_alt_24h` score `14.366` n `142` status `ready` deltaP `13.9867` edge `1.4956` maxDD `-22.6673`
- `market_context_high->equity_24h` score `7.0779` n `142` status `ready` deltaP `16.1996` edge `0.6822` maxDD `-12.6963`
- `market_context_high->unknown_24h` score `6.2163` n `142` status `ready` deltaP `14.2336` edge `0.4696` maxDD `-1.7175`
- `market_context_high->index_24h` score `2.4498` n `142` status `ready` deltaP `11.9743` edge `0.2224` maxDD `-2.5127`
- `market_context_high->commodity_24h` score `1.8523` n `142` status `ready` deltaP `15.7252` edge `0.3589` maxDD `-12.4171`
- `market_context_high->equity_4h` score `0.728` n `142` status `ready` deltaP `8.0599` edge `0.1449` maxDD `-5.7037`
- `market_context_high->index_4h` score `0.6609` n `142` status `ready` deltaP `14.3679` edge `0.0731` maxDD `-2.3986`
- `market_context_high->unknown_4h` score `0.0571` n `142` status `ready` deltaP `3.899` edge `0.0841` maxDD `-3.7602`
- `market_context_high->crypto_alt_4h` score `-0.0361` n `142` status `ready` deltaP `15.1` edge `0.3304` maxDD `-28.7261`
- `market_context_high->index_1h` score `-0.0381` n `143` status `ready` deltaP `4.0985` edge `0.0172` maxDD `-1.2855`
- `market_context_high->unknown_1h` score `-0.4535` n `143` status `ready` deltaP `3.4484` edge `0.0123` maxDD `-3.1801`
- `market_context_high->equity_1h` score `-0.4591` n `143` status `ready` deltaP `0.3047` edge `0.043` maxDD `-2.6634`
- `market_context_high->crypto_alt_1h` score `-0.5398` n `143` status `ready` deltaP `5.5955` edge `0.0695` maxDD `-10.747`
- `market_context_high->fx_1h` score `-0.5841` n `143` status `ready` deltaP `-1.096` edge `0.003` maxDD `-0.2164`
- `market_context_high->metal_1h` score `-0.6512` n `143` status `ready` deltaP `0.247` edge `0.0036` maxDD `-3.4325`
- `market_context_high->commodity_1h` score `-0.6867` n `143` status `ready` deltaP `-1.6948` edge `-0.0014` maxDD `-4.3601`
- `market_context_high->crypto_major_1h` score `-0.71` n `143` status `ready` deltaP `5.3432` edge `0.0603` maxDD `-9.622`
- `market_context_high->fx_4h` score `-1.0128` n `142` status `ready` deltaP `-1.9237` edge `0.0063` maxDD `-0.5631`
- `market_context_high->commodity_4h` score `-1.2725` n `142` status `ready` deltaP `1.9903` edge `0.0156` maxDD `-10.0279`
- `market_context_high->fx_24h` score `-1.2888` n `142` status `ready` deltaP `-1.7116` edge `-0.0088` maxDD `-0.6418`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-27T08:37:25.802652+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11908`

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

- `news_risk_high->unknown_24h` score `1423.8456` n `123` status `ready` deltaP `1.2153` edge `118.6457` maxDD `0.0`
- `market_context_high->unknown_1h` score `133.4743` n `43` status `ready` deltaP `10.6984` edge `11.0562` maxDD `-0.0395`
- `market_context_high->crypto_major_24h` score `55.48` n `39` status `ready` deltaP `29.9012` edge `4.4591` maxDD `-2.4756`
- `market_context_high->equity_24h` score `29.5727` n `39` status `ready` deltaP `35.804` edge `2.2571` maxDD `-2.1786`
- `market_context_high->crypto_alt_24h` score `28.6429` n `39` status `ready` deltaP `14.6234` edge `2.3274` maxDD `-2.7051`
- `market_context_high->index_24h` score `8.2408` n `39` status `ready` deltaP `33.1998` edge `0.4742` maxDD `-0.3705`
- `market_context_high->metal_24h` score `4.318` n `39` status `ready` deltaP `38.9957` edge `0.1237` maxDD `-0.2401`
- `market_context_high->equity_4h` score `3.8356` n `42` status `ready` deltaP `25.2903` edge `0.1845` maxDD `-1.3444`
- `market_context_high->crypto_alt_4h` score `3.5895` n `42` status `ready` deltaP `17.1748` edge `0.2389` maxDD `-3.3417`
- `market_context_high->index_4h` score `3.1341` n `42` status `ready` deltaP `34.5674` edge `0.0378` maxDD `-0.2323`
- `market_context_high->crypto_major_4h` score `1.9643` n `42` status `ready` deltaP `9.2915` edge `0.1922` maxDD `-5.2359`
- `market_context_high->equity_1h` score `1.4817` n `43` status `ready` deltaP `16.5541` edge `0.0534` maxDD `-1.5564`
- `market_context_high->index_1h` score `1.1695` n `43` status `ready` deltaP `16.105` edge `0.0096` maxDD `-0.2275`
- `market_context_high->crypto_major_1h` score `1.1619` n `43` status `ready` deltaP `9.647` edge `0.1183` maxDD `-4.8632`
- `market_context_high->crypto_alt_1h` score `1.0169` n `43` status `ready` deltaP `9.1283` edge `0.1128` maxDD `-5.7799`
- `news_risk_high->index_24h` score `0.6442` n `123` status `ready` deltaP `14.6257` edge `0.0257` maxDD `-2.2287`
- `news_risk_high->metal_24h` score `0.4802` n `123` status `ready` deltaP `15.481` edge `0.1223` maxDD `-6.8392`
- `market_context_high->fx_1h` score `0.3879` n `43` status `ready` deltaP `11.6523` edge `0.0077` maxDD `-0.1854`
- `market_context_high->metal_4h` score `-0.0245` n `42` status `ready` deltaP `2.497` edge `0.0192` maxDD `-0.3647`
- `market_context_high->metal_1h` score `-0.0864` n `43` status `ready` deltaP `1.6014` edge `0.0101` maxDD `-0.215`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

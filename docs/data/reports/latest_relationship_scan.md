# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-11T22:37:27.866896+00:00`
- Price records: `672`
- Market context records: `6437`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5875`

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

- `news_risk_high->crypto_alt_24h` score `11.6655` n `32` status `ready` deltaP `29.8611` edge `0.7878` maxDD `-0.5131`
- `market_context_high->unknown_24h` score `8.6721` n `146` status `ready` deltaP `21.3304` edge `0.9105` maxDD `-15.0689`
- `news_risk_high->fx_24h` score `6.4428` n `32` status `ready` deltaP `53.8194` edge `0.1781` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.1084` n `32` status `ready` deltaP `42.7591` edge `0.0619` maxDD `-0.0345`
- `news_risk_high->commodity_24h` score `4.0993` n `32` status `ready` deltaP `35.2431` edge `0.1272` maxDD `-0.3101`
- `news_risk_high->crypto_major_24h` score `3.2427` n `32` status `ready` deltaP `11.4583` edge `0.4173` maxDD `-4.2368`
- `news_risk_high->fx_1h` score `2.4326` n `32` status `ready` deltaP `29.3413` edge `0.021` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `1.4523` n `32` status `ready` deltaP `13.5292` edge `0.1427` maxDD `-2.0691`
- `market_context_high->unknown_1h` score `1.4379` n `191` status `ready` deltaP `-4.9009` edge `0.2426` maxDD `-3.2083`
- `news_risk_high->crypto_alt_1h` score `0.8341` n `32` status `ready` deltaP `9.6744` edge `0.0886` maxDD `-1.6923`
- `market_context_high->index_4h` score `0.0326` n `191` status `ready` deltaP `7.1933` edge `0.0224` maxDD `-0.4108`
- `market_context_high->metal_4h` score `-0.2015` n `191` status `ready` deltaP `7.744` edge `0.0404` maxDD `-2.7056`
- `news_risk_high->unknown_1h` score `-0.2645` n `32` status `ready` deltaP `6.8301` edge `-0.0331` maxDD `-0.7581`
- `market_context_high->metal_1h` score `-0.5361` n `191` status `ready` deltaP `1.0847` edge `0.0018` maxDD `-1.8877`
- `market_context_high->metal_24h` score `-0.5557` n `146` status `ready` deltaP `13.9959` edge `0.0923` maxDD `-11.8809`
- `news_risk_high->metal_1h` score `-0.5643` n `32` status `ready` deltaP `0.2994` edge `-0.0246` maxDD `-1.6464`
- `market_context_high->equity_4h` score `-0.6343` n `191` status `ready` deltaP `6.3984` edge `0.0459` maxDD `-8.2573`
- `market_context_high->commodity_1h` score `-0.6391` n `191` status `ready` deltaP `-1.6091` edge `-0.0029` maxDD `-2.1314`
- `market_context_high->fx_1h` score `-0.6969` n `191` status `ready` deltaP `-0.6325` edge `-0.0015` maxDD `-0.8555`
- `market_context_high->index_1h` score `-0.725` n `191` status `ready` deltaP `-3.5536` edge `0.0027` maxDD `-0.7564`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

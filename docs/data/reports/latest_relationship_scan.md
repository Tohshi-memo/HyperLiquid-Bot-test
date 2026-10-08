# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-08T16:07:46.759879+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8888`

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

- `market_context_high->unknown_4h` score `40.165` n `91` status `ready` deltaP `-2.2246` edge `3.4158` maxDD `-2.3109`
- `news_risk_high->crypto_alt_4h` score `13.519` n `49` status `ready` deltaP `42.9878` edge `0.84` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `13.2708` n `49` status `ready` deltaP `44.394` edge `0.8167` maxDD `-0.2073`
- `news_risk_high->equity_24h` score `7.487` n `49` status `ready` deltaP `22.2865` edge `0.4853` maxDD `-0.1298`
- `market_context_high->crypto_major_24h` score `7.2674` n `90` status `ready` deltaP `18.8696` edge `1.1033` maxDD `-16.7906`
- `news_risk_high->index_24h` score `5.761` n `49` status `ready` deltaP `42.3875` edge `0.1975` maxDD `0.0`
- `news_risk_high->equity_4h` score `5.1074` n `49` status `ready` deltaP `29.9465` edge `0.2465` maxDD `-0.6421`
- `market_context_high->equity_24h` score `4.8186` n `90` status `ready` deltaP `21.5609` edge `0.3007` maxDD `-1.0977`
- `news_risk_high->index_4h` score `4.2955` n `49` status `ready` deltaP `43.386` edge `0.0732` maxDD `-0.025`
- `news_risk_high->commodity_24h` score `3.2014` n `49` status `ready` deltaP `33.9807` edge `0.0487` maxDD `-0.0096`
- `news_risk_high->crypto_major_1h` score `3.1745` n `49` status `ready` deltaP `12.6115` edge `0.216` maxDD `-1.5096`
- `news_risk_high->crypto_alt_1h` score `2.6862` n `49` status `ready` deltaP `6.6388` edge `0.2113` maxDD `-1.2034`
- `news_risk_high->index_1h` score `2.399` n `49` status `ready` deltaP `29.8363` edge `0.015` maxDD `-0.1194`
- `market_context_high->metal_24h` score `1.4488` n `90` status `ready` deltaP `23.8869` edge `0.175` maxDD `-3.5466`
- `market_context_high->crypto_major_4h` score `1.4267` n `91` status `ready` deltaP `17.7064` edge `0.1979` maxDD `-6.9761`
- `market_context_high->crypto_alt_24h` score `1.279` n `90` status `ready` deltaP `10.5729` edge `0.6873` maxDD `-34.5048`
- `news_risk_high->metal_4h` score `1.1849` n `49` status `ready` deltaP `18.4482` edge `0.0705` maxDD `-0.993`
- `market_context_high->fx_4h` score `0.5757` n `91` status `ready` deltaP `16.4484` edge `0.013` maxDD `-0.3077`
- `market_context_high->fx_1h` score `0.5314` n `91` status `ready` deltaP `9.8408` edge `0.0029` maxDD `-0.271`
- `market_context_high->crypto_major_1h` score `0.352` n `91` status `ready` deltaP `11.0417` edge `0.0604` maxDD `-3.7778`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

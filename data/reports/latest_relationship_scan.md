# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-08T15:37:47.577874+00:00`
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

- `market_context_high->unknown_4h` score `40.1218` n `91` status `ready` deltaP `-2.2246` edge `3.4122` maxDD `-2.3109`
- `news_risk_high->crypto_alt_4h` score `13.3398` n `49` status `ready` deltaP `42.6829` edge `0.8271` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `13.1252` n `49` status `ready` deltaP `44.0891` edge `0.8066` maxDD `-0.2073`
- `news_risk_high->equity_24h` score `7.295` n `49` status `ready` deltaP `21.9405` edge `0.4716` maxDD `-0.1298`
- `market_context_high->crypto_major_24h` score `7.0442` n `90` status `ready` deltaP `18.5236` edge `1.077` maxDD `-16.7906`
- `news_risk_high->index_24h` score `5.7057` n `49` status `ready` deltaP `42.0415` edge `0.1952` maxDD `0.0`
- `news_risk_high->equity_4h` score `5.035` n `49` status `ready` deltaP `29.6416` edge `0.2425` maxDD `-0.6421`
- `market_context_high->equity_24h` score `4.6265` n `90` status `ready` deltaP `21.2149` edge `0.287` maxDD `-1.0977`
- `news_risk_high->index_4h` score `4.2809` n `49` status `ready` deltaP `43.2336` edge `0.073` maxDD `-0.025`
- `news_risk_high->commodity_24h` score `3.2867` n `49` status `ready` deltaP `34.3267` edge `0.0535` maxDD `-0.0096`
- `news_risk_high->crypto_major_1h` score `3.0497` n `49` status `ready` deltaP `12.3121` edge `0.2076` maxDD `-1.5096`
- `news_risk_high->crypto_alt_1h` score `2.5578` n `49` status `ready` deltaP `6.6388` edge `0.2006` maxDD `-1.2034`
- `news_risk_high->index_1h` score `2.4026` n `49` status `ready` deltaP `29.8363` edge `0.0153` maxDD `-0.1194`
- `market_context_high->metal_24h` score `1.4215` n `90` status `ready` deltaP `23.5409` edge `0.1738` maxDD `-3.5466`
- `market_context_high->crypto_major_4h` score `1.332` n `91` status `ready` deltaP `17.4015` edge `0.1878` maxDD `-6.9761`
- `news_risk_high->metal_4h` score `1.1715` n `49` status `ready` deltaP `18.2958` edge `0.0698` maxDD `-0.993`
- `market_context_high->crypto_alt_24h` score `1.073` n `90` status `ready` deltaP `10.2269` edge `0.6632` maxDD `-34.5048`
- `market_context_high->fx_4h` score `0.6073` n `91` status `ready` deltaP `16.7533` edge `0.0136` maxDD `-0.3077`
- `market_context_high->fx_1h` score `0.5326` n `91` status `ready` deltaP `9.8408` edge `0.003` maxDD `-0.271`
- `market_context_high->crypto_major_1h` score `0.2709` n `91` status `ready` deltaP `10.7423` edge `0.052` maxDD `-3.7778`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

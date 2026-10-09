# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-09T02:37:25.182147+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8896`

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

- `market_context_high->unknown_4h` score `39.8284` n `91` status `ready` deltaP `-3.5965` edge `3.3969` maxDD `-2.3109`
- `news_risk_high->crypto_alt_4h` score `14.344` n `45` status `ready` deltaP `43.4451` edge `0.9057` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `13.7256` n `45` status `ready` deltaP `44.1836` edge `0.856` maxDD `-0.2073`
- `news_risk_high->equity_24h` score `11.0785` n `45` status `ready` deltaP `28.7194` edge `0.7417` maxDD `-0.1298`
- `market_context_high->crypto_major_24h` score `9.6213` n `90` status `ready` deltaP `21.9122` edge `1.3848` maxDD `-16.7906`
- `market_context_high->equity_24h` score `8.7453` n `90` status `ready` deltaP `28.7194` edge `0.5802` maxDD `-1.0977`
- `news_risk_high->index_24h` score `6.8777` n `45` status `ready` deltaP `49.5667` edge `0.2427` maxDD `0.0`
- `news_risk_high->equity_4h` score `5.9211` n `45` status `ready` deltaP `31.5074` edge `0.3039` maxDD `-0.6421`
- `news_risk_high->index_4h` score `4.55` n `45` status `ready` deltaP `45.1863` edge `0.0824` maxDD `-0.025`
- `market_context_high->crypto_alt_24h` score `3.3763` n `90` status `ready` deltaP `13.6145` edge `0.9359` maxDD `-34.5048`
- `news_risk_high->crypto_major_1h` score `3.2403` n `45` status `ready` deltaP `13.0739` edge `0.2184` maxDD `-1.5096`
- `news_risk_high->crypto_alt_1h` score `2.3578` n `45` status `ready` deltaP `4.6341` edge `0.1973` maxDD `-1.2034`
- `news_risk_high->index_1h` score `2.2648` n `45` status `ready` deltaP `28.2036` edge `0.0147` maxDD `-0.1194`
- `news_risk_high->commodity_24h` score `2.1859` n `45` status `ready` deltaP `28.8312` edge `-0.0016` maxDD `-0.0096`
- `market_context_high->crypto_major_4h` score `1.7294` n `91` status `ready` deltaP `17.8588` edge `0.2357` maxDD `-6.9761`
- `news_risk_high->metal_4h` score `1.3093` n `45` status `ready` deltaP `20.6301` edge `0.0719` maxDD `-0.993`
- `market_context_high->metal_24h` score `1.1672` n `90` status `ready` deltaP `20.5257` edge `0.1613` maxDD `-3.5466`
- `market_context_high->fx_4h` score `0.4358` n `91` status `ready` deltaP `14.924` edge `0.0115` maxDD `-0.3077`
- `market_context_high->fx_1h` score `0.4284` n `91` status `ready` deltaP `8.6432` edge `0.0023` maxDD `-0.271`
- `news_risk_high->metal_1h` score `0.3777` n `45` status `ready` deltaP `9.5509` edge `0.0159` maxDD `-0.4919`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

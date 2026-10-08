# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-08T15:22:35.926489+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8739`

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

- `market_context_high->unknown_4h` score `40.7447` n `90` status `ready` deltaP `-2.4932` edge `3.4659` maxDD `-2.3109`
- `news_risk_high->crypto_alt_4h` score `13.2618` n `49` status `ready` deltaP `42.6829` edge `0.8206` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `13.053` n `49` status `ready` deltaP `43.9367` edge `0.8016` maxDD `-0.2073`
- `news_risk_high->equity_24h` score `7.1995` n `49` status `ready` deltaP `21.7675` edge `0.4648` maxDD `-0.1298`
- `market_context_high->crypto_major_24h` score `6.9315` n `90` status `ready` deltaP `18.3506` edge `1.0637` maxDD `-16.7906`
- `news_risk_high->index_24h` score `5.6775` n `49` status `ready` deltaP `41.8685` edge `0.194` maxDD `0.0`
- `news_risk_high->equity_4h` score `5.0206` n `49` status `ready` deltaP `29.6416` edge `0.2413` maxDD `-0.6421`
- `market_context_high->equity_24h` score `4.5311` n `90` status `ready` deltaP `21.0419` edge `0.2802` maxDD `-1.0977`
- `news_risk_high->index_4h` score `4.2821` n `49` status `ready` deltaP `43.2336` edge `0.0731` maxDD `-0.025`
- `news_risk_high->commodity_24h` score `3.3257` n `49` status `ready` deltaP `34.4997` edge `0.0556` maxDD `-0.0096`
- `news_risk_high->crypto_major_1h` score `2.9778` n `49` status `ready` deltaP `12.1624` edge `0.2026` maxDD `-1.5096`
- `market_context_high->crypto_major_4h` score `2.9256` n `90` status `ready` deltaP `18.0183` edge `0.2201` maxDD `-4.047`
- `news_risk_high->crypto_alt_1h` score `2.4798` n `49` status `ready` deltaP `6.6388` edge `0.1941` maxDD `-1.2034`
- `news_risk_high->index_1h` score `2.4038` n `49` status `ready` deltaP `29.8363` edge `0.0154` maxDD `-0.1194`
- `market_context_high->metal_24h` score `1.407` n `90` status `ready` deltaP `23.3679` edge `0.1731` maxDD `-3.5466`
- `news_risk_high->metal_4h` score `1.1715` n `49` status `ready` deltaP `18.2958` edge `0.0698` maxDD `-0.993`
- `market_context_high->crypto_alt_24h` score `0.972` n `90` status `ready` deltaP `10.0539` edge `0.6514` maxDD `-34.5048`
- `market_context_high->fx_4h` score `0.5839` n `90` status `ready` deltaP `16.4905` edge `0.0134` maxDD `-0.3077`
- `market_context_high->fx_1h` score `0.5206` n `91` status `ready` deltaP `9.6911` edge `0.003` maxDD `-0.271`
- `market_context_high->crypto_major_1h` score `0.2241` n `91` status `ready` deltaP `10.5926` edge `0.047` maxDD `-3.7778`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

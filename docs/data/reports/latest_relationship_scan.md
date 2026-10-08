# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-08T13:37:31.690903+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8747`

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

- `market_context_high->unknown_4h` score `40.7253` n `90` status `ready` deltaP `-2.6456` edge `3.4653` maxDD `-2.3109`
- `news_risk_high->crypto_alt_4h` score `13.2402` n `49` status `ready` deltaP `42.6829` edge `0.8188` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `12.9894` n `49` status `ready` deltaP `43.9367` edge `0.7963` maxDD `-0.2073`
- `news_risk_high->equity_24h` score `6.8005` n `49` status `ready` deltaP `20.6795` edge `0.4388` maxDD `-0.1298`
- `market_context_high->crypto_major_24h` score `6.5115` n `90` status `ready` deltaP `17.2193` edge `1.0174` maxDD `-16.7906`
- `news_risk_high->index_24h` score `5.5456` n `49` status `ready` deltaP `40.7599` edge `0.1904` maxDD `0.0`
- `news_risk_high->equity_4h` score `5.064` n `49` status `ready` deltaP `29.794` edge `0.2439` maxDD `-0.6421`
- `news_risk_high->index_4h` score `4.3865` n `49` status `ready` deltaP `44.1482` edge `0.0757` maxDD `-0.025`
- `market_context_high->equity_24h` score `4.1321` n `90` status `ready` deltaP `19.9539` edge `0.2542` maxDD `-1.0977`
- `news_risk_high->commodity_24h` score `3.5851` n `49` status `ready` deltaP `35.6421` edge `0.0696` maxDD `-0.0096`
- `news_risk_high->crypto_major_1h` score `2.9921` n `49` status `ready` deltaP `12.3121` edge `0.2028` maxDD `-1.5096`
- `market_context_high->crypto_major_4h` score `2.862` n `90` status `ready` deltaP `18.0183` edge `0.2148` maxDD `-4.047`
- `news_risk_high->crypto_alt_1h` score `2.5481` n `49` status `ready` deltaP `7.2376` edge `0.1958` maxDD `-1.2034`
- `news_risk_high->index_1h` score `2.4301` n `49` status `ready` deltaP `30.1357` edge `0.0156` maxDD `-0.1194`
- `market_context_high->metal_24h` score `1.4106` n `90` status `ready` deltaP `23.4369` edge `0.1731` maxDD `-3.5466`
- `news_risk_high->metal_4h` score `1.1927` n `49` status `ready` deltaP `18.4482` edge `0.0715` maxDD `-0.993`
- `market_context_high->crypto_alt_24h` score `0.8006` n `90` status `ready` deltaP `9.787` edge `0.6312` maxDD `-34.5048`
- `market_context_high->fx_4h` score `0.6933` n `90` status `ready` deltaP `17.5576` edge `0.0154` maxDD `-0.3077`
- `market_context_high->fx_1h` score `0.5973` n `91` status `ready` deltaP `10.5893` edge `0.0034` maxDD `-0.271`
- `market_context_high->crypto_major_1h` score `0.2334` n `91` status `ready` deltaP `10.7423` edge `0.0472` maxDD `-3.7778`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

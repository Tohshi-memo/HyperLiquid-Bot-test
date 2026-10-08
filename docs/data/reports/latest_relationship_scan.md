# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-08T16:37:28.248679+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8898`

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

- `market_context_high->unknown_4h` score `40.1602` n `91` status `ready` deltaP `-2.2246` edge `3.4154` maxDD `-2.3109`
- `news_risk_high->crypto_alt_4h` score `13.697` n `49` status `ready` deltaP `43.2927` edge `0.8528` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `13.4056` n `49` status `ready` deltaP `44.6989` edge `0.8259` maxDD `-0.2073`
- `news_risk_high->equity_24h` score `7.6923` n `49` status `ready` deltaP `22.6325` edge `0.5001` maxDD `-0.1298`
- `market_context_high->crypto_major_24h` score `7.4702` n `90` status `ready` deltaP `19.2157` edge `1.127` maxDD `-16.7906`
- `news_risk_high->index_24h` score `5.8211` n `49` status `ready` deltaP `42.7336` edge `0.2002` maxDD `0.0`
- `news_risk_high->equity_4h` score `5.1906` n `49` status `ready` deltaP `30.2513` edge `0.2514` maxDD `-0.6421`
- `market_context_high->equity_24h` score `5.0239` n `90` status `ready` deltaP `21.9069` edge `0.3155` maxDD `-1.0977`
- `news_risk_high->index_4h` score `4.3247` n `49` status `ready` deltaP `43.6909` edge `0.0736` maxDD `-0.025`
- `news_risk_high->crypto_major_1h` score `3.1553` n `49` status `ready` deltaP `12.4618` edge `0.2154` maxDD `-1.5096`
- `news_risk_high->commodity_24h` score `3.1257` n `49` status `ready` deltaP `33.6347` edge `0.0447` maxDD `-0.0096`
- `news_risk_high->crypto_alt_1h` score `2.6574` n `49` status `ready` deltaP `6.4891` edge `0.2099` maxDD `-1.2034`
- `news_risk_high->index_1h` score `2.3702` n `49` status `ready` deltaP `29.5369` edge `0.0146` maxDD `-0.1194`
- `market_context_high->crypto_major_4h` score `1.5143` n `91` status `ready` deltaP `18.0113` edge `0.2071` maxDD `-6.9761`
- `market_context_high->metal_24h` score `1.4762` n `90` status `ready` deltaP `24.233` edge `0.1762` maxDD `-3.5466`
- `market_context_high->crypto_alt_24h` score `1.4756` n `90` status `ready` deltaP `10.9189` edge `0.7102` maxDD `-34.5048`
- `news_risk_high->metal_4h` score `1.188` n `49` status `ready` deltaP `18.4482` edge `0.0709` maxDD `-0.993`
- `market_context_high->fx_4h` score `0.5697` n `91` status `ready` deltaP `16.4484` edge `0.0125` maxDD `-0.3077`
- `market_context_high->fx_1h` score `0.5302` n `91` status `ready` deltaP `9.8408` edge `0.0028` maxDD `-0.271`
- `market_context_high->crypto_major_1h` score `0.3395` n `91` status `ready` deltaP `10.892` edge `0.0598` maxDD `-3.7778`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

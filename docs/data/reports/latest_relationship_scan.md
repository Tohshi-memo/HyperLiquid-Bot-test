# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-08T22:07:28.010905+00:00`
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

- `market_context_high->unknown_4h` score `39.8854` n `91` status `ready` deltaP `-3.1392` edge `3.3986` maxDD `-2.3109`
- `news_risk_high->crypto_alt_4h` score `14.2506` n `49` status `ready` deltaP `43.5976` edge `0.8969` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `13.7972` n `49` status `ready` deltaP `45.0038` edge `0.8565` maxDD `-0.2073`
- `news_risk_high->equity_24h` score `9.9078` n `49` status `ready` deltaP `26.3254` edge `0.6601` maxDD `-0.1298`
- `market_context_high->crypto_major_24h` score `8.9466` n `90` status `ready` deltaP `21.9122` edge `1.2983` maxDD `-16.7906`
- `market_context_high->equity_24h` score `7.2393` n `90` status `ready` deltaP `25.5998` edge `0.4755` maxDD `-1.0977`
- `news_risk_high->index_24h` score `6.483` n `49` status `ready` deltaP `46.4471` edge `0.2306` maxDD `0.0`
- `news_risk_high->equity_4h` score `5.9181` n `49` status `ready` deltaP `32.3855` edge `0.2978` maxDD `-0.6421`
- `news_risk_high->index_4h` score `4.5867` n `49` status `ready` deltaP `45.8251` edge `0.0812` maxDD `-0.025`
- `news_risk_high->crypto_major_1h` score `3.0977` n `49` status `ready` deltaP `12.3121` edge `0.2116` maxDD `-1.5096`
- `market_context_high->crypto_alt_24h` score `2.8989` n `90` status `ready` deltaP `13.6145` edge `0.8747` maxDD `-34.5048`
- `news_risk_high->crypto_alt_1h` score `2.6382` n `49` status `ready` deltaP `6.4891` edge `0.2083` maxDD `-1.2034`
- `news_risk_high->index_1h` score `2.4649` n `49` status `ready` deltaP `30.4351` edge `0.0165` maxDD `-0.1194`
- `news_risk_high->commodity_24h` score `2.3327` n `49` status `ready` deltaP `29.8872` edge `0.0036` maxDD `-0.0096`
- `market_context_high->crypto_major_4h` score `1.7688` n `91` status `ready` deltaP `18.3162` edge `0.2377` maxDD `-6.9761`
- `market_context_high->metal_24h` score `1.3937` n `90` status `ready` deltaP `23.4719` edge `0.1707` maxDD `-3.5466`
- `news_risk_high->metal_4h` score `1.2575` n `49` status `ready` deltaP `19.5153` edge `0.0727` maxDD `-0.993`
- `market_context_high->fx_4h` score `0.5929` n `91` status `ready` deltaP `16.7533` edge `0.0124` maxDD `-0.3077`
- `market_context_high->fx_1h` score `0.4763` n `91` status `ready` deltaP `9.242` edge `0.0023` maxDD `-0.271`
- `market_context_high->crypto_major_1h` score `0.3021` n `91` status `ready` deltaP `10.7423` edge `0.056` maxDD `-3.7778`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

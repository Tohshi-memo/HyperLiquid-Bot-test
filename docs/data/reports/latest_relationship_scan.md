# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-09T02:07:29.967690+00:00`
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

- `market_context_high->unknown_4h` score `39.8272` n `91` status `ready` deltaP `-3.5965` edge `3.3968` maxDD `-2.3109`
- `news_risk_high->crypto_alt_4h` score `14.2168` n `47` status `ready` deltaP `43.4451` edge `0.8951` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `13.7395` n `47` status `ready` deltaP `44.3727` edge `0.8559` maxDD `-0.2073`
- `news_risk_high->equity_24h` score `11.111` n `47` status `ready` deltaP `28.7511` edge `0.7442` maxDD `-0.1298`
- `market_context_high->crypto_major_24h` score `9.5371` n `90` status `ready` deltaP `21.9122` edge `1.374` maxDD `-16.7906`
- `market_context_high->equity_24h` score `8.5892` n `90` status `ready` deltaP `28.3728` edge `0.5695` maxDD `-1.0977`
- `news_risk_high->index_24h` score `6.8728` n `47` status `ready` deltaP `49.2201` edge `0.2446` maxDD `0.0`
- `news_risk_high->equity_4h` score `5.8865` n `47` status `ready` deltaP `31.8857` edge `0.2985` maxDD `-0.6421`
- `news_risk_high->index_4h` score `4.5479` n `47` status `ready` deltaP `45.2808` edge `0.0816` maxDD `-0.025`
- `market_context_high->crypto_alt_24h` score `3.3029` n `90` status `ready` deltaP `13.6145` edge `0.9265` maxDD `-34.5048`
- `news_risk_high->crypto_major_1h` score `3.1367` n `47` status `ready` deltaP `12.5143` edge `0.2135` maxDD `-1.5096`
- `news_risk_high->index_1h` score `2.3401` n `47` status `ready` deltaP `29.0547` edge `0.0153` maxDD `-0.1194`
- `news_risk_high->crypto_alt_1h` score `2.2953` n `47` status `ready` deltaP `4.3031` edge `0.1943` maxDD `-1.2034`
- `news_risk_high->commodity_24h` score `2.159` n `47` status `ready` deltaP `29.0203` edge `-0.0051` maxDD `-0.0096`
- `market_context_high->crypto_major_4h` score `1.7131` n `91` status `ready` deltaP `17.8588` edge `0.2336` maxDD `-6.9761`
- `news_risk_high->metal_4h` score `1.2647` n `47` status `ready` deltaP `20.0733` edge `0.0699` maxDD `-0.993`
- `market_context_high->metal_24h` score `1.193` n `90` status `ready` deltaP `20.8723` edge `0.1623` maxDD `-3.5466`
- `market_context_high->fx_4h` score `0.4614` n `91` status `ready` deltaP `15.2289` edge `0.0116` maxDD `-0.3077`
- `market_context_high->fx_1h` score `0.4284` n `91` status `ready` deltaP `8.6432` edge `0.0023` maxDD `-0.271`
- `market_context_high->crypto_major_1h` score `0.2717` n `91` status `ready` deltaP `10.2932` edge `0.0551` maxDD `-3.7778`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

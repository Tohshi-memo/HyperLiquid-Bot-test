# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-09T03:22:34.589418+00:00`
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

- `market_context_high->unknown_4h` score `39.9184` n `91` status `ready` deltaP `-3.5965` edge `3.4044` maxDD `-2.3109`
- `news_risk_high->crypto_alt_4h` score `13.972` n `42` status `ready` deltaP `43.4451` edge `0.8747` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `12.985` n `42` status `ready` deltaP `43.8661` edge `0.7964` maxDD `-0.2073`
- `news_risk_high->equity_24h` score `11.0583` n `42` status `ready` deltaP `28.497` edge `0.7415` maxDD `-0.1298`
- `market_context_high->crypto_major_24h` score `9.7093` n `90` status `ready` deltaP `22.0139` edge `1.3954` maxDD `-16.7906`
- `market_context_high->equity_24h` score `8.9091` n `90` status `ready` deltaP `29.1319` edge `0.5911` maxDD `-1.0977`
- `news_risk_high->index_24h` score `6.892` n `42` status `ready` deltaP `50.0` edge `0.241` maxDD `0.0`
- `news_risk_high->equity_4h` score `6.1902` n `42` status `ready` deltaP `33.101` edge `0.3157` maxDD `-0.6421`
- `news_risk_high->index_4h` score `4.5793` n `42` status `ready` deltaP `45.0275` edge `0.0859` maxDD `-0.025`
- `news_risk_high->crypto_major_1h` score `3.8949` n `42` status `ready` deltaP `17.3867` edge `0.2442` maxDD `-1.5096`
- `market_context_high->crypto_alt_24h` score `3.4302` n `90` status `ready` deltaP `13.5417` edge `0.9433` maxDD `-34.5048`
- `news_risk_high->crypto_alt_1h` score `2.8695` n `42` status `ready` deltaP `6.2304` edge `0.2293` maxDD `-1.2034`
- `news_risk_high->index_1h` score `2.7898` n `42` status `ready` deltaP `33.4688` edge `0.0183` maxDD `-0.0484`
- `news_risk_high->commodity_24h` score `2.2395` n `42` status `ready` deltaP `28.5714` edge `0.0046` maxDD `-0.0096`
- `market_context_high->crypto_major_4h` score `1.7731` n `91` status `ready` deltaP `17.8588` edge `0.2413` maxDD `-6.9761`
- `market_context_high->metal_24h` score `1.1367` n `90` status `ready` deltaP `20.1041` edge `0.1602` maxDD `-3.5466`
- `news_risk_high->metal_4h` score `1.1324` n `42` status `ready` deltaP `18.2491` edge `0.0651` maxDD `-0.993`
- `news_risk_high->metal_1h` score `0.6759` n `42` status `ready` deltaP `13.3875` edge `0.0279` maxDD `-0.44`
- `market_context_high->fx_1h` score `0.4152` n `91` status `ready` deltaP `8.4935` edge `0.0022` maxDD `-0.271`
- `market_context_high->fx_4h` score `0.3932` n `91` status `ready` deltaP `14.4667` edge `0.011` maxDD `-0.3077`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

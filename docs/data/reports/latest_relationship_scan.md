# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-08T22:22:32.393862+00:00`
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

- `market_context_high->unknown_4h` score `39.8636` n `91` status `ready` deltaP `-3.2917` edge `3.3978` maxDD `-2.3109`
- `news_risk_high->crypto_alt_4h` score `14.2036` n `49` status `ready` deltaP `43.4451` edge `0.894` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `13.761` n `49` status `ready` deltaP `44.8513` edge `0.8545` maxDD `-0.2073`
- `news_risk_high->equity_24h` score `9.9888` n `49` status `ready` deltaP `26.4987` edge `0.6657` maxDD `-0.1298`
- `market_context_high->crypto_major_24h` score `8.9731` n `90` status `ready` deltaP `21.9122` edge `1.3017` maxDD `-16.7906`
- `market_context_high->equity_24h` score `7.3204` n `90` status `ready` deltaP `25.7731` edge `0.4811` maxDD `-1.0977`
- `news_risk_high->index_24h` score `6.51` n `49` status `ready` deltaP `46.6205` edge `0.2317` maxDD `0.0`
- `news_risk_high->equity_4h` score `5.9121` n `49` status `ready` deltaP `32.3855` edge `0.2973` maxDD `-0.6421`
- `news_risk_high->index_4h` score `4.5721` n `49` status `ready` deltaP `45.6726` edge `0.081` maxDD `-0.025`
- `news_risk_high->crypto_major_1h` score `3.0834` n `49` status `ready` deltaP `12.1624` edge `0.2114` maxDD `-1.5096`
- `market_context_high->crypto_alt_24h` score `2.9067` n `90` status `ready` deltaP `13.6145` edge `0.8757` maxDD `-34.5048`
- `news_risk_high->crypto_alt_1h` score `2.625` n `49` status `ready` deltaP `6.3394` edge `0.2082` maxDD `-1.2034`
- `news_risk_high->index_1h` score `2.4529` n `49` status `ready` deltaP `30.2854` edge `0.0165` maxDD `-0.1194`
- `news_risk_high->commodity_24h` score `2.3069` n `49` status `ready` deltaP `29.7139` edge `0.0026` maxDD `-0.0096`
- `market_context_high->crypto_major_4h` score `1.7453` n `91` status `ready` deltaP `18.1637` edge `0.2357` maxDD `-6.9761`
- `market_context_high->metal_24h` score `1.3808` n `90` status `ready` deltaP `23.2986` edge `0.1702` maxDD `-3.5466`
- `news_risk_high->metal_4h` score `1.2575` n `49` status `ready` deltaP `19.5153` edge `0.0727` maxDD `-0.993`
- `market_context_high->fx_4h` score `0.5795` n `91` status `ready` deltaP `16.6008` edge `0.0123` maxDD `-0.3077`
- `market_context_high->fx_1h` score `0.4643` n `91` status `ready` deltaP `9.0923` edge `0.0023` maxDD `-0.271`
- `market_context_high->crypto_major_1h` score `0.2927` n `91` status `ready` deltaP `10.5926` edge `0.0558` maxDD `-3.7778`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

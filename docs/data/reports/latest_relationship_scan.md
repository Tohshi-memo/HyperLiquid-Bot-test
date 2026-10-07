# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-07T22:22:31.187364+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8574`

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

- `market_context_high->unknown_4h` score `38.34` n `90` status `ready` deltaP `-5.2371` edge `3.2838` maxDD `-2.3109`
- `news_risk_high->crypto_major_4h` score `10.9633` n `62` status `ready` deltaP `38.7343` edge `0.6757` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `7.0443` n `62` status `ready` deltaP `22.325` edge `0.5726` maxDD `-6.4195`
- `news_risk_high->equity_24h` score `5.0748` n `62` status `ready` deltaP `12.2335` edge `0.3513` maxDD `-0.1298`
- `news_risk_high->index_24h` score `4.4001` n `62` status `ready` deltaP `31.6609` edge `0.1556` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `3.6741` n `90` status `ready` deltaP `9.8731` edge `0.7026` maxDD `-16.7906`
- `news_risk_high->index_4h` score `2.8378` n `62` status `ready` deltaP `31.3926` edge `0.0534` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.5067` n `62` status `ready` deltaP `10.4742` edge `0.1746` maxDD `-1.5096`
- `market_context_high->crypto_major_4h` score `2.4585` n `90` status `ready` deltaP `16.7988` edge `0.1893` maxDD `-4.047`
- `news_risk_high->equity_4h` score `2.0602` n `62` status `ready` deltaP `17.4715` edge `0.115` maxDD `-2.7837`
- `news_risk_high->index_1h` score `1.9241` n `62` status `ready` deltaP `24.2757` edge `0.0135` maxDD `-0.1997`
- `news_risk_high->metal_4h` score `1.5133` n `62` status `ready` deltaP `21.5529` edge `0.0919` maxDD `-0.993`
- `news_risk_high->crypto_alt_1h` score `1.1502` n `62` status `ready` deltaP `3.3079` edge `0.1257` maxDD `-2.4854`
- `news_risk_high->unknown_4h` score `1.1196` n `62` status `ready` deltaP `-8.2121` edge `0.2726` maxDD `-5.6309`
- `market_context_high->metal_24h` score `1.0419` n `90` status `ready` deltaP `20.0807` edge `0.1482` maxDD `-3.5466`
- `market_context_high->fx_4h` score `0.9224` n `90` status `ready` deltaP `20.3015` edge `0.0162` maxDD `-0.3077`
- `market_context_high->fx_1h` score `0.6795` n `90` status `ready` deltaP `11.6467` edge `0.0032` maxDD `-0.271`
- `market_context_high->equity_24h` score `0.5702` n `90` status `ready` deltaP `9.7962` edge `0.0251` maxDD `-1.0977`
- `market_context_high->crypto_major_1h` score `0.1643` n `90` status `ready` deltaP `10.4025` edge `0.0406` maxDD `-3.7778`
- `news_risk_high->metal_1h` score `0.1269` n `62` status `ready` deltaP `6.6013` edge `0.0084` maxDD `-1.0132`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

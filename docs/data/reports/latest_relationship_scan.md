# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-07T22:52:30.107406+00:00`
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

- `market_context_high->unknown_4h` score `38.3412` n `90` status `ready` deltaP `-5.2371` edge `3.2839` maxDD `-2.3109`
- `news_risk_high->crypto_major_4h` score `10.9645` n `62` status `ready` deltaP `38.7343` edge `0.6758` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `7.0275` n `62` status `ready` deltaP `22.325` edge `0.5712` maxDD `-6.4195`
- `news_risk_high->equity_24h` score `5.1973` n `62` status `ready` deltaP `12.5795` edge `0.3592` maxDD `-0.1298`
- `news_risk_high->index_24h` score `4.4446` n `62` status `ready` deltaP `32.0069` edge `0.157` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `3.7767` n `90` status `ready` deltaP `10.0461` edge `0.7146` maxDD `-16.7906`
- `news_risk_high->index_4h` score `2.8256` n `62` status `ready` deltaP `31.2402` edge `0.0534` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.5007` n `62` status `ready` deltaP `10.4742` edge `0.1741` maxDD `-1.5096`
- `market_context_high->crypto_major_4h` score `2.4597` n `90` status `ready` deltaP `16.7988` edge `0.1894` maxDD `-4.047`
- `news_risk_high->equity_4h` score `2.0298` n `62` status `ready` deltaP `17.1666` edge `0.1145` maxDD `-2.7837`
- `news_risk_high->index_1h` score `1.8977` n `62` status `ready` deltaP `23.9763` edge `0.0133` maxDD `-0.1997`
- `news_risk_high->metal_4h` score `1.5117` n `62` status `ready` deltaP `21.5529` edge `0.0917` maxDD `-0.993`
- `news_risk_high->unknown_4h` score `1.1208` n `62` status `ready` deltaP `-8.2121` edge `0.2727` maxDD `-5.6309`
- `news_risk_high->crypto_alt_1h` score `1.0939` n `62` status `ready` deltaP `3.0085` edge `0.123` maxDD `-2.4854`
- `market_context_high->metal_24h` score `1.0606` n `90` status `ready` deltaP `20.0807` edge `0.1506` maxDD `-3.5466`
- `market_context_high->fx_4h` score `0.9236` n `90` status `ready` deltaP `20.3015` edge `0.0163` maxDD `-0.3077`
- `market_context_high->equity_24h` score `0.6927` n `90` status `ready` deltaP `10.1422` edge `0.033` maxDD `-1.0977`
- `market_context_high->fx_1h` score `0.6915` n `90` status `ready` deltaP `11.7964` edge `0.0032` maxDD `-0.271`
- `market_context_high->crypto_major_1h` score `0.1604` n `90` status `ready` deltaP `10.4025` edge `0.0401` maxDD `-3.7778`
- `news_risk_high->metal_1h` score `0.1521` n `62` status `ready` deltaP `6.9007` edge `0.0085` maxDD `-1.0132`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

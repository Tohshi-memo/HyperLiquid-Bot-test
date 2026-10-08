# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-08T01:22:29.179129+00:00`
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

- `market_context_high->unknown_4h` score `38.6052` n `90` status `ready` deltaP `-4.3224` edge `3.2998` maxDD `-2.3109`
- `news_risk_high->crypto_major_4h` score `10.8447` n `62` status `ready` deltaP `37.9721` edge `0.6709` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `6.9241` n `62` status `ready` deltaP `22.1725` edge `0.5636` maxDD `-6.4195`
- `news_risk_high->equity_24h` score `5.8277` n `62` status `ready` deltaP `14.3096` edge `0.4002` maxDD `-0.1298`
- `news_risk_high->index_24h` score `4.673` n `62` status `ready` deltaP `33.737` edge `0.1645` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `4.1573` n `90` status `ready` deltaP `10.0461` edge `0.7634` maxDD `-16.7906`
- `news_risk_high->index_4h` score `2.8948` n `62` status `ready` deltaP `31.8499` edge `0.0551` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.4384` n `62` status `ready` deltaP `10.0251` edge `0.1719` maxDD `-1.5096`
- `market_context_high->crypto_major_4h` score `2.3399` n `90` status `ready` deltaP `16.0366` edge `0.1845` maxDD `-4.047`
- `news_risk_high->equity_4h` score `2.0598` n `62` status `ready` deltaP `17.1666` edge `0.117` maxDD `-2.7837`
- `news_risk_high->index_1h` score `1.9672` n `62` status `ready` deltaP `24.7248` edge `0.0141` maxDD `-0.1997`
- `news_risk_high->metal_4h` score `1.477` n `62` status `ready` deltaP `21.0956` edge `0.0903` maxDD `-0.993`
- `news_risk_high->unknown_4h` score `1.3848` n `62` status `ready` deltaP `-7.2974` edge `0.2886` maxDD `-5.6309`
- `market_context_high->equity_24h` score `1.3231` n `90` status `ready` deltaP `11.8723` edge `0.074` maxDD `-1.0977`
- `market_context_high->metal_24h` score `1.1491` n `90` status `ready` deltaP `20.2537` edge `0.1608` maxDD `-3.5466`
- `news_risk_high->crypto_alt_1h` score `1.022` n `62` status `ready` deltaP `2.4097` edge `0.121` maxDD `-2.4854`
- `market_context_high->fx_4h` score `1.0195` n `90` status `ready` deltaP `21.2161` edge `0.0182` maxDD `-0.3077`
- `market_context_high->fx_1h` score `0.7082` n `90` status `ready` deltaP `11.9461` edge `0.0036` maxDD `-0.271`
- `market_context_high->crypto_major_1h` score `0.1199` n `90` status `ready` deltaP `9.9534` edge `0.0379` maxDD `-3.7778`
- `news_risk_high->metal_1h` score `0.067` n `62` status `ready` deltaP `6.0025` edge `0.0074` maxDD `-1.0132`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

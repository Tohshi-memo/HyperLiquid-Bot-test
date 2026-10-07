# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-07T03:52:35.747464+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8730`

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

- `market_context_high->unknown_24h` score `1330.5342` n `116` status `ready` deltaP `11.2308` edge `110.841` maxDD `-1.3748`
- `market_context_high->unknown_4h` score `29.6191` n `116` status `ready` deltaP `-0.3679` edge `2.5246` maxDD `-2.3109`
- `news_risk_high->crypto_major_4h` score `9.7176` n `62` status `ready` deltaP `34.9233` edge `0.5973` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `6.0335` n `62` status `ready` deltaP `21.1055` edge `0.4965` maxDD `-6.4195`
- `market_context_high->crypto_major_4h` score `3.0787` n `116` status `ready` deltaP `15.4016` edge `0.2503` maxDD `-4.047`
- `news_risk_high->index_24h` score `3.0746` n `62` status `ready` deltaP `21.5278` edge `0.1127` maxDD `0.0`
- `news_risk_high->index_4h` score `2.6728` n `62` status `ready` deltaP `30.0207` edge `0.0488` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.1123` n `62` status `ready` deltaP `7.7796` edge `0.1597` maxDD `-1.5096`
- `news_risk_high->equity_24h` score `1.8904` n `62` status `ready` deltaP `2.9234` edge `0.148` maxDD `-0.1298`
- `news_risk_high->index_1h` score `1.8869` n `62` status `ready` deltaP `23.9763` edge `0.0124` maxDD `-0.1997`
- `news_risk_high->equity_4h` score `1.6552` n `62` status `ready` deltaP `16.0996` edge `0.0904` maxDD `-2.7837`
- `news_risk_high->metal_4h` score `1.2324` n `62` status `ready` deltaP `17.7419` edge `0.0813` maxDD `-0.993`
- `market_context_high->crypto_major_24h` score `1.0705` n `116` status `ready` deltaP `7.154` edge `0.3389` maxDD `-16.7906`
- `market_context_high->crypto_alt_4h` score `0.9968` n `116` status `ready` deltaP `0.6939` edge `0.2508` maxDD `-7.1222`
- `news_risk_high->crypto_alt_1h` score `0.9619` n `62` status `ready` deltaP `2.7091` edge `0.114` maxDD `-2.4854`
- `news_risk_high->commodity_24h` score `0.8982` n `62` status `ready` deltaP `28.9315` edge `0.0789` maxDD `-8.196`
- `market_context_high->fx_4h` score `0.8614` n `116` status `ready` deltaP `19.2231` edge `0.0193` maxDD `-0.3868`
- `market_context_high->fx_1h` score `0.7682` n `116` status `ready` deltaP `13.0807` edge `0.0052` maxDD `-0.271`
- `market_context_high->commodity_4h` score `0.5029` n `116` status `ready` deltaP `12.0164` edge `0.0318` maxDD `-1.6002`
- `market_context_high->commodity_1h` score `0.3037` n `116` status `ready` deltaP `7.9445` edge `0.012` maxDD `-0.5059`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-07T02:23:03.471774+00:00`
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

- `market_context_high->unknown_24h` score `1391.5216` n `117` status `ready` deltaP `11.3782` edge `115.9223` maxDD `-1.3748`
- `market_context_high->unknown_4h` score `29.3057` n `117` status `ready` deltaP `-0.2058` edge `2.4974` maxDD `-2.3109`
- `news_risk_high->crypto_major_4h` score `9.4868` n `62` status `ready` deltaP `34.6184` edge `0.5801` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `5.6873` n `62` status `ready` deltaP `20.6482` edge `0.4707` maxDD `-6.4195`
- `news_risk_high->index_24h` score `3.0408` n `62` status `ready` deltaP `21.1806` edge `0.1122` maxDD `0.0`
- `market_context_high->crypto_major_4h` score `2.742` n `117` status `ready` deltaP `14.4778` edge `0.2284` maxDD `-4.047`
- `news_risk_high->index_4h` score `2.6302` n `62` status `ready` deltaP `29.5634` edge `0.0483` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.0631` n `62` status `ready` deltaP `7.7796` edge `0.1556` maxDD `-1.5096`
- `news_risk_high->equity_24h` score `1.9362` n `62` status `ready` deltaP `3.2706` edge `0.1495` maxDD `-0.1298`
- `news_risk_high->index_1h` score `1.9133` n `62` status `ready` deltaP `24.2757` edge `0.0126` maxDD `-0.1997`
- `news_risk_high->equity_4h` score `1.6132` n `62` status `ready` deltaP `16.0996` edge `0.0869` maxDD `-2.7837`
- `news_risk_high->metal_4h` score `1.1969` n `62` status `ready` deltaP `17.2846` edge `0.0798` maxDD `-0.993`
- `news_risk_high->commodity_24h` score `0.9773` n `62` status `ready` deltaP `29.6259` edge `0.0844` maxDD `-8.196`
- `news_risk_high->crypto_alt_1h` score `0.8983` n `62` status `ready` deltaP `2.7091` edge `0.1087` maxDD `-2.4854`
- `market_context_high->fx_4h` score `0.863` n `117` status `ready` deltaP `19.1982` edge `0.0196` maxDD `-0.3868`
- `market_context_high->fx_1h` score `0.7408` n `117` status `ready` deltaP `12.6926` edge `0.0055` maxDD `-0.271`
- `market_context_high->crypto_major_24h` score `0.6034` n `117` status `ready` deltaP `6.3702` edge `0.3052` maxDD `-16.7906`
- `market_context_high->crypto_alt_4h` score `0.5625` n `117` status `ready` deltaP `-0.2644` edge `0.221` maxDD `-7.1222`
- `market_context_high->commodity_4h` score `0.556` n `117` status `ready` deltaP `12.4857` edge `0.0331` maxDD `-1.6002`
- `market_context_high->commodity_1h` score `0.3535` n `117` status `ready` deltaP `8.4626` edge `0.0127` maxDD `-0.5059`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

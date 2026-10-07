# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-07T02:07:29.779364+00:00`
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

- `market_context_high->unknown_24h` score `1393.3324` n `117` status `ready` deltaP `11.3782` edge `116.0732` maxDD `-1.3748`
- `market_context_high->unknown_4h` score `29.2553` n `117` status `ready` deltaP `-0.2058` edge `2.4932` maxDD `-2.3109`
- `news_risk_high->crypto_major_4h` score `9.4302` n `62` status `ready` deltaP `34.466` edge `0.5764` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `5.6103` n `62` status `ready` deltaP `20.4957` edge `0.4653` maxDD `-6.4195`
- `news_risk_high->index_24h` score `3.0408` n `62` status `ready` deltaP `21.1806` edge `0.1122` maxDD `0.0`
- `market_context_high->crypto_major_4h` score `2.6854` n `117` status `ready` deltaP `14.3254` edge `0.2247` maxDD `-4.047`
- `news_risk_high->index_4h` score `2.629` n `62` status `ready` deltaP `29.5634` edge `0.0482` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.014` n `62` status `ready` deltaP `7.6299` edge `0.1525` maxDD `-1.5096`
- `news_risk_high->equity_24h` score `1.941` n `62` status `ready` deltaP `3.2706` edge `0.1499` maxDD `-0.1298`
- `news_risk_high->index_1h` score `1.9133` n `62` status `ready` deltaP `24.2757` edge `0.0126` maxDD `-0.1997`
- `news_risk_high->equity_4h` score `1.6` n `62` status `ready` deltaP `16.0996` edge `0.0858` maxDD `-2.7837`
- `news_risk_high->metal_4h` score `1.1954` n `62` status `ready` deltaP `17.2846` edge `0.0796` maxDD `-0.993`
- `news_risk_high->commodity_24h` score `0.9804` n `62` status `ready` deltaP `29.6259` edge `0.0848` maxDD `-8.196`
- `market_context_high->fx_4h` score `0.8764` n `117` status `ready` deltaP `19.3507` edge `0.0197` maxDD `-0.3868`
- `news_risk_high->crypto_alt_1h` score `0.8263` n `62` status `ready` deltaP `2.5594` edge `0.1037` maxDD `-2.4854`
- `market_context_high->fx_1h` score `0.7539` n `117` status `ready` deltaP `12.8423` edge `0.0056` maxDD `-0.271`
- `market_context_high->commodity_4h` score `0.5596` n `117` status `ready` deltaP `12.4857` edge `0.0334` maxDD `-1.6002`
- `market_context_high->crypto_major_24h` score `0.5151` n `117` status `ready` deltaP `6.1966` edge `0.299` maxDD `-16.7906`
- `market_context_high->crypto_alt_4h` score `0.4855` n `117` status `ready` deltaP `-0.4169` edge `0.2156` maxDD `-7.1222`
- `market_context_high->commodity_1h` score `0.3391` n `117` status `ready` deltaP `8.3129` edge `0.0125` maxDD `-0.5059`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

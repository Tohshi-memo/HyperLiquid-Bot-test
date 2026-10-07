# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-07T01:08:07.482662+00:00`
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

- `market_context_high->unknown_24h` score `1401.2848` n `117` status `ready` deltaP `11.3782` edge `116.7359` maxDD `-1.3748`
- `market_context_high->unknown_4h` score `29.0849` n `117` status `ready` deltaP `-0.2058` edge `2.479` maxDD `-2.3109`
- `news_risk_high->crypto_major_4h` score `9.3472` n `62` status `ready` deltaP `34.3135` edge `0.5705` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `5.4549` n `62` status `ready` deltaP `20.0384` edge `0.4554` maxDD `-6.4195`
- `news_risk_high->index_24h` score `3.0849` n `62` status `ready` deltaP `21.7014` edge `0.1124` maxDD `0.0`
- `news_risk_high->index_4h` score `2.6424` n `62` status `ready` deltaP `29.7158` edge `0.0483` maxDD `-0.4296`
- `market_context_high->crypto_major_4h` score `2.6024` n `117` status `ready` deltaP `14.1729` edge `0.2188` maxDD `-4.047`
- `news_risk_high->equity_24h` score `2.0234` n `62` status `ready` deltaP `3.7915` edge `0.1533` maxDD `-0.1298`
- `news_risk_high->crypto_major_1h` score `1.9396` n `62` status `ready` deltaP `7.4802` edge `0.1473` maxDD `-1.5096`
- `news_risk_high->index_1h` score `1.9109` n `62` status `ready` deltaP `24.2757` edge `0.0124` maxDD `-0.1997`
- `news_risk_high->equity_4h` score `1.5964` n `62` status `ready` deltaP `16.0996` edge `0.0855` maxDD `-2.7837`
- `news_risk_high->metal_4h` score `1.1961` n `62` status `ready` deltaP `17.2846` edge `0.0797` maxDD `-0.993`
- `news_risk_high->commodity_24h` score `0.9968` n `62` status `ready` deltaP `29.6259` edge `0.0869` maxDD `-8.196`
- `market_context_high->fx_4h` score `0.8776` n `117` status `ready` deltaP `19.3507` edge `0.0198` maxDD `-0.3868`
- `market_context_high->fx_1h` score `0.7132` n `117` status `ready` deltaP `12.3932` edge `0.0052` maxDD `-0.271`
- `news_risk_high->crypto_alt_1h` score `0.6908` n `62` status `ready` deltaP `2.26` edge `0.0944` maxDD `-2.4854`
- `market_context_high->commodity_4h` score `0.5716` n `117` status `ready` deltaP `12.4857` edge `0.0344` maxDD `-1.6002`
- `market_context_high->commodity_1h` score `0.3308` n `117` status `ready` deltaP `8.1632` edge `0.0128` maxDD `-0.5059`
- `market_context_high->crypto_alt_4h` score `0.3301` n `117` status `ready` deltaP `-0.8742` edge `0.2057` maxDD `-7.1222`
- `market_context_high->crypto_major_24h` score `0.252` n `117` status `ready` deltaP `5.5022` edge `0.2817` maxDD `-16.7906`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

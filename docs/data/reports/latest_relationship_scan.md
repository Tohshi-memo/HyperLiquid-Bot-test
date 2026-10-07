# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-07T02:52:35.361697+00:00`
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

- `market_context_high->unknown_24h` score `1387.8412` n `117` status `ready` deltaP `11.3782` edge `115.6156` maxDD `-1.3748`
- `market_context_high->unknown_4h` score `29.3381` n `117` status `ready` deltaP `-0.2058` edge `2.5001` maxDD `-2.3109`
- `news_risk_high->crypto_major_4h` score `9.5734` n `62` status `ready` deltaP `34.7709` edge `0.5863` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `5.8197` n `62` status `ready` deltaP `20.953` edge `0.4797` maxDD `-6.4195`
- `news_risk_high->index_24h` score `3.042` n `62` status `ready` deltaP `21.1806` edge `0.1123` maxDD `0.0`
- `market_context_high->crypto_major_4h` score `2.8286` n `117` status `ready` deltaP `14.6303` edge `0.2346` maxDD `-4.047`
- `news_risk_high->index_4h` score `2.6448` n `62` status `ready` deltaP `29.7158` edge `0.0485` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.1579` n `62` status `ready` deltaP `8.079` edge `0.1615` maxDD `-1.5096`
- `news_risk_high->index_1h` score `1.9385` n `62` status `ready` deltaP `24.5751` edge `0.0127` maxDD `-0.1997`
- `news_risk_high->equity_24h` score `1.9139` n `62` status `ready` deltaP `3.097` edge `0.1488` maxDD `-0.1298`
- `news_risk_high->equity_4h` score `1.6312` n `62` status `ready` deltaP `16.0996` edge `0.0884` maxDD `-2.7837`
- `news_risk_high->metal_4h` score `1.1985` n `62` status `ready` deltaP `17.2846` edge `0.08` maxDD `-0.993`
- `news_risk_high->crypto_alt_1h` score `1.0207` n `62` status `ready` deltaP `3.0085` edge `0.1169` maxDD `-2.4854`
- `news_risk_high->commodity_24h` score `0.9702` n `62` status `ready` deltaP `29.6259` edge `0.0835` maxDD `-8.196`
- `market_context_high->fx_4h` score `0.8606` n `117` status `ready` deltaP `19.1982` edge `0.0194` maxDD `-0.3868`
- `market_context_high->crypto_major_24h` score `0.7716` n `117` status `ready` deltaP `6.7174` edge `0.3169` maxDD `-16.7906`
- `market_context_high->fx_1h` score `0.7384` n `117` status `ready` deltaP `12.6926` edge `0.0053` maxDD `-0.271`
- `market_context_high->crypto_alt_4h` score `0.6949` n `117` status `ready` deltaP `0.0404` edge `0.23` maxDD `-7.1222`
- `market_context_high->commodity_4h` score `0.55` n `117` status `ready` deltaP `12.4857` edge `0.0326` maxDD `-1.6002`
- `market_context_high->commodity_1h` score `0.3655` n `117` status `ready` deltaP `8.6123` edge `0.0127` maxDD `-0.5059`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

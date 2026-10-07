# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-07T00:52:30.530756+00:00`
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

- `market_context_high->unknown_24h` score `1403.3728` n `117` status `ready` deltaP `11.3782` edge `116.9099` maxDD `-1.3748`
- `market_context_high->unknown_4h` score `29.0033` n `117` status `ready` deltaP `-0.2058` edge `2.4722` maxDD `-2.3109`
- `news_risk_high->crypto_major_4h` score `9.3508` n `62` status `ready` deltaP `34.3135` edge `0.5708` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `5.4573` n `62` status `ready` deltaP `20.0384` edge `0.4556` maxDD `-6.4195`
- `news_risk_high->index_24h` score `3.0849` n `62` status `ready` deltaP `21.7014` edge `0.1124` maxDD `0.0`
- `news_risk_high->index_4h` score `2.6558` n `62` status `ready` deltaP `29.8682` edge `0.0484` maxDD `-0.4296`
- `market_context_high->crypto_major_4h` score `2.606` n `117` status `ready` deltaP `14.1729` edge `0.2191` maxDD `-4.047`
- `news_risk_high->equity_24h` score `2.0505` n `62` status `ready` deltaP `3.9651` edge `0.1544` maxDD `-0.1298`
- `news_risk_high->crypto_major_1h` score `1.9624` n `62` status `ready` deltaP `7.6299` edge `0.1482` maxDD `-1.5096`
- `news_risk_high->index_1h` score `1.9109` n `62` status `ready` deltaP `24.2757` edge `0.0124` maxDD `-0.1997`
- `news_risk_high->equity_4h` score `1.6146` n `62` status `ready` deltaP `16.252` edge `0.086` maxDD `-2.7837`
- `news_risk_high->metal_4h` score `1.1969` n `62` status `ready` deltaP `17.2846` edge `0.0798` maxDD `-0.993`
- `news_risk_high->commodity_24h` score `1.0014` n `62` status `ready` deltaP `29.6259` edge `0.0875` maxDD `-8.196`
- `market_context_high->fx_4h` score `0.8776` n `117` status `ready` deltaP `19.3507` edge `0.0198` maxDD `-0.3868`
- `news_risk_high->crypto_alt_1h` score `0.7052` n `62` status `ready` deltaP `2.26` edge `0.0956` maxDD `-2.4854`
- `market_context_high->fx_1h` score `0.7` n `117` status `ready` deltaP `12.2435` edge `0.0051` maxDD `-0.271`
- `market_context_high->commodity_4h` score `0.574` n `117` status `ready` deltaP `12.4857` edge `0.0346` maxDD `-1.6002`
- `market_context_high->commodity_1h` score `0.3439` n `117` status `ready` deltaP `8.3129` edge `0.0129` maxDD `-0.5059`
- `market_context_high->crypto_alt_4h` score `0.3325` n `117` status `ready` deltaP `-0.8742` edge `0.2059` maxDD `-7.1222`
- `market_context_high->crypto_major_24h` score `0.1973` n `117` status `ready` deltaP `5.3286` edge `0.2783` maxDD `-16.7906`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

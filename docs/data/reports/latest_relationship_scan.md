# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-19T21:26:57.489557+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8478`

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

- `news_risk_high->crypto_major_24h` score `51.0824` n `72` status `ready` deltaP `27.0833` edge `4.1655` maxDD `-5.8019`
- `news_risk_high->crypto_alt_24h` score `44.5616` n `72` status `ready` deltaP `33.507` edge `3.628` maxDD `-9.3661`
- `market_context_high->unknown_4h` score `27.7733` n `113` status `ready` deltaP `-4.3101` edge `2.3665` maxDD `-0.5326`
- `news_risk_high->equity_24h` score `8.7395` n `72` status `ready` deltaP `36.9792` edge `0.486` maxDD `-0.0053`
- `market_context_high->commodity_24h` score `7.8986` n `113` status `ready` deltaP `39.9351` edge `0.4445` maxDD `-0.8682`
- `news_risk_high->crypto_alt_4h` score `5.6318` n `98` status `ready` deltaP `21.0085` edge `0.4502` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `4.3761` n `98` status `ready` deltaP `21.9232` edge `0.3443` maxDD `-8.0625`
- `news_risk_high->crypto_alt_1h` score `3.276` n `98` status `ready` deltaP `18.7737` edge `0.1944` maxDD `-2.058`
- `market_context_high->commodity_4h` score `2.8818` n `113` status `ready` deltaP `29.3709` edge `0.085` maxDD `-0.2528`
- `news_risk_high->crypto_major_1h` score `2.4283` n `98` status `ready` deltaP `20.121` edge `0.1205` maxDD `-2.8494`
- `news_risk_high->metal_24h` score `1.705` n `72` status `ready` deltaP `22.3958` edge `0.0772` maxDD `-2.4203`
- `market_context_high->commodity_1h` score `1.5873` n `113` status `ready` deltaP `19.4359` edge `0.0279` maxDD `-0.3491`
- `market_context_high->fx_4h` score `1.0307` n `113` status `ready` deltaP `19.9196` edge `-0.0001` maxDD `-0.0779`
- `news_risk_high->metal_4h` score `0.7711` n `98` status `ready` deltaP `18.5197` edge `0.0462` maxDD `-2.0994`
- `news_risk_high->metal_1h` score `0.6943` n `98` status `ready` deltaP `15.3061` edge `0.016` maxDD `-0.8144`
- `news_risk_high->fx_24h` score `0.4718` n `72` status `ready` deltaP `2.7778` edge `0.039` maxDD `-0.1231`
- `news_risk_high->equity_1h` score `0.4426` n `98` status `ready` deltaP `6.9657` edge `0.031` maxDD `-0.9112`
- `market_context_high->fx_24h` score `0.3386` n `113` status `ready` deltaP `8.8372` edge `-0.0265` maxDD `-0.0027`
- `market_context_high->fx_1h` score `0.1503` n `113` status `ready` deltaP `5.5363` edge `0.0014` maxDD `-0.063`
- `news_risk_high->equity_4h` score `-0.0765` n `98` status `ready` deltaP `8.5988` edge `0.0807` maxDD `-5.2186`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

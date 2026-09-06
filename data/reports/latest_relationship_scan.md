# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-06T16:52:28.240998+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10109`

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

- `risk_on_high->unknown_24h` score `131.5184` n `108` status `ready` deltaP `25.3472` edge `10.8008` maxDD `-0.1262`
- `risk_on_and_context->unknown_24h` score `131.5184` n `108` status `ready` deltaP `25.3472` edge `10.8008` maxDD `-0.1262`
- `risk_on_high->crypto_major_24h` score `14.8704` n `108` status `ready` deltaP `28.7616` edge `1.3022` maxDD `-15.7129`
- `risk_on_and_context->crypto_major_24h` score `14.8704` n `108` status `ready` deltaP `28.7616` edge `1.3022` maxDD `-15.7129`
- `risk_on_high->crypto_alt_24h` score `6.1783` n `108` status `ready` deltaP `17.0139` edge `0.6662` maxDD `-15.5145`
- `risk_on_and_context->crypto_alt_24h` score `6.1783` n `108` status `ready` deltaP `17.0139` edge `0.6662` maxDD `-15.5145`
- `market_context_high->equity_24h` score `4.4173` n `196` status `ready` deltaP `18.3779` edge `0.375` maxDD `-5.6865`
- `market_context_high->crypto_alt_24h` score `3.582` n `196` status `ready` deltaP `16.8439` edge `0.4763` maxDD `-16.8739`
- `risk_on_high->equity_24h` score `2.4396` n `108` status `ready` deltaP `12.5578` edge `0.249` maxDD `-5.6865`
- `risk_on_and_context->equity_24h` score `2.4396` n `108` status `ready` deltaP `12.5578` edge `0.249` maxDD `-5.6865`
- `market_context_high->index_24h` score `0.3836` n `196` status `ready` deltaP `15.9014` edge `0.0813` maxDD `-4.0939`
- `risk_on_high->index_24h` score `0.0611` n `108` status `ready` deltaP `11.5741` edge `0.0519` maxDD `-3.5844`
- `risk_on_and_context->index_24h` score `0.0611` n `108` status `ready` deltaP `11.5741` edge `0.0519` maxDD `-3.5844`
- `risk_on_high->index_1h` score `-0.1601` n `129` status `ready` deltaP `4.1673` edge `-0.0036` maxDD `-0.5764`
- `risk_on_and_context->index_1h` score `-0.1601` n `129` status `ready` deltaP `4.1673` edge `-0.0036` maxDD `-0.5764`
- `risk_on_high->crypto_alt_1h` score `-0.1942` n `129` status `ready` deltaP `3.2261` edge `0.064` maxDD `-5.4685`
- `risk_on_and_context->crypto_alt_1h` score `-0.1942` n `129` status `ready` deltaP `3.2261` edge `0.064` maxDD `-5.4685`
- `risk_on_high->metal_1h` score `-0.338` n `129` status `ready` deltaP `4.6059` edge `-0.003` maxDD `-1.6835`
- `risk_on_and_context->metal_1h` score `-0.338` n `129` status `ready` deltaP `4.6059` edge `-0.003` maxDD `-1.6835`
- `risk_on_high->equity_1h` score `-0.4353` n `129` status `ready` deltaP `6.8561` edge `-0.0143` maxDD `-2.6442`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

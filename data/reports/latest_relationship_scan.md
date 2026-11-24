# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-24T19:07:29.317716+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4092`

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

- `market_context_high->unknown_1h` score `32278.2446` n `45` status `ready` deltaP `1.4171` edge `2689.8537` maxDD `-0.4209`
- `market_context_high->unknown_4h` score `22088.8981` n `45` status `ready` deltaP `3.1776` edge `1840.7342` maxDD `-0.7765`
- `news_risk_high->unknown_1h` score `1043.2897` n `31` status `ready` deltaP `1.6322` edge `86.9475` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `835.9506` n `31` status `ready` deltaP `4.3962` edge `69.6389` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `38.2343` n `31` status `ready` deltaP `50.1736` edge `2.8517` maxDD `0.0`
- `news_risk_high->equity_24h` score `36.3694` n `31` status `ready` deltaP `42.8819` edge `2.7449` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `33.6249` n `31` status `ready` deltaP `48.6111` edge `2.478` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `11.5199` n `31` status `ready` deltaP `25.9982` edge `0.8737` maxDD `-5.2957`
- `news_risk_high->metal_24h` score `11.1026` n `31` status `ready` deltaP `41.2355` edge `0.6778` maxDD `-0.1986`
- `news_risk_high->equity_4h` score `10.0598` n `31` status `ready` deltaP `34.4808` edge `0.6565` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `7.1422` n `31` status `ready` deltaP `17.083` edge `0.9435` maxDD `-7.6714`
- `news_risk_high->fx_24h` score `6.1564` n `31` status `ready` deltaP `51.9545` edge `0.1795` maxDD `-0.0262`
- `news_risk_high->index_24h` score `5.422` n `31` status `ready` deltaP `40.625` edge `0.181` maxDD `0.0`
- `news_risk_high->equity_1h` score `3.4281` n `31` status `ready` deltaP `18.3407` edge `0.1821` maxDD `-0.1621`
- `news_risk_high->index_4h` score `3.0395` n `31` status `ready` deltaP `32.9564` edge `0.0596` maxDD `-0.4146`
- `market_context_high->fx_4h` score `2.7805` n `45` status `ready` deltaP `33.7466` edge `0.0352` maxDD `-0.2774`
- `news_risk_high->crypto_major_1h` score `2.5927` n `31` status `ready` deltaP `11.5076` edge `0.3018` maxDD `-1.6897`
- `news_risk_high->index_1h` score `2.4985` n `31` status `ready` deltaP `29.747` edge `0.0184` maxDD `-0.0136`
- `news_risk_high->crypto_alt_1h` score `2.245` n `31` status `ready` deltaP `11.2082` edge `0.2488` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.6326` n `31` status `ready` deltaP `30.6306` edge `0.033` maxDD `-0.2315`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-29T12:22:24.401281+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11416`

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

- `news_risk_high->unknown_24h` score `49.9254` n `56` status `ready` deltaP `14.9801` edge `4.1151` maxDD `-2.3617`
- `news_risk_high->crypto_alt_24h` score `24.5221` n `56` status `ready` deltaP `36.756` edge `2.0191` maxDD `-14.9839`
- `market_context_high->unknown_24h` score `8.7334` n `108` status `ready` deltaP `18.287` edge `0.6791` maxDD `-3.1917`
- `news_risk_high->unknown_4h` score `6.3401` n `80` status `ready` deltaP `11.4329` edge `0.5111` maxDD `-1.7183`
- `market_context_high->metal_24h` score `4.1388` n `108` status `ready` deltaP `31.3079` edge `0.2381` maxDD `-3.1535`
- `market_context_high->unknown_4h` score `2.7565` n `110` status `ready` deltaP `17.342` edge `0.1548` maxDD `-0.5894`
- `news_risk_high->equity_24h` score `2.742` n `56` status `ready` deltaP `23.9583` edge `0.381` maxDD `-12.4677`
- `news_risk_high->unknown_1h` score `2.7267` n `80` status `ready` deltaP `5.9731` edge `0.2231` maxDD `-0.8558`
- `news_risk_high->fx_4h` score `2.3925` n `80` status `ready` deltaP `34.8171` edge `0.0222` maxDD `-0.3953`
- `news_risk_high->crypto_major_24h` score `2.3488` n `56` status `ready` deltaP `20.3125` edge `0.4056` maxDD `-16.524`
- `news_risk_high->metal_24h` score `1.763` n `56` status `ready` deltaP `37.3264` edge `0.0486` maxDD `-3.7137`
- `news_risk_high->index_24h` score `1.444` n `56` status `ready` deltaP `20.2381` edge `0.0274` maxDD `-1.0255`
- `market_context_high->unknown_1h` score `0.9314` n `122` status `ready` deltaP `8.1452` edge `0.0725` maxDD `-1.6015`
- `news_risk_high->fx_1h` score `0.7735` n `80` status `ready` deltaP `14.6407` edge `0.0057` maxDD `-0.108`
- `news_risk_high->commodity_1h` score `0.4096` n `80` status `ready` deltaP `11.9012` edge `0.0052` maxDD `-0.5618`
- `market_context_high->metal_4h` score `-0.2846` n `110` status `ready` deltaP `7.0704` edge `0.0081` maxDD `-3.3377`
- `news_risk_high->index_1h` score `-0.4066` n `80` status `ready` deltaP `0.0075` edge `-0.0085` maxDD `-0.8275`
- `news_risk_high->index_4h` score `-0.5206` n `80` status `ready` deltaP `2.0732` edge `-0.0164` maxDD `-1.7996`
- `market_context_high->crypto_major_4h` score `-0.5543` n `110` status `ready` deltaP `14.9972` edge `0.1989` maxDD `-20.9394`
- `market_context_high->commodity_1h` score `-0.6132` n `122` status `ready` deltaP `-2.2381` edge `0.0073` maxDD `-1.6796`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-29T12:07:27.260210+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11440`

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

- `news_risk_high->unknown_24h` score `49.8371` n `56` status `ready` deltaP `14.8065` edge `4.1089` maxDD `-2.3617`
- `news_risk_high->crypto_alt_24h` score `24.4482` n `56` status `ready` deltaP `36.5824` edge `2.0141` maxDD `-14.9839`
- `market_context_high->unknown_24h` score `8.6451` n `108` status `ready` deltaP `18.1134` edge `0.6729` maxDD `-3.1917`
- `news_risk_high->unknown_4h` score `6.3267` n `80` status `ready` deltaP `11.2805` edge `0.511` maxDD `-1.7183`
- `market_context_high->metal_24h` score `4.1069` n `108` status `ready` deltaP `31.1343` edge `0.2366` maxDD `-3.1535`
- `market_context_high->unknown_4h` score `2.8697` n `109` status `ready` deltaP `17.9319` edge `0.1603` maxDD `-0.5894`
- `news_risk_high->unknown_1h` score `2.7231` n `80` status `ready` deltaP `5.9731` edge `0.2228` maxDD `-0.8558`
- `news_risk_high->equity_24h` score `2.708` n `56` status `ready` deltaP `23.7847` edge `0.3778` maxDD `-12.4677`
- `news_risk_high->fx_4h` score `2.3925` n `80` status `ready` deltaP `34.8171` edge `0.0222` maxDD `-0.3953`
- `news_risk_high->crypto_major_24h` score `2.2922` n `56` status `ready` deltaP `20.1389` edge `0.3995` maxDD `-16.524`
- `news_risk_high->metal_24h` score `1.7422` n `56` status `ready` deltaP `37.1528` edge `0.0471` maxDD `-3.7137`
- `news_risk_high->index_24h` score `1.4265` n `56` status `ready` deltaP `20.0645` edge `0.0271` maxDD `-1.0255`
- `market_context_high->unknown_1h` score `0.9245` n `121` status `ready` deltaP `7.8946` edge `0.0736` maxDD `-1.6015`
- `news_risk_high->fx_1h` score `0.7735` n `80` status `ready` deltaP `14.6407` edge `0.0057` maxDD `-0.108`
- `news_risk_high->commodity_1h` score `0.4096` n `80` status `ready` deltaP `11.9012` edge `0.0052` maxDD `-0.5618`
- `market_context_high->metal_4h` score `-0.3018` n `109` status `ready` deltaP `6.7535` edge `0.008` maxDD `-3.3377`
- `news_risk_high->index_1h` score `-0.4066` n `80` status `ready` deltaP `0.0075` edge `-0.0085` maxDD `-0.8275`
- `news_risk_high->index_4h` score `-0.5206` n `80` status `ready` deltaP `2.0732` edge `-0.0164` maxDD `-1.7996`
- `market_context_high->crypto_major_4h` score `-0.5579` n `109` status `ready` deltaP `14.8327` edge `0.1997` maxDD `-20.9394`
- `market_context_high->commodity_1h` score `-0.6362` n `121` status `ready` deltaP `-2.6649` edge `0.0072` maxDD `-1.6796`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-29T12:37:32.481644+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11392`

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

- `news_risk_high->unknown_24h` score `50.0148` n `56` status `ready` deltaP `15.1538` edge `4.1214` maxDD `-2.3617`
- `news_risk_high->crypto_alt_24h` score `24.584` n `56` status `ready` deltaP `36.9296` edge `2.0231` maxDD `-14.9839`
- `market_context_high->unknown_24h` score `8.8229` n `108` status `ready` deltaP `18.4607` edge `0.6854` maxDD `-3.1917`
- `news_risk_high->unknown_4h` score `6.3643` n `80` status `ready` deltaP `11.5854` edge `0.5121` maxDD `-1.7183`
- `market_context_high->metal_24h` score `4.1695` n `108` status `ready` deltaP `31.4815` edge `0.2395` maxDD `-3.1535`
- `news_risk_high->equity_24h` score `2.776` n `56` status `ready` deltaP `24.1319` edge `0.3842` maxDD `-12.4677`
- `news_risk_high->unknown_1h` score `2.7231` n `80` status `ready` deltaP `5.9731` edge `0.2228` maxDD `-0.8558`
- `market_context_high->unknown_4h` score `2.5762` n `111` status `ready` deltaP `16.7656` edge `0.1461` maxDD `-0.788`
- `news_risk_high->crypto_major_24h` score `2.4` n `56` status `ready` deltaP `20.4861` edge `0.411` maxDD `-16.524`
- `news_risk_high->fx_4h` score `2.3925` n `80` status `ready` deltaP `34.8171` edge `0.0222` maxDD `-0.3953`
- `news_risk_high->metal_24h` score `1.7829` n `56` status `ready` deltaP `37.5` edge `0.05` maxDD `-3.7137`
- `news_risk_high->index_24h` score `1.4615` n `56` status `ready` deltaP `20.4117` edge `0.0277` maxDD `-1.0255`
- `market_context_high->unknown_1h` score `0.9463` n `123` status `ready` deltaP `8.3918` edge `0.0721` maxDD `-1.6015`
- `news_risk_high->fx_1h` score `0.7735` n `80` status `ready` deltaP `14.6407` edge `0.0057` maxDD `-0.108`
- `news_risk_high->commodity_1h` score `0.4096` n `80` status `ready` deltaP `11.9012` edge `0.0052` maxDD `-0.5618`
- `market_context_high->metal_4h` score `-0.3073` n `111` status `ready` deltaP `6.6332` edge `0.0081` maxDD `-3.3377`
- `news_risk_high->index_1h` score `-0.3988` n `80` status `ready` deltaP `0.1572` edge `-0.0085` maxDD `-0.8275`
- `news_risk_high->index_4h` score `-0.5206` n `80` status `ready` deltaP `2.0732` edge `-0.0164` maxDD `-1.7996`
- `market_context_high->crypto_major_4h` score `-0.5596` n `111` status `ready` deltaP `15.156` edge `0.1974` maxDD `-20.9394`
- `market_context_high->commodity_1h` score `-0.5914` n `123` status `ready` deltaP `-1.8183` edge `0.0073` maxDD `-1.6796`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

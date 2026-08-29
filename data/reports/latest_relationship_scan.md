# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-29T14:22:28.968172+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11444`

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

- `news_risk_high->unknown_24h` score `49.449` n `57` status `ready` deltaP `14.8026` edge `4.0847` maxDD `-2.6776`
- `news_risk_high->crypto_alt_24h` score `23.9838` n `57` status `ready` deltaP `36.1202` edge `1.9942` maxDD `-15.9083`
- `market_context_high->unknown_24h` score `8.0681` n `104` status `ready` deltaP `19.391` edge `0.6163` maxDD `-3.1917`
- `news_risk_high->unknown_4h` score `6.3739` n `80` status `ready` deltaP `11.5854` edge `0.5129` maxDD `-1.7183`
- `market_context_high->metal_24h` score `4.3957` n `104` status `ready` deltaP `31.9845` edge `0.255` maxDD `-3.1535`
- `news_risk_high->unknown_1h` score `2.6463` n `80` status `ready` deltaP `5.524` edge `0.2194` maxDD `-0.8558`
- `news_risk_high->equity_24h` score `2.619` n `57` status `ready` deltaP `24.0314` edge `0.3793` maxDD `-13.6328`
- `news_risk_high->fx_4h` score `2.4558` n `80` status `ready` deltaP `35.5793` edge `0.0224` maxDD `-0.3953`
- `market_context_high->unknown_4h` score `2.4284` n `114` status `ready` deltaP `17.2872` edge `0.1303` maxDD `-0.788`
- `news_risk_high->crypto_major_24h` score `2.2319` n `57` status `ready` deltaP `20.3856` edge `0.4097` maxDD `-17.7572`
- `news_risk_high->metal_24h` score `1.6783` n `57` status `ready` deltaP `37.1802` edge `0.0498` maxDD `-4.2666`
- `market_context_high->unknown_1h` score `1.1282` n `126` status `ready` deltaP `9.4526` edge `0.0791` maxDD `-1.5148`
- `news_risk_high->index_24h` score `0.8797` n `57` status `ready` deltaP `20.2486` edge `0.0261` maxDD `-1.198`
- `news_risk_high->fx_1h` score `0.7723` n `80` status `ready` deltaP `14.6407` edge `0.0056` maxDD `-0.108`
- `news_risk_high->commodity_1h` score `0.3917` n `80` status `ready` deltaP `11.6018` edge `0.0049` maxDD `-0.5618`
- `market_context_high->crypto_major_4h` score `-0.2194` n `114` status `ready` deltaP `17.7738` edge `0.2083` maxDD `-20.9394`
- `market_context_high->metal_4h` score `-0.3362` n `114` status `ready` deltaP `6.1083` edge `0.0079` maxDD `-3.3377`
- `news_risk_high->index_1h` score `-0.391` n `80` status `ready` deltaP `0.3069` edge `-0.0085` maxDD `-0.8275`
- `market_context_high->commodity_1h` score `-0.4803` n `126` status `ready` deltaP `-0.1045` edge `0.0085` maxDD `-1.5507`
- `news_risk_high->index_4h` score `-0.5364` n `80` status `ready` deltaP `1.7683` edge `-0.0164` maxDD `-1.7996`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

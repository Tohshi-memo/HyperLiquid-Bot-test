# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-09T11:52:30.541092+00:00`
- Price records: `672`
- Market context records: `6180`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11132`

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

- `news_risk_high->crypto_alt_24h` score `12.6638` n `32` status `ready` deltaP `42.3848` edge `0.7875` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `7.1146` n `32` status `ready` deltaP `62.4573` edge `0.1765` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.0057` n `32` status `ready` deltaP `41.6856` edge `0.0605` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.3332` n `32` status `ready` deltaP `28.1437` edge `0.0207` maxDD `-0.1113`
- `news_risk_high->crypto_major_24h` score `1.8645` n `32` status `ready` deltaP `15.7956` edge `0.2117` maxDD `-4.2368`
- `market_context_high->unknown_1h` score `1.8264` n `193` status `ready` deltaP `1.352` edge `0.244` maxDD `-3.7317`
- `news_risk_high->crypto_major_1h` score `1.301` n `32` status `ready` deltaP `13.5292` edge `0.1233` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.6892` n `32` status `ready` deltaP `8.7762` edge `0.076` maxDD `-1.6923`
- `market_context_high->unknown_4h` score `0.4336` n `193` status `ready` deltaP `-1.026` edge `0.2962` maxDD `-11.925`
- `market_context_high->metal_24h` score `0.1108` n `193` status `ready` deltaP `20.1967` edge `0.1364` maxDD `-11.8809`
- `news_risk_high->index_24h` score `-0.104` n `32` status `ready` deltaP `9.663` edge `0.0094` maxDD `-2.3058`
- `market_context_high->equity_4h` score `-0.1042` n `193` status `ready` deltaP `2.6158` edge `0.0656` maxDD `-2.671`
- `market_context_high->fx_1h` score `-0.2863` n `193` status `ready` deltaP `1.3302` edge `-0.001` maxDD `-0.5659`
- `news_risk_high->commodity_24h` score `-0.3502` n `32` status `ready` deltaP `14.4091` edge `-0.1047` maxDD `-0.3101`
- `market_context_high->metal_4h` score `-0.6666` n `193` status `ready` deltaP `3.6129` edge `0.0092` maxDD `-3.4996`
- `market_context_high->commodity_1h` score `-0.7845` n `193` status `ready` deltaP `-2.4355` edge `-0.0045` maxDD `-0.5708`
- `news_risk_high->metal_1h` score `-0.7909` n `32` status `ready` deltaP `-3.2934` edge `-0.0297` maxDD `-1.6464`
- `market_context_high->metal_1h` score `-0.9001` n `193` status `ready` deltaP `1.6289` edge `-0.006` maxDD `-2.0564`
- `market_context_high->crypto_alt_1h` score `-0.955` n `193` status `ready` deltaP `3.2872` edge `0.0309` maxDD `-9.3536`
- `market_context_high->crypto_major_1h` score `-0.9742` n `193` status `ready` deltaP `3.8627` edge `0.0261` maxDD `-9.807`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

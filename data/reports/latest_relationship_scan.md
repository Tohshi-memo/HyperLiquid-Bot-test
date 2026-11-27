# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-27T18:52:27.196880+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `2886`

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

- `news_risk_high->unknown_1h` score `3289.4259` n `31` status `ready` deltaP `1.6201` edge `274.1256` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3186.7209` n `31` status `ready` deltaP `3.3191` edge `265.5436` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `16.2991` n `31` status `ready` deltaP `25.8232` edge `1.1861` maxDD `0.0`
- `news_risk_high->equity_24h` score `12.7385` n `31` status `ready` deltaP `23.9168` edge `0.9021` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `11.9459` n `31` status `ready` deltaP `25.3033` edge `0.8268` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `8.0778` n `31` status `ready` deltaP `20.8916` edge `0.6209` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `5.5017` n `31` status `ready` deltaP `29.9897` edge `0.3066` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `4.9689` n `31` status `ready` deltaP `13.3451` edge `0.6898` maxDD `-7.6714`
- `news_risk_high->fx_24h` score `4.6526` n `31` status `ready` deltaP `38.6762` edge `0.1427` maxDD `-0.0262`
- `news_risk_high->metal_24h` score `3.8012` n `31` status `ready` deltaP `12.1877` edge `0.263` maxDD `-0.1986`
- `news_risk_high->index_4h` score `2.3741` n `31` status `ready` deltaP `29.2287` edge `0.029` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.2604` n `31` status `ready` deltaP `27.7304` edge `0.012` maxDD `-0.0136`
- `news_risk_high->index_24h` score `2.2539` n `31` status `ready` deltaP `24.7834` edge `0.0226` maxDD `0.0`
- `news_risk_high->equity_1h` score `2.2362` n `31` status `ready` deltaP `15.1261` edge `0.1042` maxDD `-0.1621`
- `news_risk_high->crypto_major_1h` score `1.8649` n `31` status `ready` deltaP `6.0466` edge `0.2449` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.6641` n `31` status `ready` deltaP `8.5877` edge `0.1918` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.1488` n `31` status `ready` deltaP `24.8661` edge `0.0094` maxDD `-0.2315`
- `news_risk_high->commodity_4h` score `0.4001` n `31` status `ready` deltaP `10.1193` edge `0.0236` maxDD `-0.5151`
- `news_risk_high->metal_4h` score `0.3821` n `31` status `ready` deltaP `11.823` edge `0.0259` maxDD `-0.7918`
- `news_risk_high->commodity_1h` score `-0.3459` n `31` status `ready` deltaP `-1.9866` edge `0.0106` maxDD `-0.0947`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

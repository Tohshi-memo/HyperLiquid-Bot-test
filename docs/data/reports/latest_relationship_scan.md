# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-27T05:37:26.516749+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3564`

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

- `news_risk_high->unknown_1h` score `3218.7961` n `31` status `ready` deltaP `1.6322` edge `268.2397` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3186.085` n `31` status `ready` deltaP `3.7864` edge `265.4875` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `23.0661` n `31` status `ready` deltaP `32.2917` edge `1.7069` maxDD `0.0`
- `news_risk_high->equity_24h` score `20.6377` n `31` status `ready` deltaP `31.7708` edge `1.508` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `17.5307` n `31` status `ready` deltaP `31.4236` edge `1.2514` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `9.2006` n `31` status `ready` deltaP `23.4067` edge `0.6977` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `7.2726` n `31` status `ready` deltaP `32.9564` edge `0.4344` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `5.92` n `31` status `ready` deltaP `16.3208` edge `0.7919` maxDD `-7.6714`
- `news_risk_high->metal_24h` score `5.7468` n `31` status `ready` deltaP `19.7077` edge `0.375` maxDD `-0.1986`
- `news_risk_high->fx_24h` score `4.7256` n `31` status `ready` deltaP `39.4545` edge `0.1436` maxDD `-0.0262`
- `news_risk_high->index_24h` score `3.6603` n `31` status `ready` deltaP `33.3333` edge `0.0828` maxDD `0.0`
- `news_risk_high->index_4h` score `2.7232` n `31` status `ready` deltaP `31.432` edge `0.0434` maxDD `-0.4146`
- `news_risk_high->equity_1h` score `2.676` n `31` status `ready` deltaP `16.5443` edge `0.1314` maxDD `-0.1621`
- `news_risk_high->index_1h` score `2.3847` n `31` status `ready` deltaP `28.8488` edge `0.0149` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.0854` n `31` status `ready` deltaP `6.8669` edge `0.2677` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.8785` n `31` status `ready` deltaP `10.0106` edge `0.2098` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.1862` n `31` status `ready` deltaP `25.5408` edge `0.0097` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `0.4631` n `31` status `ready` deltaP `12.5098` edge `0.0317` maxDD `-0.7918`
- `news_risk_high->commodity_4h` score `-0.0146` n `31` status `ready` deltaP `6.5401` edge `-0.0057` maxDD `-0.5151`
- `news_risk_high->commodity_1h` score `-0.6407` n `31` status `ready` deltaP `-4.7566` edge `0.0045` maxDD `-0.0947`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

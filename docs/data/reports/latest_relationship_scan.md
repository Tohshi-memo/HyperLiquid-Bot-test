# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-31T11:22:26.630552+00:00`
- Price records: `672`
- Market context records: `8510`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5882`

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

- `news_risk_high->unknown_24h` score `6276.1617` n `52` status `ready` deltaP `44.7383` edge `522.7573` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `5.7936` n `64` status `ready` deltaP `21.5701` edge `0.3987` maxDD `-3.4427`
- `news_risk_high->index_4h` score `1.9951` n `64` status `ready` deltaP `16.5015` edge `0.0753` maxDD `-0.191`
- `news_risk_high->equity_1h` score `1.7134` n `64` status `ready` deltaP `15.8028` edge `0.0851` maxDD `-2.4803`
- `news_risk_high->crypto_major_4h` score `0.8986` n `64` status `ready` deltaP `5.8308` edge `0.1539` maxDD `-3.5385`
- `news_risk_high->crypto_alt_4h` score `0.8178` n `64` status `ready` deltaP `14.3293` edge `0.1485` maxDD `-5.8012`
- `news_risk_high->crypto_alt_1h` score `0.5692` n `64` status `ready` deltaP `9.3095` edge `0.0636` maxDD `-1.8813`
- `market_context_high->equity_1h` score `0.448` n `38` status `ready` deltaP `2.8916` edge `0.0472` maxDD `-0.9985`
- `news_risk_high->crypto_major_1h` score `0.3415` n `64` status `ready` deltaP `6.6149` edge `0.0509` maxDD `-2.0972`
- `market_context_high->index_1h` score `0.2` n `38` status `ready` deltaP `6.9335` edge `-0.0009` maxDD `-0.2417`
- `news_risk_high->fx_1h` score `0.1095` n `64` status `ready` deltaP `5.7354` edge `0.0039` maxDD `-0.2475`
- `news_risk_high->index_1h` score `0.0387` n `64` status `ready` deltaP `4.2197` edge `0.0085` maxDD `-0.5338`
- `news_risk_high->fx_4h` score `0.012` n `64` status `ready` deltaP `11.3186` edge `0.0213` maxDD `-0.6604`
- `market_context_high->crypto_major_1h` score `-0.0553` n `38` status `ready` deltaP `6.6971` edge `-0.002` maxDD `-1.9791`
- `news_risk_high->metal_4h` score `-0.0682` n `64` status `ready` deltaP `1.1052` edge `0.0315` maxDD `-0.8085`
- `market_context_high->metal_1h` score `-0.0914` n `38` status `ready` deltaP `4.751` edge `-0.0066` maxDD `-0.6101`
- `market_context_high->commodity_1h` score `-0.1208` n `38` status `ready` deltaP `7.0596` edge `0.0` maxDD `-2.0038`
- `news_risk_high->metal_1h` score `-0.1419` n `64` status `ready` deltaP `3.1063` edge `0.0078` maxDD `-0.5599`
- `market_context_high->crypto_alt_1h` score `-0.6022` n `38` status `ready` deltaP `-6.3977` edge `0.0156` maxDD `-2.012`
- `market_context_high->fx_1h` score `-0.7065` n `38` status `ready` deltaP `-6.8468` edge `0.0016` maxDD `-0.3888`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-20T15:37:39.400323+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `24`

- Symbol pattern count: `2680`

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

- `market_context_high->unknown_1h` score `10177.0228` n `126` status `ready` deltaP `2.0626` edge `848.0913` maxDD `-0.9188`
- `market_context_high->unknown_4h` score `6615.9081` n `120` status `ready` deltaP `1.2601` edge `551.3457` maxDD `-0.6076`
- `market_context_high->crypto_major_24h` score `4.7833` n `107` status `ready` deltaP `27.4257` edge `1.1434` maxDD `-50.7065`
- `market_context_high->crypto_alt_24h` score `1.5851` n `107` status `ready` deltaP `14.3156` edge `0.9487` maxDD `-66.63`
- `market_context_high->metal_4h` score `-0.0592` n `120` status `ready` deltaP `14.4817` edge `0.0476` maxDD `-7.8056`
- `market_context_high->metal_1h` score `-0.1719` n `126` status `ready` deltaP `4.4007` edge `0.0151` maxDD `-2.6517`
- `market_context_high->index_1h` score `-0.3256` n `126` status `ready` deltaP `2.7088` edge `0.0014` maxDD `-1.2295`
- `market_context_high->crypto_major_4h` score `-1.1385` n `120` status `ready` deltaP `1.8699` edge `0.2426` maxDD `-25.7488`
- `market_context_high->fx_1h` score `-1.3064` n `126` status `ready` deltaP `-7.7583` edge `-0.0012` maxDD `-0.4757`
- `market_context_high->crypto_alt_4h` score `-1.8841` n `120` status `ready` deltaP `2.937` edge `0.1615` maxDD `-27.8101`
- `market_context_high->index_4h` score `-1.9827` n `120` status `ready` deltaP `-2.6118` edge `-0.0105` maxDD `-4.9851`
- `market_context_high->fx_4h` score `-2.0176` n `120` status `ready` deltaP `-8.5772` edge `0.0001` maxDD `-1.794`
- `market_context_high->equity_1h` score `-2.0483` n `126` status `ready` deltaP `5.5389` edge `-0.0017` maxDD `-13.1399`
- `market_context_high->commodity_1h` score `-2.051` n `126` status `ready` deltaP `-6.1259` edge `-0.0169` maxDD `-4.3877`
- `market_context_high->crypto_major_1h` score `-2.5758` n `126` status `ready` deltaP `2.2597` edge `0.0021` maxDD `-13.8788`
- `market_context_high->crypto_alt_1h` score `-3.1644` n `126` status `ready` deltaP `-3.2958` edge `-0.014` maxDD `-13.8848`
- `market_context_high->metal_24h` score `-5.8582` n `107` status `ready` deltaP `13.2139` edge `0.0967` maxDD `-43.8379`
- `market_context_high->fx_24h` score `-6.6607` n `107` status `ready` deltaP `-17.7521` edge `-0.0094` maxDD `-5.5179`
- `market_context_high->commodity_4h` score `-6.9929` n `120` status `ready` deltaP `-21.1585` edge `-0.0724` maxDD `-15.5426`
- `market_context_high->equity_4h` score `-11.3943` n `120` status `ready` deltaP `-5.6911` edge `-0.1106` maxDD `-53.7455`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

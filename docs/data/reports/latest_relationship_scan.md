# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-09T23:07:28.169457+00:00`
- Price records: `672`
- Market context records: `6226`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11110`

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

- `news_risk_high->crypto_alt_24h` score `13.4198` n `32` status `ready` deltaP `42.2194` edge `0.8516` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `6.3938` n `32` status `ready` deltaP `54.932` edge `0.1666` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.1659` n `32` status `ready` deltaP `43.6738` edge `0.0606` maxDD `-0.0345`
- `news_risk_high->crypto_major_24h` score `2.6669` n `32` status `ready` deltaP `15.625` edge `0.3157` maxDD `-4.2368`
- `news_risk_high->fx_1h` score `2.3452` n `32` status `ready` deltaP `28.2934` edge `0.0207` maxDD `-0.1113`
- `market_context_high->unknown_1h` score `2.1007` n `192` status `ready` deltaP `2.5605` edge `0.2588` maxDD `-3.7317`
- `news_risk_high->commodity_24h` score `1.4959` n `32` status `ready` deltaP `21.96` edge `-0.0012` maxDD `-0.3101`
- `news_risk_high->crypto_major_1h` score `1.3751` n `32` status `ready` deltaP `14.128` edge `0.1288` maxDD `-2.0691`
- `market_context_high->unknown_4h` score `0.9549` n `192` status `ready` deltaP `-1.0798` edge `0.34` maxDD `-11.925`
- `news_risk_high->crypto_alt_1h` score `0.7514` n `32` status `ready` deltaP `9.9738` edge `0.076` maxDD `-1.6923`
- `market_context_high->metal_24h` score `-0.0486` n `192` status `ready` deltaP `19.8023` edge `0.1186` maxDD `-11.8809`
- `news_risk_high->index_24h` score `-0.2073` n `32` status `ready` deltaP `8.801` edge `0.0019` maxDD `-2.3058`
- `market_context_high->fx_1h` score `-0.2926` n `192` status `ready` deltaP `1.2101` edge `-0.001` maxDD `-0.5659`
- `market_context_high->commodity_1h` score `-0.5679` n `192` status `ready` deltaP `-0.7485` edge `0.0023` maxDD `-0.5708`
- `market_context_high->metal_4h` score `-0.6008` n `192` status `ready` deltaP `4.1286` edge `0.0142` maxDD `-3.4996`
- `news_risk_high->metal_1h` score `-0.8135` n `32` status `ready` deltaP `-4.0419` edge `-0.0276` maxDD `-1.6464`
- `market_context_high->metal_1h` score `-0.9107` n `192` status `ready` deltaP `1.1664` edge `-0.0038` maxDD `-2.0564`
- `market_context_high->crypto_alt_1h` score `-0.9123` n `192` status `ready` deltaP `4.2446` edge `0.03` maxDD `-9.3536`
- `market_context_high->crypto_major_1h` score `-0.9246` n `192` status `ready` deltaP `4.2322` edge `0.03` maxDD `-9.807`
- `market_context_high->equity_4h` score `-0.9316` n `192` status `ready` deltaP `1.753` edge `0.0024` maxDD `-2.671`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

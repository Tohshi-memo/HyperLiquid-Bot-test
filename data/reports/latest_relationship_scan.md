# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-08T18:07:30.760597+00:00`
- Price records: `672`
- Market context records: `6111`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11131`

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

- `news_risk_high->crypto_alt_24h` score `8.7784` n `30` status `ready` deltaP `36.0416` edge `0.506` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `8.0128` n `30` status `ready` deltaP `71.1806` edge `0.1932` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.1849` n `32` status `ready` deltaP `43.5213` edge `0.0632` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.2913` n `32` status `ready` deltaP `27.5449` edge `0.0212` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `1.2597` n `32` status `ready` deltaP `13.6789` edge `0.117` maxDD `-2.0691`
- `market_context_high->equity_4h` score `1.0118` n `195` status `ready` deltaP `6.9512` edge `0.1297` maxDD `-2.671`
- `news_risk_high->crypto_alt_1h` score `0.647` n `32` status `ready` deltaP `8.9259` edge `0.0696` maxDD `-1.6923`
- `news_risk_high->index_24h` score `0.0415` n `30` status `ready` deltaP `9.2361` edge `0.0309` maxDD `-2.3058`
- `market_context_high->fx_1h` score `-0.3408` n `195` status `ready` deltaP `0.2372` edge `-0.0007` maxDD `-0.5659`
- `news_risk_high->commodity_24h` score `-0.3803` n `30` status `ready` deltaP `14.6181` edge `-0.1086` maxDD `-0.3101`
- `market_context_high->metal_4h` score `-0.6146` n `195` status `ready` deltaP `3.847` edge `0.0143` maxDD `-3.4996`
- `market_context_high->commodity_1h` score `-0.6697` n `195` status `ready` deltaP `-1.2406` edge `-0.0029` maxDD `-0.5708`
- `market_context_high->equity_1h` score `-0.6856` n `195` status `ready` deltaP `0.6387` edge `0.0194` maxDD `-4.2573`
- `news_risk_high->metal_1h` score `-0.745` n `32` status `ready` deltaP `-2.5449` edge `-0.0288` maxDD `-1.6464`
- `market_context_high->metal_1h` score `-0.7805` n `195` status `ready` deltaP `2.8397` edge `-0.0041` maxDD `-2.0564`
- `market_context_high->index_4h` score `-0.8774` n `195` status `ready` deltaP `1.8511` edge `0.0216` maxDD `-1.381`
- `market_context_high->crypto_alt_1h` score `-0.9289` n `195` status `ready` deltaP `3.9099` edge `0.0301` maxDD `-9.3536`
- `market_context_high->crypto_major_1h` score `-0.9383` n `195` status `ready` deltaP `4.4642` edge `0.0267` maxDD `-9.807`
- `news_risk_high->index_1h` score `-1.1264` n `32` status `ready` deltaP `-10.1235` edge `-0.0206` maxDD `-1.1725`
- `market_context_high->index_1h` score `-1.2599` n `195` status `ready` deltaP `-3.0562` edge `0.0023` maxDD `-0.9531`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

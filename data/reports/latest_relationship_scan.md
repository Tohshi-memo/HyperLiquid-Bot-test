# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-09T14:07:30.786695+00:00`
- Price records: `672`
- Market context records: `6188`
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

- `news_risk_high->crypto_alt_24h` score `12.647` n `32` status `ready` deltaP `42.2194` edge `0.7872` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `6.9664` n `32` status `ready` deltaP `61.0544` edge `0.1735` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.0703` n `32` status `ready` deltaP `42.4487` edge `0.0608` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.3464` n `32` status `ready` deltaP `28.2934` edge `0.0208` maxDD `-0.1113`
- `news_risk_high->crypto_major_24h` score `2.0242` n `32` status `ready` deltaP `15.625` edge `0.2333` maxDD `-4.2368`
- `market_context_high->unknown_1h` score `1.8201` n `192` status `ready` deltaP `0.9138` edge `0.2464` maxDD `-3.7317`
- `news_risk_high->crypto_major_1h` score `1.3564` n `32` status `ready` deltaP `13.9783` edge `0.1274` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.7102` n `32` status `ready` deltaP `9.0756` edge `0.0767` maxDD `-1.6923`
- `market_context_high->unknown_4h` score `0.4023` n `192` status `ready` deltaP `-1.5214` edge `0.2969` maxDD `-11.925`
- `market_context_high->metal_24h` score `0.0614` n `192` status `ready` deltaP `19.8023` edge `0.1327` maxDD `-11.8809`
- `news_risk_high->commodity_24h` score `-0.0919` n `32` status `ready` deltaP `15.8376` edge `-0.0927` maxDD `-0.3101`
- `news_risk_high->index_24h` score `-0.1517` n `32` status `ready` deltaP `9.4813` edge `0.0045` maxDD `-2.3058`
- `market_context_high->equity_4h` score `-0.1661` n `192` status `ready` deltaP `2.2321` edge `0.063` maxDD `-2.671`
- `market_context_high->fx_1h` score `-0.2918` n `192` status `ready` deltaP `1.2101` edge `-0.0009` maxDD `-0.5659`
- `market_context_high->metal_4h` score `-0.6566` n `192` status `ready` deltaP `3.5351` edge `0.011` maxDD `-3.4996`
- `market_context_high->commodity_1h` score `-0.8076` n `192` status `ready` deltaP `-2.8443` edge `-0.0037` maxDD `-0.5708`
- `news_risk_high->metal_1h` score `-0.8455` n `32` status `ready` deltaP `-4.0419` edge `-0.0317` maxDD `-1.6464`
- `market_context_high->crypto_major_1h` score `-0.9433` n `192` status `ready` deltaP `4.0825` edge `0.0286` maxDD `-9.807`
- `market_context_high->crypto_alt_1h` score `-0.9535` n `192` status `ready` deltaP `3.3464` edge `0.0307` maxDD `-9.3536`
- `market_context_high->metal_1h` score `-0.9599` n `192` status `ready` deltaP `1.1664` edge `-0.0079` maxDD `-2.0564`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

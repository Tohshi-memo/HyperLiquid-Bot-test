# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-14T00:22:24.966235+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `10332`

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

- `market_context_high->unknown_24h` score `389.5025` n `75` status `ready` deltaP `2.1944` edge `32.458` maxDD `-0.4606`
- `news_risk_high->equity_24h` score `35.3785` n `53` status `ready` deltaP `34.5356` edge `2.7886` maxDD `-3.6503`
- `market_context_high->equity_24h` score `27.1448` n `75` status `ready` deltaP `29.0764` edge `2.2224` maxDD `-9.0005`
- `market_context_high->crypto_alt_24h` score `16.8978` n `75` status `ready` deltaP `47.5834` edge `1.3424` maxDD `-16.4511`
- `news_risk_high->crypto_major_24h` score `14.8663` n `53` status `ready` deltaP `42.0434` edge `1.8222` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `11.0384` n `53` status `ready` deltaP `35.1731` edge `0.7984` maxDD `-7.0416`
- `news_risk_high->commodity_24h` score `6.1099` n `53` status `ready` deltaP `40.1042` edge `0.2418` maxDD `0.0`
- `market_context_high->index_24h` score `5.3148` n `75` status `ready` deltaP `29.9028` edge `0.2527` maxDD `-0.0653`
- `news_risk_high->metal_4h` score `5.0515` n `53` status `ready` deltaP `48.073` edge `0.1381` maxDD `-1.0104`
- `news_risk_high->index_24h` score `4.6338` n `53` status `ready` deltaP `27.9153` edge `0.2304` maxDD `-0.4279`
- `market_context_high->metal_24h` score `4.134` n `75` status `ready` deltaP `41.3334` edge `0.3436` maxDD `-3.7989`
- `news_risk_high->equity_1h` score `3.5409` n `53` status `ready` deltaP `18.464` edge `0.235` maxDD `-3.7082`
- `news_risk_high->crypto_major_4h` score `3.5142` n `53` status `ready` deltaP `20.8957` edge `0.3023` maxDD `-9.2335`
- `news_risk_high->commodity_4h` score `3.1649` n `53` status `ready` deltaP `28.6931` edge `0.0978` maxDD `-0.3611`
- `news_risk_high->metal_1h` score `2.2901` n `53` status `ready` deltaP `26.7879` edge `0.0377` maxDD `-0.3692`
- `news_risk_high->index_4h` score `1.9264` n `53` status `ready` deltaP `19.3741` edge `0.075` maxDD `-0.8235`
- `news_risk_high->crypto_alt_4h` score `1.8501` n `53` status `ready` deltaP `25.5838` edge `0.2305` maxDD `-10.1088`
- `news_risk_high->crypto_alt_24h` score `1.7777` n `53` status `ready` deltaP `14.4261` edge `0.5823` maxDD `-29.0448`
- `news_risk_high->index_1h` score `1.146` n `53` status `ready` deltaP `15.679` edge `0.0211` maxDD `-0.4103`
- `news_risk_high->crypto_alt_1h` score `0.6338` n `53` status `ready` deltaP `16.9952` edge `0.0659` maxDD `-6.1688`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

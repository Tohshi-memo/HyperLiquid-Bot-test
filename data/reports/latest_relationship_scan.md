# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-29T11:52:20.073220+00:00`
- Price records: `672`
- Market context records: `2241`
- Flow alert records: `8346`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9203`

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

- `news_risk_high->crypto_alt_24h` score `25.6985` n `39` status `ready` deltaP `55.6357` edge `1.8295` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `16.2546` n `39` status `ready` deltaP `45.5262` edge `1.095` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `15.4052` n `39` status `ready` deltaP `36.4984` edge `1.0719` maxDD `-2.1831`
- `market_context_high->crypto_alt_4h` score `12.5208` n `131` status `ready` deltaP `34.1149` edge `0.9096` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `11.3329` n `131` status `ready` deltaP `40.3801` edge `0.7282` maxDD `-1.9063`
- `news_risk_high->unknown_24h` score `9.9887` n `39` status `ready` deltaP `36.5385` edge `0.6114` maxDD `-1.4744`
- `news_risk_high->crypto_major_24h` score `8.833` n `39` status `ready` deltaP `23.6111` edge `1.0331` maxDD `-3.3119`
- `market_context_high->unknown_24h` score `7.8271` n `121` status `ready` deltaP `28.4436` edge `0.609` maxDD `-9.7091`
- `market_context_high->unknown_4h` score `6.1621` n `131` status `ready` deltaP `23.8934` edge `0.3996` maxDD `-1.6306`
- `market_context_high->crypto_major_24h` score `5.7315` n `121` status `ready` deltaP `17.275` edge `1.0089` maxDD `-25.1408`
- `market_context_high->equity_4h` score `4.234` n `131` status `ready` deltaP `24.3705` edge `0.2493` maxDD `-2.048`
- `market_context_high->index_4h` score `4.1545` n `131` status `ready` deltaP `31.5409` edge `0.1733` maxDD `-0.3228`
- `news_risk_high->commodity_4h` score `3.9177` n `43` status `ready` deltaP `33.2246` edge `0.3479` maxDD `-3.0367`
- `news_risk_high->fx_24h` score `3.4694` n `39` status `ready` deltaP `35.0828` edge `0.0737` maxDD `-0.1442`
- `news_risk_high->index_24h` score `3.366` n `39` status `ready` deltaP `12.687` edge `0.2378` maxDD `-1.3507`
- `market_context_high->index_24h` score `3.1272` n `121` status `ready` deltaP `12.6234` edge `0.2282` maxDD `-1.4737`
- `market_context_high->crypto_alt_1h` score `2.6563` n `143` status `ready` deltaP `15.1847` edge `0.2065` maxDD `-4.9097`
- `market_context_high->crypto_major_1h` score `2.6175` n `143` status `ready` deltaP `14.0855` edge `0.1761` maxDD `-1.817`
- `news_risk_high->fx_4h` score `2.1512` n `43` status `ready` deltaP `27.2794` edge `0.0158` maxDD `-0.1382`
- `market_context_high->equity_24h` score `2.0446` n `121` status `ready` deltaP `20.0542` edge `0.2293` maxDD `-10.0756`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

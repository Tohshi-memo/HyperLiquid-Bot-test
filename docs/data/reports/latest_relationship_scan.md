# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-11T09:07:25.963879+00:00`
- Price records: `672`
- Market context records: `6376`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11120`

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

- `news_risk_high->crypto_alt_24h` score `14.3153` n `32` status `ready` deltaP `38.3681` edge `0.9519` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `6.3208` n `32` status `ready` deltaP `52.4306` edge `0.1772` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `4.2981` n `32` status `ready` deltaP `17.5347` edge `0.5121` maxDD `-4.2368`
- `news_risk_high->commodity_24h` score `4.123` n `32` status `ready` deltaP `35.7639` edge `0.1257` maxDD `-0.3101`
- `news_risk_high->fx_4h` score `3.9364` n `32` status `ready` deltaP `40.625` edge `0.0618` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.3859` n `32` status `ready` deltaP `28.7425` edge `0.0211` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `1.4912` n `32` status `ready` deltaP `14.4274` edge `0.1417` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.8792` n `32` status `ready` deltaP `11.0217` edge `0.0854` maxDD `-1.6923`
- `market_context_high->metal_4h` score `0.466` n `218` status `ready` deltaP `14.6998` edge `0.0414` maxDD `-2.7056`
- `market_context_high->unknown_1h` score `0.2629` n `222` status `ready` deltaP `-6.1472` edge `0.1637` maxDD `-3.7317`
- `market_context_high->index_4h` score `0.1728` n `218` status `ready` deltaP `9.0498` edge `0.0217` maxDD `-0.4108`
- `news_risk_high->unknown_1h` score `-0.2944` n `32` status `ready` deltaP `6.381` edge `-0.0326` maxDD `-0.7581`
- `market_context_high->metal_1h` score `-0.3813` n `222` status `ready` deltaP `3.9111` edge `0.0028` maxDD `-1.8877`
- `market_context_high->metal_24h` score `-0.3877` n `140` status `ready` deltaP `18.006` edge `0.0871` maxDD `-11.8809`
- `market_context_high->index_1h` score `-0.6321` n `222` status `ready` deltaP `-1.7978` edge `0.0029` maxDD `-0.7564`
- `market_context_high->fx_1h` score `-0.6824` n `222` status `ready` deltaP `-0.3116` edge `-0.0014` maxDD `-0.9376`
- `news_risk_high->metal_1h` score `-0.7091` n `32` status `ready` deltaP `-2.3952` edge `-0.0252` maxDD `-1.6464`
- `market_context_high->commodity_24h` score `-0.7239` n `140` status `ready` deltaP `-5.0397` edge `0.1272` maxDD `-6.2457`
- `news_risk_high->index_24h` score `-0.7284` n `32` status `ready` deltaP `0.5208` edge `-0.0097` maxDD `-2.3058`
- `market_context_high->equity_4h` score `-0.881` n `218` status `ready` deltaP `7.0444` edge `0.0495` maxDD `-8.2573`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

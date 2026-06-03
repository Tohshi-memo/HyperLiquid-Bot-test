# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-03T13:22:27.888633+00:00`
- Price records: `672`
- Market context records: `2767`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9237`

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

- `market_context_high->unknown_24h` score `4.8198` n `133` status `ready` deltaP `10.4806` edge `0.3646` maxDD `-1.6255`
- `market_context_high->crypto_alt_24h` score `3.0517` n `133` status `ready` deltaP `5.1757` edge `0.7096` maxDD `-20.2289`
- `market_context_high->unknown_4h` score `1.0113` n `143` status `ready` deltaP `6.7063` edge `0.1449` maxDD `-3.7602`
- `market_context_high->commodity_24h` score `0.122` n `133` status `ready` deltaP `8.9886` edge `0.2651` maxDD `-12.4171`
- `market_context_high->index_4h` score `-0.005` n `143` status `ready` deltaP `10.2465` edge `0.0152` maxDD `-2.3986`
- `market_context_high->unknown_1h` score `-0.0249` n `143` status `ready` deltaP `4.0964` edge `0.0437` maxDD `-3.1801`
- `market_context_high->index_1h` score `-0.1877` n `143` status `ready` deltaP `3.0506` edge `0.005` maxDD `-1.2855`
- `market_context_high->fx_1h` score `-0.5722` n `143` status `ready` deltaP `-0.9463` edge `0.003` maxDD `-0.2164`
- `market_context_high->commodity_1h` score `-0.5919` n `143` status `ready` deltaP `0.3518` edge `-0.0029` maxDD `-4.3601`
- `market_context_high->crypto_alt_1h` score `-0.7326` n `143` status `ready` deltaP `5.3966` edge `0.0461` maxDD `-10.747`
- `market_context_high->metal_1h` score `-0.7458` n `143` status `ready` deltaP `-0.6512` edge `-0.0067` maxDD `-3.0996`
- `market_context_high->crypto_major_1h` score `-1.0126` n `143` status `ready` deltaP `3.3479` edge `0.0348` maxDD `-9.622`
- `market_context_high->equity_1h` score `-1.2208` n `143` status `ready` deltaP `-3.7864` edge `0.0068` maxDD `-2.6634`
- `market_context_high->fx_4h` score `-1.2441` n `143` status `ready` deltaP `-4.86` edge `0.0066` maxDD `-0.5631`
- `market_context_high->crypto_alt_4h` score `-1.3298` n `143` status `ready` deltaP `14.2291` edge `0.2284` maxDD `-28.7261`
- `market_context_high->fx_24h` score `-1.3615` n `133` status `ready` deltaP `-0.9699` edge `-0.0198` maxDD `-0.6418`
- `market_context_high->commodity_4h` score `-1.6012` n `143` status `ready` deltaP `-0.0106` edge `-0.0132` maxDD `-10.0279`
- `market_context_high->equity_4h` score `-2.1935` n `143` status `ready` deltaP `-1.2493` edge `-0.0365` maxDD `-5.7037`
- `market_context_high->metal_4h` score `-2.4387` n `143` status `ready` deltaP `-2.4913` edge `-0.041` maxDD `-11.4038`
- `market_context_high->crypto_major_4h` score `-2.6823` n `143` status `ready` deltaP `4.7704` edge `0.1149` maxDD `-32.2466`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

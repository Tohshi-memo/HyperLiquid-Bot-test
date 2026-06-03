# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-03T12:22:21.772238+00:00`
- Price records: `672`
- Market context records: `2763`
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

- `market_context_high->unknown_24h` score `5.3575` n `131` status `ready` deltaP `11.8466` edge `0.4003` maxDD `-1.6255`
- `market_context_high->crypto_alt_24h` score `3.5247` n `131` status `ready` deltaP `6.0366` edge `0.761` maxDD `-19.9486`
- `market_context_high->unknown_4h` score `0.9969` n `143` status `ready` deltaP `6.7063` edge `0.1437` maxDD `-3.7602`
- `market_context_high->index_4h` score `0.0278` n `143` status `ready` deltaP `10.2465` edge `0.0194` maxDD `-2.3986`
- `market_context_high->commodity_24h` score `0.0067` n `131` status `ready` deltaP `8.495` edge `0.2536` maxDD `-12.4171`
- `market_context_high->unknown_1h` score `-0.0849` n `143` status `ready` deltaP `3.9467` edge `0.0397` maxDD `-3.1801`
- `market_context_high->index_1h` score `-0.1643` n `143` status `ready` deltaP `3.0506` edge `0.008` maxDD `-1.2855`
- `market_context_high->fx_1h` score `-0.559` n `143` status `ready` deltaP `-0.7966` edge `0.0031` maxDD `-0.2164`
- `market_context_high->commodity_1h` score `-0.6465` n `143` status `ready` deltaP `-0.0973` edge `-0.0069` maxDD `-4.3601`
- `market_context_high->crypto_alt_1h` score `-0.6687` n `143` status `ready` deltaP `5.8457` edge `0.0513` maxDD `-10.747`
- `market_context_high->metal_1h` score `-0.7762` n `143` status `ready` deltaP `-0.9506` edge `-0.0086` maxDD `-3.0996`
- `market_context_high->crypto_major_1h` score `-0.9565` n `143` status `ready` deltaP `3.6473` edge `0.04` maxDD `-9.622`
- `market_context_high->equity_1h` score `-1.18` n `143` status `ready` deltaP `-3.7864` edge `0.0102` maxDD `-2.6634`
- `market_context_high->crypto_alt_4h` score `-1.2282` n `143` status `ready` deltaP `14.8389` edge `0.2328` maxDD `-28.7261`
- `market_context_high->fx_4h` score `-1.2307` n `143` status `ready` deltaP `-4.7075` edge `0.0067` maxDD `-0.5631`
- `market_context_high->fx_24h` score `-1.3063` n `131` status `ready` deltaP `-0.4002` edge `-0.019` maxDD `-0.6418`
- `market_context_high->commodity_4h` score `-1.6844` n `143` status `ready` deltaP `-0.6204` edge `-0.0198` maxDD `-10.0279`
- `market_context_high->equity_4h` score `-2.1321` n `143` status `ready` deltaP `-1.0969` edge `-0.0324` maxDD `-5.7037`
- `market_context_high->metal_4h` score `-2.4678` n `143` status `ready` deltaP `-2.7962` edge `-0.0427` maxDD `-11.4038`
- `market_context_high->crypto_major_4h` score `-2.6257` n `143` status `ready` deltaP `5.2277` edge `0.1191` maxDD `-32.2466`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

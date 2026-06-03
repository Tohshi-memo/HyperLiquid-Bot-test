# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-03T10:22:24.200782+00:00`
- Price records: `672`
- Market context records: `2755`
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

- `market_context_high->unknown_24h` score `6.578` n `124` status `ready` deltaP `14.4433` edge `0.4847` maxDD `-1.6255`
- `market_context_high->crypto_alt_24h` score `4.6826` n `124` status `ready` deltaP `9.2686` edge `0.8879` maxDD `-19.9486`
- `market_context_high->unknown_4h` score `0.9291` n `143` status `ready` deltaP `6.249` edge `0.1411` maxDD `-3.7602`
- `market_context_high->index_4h` score `0.1453` n `143` status `ready` deltaP `10.8563` edge `0.0304` maxDD `-2.3986`
- `market_context_high->unknown_1h` score `-0.1208` n `143` status `ready` deltaP `3.4976` edge `0.0397` maxDD `-3.1801`
- `market_context_high->index_1h` score `-0.1542` n `143` status `ready` deltaP `3.2003` edge `0.0083` maxDD `-1.2855`
- `market_context_high->commodity_24h` score `-0.5374` n `124` status `ready` deltaP `6.642` edge `0.1962` maxDD `-12.4171`
- `market_context_high->fx_1h` score `-0.5853` n `143` status `ready` deltaP `-1.096` edge `0.0029` maxDD `-0.2164`
- `market_context_high->crypto_alt_1h` score `-0.6508` n `143` status `ready` deltaP `5.9954` edge `0.0526` maxDD `-10.747`
- `market_context_high->commodity_1h` score `-0.7057` n `143` status `ready` deltaP `-0.8458` edge `-0.0095` maxDD `-4.3601`
- `market_context_high->metal_1h` score `-0.724` n `143` status `ready` deltaP `-0.6512` edge `-0.0039` maxDD `-3.0996`
- `market_context_high->crypto_major_1h` score `-0.9417` n `143` status `ready` deltaP `3.797` edge `0.0409` maxDD `-9.622`
- `market_context_high->crypto_alt_4h` score `-1.1254` n `143` status `ready` deltaP `15.4486` edge `0.2373` maxDD `-28.7261`
- `market_context_high->equity_1h` score `-1.1596` n `143` status `ready` deltaP `-3.7864` edge `0.0119` maxDD `-2.6634`
- `market_context_high->fx_24h` score `-1.2346` n `124` status `ready` deltaP `0.2857` edge `-0.0176` maxDD `-0.6418`
- `market_context_high->fx_4h` score `-1.2405` n `143` status `ready` deltaP `-4.86` edge `0.0069` maxDD `-0.5631`
- `market_context_high->commodity_4h` score `-1.7017` n `143` status `ready` deltaP `-0.7728` edge `-0.021` maxDD `-10.0279`
- `market_context_high->equity_4h` score `-1.9855` n `143` status `ready` deltaP `-0.9444` edge `-0.0212` maxDD `-5.7037`
- `market_context_high->metal_4h` score `-2.4026` n `143` status `ready` deltaP `-2.1864` edge `-0.0384` maxDD `-11.4038`
- `market_context_high->crypto_major_4h` score `-2.5271` n `143` status `ready` deltaP `5.6851` edge `0.1287` maxDD `-32.2466`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

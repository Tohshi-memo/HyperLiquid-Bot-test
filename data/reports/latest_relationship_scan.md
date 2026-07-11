# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-11T04:07:30.096099+00:00`
- Price records: `672`
- Market context records: `6353`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11134`

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

- `news_risk_high->crypto_alt_24h` score `15.0431` n `32` status `ready` deltaP `41.8403` edge `0.9894` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `6.1665` n `32` status `ready` deltaP `51.0417` edge `0.1736` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `4.46` n `32` status `ready` deltaP `17.7083` edge `0.5317` maxDD `-4.2368`
- `news_risk_high->fx_4h` score `4.09` n `32` status `ready` deltaP `42.4543` edge `0.0624` maxDD `-0.0345`
- `news_risk_high->commodity_24h` score `3.7144` n `32` status `ready` deltaP `32.2917` edge `0.1148` maxDD `-0.3101`
- `news_risk_high->fx_1h` score `2.3512` n `32` status `ready` deltaP `28.2934` edge `0.0212` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `1.5014` n `32` status `ready` deltaP `14.7268` edge `0.141` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.887` n `32` status `ready` deltaP `11.3211` edge `0.0844` maxDD `-1.6923`
- `market_context_high->metal_4h` score `0.6968` n `199` status `ready` deltaP `14.2825` edge `0.0425` maxDD `-2.7056`
- `market_context_high->unknown_1h` score `0.0285` n `211` status `ready` deltaP `-7.6212` edge `0.154` maxDD `-3.7317`
- `market_context_high->index_4h` score `-0.002` n `199` status `ready` deltaP `6.79` edge `0.0222` maxDD `-0.4108`
- `market_context_high->commodity_24h` score `-0.5888` n `129` status `ready` deltaP `-4.7965` edge `0.1429` maxDD `-6.2457`
- `market_context_high->metal_1h` score `-0.5889` n `211` status `ready` deltaP `3.9277` edge `0.0025` maxDD `-1.8877`
- `market_context_high->commodity_1h` score `-0.6419` n `211` status `ready` deltaP `-1.9333` edge `-0.0011` maxDD `-2.1314`
- `market_context_high->metal_24h` score `-0.6815` n `129` status `ready` deltaP `14.2159` edge `0.0747` maxDD `-11.8809`
- `news_risk_high->unknown_1h` score `-0.6855` n `32` status `ready` deltaP `5.7822` edge `-0.0612` maxDD `-0.7581`
- `news_risk_high->index_24h` score `-0.7034` n `32` status `ready` deltaP `0.5208` edge `-0.0065` maxDD `-2.3058`
- `market_context_high->fx_1h` score `-0.7234` n `211` status `ready` deltaP `-0.735` edge `-0.002` maxDD `-0.9376`
- `news_risk_high->metal_1h` score `-0.7893` n `32` status `ready` deltaP `-3.8922` edge `-0.0255` maxDD `-1.6464`
- `market_context_high->unknown_4h` score `-0.906` n `199` status `ready` deltaP `-13.2093` edge `0.2293` maxDD `-11.925`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

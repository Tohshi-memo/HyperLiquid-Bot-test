# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-09T08:22:51.587629+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `8841`

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

- `market_context_high->equity_24h` score `3.7344` n `103` status `ready` deltaP `4.5729` edge `0.5867` maxDD `-21.1456`
- `market_context_high->metal_24h` score `2.7024` n `103` status `ready` deltaP `13.0799` edge `0.1956` maxDD `-2.2743`
- `market_context_high->commodity_4h` score `1.162` n `143` status `ready` deltaP `14.8996` edge `0.0648` maxDD `-2.7169`
- `market_context_high->commodity_1h` score `0.7905` n `143` status `ready` deltaP `10.8413` edge `0.0279` maxDD `-0.7439`
- `market_context_high->fx_24h` score `0.7876` n `103` status `ready` deltaP `21.575` edge `0.0438` maxDD `-1.9329`
- `market_context_high->index_24h` score `0.5618` n `103` status `ready` deltaP `9.1002` edge `0.1645` maxDD `-5.9181`
- `market_context_high->fx_1h` score `-0.293` n `143` status `ready` deltaP `4.2953` edge `-0.0035` maxDD `-0.9639`
- `market_context_high->index_1h` score `-0.44` n `143` status `ready` deltaP `-1.8424` edge `-0.0052` maxDD `-0.7809`
- `market_context_high->fx_4h` score `-0.4579` n `143` status `ready` deltaP `5.9803` edge `-0.0027` maxDD `-1.6928`
- `market_context_high->metal_1h` score `-0.69` n `143` status `ready` deltaP `-4.8877` edge `-0.0063` maxDD `-0.9664`
- `market_context_high->equity_1h` score `-0.9025` n `143` status `ready` deltaP `-0.0376` edge `0.0079` maxDD `-4.6286`
- `market_context_high->index_4h` score `-0.9306` n `143` status `ready` deltaP `-1.2205` edge `-0.0089` maxDD `-1.1743`
- `market_context_high->metal_4h` score `-0.9591` n `143` status `ready` deltaP `-0.7462` edge `-0.0171` maxDD `-2.7373`
- `market_context_high->crypto_alt_1h` score `-1.8809` n `143` status `ready` deltaP `-9.9839` edge `-0.026` maxDD `-2.4677`
- `market_context_high->equity_4h` score `-2.5113` n `143` status `ready` deltaP `-1.2664` edge `-0.0671` maxDD `-7.6983`
- `market_context_high->crypto_major_1h` score `-3.122` n `143` status `ready` deltaP `-10.5377` edge `-0.0577` maxDD `-7.2436`
- `market_context_high->crypto_major_24h` score `-3.245` n `103` status `ready` deltaP `6.0461` edge `-0.0613` maxDD `-14.2873`
- `market_context_high->crypto_alt_4h` score `-3.6117` n `143` status `ready` deltaP `-6.9046` edge `-0.0893` maxDD `-6.585`
- `market_context_high->crypto_alt_24h` score `-4.9268` n `103` status `ready` deltaP `-13.3142` edge `-0.1775` maxDD `-4.5445`
- `market_context_high->unknown_1h` score `-7.8005` n `143` status `ready` deltaP `-5.7944` edge `-0.5667` maxDD `-1.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

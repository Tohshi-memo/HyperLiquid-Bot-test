# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-05T03:52:26.965804+00:00`
- Price records: `672`
- Market context records: `2933`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6927`

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

- `market_context_high->crypto_alt_24h` score `15.449` n `142` status `ready` deltaP `15.0284` edge `1.5789` maxDD `-22.6673`
- `market_context_high->equity_24h` score `7.4709` n `142` status `ready` deltaP `17.2413` edge `0.708` maxDD `-12.6963`
- `market_context_high->unknown_24h` score `6.4549` n `142` status `ready` deltaP `15.1017` edge `0.4837` maxDD `-1.7175`
- `market_context_high->index_24h` score `2.604` n `142` status `ready` deltaP `13.016` edge `0.2283` maxDD `-2.5127`
- `market_context_high->commodity_24h` score `1.8077` n `142` status `ready` deltaP `15.378` edge `0.3575` maxDD `-12.4171`
- `market_context_high->equity_4h` score `0.9344` n `142` status `ready` deltaP `8.9746` edge `0.156` maxDD `-5.7037`
- `market_context_high->index_4h` score `0.7616` n `142` status `ready` deltaP `15.2826` edge `0.0799` maxDD `-2.3986`
- `market_context_high->crypto_alt_4h` score `0.3047` n `142` status `ready` deltaP `16.0147` edge `0.3527` maxDD `-28.7261`
- `market_context_high->unknown_4h` score `0.0125` n `142` status `ready` deltaP `3.7465` edge `0.0814` maxDD `-3.7602`
- `market_context_high->index_1h` score `-0.0046` n `143` status `ready` deltaP `4.5476` edge `0.0185` maxDD `-1.2855`
- `market_context_high->equity_1h` score `-0.3609` n `143` status `ready` deltaP `1.0532` edge `0.0462` maxDD `-2.6634`
- `market_context_high->crypto_alt_1h` score `-0.4423` n `143` status `ready` deltaP `5.8949` edge `0.08` maxDD `-10.747`
- `market_context_high->unknown_1h` score `-0.5243` n `143` status `ready` deltaP `3.149` edge `0.0084` maxDD `-3.1801`
- `market_context_high->fx_1h` score `-0.571` n `143` status `ready` deltaP `-0.9463` edge `0.0031` maxDD `-0.2164`
- `market_context_high->crypto_major_1h` score `-0.6117` n `143` status `ready` deltaP `5.942` edge `0.0689` maxDD `-9.622`
- `market_context_high->metal_1h` score `-0.6271` n `143` status `ready` deltaP `0.5464` edge `0.0047` maxDD `-3.4325`
- `market_context_high->commodity_1h` score `-0.6797` n `143` status `ready` deltaP `-1.5451` edge `-0.0015` maxDD `-4.3601`
- `market_context_high->fx_4h` score `-1.02` n `142` status `ready` deltaP `-1.9237` edge `0.0057` maxDD `-0.5631`
- `market_context_high->commodity_4h` score `-1.2876` n `142` status `ready` deltaP `1.6854` edge `0.0157` maxDD `-10.0279`
- `market_context_high->fx_24h` score `-1.3008` n `142` status `ready` deltaP `-1.7116` edge `-0.0098` maxDD `-0.6418`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

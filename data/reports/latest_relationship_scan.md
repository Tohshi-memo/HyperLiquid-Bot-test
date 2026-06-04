# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-04T08:58:24.786637+00:00`
- Price records: `672`
- Market context records: `2851`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9187`

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

- `market_context_high->unknown_24h` score `2.93` n `142` status `ready` deltaP `4.685` edge `0.2594` maxDD `-1.7175`
- `market_context_high->crypto_alt_24h` score `2.9081` n `142` status `ready` deltaP `2.702` edge `0.616` maxDD `-22.6673`
- `market_context_high->commodity_24h` score `1.048` n `142` status `ready` deltaP `12.9475` edge `0.3104` maxDD `-12.4171`
- `market_context_high->unknown_4h` score `0.8158` n `142` status `ready` deltaP `6.0331` edge `0.1331` maxDD `-3.7602`
- `market_context_high->index_24h` score `0.5131` n `142` status `ready` deltaP `6.2451` edge `0.0992` maxDD `-2.5127`
- `market_context_high->equity_24h` score `0.4105` n `142` status `ready` deltaP `4.0468` edge `0.2076` maxDD `-12.6963`
- `market_context_high->index_4h` score `0.2922` n `142` status `ready` deltaP `12.6911` edge `0.037` maxDD `-2.3986`
- `market_context_high->unknown_1h` score `0.1186` n `142` status `ready` deltaP `4.7799` edge `0.0511` maxDD `-3.1801`
- `market_context_high->index_1h` score `-0.0773` n `142` status `ready` deltaP `4.198` edge `0.0115` maxDD `-1.2855`
- `market_context_high->crypto_alt_1h` score `-0.6492` n `142` status `ready` deltaP `5.0962` edge `0.0588` maxDD `-10.747`
- `market_context_high->commodity_1h` score `-0.6623` n `142` status `ready` deltaP `-1.031` edge `-0.0027` maxDD `-4.3601`
- `market_context_high->fx_1h` score `-0.67` n `142` status `ready` deltaP `-2.0346` edge `0.0021` maxDD `-0.2164`
- `market_context_high->metal_1h` score `-0.7051` n `142` status `ready` deltaP `0.1328` edge `-0.0067` maxDD `-3.0996`
- `market_context_high->equity_1h` score `-0.8464` n `142` status `ready` deltaP `-2.0009` edge `0.0261` maxDD `-2.6634`
- `market_context_high->crypto_major_1h` score `-0.8585` n `142` status `ready` deltaP `4.0757` edge `0.0497` maxDD `-9.622`
- `market_context_high->equity_4h` score `-1.0256` n `142` status `ready` deltaP `2.1148` edge `0.0384` maxDD `-5.7037`
- `market_context_high->fx_4h` score `-1.2333` n `142` status `ready` deltaP `-4.5152` edge `0.0052` maxDD `-0.5631`
- `market_context_high->crypto_alt_4h` score `-1.2439` n `142` status `ready` deltaP `13.7281` edge `0.2389` maxDD `-28.7261`
- `market_context_high->commodity_4h` score `-1.3452` n `142` status `ready` deltaP `1.8378` edge `0.0073` maxDD `-10.0279`
- `market_context_high->fx_24h` score `-1.4083` n `142` status `ready` deltaP `-1.8852` edge `-0.0176` maxDD `-0.6418`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-08T12:52:27.563616+00:00`
- Price records: `672`
- Market context records: `6088`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11095`

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

- `news_risk_high->fx_24h` score `8.1594` n `30` status `ready` deltaP `72.7431` edge `0.195` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `6.1359` n `30` status `ready` deltaP `32.3958` edge `0.3101` maxDD `-0.5131`
- `news_risk_high->fx_4h` score `4.3005` n `32` status `ready` deltaP `44.7409` edge `0.0647` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.4314` n `32` status `ready` deltaP `29.1916` edge `0.0219` maxDD `-0.1113`
- `market_context_high->equity_4h` score `1.9758` n `198` status `ready` deltaP `10.3012` edge `0.1877` maxDD `-2.671`
- `news_risk_high->crypto_major_1h` score `1.1466` n `32` status `ready` deltaP `13.0801` edge `0.1065` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.6104` n `32` status `ready` deltaP `8.7762` edge `0.0659` maxDD `-1.6923`
- `news_risk_high->commodity_24h` score `0.4423` n `30` status `ready` deltaP `18.0903` edge `-0.0632` maxDD `-0.3101`
- `news_risk_high->index_24h` score `0.1117` n `30` status `ready` deltaP `9.2361` edge `0.0399` maxDD `-2.3058`
- `market_context_high->fx_1h` score `-0.261` n `198` status `ready` deltaP `1.6663` edge `0.0` maxDD `-0.5659`
- `market_context_high->metal_1h` score `-0.3622` n `198` status `ready` deltaP `4.1145` edge `0.006` maxDD `-2.0564`
- `market_context_high->equity_1h` score `-0.4328` n `198` status `ready` deltaP `2.5434` edge `0.0391` maxDD `-4.2573`
- `market_context_high->index_4h` score `-0.6833` n `198` status `ready` deltaP `4.1744` edge `0.031` maxDD `-1.381`
- `market_context_high->index_1h` score `-0.7051` n `198` status `ready` deltaP `-1.2717` edge `0.005` maxDD `-0.9531`
- `market_context_high->commodity_1h` score `-0.7186` n `198` status `ready` deltaP `-1.7027` edge `-0.0039` maxDD `-0.5708`
- `news_risk_high->metal_1h` score `-0.7256` n `32` status `ready` deltaP `-1.9461` edge `-0.0303` maxDD `-1.6464`
- `market_context_high->metal_4h` score `-0.7339` n `198` status `ready` deltaP `4.9181` edge `0.0248` maxDD `-3.4996`
- `market_context_high->crypto_alt_1h` score `-0.8188` n `198` status `ready` deltaP `4.4517` edge `0.0406` maxDD `-9.3536`
- `market_context_high->crypto_major_1h` score `-0.8914` n `198` status `ready` deltaP `4.5258` edge `0.0323` maxDD `-9.807`
- `news_risk_high->index_1h` score `-1.0283` n `32` status `ready` deltaP `-8.6265` edge `-0.018` maxDD `-1.1725`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

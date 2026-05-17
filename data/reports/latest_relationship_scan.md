# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-17T16:22:19.193329+00:00`
- Price records: `672`
- Market context records: `1029`
- Flow alert records: `4871`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8635`

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

- `market_context_high->crypto_major_24h` score `14.1065` n `185` status `ready` deltaP `32.8198` edge `1.0156` maxDD `-3.3749`
- `market_context_high->crypto_alt_24h` score `4.48` n `185` status `ready` deltaP `11.2705` edge `0.4216` maxDD `-9.5387`
- `market_context_high->equity_24h` score `2.9009` n `185` status `ready` deltaP `10.8108` edge `0.2704` maxDD `-4.3917`
- `market_context_high->index_24h` score `2.2065` n `185` status `ready` deltaP `10.1128` edge `0.2117` maxDD `-2.2864`
- `market_context_high->fx_1h` score `-0.0894` n `185` status `ready` deltaP `5.0267` edge `0.0006` maxDD `-0.3124`
- `market_context_high->metal_24h` score `-0.3634` n `185` status `ready` deltaP `-6.512` edge `0.3757` maxDD `-21.6725`
- `market_context_high->index_1h` score `-0.4891` n `185` status `ready` deltaP `3.9197` edge `0.0111` maxDD `-2.2395`
- `market_context_high->equity_1h` score `-0.5993` n `185` status `ready` deltaP `0.377` edge `0.0232` maxDD `-4.3858`
- `market_context_high->commodity_1h` score `-0.7263` n `185` status `ready` deltaP `0.653` edge `0.0159` maxDD `-3.7959`
- `market_context_high->fx_4h` score `-1.0199` n `185` status `ready` deltaP `1.8226` edge `0.0025` maxDD `-1.6381`
- `market_context_high->crypto_major_1h` score `-1.1824` n `185` status `ready` deltaP `5.6838` edge `-0.0106` maxDD `-8.0659`
- `market_context_high->index_4h` score `-1.3863` n `185` status `ready` deltaP `-0.253` edge `0.0338` maxDD `-6.1444`
- `market_context_high->crypto_alt_1h` score `-1.4334` n `185` status `ready` deltaP `-0.1294` edge `-0.01` maxDD `-5.3538`
- `market_context_high->metal_1h` score `-1.5115` n `185` status `ready` deltaP `1.459` edge `-0.0376` maxDD `-7.9398`
- `market_context_high->equity_4h` score `-1.5506` n `185` status `ready` deltaP `1.4379` edge `0.0764` maxDD `-10.5498`
- `market_context_high->crypto_alt_4h` score `-2.8762` n `185` status `ready` deltaP `0.6188` edge `0.034` maxDD `-15.2248`
- `market_context_high->crypto_major_4h` score `-3.0723` n `185` status `ready` deltaP `7.2561` edge `0.0662` maxDD `-22.648`
- `market_context_high->fx_24h` score `-3.1852` n `185` status `ready` deltaP `2.8772` edge `-0.0199` maxDD `-19.2774`
- `market_context_high->commodity_4h` score `-3.5847` n `185` status `ready` deltaP `-4.9143` edge `0.0508` maxDD `-13.0076`
- `market_context_high->metal_4h` score `-3.9772` n `185` status `ready` deltaP `-1.461` edge `-0.1566` maxDD `-20.8181`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

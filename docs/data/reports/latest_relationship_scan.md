# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-23T05:22:31.242058+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14882`

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

- `news_risk_high->unknown_4h` score `16.6733` n `43` status `ready` deltaP `28.5061` edge `1.1994` maxDD `0.0`
- `risk_on_high->unknown_1h` score `6.1655` n `30` status `ready` deltaP `-5.0099` edge `0.854` maxDD `-1.0788`
- `risk_on_and_context->unknown_1h` score `6.1655` n `30` status `ready` deltaP `-5.0099` edge `0.854` maxDD `-1.0788`
- `news_risk_high->equity_4h` score `5.3567` n `43` status `ready` deltaP `38.5636` edge `0.2106` maxDD `-0.3703`
- `news_risk_high->unknown_1h` score `3.821` n `51` status `ready` deltaP `20.6763` edge `0.211` maxDD `-0.7674`
- `news_risk_high->fx_4h` score `3.2486` n `43` status `ready` deltaP `38.6026` edge `0.0268` maxDD `-0.0746`
- `news_risk_high->metal_4h` score `1.4693` n `43` status `ready` deltaP `21.2954` edge `-0.0023` maxDD `-0.0449`
- `news_risk_high->index_4h` score `1.4174` n `43` status `ready` deltaP `19.7285` edge `0.0252` maxDD `-0.0884`
- `market_context_high->unknown_1h` score `1.2242` n `135` status `ready` deltaP `4.9901` edge `0.0989` maxDD `-1.0788`
- `news_risk_high->fx_1h` score `1.1966` n `51` status `ready` deltaP `16.5463` edge `0.0064` maxDD `-0.0257`
- `risk_on_high->fx_1h` score `0.871` n `30` status `ready` deltaP `12.6248` edge `0.0056` maxDD `-0.041`
- `risk_on_and_context->fx_1h` score `0.871` n `30` status `ready` deltaP `12.6248` edge `0.0056` maxDD `-0.041`
- `news_risk_high->equity_1h` score `0.8267` n `51` status `ready` deltaP `18.0433` edge `0.0222` maxDD `-0.9204`
- `market_context_high->unknown_4h` score `0.8084` n `131` status `ready` deltaP `21.6359` edge `-0.0597` maxDD `-0.3736`
- `news_risk_high->index_1h` score `0.199` n `51` status `ready` deltaP `8.6738` edge `0.003` maxDD `-0.1583`
- `risk_on_high->equity_1h` score `0.1986` n `30` status `ready` deltaP `0.7884` edge `0.0545` maxDD `-0.7435`
- `risk_on_and_context->equity_1h` score `0.1986` n `30` status `ready` deltaP `0.7884` edge `0.0545` maxDD `-0.7435`
- `news_risk_high->commodity_1h` score `0.1739` n `51` status `ready` deltaP `8.3891` edge `-0.0106` maxDD `-0.4666`
- `market_context_high->fx_4h` score `0.1531` n `131` status `ready` deltaP `8.1747` edge `0.0085` maxDD `-0.3527`
- `risk_on_high->index_1h` score `0.0998` n `30` status `ready` deltaP `3.1836` edge `0.0092` maxDD `-0.0768`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

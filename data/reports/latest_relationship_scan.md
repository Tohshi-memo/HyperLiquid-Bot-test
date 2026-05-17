# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-17T23:52:16.058446+00:00`
- Price records: `672`
- Market context records: `1063`
- Flow alert records: `4966`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8669`

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

- `market_context_high->crypto_major_24h` score `15.2683` n `173` status `ready` deltaP `34.3811` edge `1.0895` maxDD `-3.3749`
- `market_context_high->crypto_alt_24h` score `5.0735` n `173` status `ready` deltaP `11.8187` edge `0.4674` maxDD `-9.5387`
- `market_context_high->equity_24h` score `4.0625` n `173` status `ready` deltaP `12.7301` edge `0.3075` maxDD `-3.6396`
- `market_context_high->index_24h` score `3.3727` n `173` status `ready` deltaP `12.3996` edge `0.2417` maxDD `-2.1308`
- `market_context_high->metal_24h` score `2.9238` n `173` status `ready` deltaP `-5.4345` edge `0.4466` maxDD `-6.3373`
- `market_context_high->equity_4h` score `-0.0087` n `175` status `ready` deltaP `3.3615` edge `0.0947` maxDD `-5.7602`
- `market_context_high->fx_1h` score `-0.0482` n `175` status `ready` deltaP `5.8631` edge `0.0003` maxDD `-0.3124`
- `market_context_high->index_4h` score `-0.2683` n `175` status `ready` deltaP `1.9905` edge `0.0532` maxDD `-3.7729`
- `market_context_high->crypto_major_1h` score `-0.2947` n `175` status `ready` deltaP `7.1831` edge `0.0209` maxDD `-5.4676`
- `market_context_high->index_1h` score `-0.4801` n `175` status `ready` deltaP `3.7784` edge `0.0128` maxDD `-2.2395`
- `market_context_high->equity_1h` score `-0.5084` n `175` status `ready` deltaP `0.2677` edge `0.0286` maxDD `-4.1532`
- `market_context_high->metal_1h` score `-0.6634` n `175` status `ready` deltaP `4.7058` edge `-0.0266` maxDD `-4.5196`
- `market_context_high->fx_4h` score `-0.6989` n `175` status `ready` deltaP `1.1612` edge `0.0023` maxDD `-1.6381`
- `market_context_high->commodity_1h` score `-0.9296` n `175` status `ready` deltaP `-0.7477` edge `0.0083` maxDD `-3.7959`
- `market_context_high->crypto_alt_1h` score `-0.9776` n `175` status `ready` deltaP `1.8486` edge `0.0148` maxDD `-5.3538`
- `market_context_high->crypto_major_4h` score `-1.4708` n `175` status `ready` deltaP `8.7412` edge `0.086` maxDD `-14.3474`
- `market_context_high->crypto_alt_4h` score `-2.0369` n `175` status `ready` deltaP `2.4137` edge `0.0646` maxDD `-13.0347`
- `market_context_high->metal_4h` score `-2.5153` n `175` status `ready` deltaP `0.8153` edge `-0.1263` maxDD `-9.7959`
- `market_context_high->commodity_4h` score `-2.5931` n `175` status `ready` deltaP `-7.0636` edge `0.0314` maxDD `-13.0076`
- `market_context_high->fx_24h` score `-3.0909` n `173` status `ready` deltaP `4.8249` edge `-0.0208` maxDD `-19.2774`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

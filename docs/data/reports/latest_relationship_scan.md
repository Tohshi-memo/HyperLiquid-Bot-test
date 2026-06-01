# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-01T01:07:21.027205+00:00`
- Price records: `672`
- Market context records: `2514`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9280`

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

- `market_context_high->unknown_24h` score `5.0267` n `119` status `ready` deltaP `19.548` edge `0.3214` maxDD `-1.626`
- `market_context_high->crypto_alt_4h` score `4.686` n `150` status `ready` deltaP `21.3902` edge `0.5158` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `3.9133` n `150` status `ready` deltaP `17.6565` edge `0.3894` maxDD `-10.1468`
- `market_context_high->crypto_major_24h` score `2.2051` n `119` status `ready` deltaP `11.2891` edge `0.5967` maxDD `-25.1408`
- `market_context_high->unknown_4h` score `2.0239` n `150` status `ready` deltaP `11.315` edge `0.1982` maxDD `-3.7312`
- `market_context_high->crypto_alt_1h` score `0.9648` n `162` status `ready` deltaP `8.1356` edge `0.1449` maxDD `-6.1656`
- `market_context_high->crypto_major_1h` score `0.589` n `162` status `ready` deltaP `7.6495` edge `0.1175` maxDD `-4.2199`
- `market_context_high->index_24h` score `-0.027` n `119` status `ready` deltaP `3.1994` edge `0.0745` maxDD `-2.5127`
- `market_context_high->crypto_alt_24h` score `-0.0452` n `119` status `ready` deltaP `0.8782` edge `0.6841` maxDD `-43.6595`
- `market_context_high->index_4h` score `-0.1592` n `150` status `ready` deltaP `6.4918` edge `0.0276` maxDD `-2.3986`
- `market_context_high->equity_24h` score `-0.1778` n `119` status `ready` deltaP `17.8324` edge `0.019` maxDD `-6.8828`
- `market_context_high->commodity_1h` score `-0.3851` n `162` status `ready` deltaP `3.9089` edge `0.0124` maxDD `-4.3601`
- `market_context_high->fx_1h` score `-0.4219` n `162` status `ready` deltaP `1.9831` edge `0.0051` maxDD `-0.278`
- `market_context_high->index_1h` score `-0.4315` n `162` status `ready` deltaP `0.9518` edge `0.0071` maxDD `-1.2855`
- `market_context_high->metal_1h` score `-0.4687` n `162` status `ready` deltaP `0.8797` edge `0.01` maxDD `-3.0759`
- `market_context_high->unknown_1h` score `-0.5804` n `162` status `ready` deltaP `1.5894` edge `0.013` maxDD `-3.0902`
- `market_context_high->fx_24h` score `-0.7866` n `119` status `ready` deltaP `4.2951` edge `0.0056` maxDD `-2.4729`
- `market_context_high->equity_1h` score `-0.8545` n `162` status `ready` deltaP `-0.3973` edge `0.0153` maxDD `-2.7085`
- `market_context_high->fx_4h` score `-0.9513` n `150` status `ready` deltaP `-0.5711` edge `0.0105` maxDD `-0.8774`
- `market_context_high->commodity_4h` score `-1.0979` n `150` status `ready` deltaP `3.122` edge `0.0327` maxDD `-10.2078`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-20T02:07:20.914399+00:00`
- Price records: `672`
- Market context records: `1277`
- Flow alert records: `5586`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8820`

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

- `market_context_high->crypto_major_24h` score `17.9221` n `128` status `ready` deltaP `41.5798` edge `1.3295` maxDD `-8.0553`
- `market_context_high->metal_24h` score `10.8435` n `128` status `ready` deltaP `6.7708` edge `1.0252` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `8.8817` n `128` status `ready` deltaP `25.7812` edge `0.7699` maxDD `-15.1306`
- `market_context_high->index_24h` score `5.3322` n `128` status `ready` deltaP `27.7778` edge `0.3678` maxDD `-5.3574`
- `market_context_high->unknown_4h` score `5.3275` n `135` status `ready` deltaP `4.6816` edge `0.5344` maxDD `-6.7322`
- `market_context_high->equity_24h` score `3.9093` n `128` status `ready` deltaP `25.3472` edge `0.5649` maxDD `-14.2815`
- `market_context_high->equity_4h` score `3.1766` n `135` status `ready` deltaP `15.8468` edge `0.2254` maxDD `-3.6396`
- `market_context_high->unknown_24h` score `2.3706` n `128` status `ready` deltaP `1.5625` edge `0.4601` maxDD `-10.1706`
- `market_context_high->commodity_24h` score `1.6275` n `128` status `ready` deltaP `-13.0208` edge `0.3706` maxDD `-6.8535`
- `market_context_high->index_4h` score `1.5103` n `135` status `ready` deltaP `11.6193` edge `0.1167` maxDD `-2.1308`
- `market_context_high->metal_4h` score `0.7674` n `135` status `ready` deltaP `17.0167` edge `0.0936` maxDD `-6.4478`
- `market_context_high->equity_1h` score `0.4967` n `147` status `ready` deltaP `5.3709` edge `0.0483` maxDD `-1.7505`
- `market_context_high->index_1h` score `0.4778` n `147` status `ready` deltaP `7.9973` edge `0.0237` maxDD `-0.9758`
- `market_context_high->metal_1h` score `0.4218` n `147` status `ready` deltaP `11.5636` edge `0.0191` maxDD `-2.2164`
- `market_context_high->fx_24h` score `0.1747` n `128` status `ready` deltaP `4.4271` edge `0.0315` maxDD `-0.3831`
- `market_context_high->crypto_major_4h` score `-0.2372` n `135` status `ready` deltaP `6.7942` edge `0.1568` maxDD `-11.6007`
- `market_context_high->crypto_alt_1h` score `-0.29` n `147` status `ready` deltaP `1.496` edge `0.0399` maxDD `-3.6309`
- `market_context_high->fx_1h` score `-0.5195` n `147` status `ready` deltaP `0.8972` edge `-0.0037` maxDD `-0.3124`
- `market_context_high->crypto_major_1h` score `-0.7118` n `147` status `ready` deltaP `0.7078` edge `0.0061` maxDD `-5.8323`
- `market_context_high->crypto_alt_4h` score `-0.8288` n `135` status `ready` deltaP `7.8444` edge `0.1734` maxDD `-19.5565`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

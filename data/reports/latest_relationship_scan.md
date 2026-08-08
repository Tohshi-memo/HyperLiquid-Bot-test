# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-08T16:07:23.871796+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11573`

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

- `market_context_high->equity_24h` score `3.2832` n `100` status `ready` deltaP `4.0486` edge `0.5526` maxDD `-21.1456`
- `market_context_high->metal_24h` score `2.438` n `100` status `ready` deltaP `11.5139` edge `0.184` maxDD `-2.2743`
- `market_context_high->commodity_4h` score `1.4824` n `103` status `ready` deltaP `14.1339` edge `0.0966` maxDD `-2.7169`
- `market_context_high->fx_24h` score `1.0948` n `100` status `ready` deltaP `25.5486` edge `0.0567` maxDD `-1.9329`
- `market_context_high->commodity_1h` score `1.0094` n `103` status `ready` deltaP `11.6868` edge `0.0405` maxDD `-0.7439`
- `market_context_high->index_24h` score `0.3915` n `100` status `ready` deltaP `8.2847` edge `0.1481` maxDD `-5.9181`
- `market_context_high->equity_1h` score `-0.4652` n `103` status `ready` deltaP `3.449` edge `0.0211` maxDD `-4.6286`
- `market_context_high->fx_1h` score `-0.4998` n `103` status `ready` deltaP `2.0551` edge `-0.0058` maxDD `-0.9639`
- `market_context_high->index_1h` score `-0.5123` n `103` status `ready` deltaP `-3.6335` edge `-0.0067` maxDD `-0.7809`
- `market_context_high->metal_1h` score `-0.6397` n `103` status `ready` deltaP `-4.0099` edge `-0.0057` maxDD `-0.9664`
- `market_context_high->index_4h` score `-0.6556` n `103` status `ready` deltaP `-1.8811` edge `-0.011` maxDD `-1.1743`
- `market_context_high->fx_4h` score `-0.8783` n `103` status `ready` deltaP `1.1751` edge `-0.0057` maxDD `-1.6928`
- `market_context_high->metal_4h` score `-1.0225` n `103` status `ready` deltaP `-2.6107` edge `-0.0128` maxDD `-2.7373`
- `market_context_high->equity_4h` score `-1.9948` n `103` status `ready` deltaP `1.9788` edge `-0.0457` maxDD `-7.6983`
- `market_context_high->crypto_alt_1h` score `-2.0428` n `103` status `ready` deltaP `-11.6272` edge `-0.0298` maxDD `-2.3669`
- `market_context_high->crypto_major_24h` score `-2.2882` n `100` status `ready` deltaP `6.0694` edge `-0.0844` maxDD `-14.2873`
- `market_context_high->crypto_major_1h` score `-2.5428` n `103` status `ready` deltaP `-8.4835` edge `-0.0557` maxDD `-4.6382`
- `market_context_high->crypto_alt_24h` score `-2.6594` n `100` status `ready` deltaP `-13.6111` edge `-0.1059` maxDD `-4.5445`
- `market_context_high->crypto_alt_4h` score `-4.2844` n `103` status `ready` deltaP `-11.6461` edge `-0.1142` maxDD `-6.5487`
- `market_context_high->crypto_major_4h` score `-7.9837` n `103` status `ready` deltaP `-14.7111` edge `-0.2281` maxDD `-18.1307`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

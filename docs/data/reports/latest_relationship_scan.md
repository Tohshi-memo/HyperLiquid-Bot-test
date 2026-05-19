# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-19T10:52:14.646456+00:00`
- Price records: `672`
- Market context records: `1212`
- Flow alert records: `5396`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8776`

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

- `market_context_high->crypto_major_24h` score `18.8509` n `128` status `ready` deltaP `44.0104` edge `1.3907` maxDD `-8.0553`
- `market_context_high->unknown_4h` score `7.6005` n `128` status `ready` deltaP `2.6296` edge `0.7375` maxDD `-6.7322`
- `market_context_high->crypto_alt_24h` score `6.997` n `128` status `ready` deltaP `21.9618` edge `0.6383` maxDD `-15.1306`
- `market_context_high->commodity_24h` score `6.1683` n `128` status `ready` deltaP `-2.4306` edge `0.6784` maxDD `-6.8535`
- `market_context_high->metal_24h` score `4.2952` n `128` status `ready` deltaP `-3.4722` edge `0.5478` maxDD `-6.3373`
- `market_context_high->equity_4h` score `2.8655` n `128` status `ready` deltaP `14.958` edge `0.2054` maxDD `-3.6396`
- `market_context_high->index_24h` score `2.0862` n `128` status `ready` deltaP `18.4028` edge `0.1598` maxDD `-5.3574`
- `market_context_high->equity_24h` score `1.8124` n `128` status `ready` deltaP `18.5764` edge `0.3412` maxDD `-14.2815`
- `market_context_high->fx_24h` score `1.0904` n `128` status `ready` deltaP `10.5035` edge `0.0673` maxDD `-0.3831`
- `market_context_high->index_4h` score `0.9944` n `128` status `ready` deltaP `10.6897` edge `0.0799` maxDD `-2.1308`
- `market_context_high->index_1h` score `0.6205` n `128` status `ready` deltaP `9.5996` edge `0.0194` maxDD `-0.5353`
- `market_context_high->equity_1h` score `0.5116` n `128` status `ready` deltaP `4.7108` edge `0.0481` maxDD `-1.2834`
- `market_context_high->metal_1h` score `-0.0225` n `128` status `ready` deltaP `9.9691` edge `-0.0073` maxDD `-2.2164`
- `market_context_high->fx_1h` score `-0.142` n `128` status `ready` deltaP `5.001` edge `0.0004` maxDD `-0.3124`
- `market_context_high->crypto_major_4h` score `-0.219` n `128` status `ready` deltaP `5.2401` edge `0.1291` maxDD `-8.3693`
- `market_context_high->unknown_24h` score `-0.3293` n `128` status `ready` deltaP `-0.5208` edge `0.249` maxDD `-10.1706`
- `market_context_high->crypto_alt_1h` score `-0.41` n `128` status `ready` deltaP `0.0468` edge `0.0314` maxDD `-3.4088`
- `market_context_high->crypto_major_1h` score `-0.4354` n `128` status `ready` deltaP `2.3765` edge `0.0049` maxDD `-4.1256`
- `market_context_high->commodity_1h` score `-0.7631` n `128` status `ready` deltaP `-2.311` edge `0.0133` maxDD `-2.252`
- `market_context_high->metal_4h` score `-1.0452` n `128` status `ready` deltaP `11.4901` edge `-0.0206` maxDD `-6.4478`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

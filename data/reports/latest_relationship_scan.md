# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-26T11:52:30.049465+00:00`
- Price records: `672`
- Market context records: `4824`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7588`

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

- `market_context_high->unknown_1h` score `13.5561` n `110` status `ready` deltaP `11.9897` edge `1.0915` maxDD `-1.674`
- `market_context_high->unknown_4h` score `8.0481` n `110` status `ready` deltaP `17.2672` edge `0.6766` maxDD `-4.6834`
- `market_context_high->unknown_24h` score `3.0756` n `103` status `ready` deltaP `15.8324` edge `0.2196` maxDD `-2.8416`
- `market_context_high->index_4h` score `0.8858` n `110` status `ready` deltaP `10.7677` edge `0.0487` maxDD `-0.7334`
- `market_context_high->equity_4h` score `0.8346` n `110` status `ready` deltaP `12.428` edge `0.1623` maxDD `-6.3852`
- `market_context_high->commodity_4h` score `0.4825` n `110` status `ready` deltaP `15.9562` edge `0.0727` maxDD `-4.377`
- `market_context_high->commodity_1h` score `0.2611` n `110` status `ready` deltaP `6.6195` edge `0.0258` maxDD `-1.1869`
- `market_context_high->equity_1h` score `0.0003` n `110` status `ready` deltaP `4.0855` edge `0.0344` maxDD `-2.928`
- `market_context_high->fx_4h` score `-0.4829` n `110` status `ready` deltaP `2.4335` edge `-0.0005` maxDD `-1.5439`
- `market_context_high->index_1h` score `-0.5011` n `110` status `ready` deltaP `0.4709` edge `0.0081` maxDD `-0.7054`
- `market_context_high->fx_1h` score `-1.1137` n `110` status `ready` deltaP `-3.5193` edge `-0.0044` maxDD `-0.8626`
- `market_context_high->crypto_alt_1h` score `-1.9077` n `110` status `ready` deltaP `5.1334` edge `-0.005` maxDD `-12.7225`
- `market_context_high->crypto_major_1h` score `-2.1344` n `110` status `ready` deltaP `3.1328` edge `-0.037` maxDD `-17.9354`
- `market_context_high->metal_1h` score `-2.1427` n `110` status `ready` deltaP `0.1061` edge `-0.0651` maxDD `-13.4916`
- `market_context_high->fx_24h` score `-2.3555` n `103` status `ready` deltaP `-11.2426` edge `-0.0195` maxDD `-2.814`
- `market_context_high->commodity_24h` score `-2.4293` n `103` status `ready` deltaP `17.5247` edge `0.0826` maxDD `-27.5371`
- `market_context_high->crypto_alt_4h` score `-3.7857` n `110` status `ready` deltaP `8.3398` edge `0.0042` maxDD `-38.2779`
- `market_context_high->index_24h` score `-3.992` n `103` status `ready` deltaP `-2.9615` edge `-0.1012` maxDD `-23.2678`
- `market_context_high->crypto_major_4h` score `-7.3017` n `110` status `ready` deltaP `5.1663` edge `-0.1474` maxDD `-60.5192`
- `market_context_high->metal_4h` score `-8.6813` n `110` status `ready` deltaP `5.8038` edge `-0.3412` maxDD `-60.1721`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-26T12:52:30.740072+00:00`
- Price records: `672`
- Market context records: `4829`
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

- `market_context_high->unknown_1h` score `13.7343` n `109` status `ready` deltaP `11.038` edge `1.1127` maxDD `-1.674`
- `market_context_high->unknown_4h` score `8.3759` n `108` status `ready` deltaP `18.0612` edge `0.6968` maxDD `-4.5371`
- `market_context_high->unknown_24h` score `3.1676` n `101` status `ready` deltaP `16.1682` edge `0.2232` maxDD `-2.6953`
- `market_context_high->index_4h` score `0.8414` n `108` status `ready` deltaP `10.4674` edge `0.047` maxDD `-0.7334`
- `market_context_high->equity_4h` score `0.7453` n `108` status `ready` deltaP `12.3306` edge `0.1515` maxDD `-6.3852`
- `market_context_high->commodity_4h` score `0.4267` n `108` status `ready` deltaP `15.1818` edge `0.0707` maxDD `-4.377`
- `market_context_high->commodity_1h` score `0.3239` n `109` status `ready` deltaP `6.8038` edge `0.0298` maxDD `-1.1869`
- `market_context_high->equity_1h` score `-0.0421` n `109` status `ready` deltaP `3.8098` edge `0.0308` maxDD `-2.928`
- `market_context_high->fx_4h` score `-0.4247` n `108` status `ready` deltaP `3.0714` edge `0.0007` maxDD `-1.3837`
- `market_context_high->index_1h` score `-0.5257` n `109` status `ready` deltaP `0.1785` edge `0.0069` maxDD `-0.7054`
- `market_context_high->fx_1h` score `-1.1228` n `109` status `ready` deltaP `-3.5873` edge `-0.0047` maxDD `-0.8626`
- `market_context_high->crypto_alt_1h` score `-2.0704` n `109` status `ready` deltaP `4.09` edge `-0.0116` maxDD `-12.7225`
- `market_context_high->metal_1h` score `-2.1808` n `109` status `ready` deltaP `0.0632` edge `-0.0697` maxDD `-13.4916`
- `market_context_high->crypto_major_1h` score `-2.2049` n `109` status `ready` deltaP `2.0477` edge `-0.0388` maxDD `-17.9354`
- `market_context_high->fx_24h` score `-2.327` n `101` status `ready` deltaP `-11.0526` edge `-0.0192` maxDD `-2.749`
- `market_context_high->commodity_24h` score `-2.4994` n `101` status `ready` deltaP `16.8523` edge `0.0781` maxDD `-27.5371`
- `market_context_high->crypto_alt_4h` score `-2.949` n `108` status `ready` deltaP `9.5528` edge `0.0402` maxDD `-33.8901`
- `market_context_high->index_24h` score `-4.0214` n `101` status `ready` deltaP `-3.2866` edge `-0.1028` maxDD `-23.2678`
- `market_context_high->crypto_major_4h` score `-5.9293` n `108` status `ready` deltaP `6.2952` edge `-0.0881` maxDD `-52.456`
- `market_context_high->metal_4h` score `-7.4322` n `108` status `ready` deltaP `6.2387` edge `-0.2943` maxDD `-52.0107`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

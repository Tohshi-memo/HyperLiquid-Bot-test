# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-25T12:37:28.239159+00:00`
- Price records: `672`
- Market context records: `4723`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7432`

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

- `market_context_high->unknown_1h` score `77.0923` n `144` status `ready` deltaP `14.9119` edge `6.3667` maxDD `-1.674`
- `market_context_high->unknown_4h` score `5.6391` n `144` status `ready` deltaP `14.7696` edge `0.4925` maxDD `-4.6834`
- `market_context_high->unknown_24h` score `3.2226` n `135` status `ready` deltaP `16.5278` edge `0.2507` maxDD `-4.7201`
- `market_context_high->commodity_1h` score `-0.2765` n `144` status `ready` deltaP `2.7071` edge `0.0261` maxDD `-2.0345`
- `market_context_high->index_4h` score `-0.6327` n `144` status `ready` deltaP `4.9289` edge `-0.0017` maxDD `-5.9823`
- `market_context_high->commodity_4h` score `-0.8497` n `144` status `ready` deltaP `9.7391` edge `0.0369` maxDD `-9.1941`
- `market_context_high->fx_4h` score `-0.8986` n `144` status `ready` deltaP `-0.7452` edge `-0.002` maxDD `-1.9927`
- `market_context_high->equity_4h` score `-0.9407` n `144` status `ready` deltaP `3.5569` edge `0.0326` maxDD `-8.8203`
- `market_context_high->equity_1h` score `-1.1378` n `144` status `ready` deltaP `-1.4429` edge `0.0135` maxDD `-5.5624`
- `market_context_high->fx_1h` score `-1.2697` n `144` status `ready` deltaP `-4.8362` edge `-0.0056` maxDD `-1.1038`
- `market_context_high->index_1h` score `-1.587` n `144` status `ready` deltaP `-3.4847` edge `-0.0086` maxDD `-2.6999`
- `market_context_high->crypto_alt_1h` score `-3.1161` n `144` status `ready` deltaP `-0.341` edge `-0.0685` maxDD `-22.2982`
- `market_context_high->crypto_major_1h` score `-3.5875` n `144` status `ready` deltaP `-0.3826` edge `-0.0821` maxDD `-27.356`
- `market_context_high->commodity_24h` score `-4.4027` n `135` status `ready` deltaP `17.1065` edge `0.0695` maxDD `-30.7016`
- `market_context_high->metal_1h` score `-4.4545` n `144` status `ready` deltaP `-5.6263` edge `-0.0769` maxDD `-17.2107`
- `market_context_high->fx_24h` score `-4.8267` n `135` status `ready` deltaP `-13.2176` edge `-0.0181` maxDD `-5.3476`
- `market_context_high->crypto_alt_4h` score `-7.9636` n `144` status `ready` deltaP `-2.0326` edge `-0.1417` maxDD `-63.9243`
- `market_context_high->index_24h` score `-8.5112` n `135` status `ready` deltaP `-11.1574` edge `-0.0974` maxDD `-29.3321`
- `market_context_high->metal_4h` score `-8.765` n `144` status `ready` deltaP `2.1341` edge `-0.2526` maxDD `-64.494`
- `market_context_high->crypto_major_4h` score `-10.5032` n `144` status `ready` deltaP `-1.355` edge `-0.2475` maxDD `-81.8692`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

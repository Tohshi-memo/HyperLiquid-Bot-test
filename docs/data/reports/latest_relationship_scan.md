# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-21T20:52:17.454726+00:00`
- Price records: `672`
- Market context records: `1459`
- Flow alert records: `6112`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8809`

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

- `market_context_high->crypto_alt_24h` score `12.7975` n `163` status `ready` deltaP `28.8887` edge `1.0755` maxDD `-15.1306`
- `market_context_high->crypto_major_24h` score `11.9496` n `163` status `ready` deltaP `27.569` edge `0.9252` maxDD `-8.0553`
- `market_context_high->metal_24h` score `11.5218` n `163` status `ready` deltaP `15.0094` edge `1.0268` maxDD `-6.3373`
- `market_context_high->index_24h` score `4.1858` n `163` status `ready` deltaP `19.8832` edge `0.3249` maxDD `-5.3574`
- `market_context_high->equity_24h` score `3.9978` n `163` status `ready` deltaP `13.1007` edge `0.4785` maxDD `-14.2815`
- `market_context_high->equity_4h` score `1.5166` n `221` status `ready` deltaP `7.077` edge `0.1622` maxDD `-3.6396`
- `market_context_high->fx_24h` score `0.252` n `163` status `ready` deltaP `11.6404` edge `0.0483` maxDD `-1.3925`
- `market_context_high->index_1h` score `-0.0949` n `223` status `ready` deltaP `3.6452` edge `0.0143` maxDD `-1.7205`
- `market_context_high->equity_1h` score `-0.144` n `223` status `ready` deltaP `1.8474` edge `0.0357` maxDD `-2.8014`
- `market_context_high->crypto_alt_4h` score `-0.2916` n `221` status `ready` deltaP `11.3184` edge `0.2322` maxDD `-19.5565`
- `market_context_high->index_4h` score `-0.4625` n `221` status `ready` deltaP `0.9381` edge `0.0641` maxDD `-3.7119`
- `market_context_high->fx_1h` score `-0.4786` n `223` status `ready` deltaP `0.67` edge `-0.0026` maxDD `-0.3914`
- `market_context_high->crypto_alt_1h` score `-0.5598` n `223` status `ready` deltaP `1.8622` edge `0.0433` maxDD `-4.1892`
- `market_context_high->fx_4h` score `-1.0459` n `221` status `ready` deltaP `-4.1607` edge `-0.0093` maxDD `-1.4313`
- `market_context_high->crypto_major_4h` score `-1.1529` n `221` status `ready` deltaP `5.1312` edge `0.1406` maxDD `-13.3376`
- `market_context_high->metal_1h` score `-1.1549` n `223` status `ready` deltaP `5.0006` edge `0.004` maxDD `-6.3532`
- `market_context_high->commodity_1h` score `-1.2481` n `223` status `ready` deltaP `-1.5708` edge `-0.0014` maxDD `-4.7041`
- `market_context_high->crypto_major_1h` score `-1.6188` n `223` status `ready` deltaP `-0.9774` edge `0.0073` maxDD `-6.1883`
- `market_context_high->metal_4h` score `-1.8035` n `221` status `ready` deltaP `7.904` edge `0.0662` maxDD `-12.5349`
- `market_context_high->commodity_4h` score `-3.9694` n `221` status `ready` deltaP `-11.5337` edge `-0.067` maxDD `-16.867`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-25T08:22:30.486167+00:00`
- Price records: `672`
- Market context records: `4706`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9638`

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

- `market_context_high->unknown_1h` score `76.9304` n `144` status `ready` deltaP `13.864` edge `6.3602` maxDD `-1.674`
- `market_context_high->unknown_4h` score `5.2547` n `137` status `ready` deltaP `12.0349` edge `0.4787` maxDD `-4.6834`
- `market_context_high->unknown_24h` score `2.6663` n `135` status `ready` deltaP `13.9237` edge `0.2217` maxDD `-4.7201`
- `market_context_high->commodity_1h` score `-0.3303` n `144` status `ready` deltaP `2.1083` edge `0.0232` maxDD `-2.0345`
- `market_context_high->index_4h` score `-0.7332` n `137` status `ready` deltaP `4.2872` edge `-0.0103` maxDD `-5.9823`
- `market_context_high->fx_4h` score `-0.9179` n `137` status `ready` deltaP `-1.086` edge `-0.0022` maxDD `-1.9927`
- `market_context_high->commodity_4h` score `-1.1396` n `137` status `ready` deltaP `6.5037` edge `0.0213` maxDD `-9.1941`
- `market_context_high->equity_1h` score `-1.1965` n `144` status `ready` deltaP `-1.7423` edge `0.0106` maxDD `-5.5624`
- `market_context_high->equity_4h` score `-1.2709` n `137` status `ready` deltaP `1.1827` edge `0.0061` maxDD `-8.8203`
- `market_context_high->fx_1h` score `-1.2816` n `144` status `ready` deltaP `-4.9859` edge `-0.0056` maxDD `-1.1038`
- `market_context_high->index_1h` score `-1.6589` n `144` status `ready` deltaP `-4.0835` edge `-0.0106` maxDD `-2.6999`
- `market_context_high->crypto_alt_1h` score `-3.2759` n `144` status `ready` deltaP `-1.5386` edge `-0.081` maxDD `-22.2982`
- `market_context_high->crypto_major_1h` score `-3.8213` n `144` status `ready` deltaP `-2.179` edge `-0.1001` maxDD `-27.356`
- `market_context_high->metal_1h` score `-4.4425` n `144` status `ready` deltaP `-5.4766` edge `-0.0769` maxDD `-17.2107`
- `market_context_high->commodity_24h` score `-4.4842` n `135` status `ready` deltaP `16.2384` edge `0.0685` maxDD `-30.7016`
- `market_context_high->fx_24h` score `-4.7913` n `135` status `ready` deltaP `-13.044` edge `-0.0163` maxDD `-5.3476`
- `market_context_high->crypto_alt_4h` score `-8.3087` n `137` status `ready` deltaP `-2.3701` edge `-0.1837` maxDD `-63.9243`
- `market_context_high->index_24h` score `-8.3999` n `135` status `ready` deltaP `-10.6366` edge `-0.0916` maxDD `-29.3321`
- `market_context_high->metal_4h` score `-8.9285` n `137` status `ready` deltaP `1.0893` edge `-0.2666` maxDD `-64.494`
- `market_context_high->crypto_major_4h` score `-11.2185` n `137` status `ready` deltaP `-2.7951` edge `-0.3296` maxDD `-81.8692`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

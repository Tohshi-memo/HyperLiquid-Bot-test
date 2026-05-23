# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-23T07:07:18.898492+00:00`
- Price records: `672`
- Market context records: `1606`
- Flow alert records: `6536`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8814`

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

- `market_context_high->metal_24h` score `13.6056` n `184` status `ready` deltaP `30.0422` edge `1.0419` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `12.0771` n `184` status `ready` deltaP `26.404` edge `1.0468` maxDD `-15.979`
- `market_context_high->crypto_major_24h` score `9.5829` n `184` status `ready` deltaP `26.2001` edge `0.8075` maxDD `-12.6875`
- `market_context_high->equity_24h` score `5.0304` n `184` status `ready` deltaP `20.6824` edge `0.514` maxDD `-14.2815`
- `market_context_high->index_24h` score `4.1485` n `184` status `ready` deltaP `22.1618` edge `0.3066` maxDD `-5.3574`
- `market_context_high->equity_4h` score `1.2336` n `197` status `ready` deltaP `10.598` edge `0.1416` maxDD `-5.0894`
- `market_context_high->crypto_alt_4h` score `0.1559` n `197` status `ready` deltaP `12.8923` edge `0.266` maxDD `-19.5565`
- `market_context_high->crypto_major_4h` score `0.0549` n `197` status `ready` deltaP `9.0341` edge `0.2177` maxDD `-13.3376`
- `market_context_high->fx_24h` score `-0.1887` n `184` status `ready` deltaP `7.8125` edge `0.0371` maxDD `-1.3925`
- `market_context_high->crypto_alt_1h` score `-0.3566` n `197` status `ready` deltaP `0.5464` edge `0.053` maxDD `-4.1892`
- `market_context_high->equity_1h` score `-0.5618` n `197` status `ready` deltaP `0.6497` edge `0.0297` maxDD `-2.8014`
- `market_context_high->index_1h` score `-0.686` n `197` status `ready` deltaP `0.3762` edge `0.0035` maxDD `-1.7205`
- `market_context_high->metal_1h` score `-0.7449` n `197` status `ready` deltaP `4.9325` edge `0.0052` maxDD `-6.3532`
- `market_context_high->commodity_1h` score `-0.7576` n `197` status `ready` deltaP `-0.7941` edge `0.0003` maxDD `-4.7041`
- `market_context_high->fx_1h` score `-0.8967` n `197` status `ready` deltaP `-1.1847` edge `-0.0036` maxDD `-0.3914`
- `market_context_high->crypto_major_1h` score `-0.9062` n `197` status `ready` deltaP `-0.9438` edge `0.0258` maxDD `-6.1883`
- `market_context_high->index_4h` score `-0.9402` n `197` status `ready` deltaP `-0.1122` edge `0.0313` maxDD `-3.7119`
- `market_context_high->metal_4h` score `-1.4094` n `197` status `ready` deltaP `9.0356` edge `0.0915` maxDD `-12.5349`
- `market_context_high->fx_4h` score `-1.4123` n `197` status `ready` deltaP `-11.0205` edge `-0.0147` maxDD `-1.4313`
- `market_context_high->commodity_4h` score `-5.2024` n `197` status `ready` deltaP `-14.2612` edge `-0.1092` maxDD `-24.683`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

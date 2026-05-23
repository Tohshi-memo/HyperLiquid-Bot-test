# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-23T07:37:18.818624+00:00`
- Price records: `672`
- Market context records: `1608`
- Flow alert records: `6542`
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

- `market_context_high->metal_24h` score `13.1044` n `184` status `ready` deltaP `29.3026` edge `1.0134` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `10.1449` n `184` status `ready` deltaP `25.6643` edge `1.006` maxDD `-24.5347`
- `market_context_high->crypto_major_24h` score `8.18` n `184` status `ready` deltaP `25.4605` edge `0.7733` maxDD `-18.2426`
- `market_context_high->equity_24h` score `4.7144` n `184` status `ready` deltaP `19.9426` edge `0.4926` maxDD `-14.2815`
- `market_context_high->index_24h` score `4.027` n `184` status `ready` deltaP `21.4221` edge `0.3014` maxDD `-5.3574`
- `market_context_high->equity_4h` score `1.2503` n `195` status `ready` deltaP `10.6114` edge `0.1429` maxDD `-5.0894`
- `market_context_high->crypto_alt_4h` score `0.151` n `195` status `ready` deltaP `12.8275` edge `0.2658` maxDD `-19.5565`
- `market_context_high->crypto_major_4h` score `0.0575` n `195` status `ready` deltaP `8.9329` edge `0.2187` maxDD `-13.3376`
- `market_context_high->fx_24h` score `-0.2055` n `184` status `ready` deltaP `7.8125` edge `0.0357` maxDD `-1.3925`
- `market_context_high->crypto_alt_1h` score `-0.3733` n `195` status `ready` deltaP `0.3616` edge `0.0521` maxDD `-4.1892`
- `market_context_high->equity_1h` score `-0.5378` n `195` status `ready` deltaP `0.8906` edge `0.0301` maxDD `-2.8014`
- `market_context_high->index_1h` score `-0.6957` n `195` status `ready` deltaP `0.2695` edge `0.0034` maxDD `-1.7205`
- `market_context_high->fx_1h` score `-0.8766` n `195` status `ready` deltaP `-0.9634` edge `-0.0034` maxDD `-0.3914`
- `market_context_high->crypto_major_1h` score `-0.9242` n `195` status `ready` deltaP `-1.1546` edge `0.0249` maxDD `-6.1883`
- `market_context_high->index_4h` score `-0.9399` n `195` status `ready` deltaP `-0.2134` edge `0.032` maxDD `-3.7119`
- `market_context_high->commodity_1h` score `-1.1498` n `195` status `ready` deltaP `-0.6418` edge `0.0006` maxDD `-4.7041`
- `market_context_high->metal_1h` score `-1.1837` n `195` status `ready` deltaP `4.5056` edge `0.0049` maxDD `-6.3532`
- `market_context_high->fx_4h` score `-1.403` n `195` status `ready` deltaP `-10.8724` edge `-0.0145` maxDD `-1.4313`
- `market_context_high->metal_4h` score `-1.4395` n `195` status `ready` deltaP `8.6139` edge `0.0918` maxDD `-12.5349`
- `market_context_high->commodity_4h` score `-5.217` n `195` status `ready` deltaP `-14.4356` edge `-0.1099` maxDD `-24.683`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

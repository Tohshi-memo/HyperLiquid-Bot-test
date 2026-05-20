# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-20T20:52:19.696754+00:00`
- Price records: `672`
- Market context records: `1355`
- Flow alert records: `5817`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8794`

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

- `market_context_high->crypto_major_24h` score `13.4983` n `130` status `ready` deltaP `33.1571` edge `1.017` maxDD `-8.0553`
- `market_context_high->metal_24h` score `12.6942` n `130` status `ready` deltaP `12.1902` edge `1.1433` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `9.5633` n `130` status `ready` deltaP `28.4215` edge `0.8091` maxDD `-15.1306`
- `market_context_high->index_24h` score `4.0949` n `130` status `ready` deltaP `23.6058` edge `0.2925` maxDD `-5.3574`
- `market_context_high->commodity_24h` score `2.8431` n `130` status `ready` deltaP `-8.3254` edge `0.4406` maxDD `-6.8535`
- `market_context_high->equity_4h` score `2.3074` n `157` status `ready` deltaP `11.8912` edge `0.1835` maxDD `-3.6396`
- `market_context_high->equity_24h` score `1.8751` n `130` status `ready` deltaP `16.5117` edge `0.363` maxDD `-14.2815`
- `market_context_high->fx_24h` score `1.4306` n `130` status `ready` deltaP `15.641` edge `0.0614` maxDD `-0.3831`
- `market_context_high->metal_4h` score `0.1239` n `157` status `ready` deltaP `13.068` edge `0.0663` maxDD `-6.4478`
- `market_context_high->index_1h` score `0.0543` n `167` status `ready` deltaP `5.0899` edge `0.016` maxDD `-1.6329`
- `market_context_high->index_4h` score `-0.0008` n `157` status `ready` deltaP `4.8742` edge `0.0763` maxDD `-3.7119`
- `market_context_high->equity_1h` score `-0.034` n `167` status `ready` deltaP `2.2456` edge `0.0268` maxDD `-1.9017`
- `market_context_high->unknown_24h` score `-0.1255` n `130` status `ready` deltaP `-4.7088` edge `0.2939` maxDD `-10.1706`
- `market_context_high->metal_1h` score `-0.1495` n `167` status `ready` deltaP `7.6348` edge `-0.0011` maxDD `-2.8509`
- `market_context_high->fx_1h` score `-0.2999` n `167` status `ready` deltaP `1.7964` edge `-0.004` maxDD `-0.3808`
- `market_context_high->commodity_1h` score `-0.5758` n `167` status `ready` deltaP `0.2994` edge `0.0115` maxDD `-2.252`
- `market_context_high->crypto_alt_1h` score `-0.8993` n `167` status `ready` deltaP `-0.8982` edge `0.0181` maxDD `-3.6309`
- `market_context_high->crypto_major_1h` score `-1.1838` n `167` status `ready` deltaP `-3.7425` edge `-0.0203` maxDD `-6.1883`
- `market_context_high->crypto_alt_4h` score `-1.2985` n `157` status `ready` deltaP `8.4676` edge `0.1673` maxDD `-19.5565`
- `market_context_high->unknown_4h` score `-1.3836` n `157` status `ready` deltaP `1.4292` edge `0.0402` maxDD `-11.1695`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

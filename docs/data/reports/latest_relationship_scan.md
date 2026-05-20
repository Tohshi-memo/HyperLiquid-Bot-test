# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-20T22:52:17.926232+00:00`
- Price records: `672`
- Market context records: `1365`
- Flow alert records: `5842`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8804`

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

- `market_context_high->crypto_major_24h` score `13.2153` n `138` status `ready` deltaP `32.0803` edge `1.0006` maxDD `-8.0553`
- `market_context_high->metal_24h` score `12.6068` n `138` status `ready` deltaP `13.6172` edge `1.1265` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `10.1824` n `138` status `ready` deltaP `28.5553` edge `0.8598` maxDD `-15.1306`
- `market_context_high->index_24h` score `4.1393` n `138` status `ready` deltaP `22.8412` edge `0.3013` maxDD `-5.3574`
- `market_context_high->equity_24h` score `2.7203` n `138` status `ready` deltaP `15.8364` edge `0.3538` maxDD `-14.2815`
- `market_context_high->equity_4h` score `2.0407` n `163` status `ready` deltaP `10.7035` edge `0.1692` maxDD `-3.6396`
- `market_context_high->fx_24h` score `0.9785` n `138` status `ready` deltaP `12.2584` edge `0.0518` maxDD `-0.8251`
- `market_context_high->metal_4h` score `0.0636` n `163` status `ready` deltaP `12.1344` edge `0.0675` maxDD `-6.4478`
- `market_context_high->index_1h` score `-0.0499` n `175` status `ready` deltaP `4.1198` edge `0.0126` maxDD `-1.7166`
- `market_context_high->index_4h` score `-0.1197` n `163` status `ready` deltaP `3.3228` edge `0.0714` maxDD `-3.7119`
- `market_context_high->equity_1h` score `-0.1659` n `175` status `ready` deltaP `1.752` edge `0.0229` maxDD `-2.8014`
- `market_context_high->fx_1h` score `-0.3329` n `175` status `ready` deltaP `1.1968` edge `-0.0041` maxDD `-0.3914`
- `market_context_high->metal_1h` score `-0.4217` n `175` status `ready` deltaP `5.9581` edge `0.0008` maxDD `-3.5666`
- `market_context_high->crypto_alt_1h` score `-0.6026` n `175` status `ready` deltaP `-1.0214` edge `0.0166` maxDD `-3.6309`
- `market_context_high->commodity_1h` score `-0.6557` n `175` status `ready` deltaP `0.0813` edge `0.0063` maxDD `-2.252`
- `market_context_high->crypto_major_1h` score `-1.114` n `175` status `ready` deltaP `-3.225` edge `-0.0148` maxDD `-6.1883`
- `market_context_high->crypto_alt_4h` score `-1.4697` n `163` status `ready` deltaP `7.5574` edge `0.1591` maxDD `-19.5565`
- `market_context_high->commodity_24h` score `-1.6312` n `138` status `ready` deltaP `-10.7715` edge `0.2846` maxDD `-22.8976`
- `market_context_high->crypto_major_4h` score `-2.0074` n `163` status `ready` deltaP `2.2959` edge `0.0883` maxDD `-13.3376`
- `market_context_high->fx_4h` score `-2.045` n `163` status `ready` deltaP `-9.1856` edge `-0.015` maxDD `-1.2009`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

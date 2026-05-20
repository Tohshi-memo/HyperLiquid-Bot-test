# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-20T13:07:21.477783+00:00`
- Price records: `672`
- Market context records: `1323`
- Flow alert records: `5721`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8783`

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

- `market_context_high->crypto_major_24h` score `15.8961` n `128` status `ready` deltaP `38.4548` edge `1.1815` maxDD `-8.0553`
- `market_context_high->metal_24h` score `13.5364` n `128` status `ready` deltaP `14.0625` edge `1.201` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `9.714` n `128` status `ready` deltaP `28.3854` edge `0.8219` maxDD `-15.1306`
- `market_context_high->index_24h` score `5.4935` n `128` status `ready` deltaP `28.8194` edge `0.3743` maxDD `-5.3574`
- `market_context_high->equity_24h` score `3.2198` n `128` status `ready` deltaP `21.7014` edge `0.5008` maxDD `-14.2815`
- `market_context_high->equity_4h` score `2.3459` n `157` status `ready` deltaP `12.0436` edge `0.1857` maxDD `-3.6396`
- `market_context_high->unknown_24h` score `1.7774` n `128` status `ready` deltaP `-1.5625` edge `0.4315` maxDD `-10.1706`
- `market_context_high->commodity_24h` score `1.3805` n `128` status `ready` deltaP `-12.6736` edge `0.3477` maxDD `-6.8535`
- `market_context_high->fx_24h` score `1.0474` n `128` status `ready` deltaP `12.066` edge `0.0533` maxDD `-0.3831`
- `market_context_high->equity_1h` score `0.1361` n `157` status `ready` deltaP `3.0683` edge `0.0336` maxDD `-1.7505`
- `market_context_high->metal_4h` score `0.1011` n `157` status `ready` deltaP `13.068` edge `0.0644` maxDD `-6.4478`
- `market_context_high->index_4h` score `0.0951` n `157` status `ready` deltaP `4.8742` edge `0.0886` maxDD `-3.7119`
- `market_context_high->index_1h` score `0.0617` n `157` status `ready` deltaP `5.3139` edge `0.0179` maxDD `-1.6329`
- `market_context_high->metal_1h` score `-0.0607` n `157` status `ready` deltaP `8.942` edge `0.0043` maxDD `-2.8509`
- `market_context_high->fx_1h` score `-0.5373` n `157` status `ready` deltaP `0.6589` edge `-0.0036` maxDD `-0.3124`
- `market_context_high->crypto_alt_1h` score `-0.5881` n `157` status `ready` deltaP `0.697` edge `0.0334` maxDD `-3.6309`
- `market_context_high->crypto_alt_4h` score `-0.9015` n `157` status `ready` deltaP `10.1444` edge `0.1892` maxDD `-19.5565`
- `market_context_high->commodity_1h` score `-0.9077` n `157` status `ready` deltaP `-1.7039` edge `-0.0028` maxDD `-2.252`
- `market_context_high->crypto_major_1h` score `-0.9117` n `157` status `ready` deltaP `-1.3664` edge `-0.0057` maxDD `-5.8323`
- `market_context_high->unknown_4h` score `-0.9277` n `157` status `ready` deltaP `3.8683` edge `0.0824` maxDD `-11.1695`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-20T13:22:26.507668+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `24`

- Symbol pattern count: `2634`

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

- `market_context_high->unknown_1h` score `10730.1172` n `120` status `ready` deltaP `1.507` edge `894.1862` maxDD `-0.9181`
- `market_context_high->unknown_4h` score `7196.3505` n `111` status `ready` deltaP `0.7196` edge `599.7195` maxDD `-0.6072`
- `market_context_high->crypto_major_24h` score `13.5537` n `102` status `ready` deltaP `30.77` edge `1.3503` maxDD `-29.4102`
- `market_context_high->crypto_alt_24h` score `7.8608` n `102` status `ready` deltaP `16.8812` edge `1.1465` maxDD `-43.6516`
- `market_context_high->crypto_major_4h` score `1.5372` n `111` status `ready` deltaP `5.3834` edge `0.3741` maxDD `-16.2179`
- `market_context_high->crypto_alt_4h` score `1.3803` n `111` status `ready` deltaP `6.4505` edge `0.2796` maxDD `-12.9396`
- `market_context_high->metal_4h` score `0.3053` n `111` status `ready` deltaP `16.2904` edge `0.0559` maxDD `-6.7918`
- `market_context_high->metal_1h` score `-0.1527` n `120` status `ready` deltaP `4.471` edge `0.0171` maxDD `-2.6517`
- `market_context_high->index_1h` score `-0.3416` n `120` status `ready` deltaP `2.2056` edge `0.0027` maxDD `-1.2295`
- `market_context_high->crypto_major_1h` score `-1.1717` n `120` status `ready` deltaP `2.8243` edge `0.0399` maxDD `-7.843`
- `market_context_high->fx_1h` score `-1.255` n `120` status `ready` deltaP `-7.1757` edge `-0.0008` maxDD `-0.4757`
- `market_context_high->equity_1h` score `-1.6054` n `120` status `ready` deltaP `5.005` edge `0.019` maxDD `-11.559`
- `market_context_high->index_4h` score `-1.815` n `111` status `ready` deltaP `-1.5464` edge `-0.0066` maxDD `-4.7471`
- `market_context_high->crypto_alt_1h` score `-1.9182` n `120` status `ready` deltaP `-3.009` edge `0.0178` maxDD `-8.2736`
- `market_context_high->commodity_1h` score `-2.0088` n `120` status `ready` deltaP `-5.8084` edge `-0.0155` maxDD `-4.3877`
- `market_context_high->fx_4h` score `-2.2492` n `111` status `ready` deltaP `-12.7459` edge `-0.0018` maxDD `-1.794`
- `market_context_high->metal_24h` score `-4.4963` n `102` status `ready` deltaP `14.5425` edge `0.1247` maxDD `-37.7071`
- `market_context_high->fx_24h` score `-6.5774` n `102` status `ready` deltaP `-16.8913` edge `-0.0082` maxDD `-5.5179`
- `market_context_high->commodity_4h` score `-7.5151` n `111` status `ready` deltaP `-24.7762` edge `-0.0918` maxDD `-15.5426`
- `market_context_high->equity_4h` score `-9.9931` n `111` status `ready` deltaP `-5.2338` edge `-0.0633` maxDD `-48.4323`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

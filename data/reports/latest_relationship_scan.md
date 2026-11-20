# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-20T10:22:41.454676+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `24`

- Symbol pattern count: `2612`

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

- `market_context_high->unknown_1h` score `11620.3457` n `111` status `ready` deltaP `1.3123` edge `968.3732` maxDD `-0.9181`
- `market_context_high->unknown_4h` score `7455.5885` n `108` status `ready` deltaP `0.5194` edge `621.324` maxDD `-0.6072`
- `market_context_high->crypto_major_24h` score `13.4565` n `102` status `ready` deltaP `30.77` edge `1.3422` maxDD `-29.4102`
- `market_context_high->crypto_alt_24h` score `7.604` n `102` status `ready` deltaP `16.8812` edge `1.1251` maxDD `-43.6516`
- `market_context_high->crypto_major_4h` score `1.8139` n `108` status `ready` deltaP `5.6176` edge `0.3956` maxDD `-16.2179`
- `market_context_high->crypto_alt_4h` score `1.5538` n `108` status `ready` deltaP `6.6847` edge `0.2925` maxDD `-12.9396`
- `market_context_high->metal_4h` score `0.5848` n `108` status `ready` deltaP `18.1741` edge `0.062` maxDD `-6.4211`
- `market_context_high->metal_1h` score `-0.1667` n `111` status `ready` deltaP `4.4869` edge `0.0152` maxDD `-2.6517`
- `market_context_high->crypto_major_1h` score `-0.4376` n `111` status `ready` deltaP `3.7439` edge `0.0586` maxDD `-6.5061`
- `market_context_high->index_1h` score `-0.493` n `111` status `ready` deltaP `2.5381` edge `0.0032` maxDD `-1.2295`
- `market_context_high->crypto_alt_1h` score `-1.231` n `111` status `ready` deltaP `-2.5625` edge `0.0367` maxDD `-5.4428`
- `market_context_high->equity_1h` score `-1.39` n `111` status `ready` deltaP `5.69` edge `0.0241` maxDD `-10.8962`
- `market_context_high->fx_1h` score `-1.4714` n `111` status `ready` deltaP `-9.7751` edge `-0.0015` maxDD `-0.4757`
- `market_context_high->index_4h` score `-1.7043` n `108` status `ready` deltaP `-0.8525` edge `-0.002` maxDD `-4.7471`
- `market_context_high->fx_4h` score `-2.3715` n `108` status `ready` deltaP `-14.7979` edge `-0.0038` maxDD `-1.794`
- `market_context_high->commodity_1h` score `-2.4424` n `111` status `ready` deltaP `-9.473` edge `-0.0272` maxDD `-4.3877`
- `market_context_high->metal_24h` score `-4.7255` n `102` status `ready` deltaP `14.5425` edge `0.1056` maxDD `-37.7071`
- `market_context_high->fx_24h` score `-6.5467` n `102` status `ready` deltaP `-16.7177` edge `-0.0068` maxDD `-5.5179`
- `market_context_high->commodity_4h` score `-7.8631` n `108` status `ready` deltaP `-27.2809` edge `-0.1041` maxDD `-15.5426`
- `market_context_high->equity_4h` score `-8.9083` n `108` status `ready` deltaP `-5.07` edge `-0.0264` maxDD `-44.2396`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

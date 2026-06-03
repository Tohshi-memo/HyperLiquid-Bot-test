# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-03T06:22:25.643837+00:00`
- Price records: `672`
- Market context records: `2738`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9230`

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

- `market_context_high->crypto_alt_24h` score `11.1139` n `111` status `ready` deltaP `16.3523` edge `1.1665` maxDD `-19.9486`
- `market_context_high->unknown_24h` score `8.4846` n `111` status `ready` deltaP `17.3048` edge `0.6245` maxDD `-1.6255`
- `market_context_high->crypto_major_24h` score `1.4108` n `111` status `ready` deltaP `6.5175` edge `0.8937` maxDD `-44.169`
- `market_context_high->unknown_4h` score `1.2202` n `143` status `ready` deltaP `7.7734` edge `0.1552` maxDD `-3.7602`
- `market_context_high->index_4h` score `0.083` n `143` status `ready` deltaP `10.0941` edge `0.0275` maxDD `-2.3986`
- `market_context_high->unknown_1h` score `-0.1387` n `143` status `ready` deltaP `3.0485` edge `0.0412` maxDD `-3.1801`
- `market_context_high->index_1h` score `-0.1877` n `143` status `ready` deltaP `2.7512` edge `0.007` maxDD `-1.2855`
- `market_context_high->crypto_alt_4h` score `-0.4819` n `143` status `ready` deltaP `16.6681` edge `0.2828` maxDD `-28.7261`
- `market_context_high->fx_1h` score `-0.5087` n `143` status `ready` deltaP `-0.1978` edge `0.0033` maxDD `-0.2164`
- `market_context_high->commodity_1h` score `-0.5701` n `143` status `ready` deltaP `0.5015` edge `-0.0011` maxDD `-4.3601`
- `market_context_high->crypto_alt_1h` score `-0.6056` n `143` status `ready` deltaP `6.1451` edge `0.0574` maxDD `-10.747`
- `market_context_high->metal_1h` score `-0.7653` n `143` status `ready` deltaP `-1.25` edge `-0.0052` maxDD `-3.0996`
- `market_context_high->crypto_major_1h` score `-0.951` n `143` status `ready` deltaP `3.6473` edge `0.0407` maxDD `-9.622`
- `market_context_high->fx_4h` score `-1.0469` n `143` status `ready` deltaP `-2.7258` edge `0.0088` maxDD `-0.5631`
- `market_context_high->fx_24h` score `-1.1935` n `111` status `ready` deltaP `0.2299` edge `-0.0138` maxDD `-0.6418`
- `market_context_high->equity_1h` score `-1.3502` n `143` status `ready` deltaP `-5.2834` edge `0.006` maxDD `-2.6634`
- `market_context_high->commodity_4h` score `-1.4774` n `143` status `ready` deltaP `0.7516` edge `-0.0024` maxDD `-10.0279`
- `market_context_high->commodity_24h` score `-1.7033` n `111` status `ready` deltaP `2.5807` edge `0.0738` maxDD `-12.4171`
- `market_context_high->equity_4h` score `-2.0675` n `143` status `ready` deltaP `-1.2493` edge `-0.026` maxDD `-5.7037`
- `market_context_high->crypto_major_4h` score `-2.2546` n `143` status `ready` deltaP `6.9046` edge `0.1555` maxDD `-32.2466`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

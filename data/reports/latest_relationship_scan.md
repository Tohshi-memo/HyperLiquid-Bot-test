# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-11T08:22:31.836005+00:00`
- Price records: `672`
- Market context records: `6372`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11118`

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

- `news_risk_high->crypto_alt_24h` score `14.4385` n `32` status `ready` deltaP `38.8889` edge `0.9587` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `6.3172` n `32` status `ready` deltaP `52.4306` edge `0.1769` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `4.3316` n `32` status `ready` deltaP `17.5347` edge `0.5164` maxDD `-4.2368`
- `news_risk_high->commodity_24h` score `4.0645` n `32` status `ready` deltaP `35.2431` edge `0.1243` maxDD `-0.3101`
- `news_risk_high->fx_4h` score `3.9742` n `32` status `ready` deltaP `41.0823` edge `0.0619` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.3979` n `32` status `ready` deltaP `28.8922` edge `0.0211` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `1.5341` n `32` status `ready` deltaP `14.8765` edge `0.1442` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.9174` n `32` status `ready` deltaP `11.4708` edge `0.0873` maxDD `-1.6923`
- `market_context_high->metal_4h` score `0.4965` n `215` status `ready` deltaP `15.241` edge `0.0417` maxDD `-2.7056`
- `market_context_high->unknown_1h` score `0.2714` n `220` status `ready` deltaP `-6.4752` edge `0.1666` maxDD `-3.7317`
- `market_context_high->index_4h` score `0.1496` n `215` status `ready` deltaP `8.7607` edge `0.0217` maxDD `-0.4108`
- `news_risk_high->unknown_1h` score `-0.3304` n `32` status `ready` deltaP `6.0816` edge `-0.0336` maxDD `-0.7581`
- `market_context_high->metal_1h` score `-0.395` n `220` status `ready` deltaP `3.6636` edge `0.0027` maxDD `-1.8877`
- `market_context_high->metal_24h` score `-0.4675` n `137` status `ready` deltaP `17.1457` edge `0.0826` maxDD `-11.8809`
- `market_context_high->fx_1h` score `-0.6382` n `220` status `ready` deltaP `0.2558` edge `-0.0015` maxDD `-0.9376`
- `market_context_high->index_1h` score `-0.6401` n `220` status `ready` deltaP `-1.9515` edge `0.0029` maxDD `-0.7564`
- `market_context_high->commodity_24h` score `-0.6553` n `137` status `ready` deltaP `-4.6064` edge `0.1331` maxDD `-6.2457`
- `news_risk_high->metal_1h` score `-0.7014` n `32` status `ready` deltaP `-2.2455` edge `-0.0252` maxDD `-1.6464`
- `news_risk_high->index_24h` score `-0.7229` n `32` status `ready` deltaP `0.5208` edge `-0.009` maxDD `-2.3058`
- `market_context_high->equity_4h` score `-0.9005` n `215` status `ready` deltaP `6.9512` edge `0.0485` maxDD `-8.2573`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

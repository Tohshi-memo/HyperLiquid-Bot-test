# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-09T15:21:06.254140+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `10826`

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

- `market_context_high->equity_24h` score `3.5994` n `104` status `ready` deltaP `4.2201` edge `0.5778` maxDD `-21.1456`
- `market_context_high->metal_24h` score `2.2944` n `104` status `ready` deltaP `9.2548` edge `0.1871` maxDD `-2.2743`
- `market_context_high->commodity_4h` score `1.293` n `143` status `ready` deltaP `15.9667` edge `0.0686` maxDD `-2.7169`
- `market_context_high->commodity_1h` score `0.8217` n `143` status `ready` deltaP `11.1407` edge `0.0285` maxDD `-0.7439`
- `market_context_high->fx_24h` score `0.6707` n `104` status `ready` deltaP `20.7665` edge `0.0342` maxDD `-1.9329`
- `market_context_high->index_24h` score `0.3821` n `104` status `ready` deltaP `6.4102` edge `0.1594` maxDD `-5.9181`
- `market_context_high->fx_1h` score `-0.3576` n `143` status `ready` deltaP `3.5468` edge `-0.0039` maxDD `-0.9639`
- `market_context_high->index_1h` score `-0.391` n `143` status `ready` deltaP `-0.9442` edge `-0.0049` maxDD `-0.7809`
- `market_context_high->fx_4h` score `-0.5187` n `143` status `ready` deltaP `5.3706` edge `-0.0037` maxDD `-1.6928`
- `market_context_high->metal_1h` score `-0.6737` n `143` status `ready` deltaP `-4.5883` edge `-0.0062` maxDD `-0.9664`
- `market_context_high->index_4h` score `-0.8696` n `143` status `ready` deltaP `-0.4583` edge `-0.0089` maxDD `-1.1743`
- `market_context_high->equity_1h` score `-0.9205` n `143` status `ready` deltaP `-0.3371` edge `0.0084` maxDD `-4.6286`
- `market_context_high->metal_4h` score `-1.0082` n `143` status `ready` deltaP `-1.6608` edge `-0.0173` maxDD `-2.7373`
- `market_context_high->crypto_alt_1h` score `-1.9432` n `143` status `ready` deltaP `-10.433` edge `-0.0282` maxDD `-2.4677`
- `market_context_high->equity_4h` score `-2.4989` n `143` status `ready` deltaP `-0.9615` edge `-0.0681` maxDD `-7.6983`
- `market_context_high->crypto_major_1h` score `-3.2406` n `143` status `ready` deltaP `-11.4359` edge `-0.0616` maxDD `-7.2436`
- `market_context_high->crypto_alt_4h` score `-3.8137` n `143` status `ready` deltaP `-8.1241` edge `-0.098` maxDD `-6.585`
- `market_context_high->crypto_major_24h` score `-4.1233` n `104` status `ready` deltaP `1.8029` edge `-0.1062` maxDD `-14.2873`
- `market_context_high->crypto_alt_24h` score `-6.4102` n `104` status `ready` deltaP `-17.8018` edge `-0.2712` maxDD `-4.5445`
- `market_context_high->unknown_1h` score `-7.8041` n `143` status `ready` deltaP `-5.9441` edge `-0.566` maxDD `-1.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

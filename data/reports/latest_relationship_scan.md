# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-09T15:37:25.683003+00:00`
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

- `market_context_high->equity_24h` score `3.5723` n `104` status `ready` deltaP `4.0465` edge `0.5767` maxDD `-21.1456`
- `market_context_high->metal_24h` score `2.2758` n `104` status `ready` deltaP `9.0812` edge `0.1867` maxDD `-2.2743`
- `market_context_high->commodity_4h` score `1.3088` n `143` status `ready` deltaP `16.1191` edge `0.0689` maxDD `-2.7169`
- `market_context_high->commodity_1h` score `0.8241` n `143` status `ready` deltaP `11.1407` edge `0.0287` maxDD `-0.7439`
- `market_context_high->fx_24h` score `0.6691` n `104` status `ready` deltaP `20.7665` edge `0.034` maxDD `-1.9329`
- `market_context_high->index_24h` score `0.3715` n `104` status `ready` deltaP `6.2366` edge `0.1592` maxDD `-5.9181`
- `market_context_high->fx_1h` score `-0.3708` n `143` status `ready` deltaP `3.3971` edge `-0.004` maxDD `-0.9639`
- `market_context_high->index_1h` score `-0.3987` n `143` status `ready` deltaP `-1.0939` edge `-0.0049` maxDD `-0.7809`
- `market_context_high->fx_4h` score `-0.5309` n `143` status `ready` deltaP `5.2182` edge `-0.0037` maxDD `-1.6928`
- `market_context_high->metal_1h` score `-0.6822` n `143` status `ready` deltaP `-4.738` edge `-0.0063` maxDD `-0.9664`
- `market_context_high->index_4h` score `-0.883` n `143` status `ready` deltaP `-0.6108` edge `-0.009` maxDD `-1.1743`
- `market_context_high->equity_1h` score `-0.9205` n `143` status `ready` deltaP `-0.3371` edge `0.0084` maxDD `-4.6286`
- `market_context_high->metal_4h` score `-1.009` n `143` status `ready` deltaP `-1.6608` edge `-0.0174` maxDD `-2.7373`
- `market_context_high->crypto_alt_1h` score `-1.9648` n `143` status `ready` deltaP `-10.5827` edge `-0.029` maxDD `-2.4677`
- `market_context_high->equity_4h` score `-2.5171` n `143` status `ready` deltaP `-1.1139` edge `-0.0686` maxDD `-7.6983`
- `market_context_high->crypto_major_1h` score `-3.2598` n `143` status `ready` deltaP `-11.5856` edge `-0.0622` maxDD `-7.2436`
- `market_context_high->crypto_alt_4h` score `-3.8439` n `143` status `ready` deltaP `-8.2765` edge `-0.0995` maxDD `-6.585`
- `market_context_high->crypto_major_24h` score `-4.1504` n `104` status `ready` deltaP `1.6293` edge `-0.1073` maxDD `-14.2873`
- `market_context_high->crypto_alt_24h` score `-6.4649` n `104` status `ready` deltaP `-17.9754` edge `-0.2746` maxDD `-4.5445`
- `market_context_high->unknown_1h` score `-7.8053` n `143` status `ready` deltaP `-5.9441` edge `-0.5661` maxDD `-1.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

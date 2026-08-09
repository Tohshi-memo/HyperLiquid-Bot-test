# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-09T23:37:27.721915+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `10906`

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

- `market_context_high->commodity_4h` score `1.2577` n `149` status `ready` deltaP `15.1958` edge `0.0708` maxDD `-2.7169`
- `market_context_high->commodity_1h` score `0.8168` n `161` status `ready` deltaP `10.6594` edge `0.0313` maxDD `-0.7439`
- `market_context_high->metal_24h` score `0.4438` n `128` status `ready` deltaP `2.5174` edge `0.0778` maxDD `-2.2743`
- `market_context_high->fx_24h` score `0.4179` n `128` status `ready` deltaP `17.7951` edge `0.0216` maxDD `-1.9329`
- `market_context_high->equity_24h` score `0.0444` n `128` status `ready` deltaP `2.5174` edge `0.2929` maxDD `-21.1456`
- `market_context_high->index_24h` score `-0.2396` n `128` status `ready` deltaP `2.7778` edge `0.1039` maxDD `-5.9181`
- `market_context_high->fx_1h` score `-0.51` n `161` status `ready` deltaP `1.5974` edge `-0.0036` maxDD `-0.9639`
- `market_context_high->metal_1h` score `-0.6904` n `161` status `ready` deltaP `-3.6421` edge `-0.0088` maxDD `-1.4345`
- `market_context_high->index_4h` score `-0.6933` n `149` status `ready` deltaP `-2.7111` edge `-0.0103` maxDD `-1.1743`
- `market_context_high->fx_4h` score `-0.7093` n `149` status `ready` deltaP `2.8677` edge `-0.0029` maxDD `-1.6928`
- `market_context_high->index_1h` score `-1.0394` n `161` status `ready` deltaP `-4.9513` edge `-0.0059` maxDD `-0.8168`
- `market_context_high->metal_4h` score `-1.1325` n `149` status `ready` deltaP `-2.8912` edge `-0.0203` maxDD `-3.1157`
- `market_context_high->equity_1h` score `-1.1723` n `161` status `ready` deltaP `-1.5555` edge `-0.0003` maxDD `-4.6286`
- `market_context_high->crypto_alt_1h` score `-1.4723` n `161` status `ready` deltaP `-9.2098` edge `-0.0404` maxDD `-4.2901`
- `market_context_high->equity_4h` score `-2.7427` n `149` status `ready` deltaP `-3.4396` edge `-0.0719` maxDD `-7.6983`
- `market_context_high->crypto_major_1h` score `-3.6307` n `161` status `ready` deltaP `-11.4237` edge `-0.0645` maxDD `-9.6189`
- `market_context_high->crypto_major_24h` score `-4.2169` n `128` status `ready` deltaP `1.5625` edge `-0.1124` maxDD `-14.2873`
- `market_context_high->crypto_alt_4h` score `-4.2525` n `149` status `ready` deltaP `-9.6047` edge `-0.1247` maxDD `-6.585`
- `market_context_high->crypto_alt_24h` score `-4.7343` n `128` status `ready` deltaP `-13.3681` edge `-0.1611` maxDD `-4.5445`
- `market_context_high->unknown_1h` score `-7.5756` n `161` status `ready` deltaP `-5.2795` edge `-0.5504` maxDD `-1.323`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

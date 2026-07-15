# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-15T14:24:29.714282+00:00`
- Price records: `672`
- Market context records: `6825`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11748`

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

- `market_context_high->unknown_24h` score `0.8952` n `176` status `ready` deltaP `-1.5467` edge `0.5003` maxDD `-12.3511`
- `market_context_high->commodity_24h` score `0.2769` n `176` status `ready` deltaP `10.5745` edge `0.1394` maxDD `-5.2791`
- `market_context_high->crypto_major_1h` score `-0.1564` n `203` status `ready` deltaP `6.2933` edge `0.031` maxDD `-4.2122`
- `market_context_high->crypto_alt_1h` score `-0.27` n `203` status `ready` deltaP `4.0235` edge `0.0271` maxDD `-3.7803`
- `market_context_high->fx_1h` score `-0.3685` n `203` status `ready` deltaP `0.1593` edge `0.0002` maxDD `-0.5468`
- `market_context_high->index_1h` score `-0.7711` n `203` status `ready` deltaP `-3.1149` edge `-0.0033` maxDD `-0.9833`
- `market_context_high->metal_1h` score `-0.9228` n `203` status `ready` deltaP `-5.4962` edge `-0.0078` maxDD `-1.9098`
- `market_context_high->commodity_1h` score `-1.073` n `203` status `ready` deltaP `-2.2359` edge `-0.0062` maxDD `-2.1314`
- `market_context_high->fx_4h` score `-1.2656` n `193` status `ready` deltaP `6.7831` edge `-0.0011` maxDD `-2.1765`
- `market_context_high->commodity_4h` score `-1.4497` n `193` status `ready` deltaP `-3.4911` edge `-0.0136` maxDD `-5.5853`
- `market_context_high->equity_1h` score `-1.6612` n `203` status `ready` deltaP `0.5944` edge `-0.0269` maxDD `-4.9061`
- `market_context_high->unknown_1h` score `-1.6879` n `203` status `ready` deltaP `-4.8538` edge `-0.0182` maxDD `-3.2083`
- `market_context_high->index_4h` score `-1.7055` n `193` status `ready` deltaP `1.8419` edge `-0.027` maxDD `-6.9818`
- `market_context_high->metal_4h` score `-2.7056` n `193` status `ready` deltaP `-3.5179` edge `-0.0251` maxDD `-5.5324`
- `market_context_high->crypto_major_4h` score `-3.0258` n `193` status `ready` deltaP `0.135` edge `-0.0561` maxDD `-16.9508`
- `market_context_high->crypto_alt_4h` score `-3.1884` n `193` status `ready` deltaP `-0.0474` edge `-0.0501` maxDD `-20.6678`
- `market_context_high->unknown_4h` score `-3.3439` n `193` status `ready` deltaP `-11.6557` edge `0.0356` maxDD `-10.2579`
- `market_context_high->fx_24h` score `-4.4552` n `176` status `ready` deltaP `-9.7853` edge `-0.0024` maxDD `-5.6237`
- `market_context_high->equity_4h` score `-5.165` n `193` status `ready` deltaP `-0.6264` edge `-0.1728` maxDD `-31.8159`
- `market_context_high->metal_24h` score `-9.5546` n `176` status `ready` deltaP `-21.2753` edge `-0.2346` maxDD `-28.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

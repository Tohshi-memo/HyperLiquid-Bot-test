# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-15T13:52:28.293725+00:00`
- Price records: `672`
- Market context records: `6822`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11700`

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

- `market_context_high->unknown_24h` score `0.8788` n `176` status `ready` deltaP `-1.5467` edge `0.4982` maxDD `-12.3511`
- `market_context_high->commodity_24h` score `0.3203` n `176` status `ready` deltaP `10.9217` edge `0.1407` maxDD `-5.2791`
- `market_context_high->crypto_major_1h` score `-0.1851` n `203` status `ready` deltaP `6.1436` edge `0.0296` maxDD `-4.2122`
- `market_context_high->crypto_alt_1h` score `-0.3227` n `203` status `ready` deltaP `3.7241` edge `0.0247` maxDD `-3.7803`
- `market_context_high->fx_1h` score `-0.3685` n `203` status `ready` deltaP `0.1593` edge `0.0002` maxDD `-0.5468`
- `market_context_high->index_1h` score `-0.7921` n `203` status `ready` deltaP `-3.4143` edge `-0.004` maxDD `-0.9833`
- `market_context_high->metal_1h` score `-0.9213` n `203` status `ready` deltaP `-5.4962` edge `-0.0076` maxDD `-1.9098`
- `market_context_high->commodity_1h` score `-1.1005` n `203` status `ready` deltaP `-2.5353` edge `-0.0065` maxDD `-2.1314`
- `market_context_high->fx_4h` score `-1.2968` n `191` status `ready` deltaP `6.2731` edge `-0.0017` maxDD `-2.1765`
- `market_context_high->commodity_4h` score `-1.4293` n `191` status `ready` deltaP `-3.2643` edge `-0.0125` maxDD `-5.5853`
- `market_context_high->index_4h` score `-1.6506` n `191` status `ready` deltaP `2.1501` edge `-0.0268` maxDD `-6.5989`
- `market_context_high->unknown_1h` score `-1.6736` n `203` status `ready` deltaP `-4.7041` edge `-0.018` maxDD `-3.2083`
- `market_context_high->equity_1h` score `-1.7091` n `203` status `ready` deltaP `0.4447` edge `-0.0299` maxDD `-4.9061`
- `market_context_high->metal_4h` score `-2.7442` n `191` status `ready` deltaP `-4.0057` edge `-0.0268` maxDD `-5.5324`
- `market_context_high->crypto_major_4h` score `-3.0958` n `191` status `ready` deltaP `-0.1628` edge `-0.0631` maxDD `-16.9508`
- `market_context_high->crypto_alt_4h` score `-3.2672` n `191` status `ready` deltaP `-0.514` edge `-0.0571` maxDD `-20.6678`
- `market_context_high->unknown_4h` score `-3.3767` n `191` status `ready` deltaP `-12.2303` edge `0.0367` maxDD `-10.2579`
- `market_context_high->fx_24h` score `-4.4588` n `176` status `ready` deltaP `-9.7853` edge `-0.0027` maxDD `-5.6237`
- `market_context_high->equity_4h` score `-4.994` n `191` status `ready` deltaP `-0.3616` edge `-0.174` maxDD `-30.1077`
- `market_context_high->metal_24h` score `-9.5906` n `176` status `ready` deltaP `-21.6225` edge `-0.2369` maxDD `-28.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

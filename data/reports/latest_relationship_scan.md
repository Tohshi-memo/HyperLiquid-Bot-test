# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-01T16:52:30.332690+00:00`
- Price records: `672`
- Market context records: `2579`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9200`

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

- `market_context_high->crypto_alt_4h` score `6.2431` n `146` status `ready` deltaP `26.8731` edge `0.609` maxDD `-15.4319`
- `market_context_high->unknown_24h` score `6.0021` n `122` status `ready` deltaP `18.9151` edge `0.4069` maxDD `-1.626`
- `market_context_high->crypto_major_4h` score `4.4004` n `146` status `ready` deltaP `18.2697` edge `0.4259` maxDD `-10.1468`
- `market_context_high->crypto_major_24h` score `1.8958` n `122` status `ready` deltaP `10.2601` edge `0.5201` maxDD `-26.108`
- `market_context_high->crypto_alt_1h` score `1.5415` n `146` status `ready` deltaP `12.0294` edge `0.167` maxDD `-6.1656`
- `market_context_high->unknown_4h` score `1.25` n `146` status `ready` deltaP `9.6663` edge `0.1447` maxDD `-3.7312`
- `market_context_high->crypto_major_1h` score `1.0686` n `146` status `ready` deltaP `10.8092` edge `0.1364` maxDD `-4.2199`
- `market_context_high->equity_24h` score `0.7922` n `122` status `ready` deltaP `17.9901` edge `0.0131` maxDD `-2.3615`
- `market_context_high->index_24h` score `0.6692` n `122` status `ready` deltaP `7.1607` edge `0.1061` maxDD `-2.5127`
- `market_context_high->crypto_alt_24h` score `0.5569` n `122` status `ready` deltaP `1.2352` edge `0.701` maxDD `-39.0265`
- `market_context_high->index_4h` score `0.3544` n `146` status `ready` deltaP `9.4325` edge `0.0508` maxDD `-2.3986`
- `market_context_high->index_1h` score `-0.1599` n `146` status `ready` deltaP `3.642` edge `0.0118` maxDD `-1.2855`
- `market_context_high->unknown_1h` score `-0.4212` n `146` status `ready` deltaP `1.8005` edge `0.0192` maxDD `-2.6375`
- `market_context_high->commodity_1h` score `-0.4626` n `146` status `ready` deltaP `5.2026` edge `0.0146` maxDD `-4.3601`
- `market_context_high->metal_4h` score `-0.5038` n `146` status `ready` deltaP `4.9594` edge `0.0637` maxDD `-4.7664`
- `market_context_high->metal_1h` score `-0.608` n `146` status `ready` deltaP `1.2612` edge `0.0157` maxDD `-2.9823`
- `market_context_high->fx_1h` score `-0.6365` n `146` status `ready` deltaP `-0.5352` edge `0.004` maxDD `-0.278`
- `market_context_high->equity_1h` score `-0.8121` n `146` status `ready` deltaP `-0.3773` edge `0.0187` maxDD `-2.7085`
- `market_context_high->fx_4h` score `-0.8378` n `146` status `ready` deltaP `0.3842` edge `0.0134` maxDD `-0.8621`
- `market_context_high->fx_24h` score `-1.0836` n `122` status `ready` deltaP `1.09` edge `0.0018` maxDD `-1.6157`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-13T19:22:25.917278+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `12738`

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

- `market_context_high->unknown_24h` score `17708.5308` n `56` status `ready` deltaP `10.2093` edge `1475.663` maxDD `-0.613`
- `risk_on_high->unknown_24h` score `7811.7411` n `37` status `ready` deltaP `11.0298` edge `650.9114` maxDD `-0.1869`
- `risk_on_and_context->unknown_24h` score `7811.7411` n `37` status `ready` deltaP `11.0298` edge `650.9114` maxDD `-0.1869`
- `news_risk_high->unknown_1h` score `426.9507` n `82` status `ready` deltaP `-5.1008` edge `35.6554` maxDD `-1.7068`
- `news_risk_high->crypto_alt_24h` score `18.6937` n `82` status `ready` deltaP `36.3751` edge `1.3641` maxDD `-2.2369`
- `news_risk_high->crypto_major_24h` score `18.3652` n `82` status `ready` deltaP `38.0236` edge `1.424` maxDD `-9.098`
- `news_risk_high->equity_24h` score `9.4733` n `82` status `ready` deltaP `27.7881` edge `0.7822` maxDD `-6.5742`
- `news_risk_high->index_24h` score `7.1889` n `82` status `ready` deltaP `51.5601` edge `0.273` maxDD `-0.0797`
- `news_risk_high->metal_24h` score `4.7532` n `82` status `ready` deltaP `26.3121` edge `0.2661` maxDD `-0.6334`
- `risk_on_high->commodity_24h` score `4.667` n `37` status `ready` deltaP `39.8276` edge `0.1234` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `4.667` n `37` status `ready` deltaP `39.8276` edge `0.1234` maxDD `0.0`
- `market_context_high->commodity_24h` score `4.5038` n `56` status `ready` deltaP `39.8276` edge `0.1098` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `2.41` n `56` status `ready` deltaP `3.4483` edge `0.4521` maxDD `-9.6226`
- `risk_on_high->crypto_alt_24h` score `2.407` n `37` status `ready` deltaP `2.0969` edge `0.4282` maxDD `-7.0204`
- `risk_on_and_context->crypto_alt_24h` score `2.407` n `37` status `ready` deltaP `2.0969` edge `0.4282` maxDD `-7.0204`
- `risk_on_high->fx_24h` score `1.2643` n `37` status `ready` deltaP `34.3477` edge `0.0078` maxDD `-1.6425`
- `risk_on_and_context->fx_24h` score `1.2643` n `37` status `ready` deltaP `34.3477` edge `0.0078` maxDD `-1.6425`
- `risk_on_high->commodity_4h` score `0.7694` n `59` status `ready` deltaP `13.8332` edge `0.0088` maxDD `-0.286`
- `risk_on_and_context->commodity_4h` score `0.7694` n `59` status `ready` deltaP `13.8332` edge `0.0088` maxDD `-0.286`
- `market_context_high->commodity_4h` score `0.6427` n `131` status `ready` deltaP `13.2122` edge `0.0117` maxDD `-0.3645`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

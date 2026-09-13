# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-13T12:37:30.673555+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `12980`

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

- `market_context_high->unknown_24h` score `17093.6572` n `58` status `ready` deltaP `11.7241` edge `1424.4077` maxDD `-0.4878`
- `news_risk_high->unknown_1h` score `411.7323` n `82` status `ready` deltaP `-4.9511` edge `34.3862` maxDD `-1.7068`
- `news_risk_high->crypto_alt_24h` score `18.0542` n `82` status `ready` deltaP `33.9613` edge `1.3269` maxDD `-2.2369`
- `news_risk_high->crypto_major_24h` score `18.0466` n `82` status `ready` deltaP `37.8512` edge `1.3986` maxDD `-9.098`
- `market_context_high->crypto_alt_24h` score `10.1386` n `58` status `ready` deltaP `23.4483` edge `0.7713` maxDD `-3.9523`
- `news_risk_high->equity_24h` score `8.0041` n `82` status `ready` deltaP `23.1329` edge `0.6908` maxDD `-6.5742`
- `market_context_high->equity_24h` score `7.5327` n `58` status `ready` deltaP `41.5517` edge `0.4819` maxDD `-8.1614`
- `news_risk_high->index_24h` score `6.709` n `82` status `ready` deltaP `47.767` edge `0.2583` maxDD `-0.0797`
- `news_risk_high->metal_24h` score `4.5696` n `82` status `ready` deltaP `24.2431` edge `0.2646` maxDD `-0.6334`
- `market_context_high->commodity_24h` score `4.0502` n `58` status `ready` deltaP `39.8276` edge `0.072` maxDD `0.0`
- `market_context_high->index_24h` score `3.8211` n `58` status `ready` deltaP `42.931` edge `0.0778` maxDD `-1.3132`
- `market_context_high->metal_24h` score `1.1652` n `58` status `ready` deltaP `14.6552` edge `0.1199` maxDD `-1.4572`
- `risk_on_high->crypto_alt_4h` score `0.5219` n `65` status `ready` deltaP `11.4416` edge `0.1581` maxDD `-6.7304`
- `risk_on_and_context->crypto_alt_4h` score `0.5219` n `65` status `ready` deltaP `11.4416` edge `0.1581` maxDD `-6.7304`
- `news_risk_high->index_4h` score `0.429` n `82` status `ready` deltaP `12.5745` edge `0.034` maxDD `-0.6935`
- `risk_on_high->fx_1h` score `0.0861` n `65` status `ready` deltaP `4.4035` edge `0.0034` maxDD `-0.0464`
- `risk_on_and_context->fx_1h` score `0.0861` n `65` status `ready` deltaP `4.4035` edge `0.0034` maxDD `-0.0464`
- `market_context_high->fx_1h` score `0.0018` n `144` status `ready` deltaP `4.8736` edge `-0.0006` maxDD `-0.5323`
- `risk_on_high->metal_1h` score `-0.0113` n `65` status `ready` deltaP `4.5117` edge `0.002` maxDD `-0.3081`
- `risk_on_and_context->metal_1h` score `-0.0113` n `65` status `ready` deltaP `4.5117` edge `0.002` maxDD `-0.3081`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

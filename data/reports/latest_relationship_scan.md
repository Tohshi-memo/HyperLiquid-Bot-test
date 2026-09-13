# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-13T12:21:08.517061+00:00`
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

- `market_context_high->unknown_24h` score `17136.74` n `58` status `ready` deltaP `13.2759` edge `1427.9817` maxDD `-0.35`
- `news_risk_high->unknown_1h` score `410.6151` n `82` status `ready` deltaP `-5.1008` edge `34.2941` maxDD `-1.7068`
- `news_risk_high->crypto_alt_24h` score `18.0446` n `82` status `ready` deltaP `33.9613` edge `1.3261` maxDD `-2.2369`
- `news_risk_high->crypto_major_24h` score `18.0202` n `82` status `ready` deltaP `37.8512` edge `1.3964` maxDD `-9.098`
- `market_context_high->crypto_alt_24h` score `10.2202` n `58` status `ready` deltaP `23.4483` edge `0.7781` maxDD `-3.9523`
- `market_context_high->equity_24h` score `8.3872` n `58` status `ready` deltaP `43.1035` edge `0.5147` maxDD `-6.2498`
- `news_risk_high->equity_24h` score `7.9459` n `82` status `ready` deltaP `22.9605` edge `0.6871` maxDD `-6.5742`
- `news_risk_high->index_24h` score `6.703` n `82` status `ready` deltaP `47.767` edge `0.2578` maxDD `-0.0797`
- `news_risk_high->metal_24h` score `4.572` n `82` status `ready` deltaP `24.2431` edge `0.2648` maxDD `-0.6334`
- `market_context_high->commodity_24h` score `4.0394` n `58` status `ready` deltaP `39.8276` edge `0.0711` maxDD `0.0`
- `market_context_high->index_24h` score `3.9708` n `58` status `ready` deltaP `42.931` edge `0.0822` maxDD `-1.0005`
- `market_context_high->metal_24h` score `1.094` n `58` status `ready` deltaP `14.6552` edge `0.1177` maxDD `-1.6786`
- `risk_on_high->crypto_alt_4h` score `0.5359` n `65` status `ready` deltaP `11.5152` edge `0.1594` maxDD `-6.7304`
- `risk_on_and_context->crypto_alt_4h` score `0.5359` n `65` status `ready` deltaP `11.5152` edge `0.1594` maxDD `-6.7304`
- `news_risk_high->index_4h` score `0.4329` n `82` status `ready` deltaP `12.6496` edge `0.034` maxDD `-0.6935`
- `risk_on_high->fx_1h` score `0.0861` n `65` status `ready` deltaP `4.4035` edge `0.0034` maxDD `-0.0464`
- `risk_on_and_context->fx_1h` score `0.0861` n `65` status `ready` deltaP `4.4035` edge `0.0034` maxDD `-0.0464`
- `market_context_high->fx_1h` score `0.0011` n `144` status `ready` deltaP `4.8736` edge `-0.0007` maxDD `-0.5323`
- `risk_on_high->metal_1h` score `-0.0233` n `65` status `ready` deltaP `4.362` edge `0.002` maxDD `-0.3081`
- `risk_on_and_context->metal_1h` score `-0.0233` n `65` status `ready` deltaP `4.362` edge `0.002` maxDD `-0.3081`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

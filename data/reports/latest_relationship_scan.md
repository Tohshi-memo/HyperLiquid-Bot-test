# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-13T09:37:27.004875+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `12964`

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

- `market_context_high->unknown_24h` score `16656.6858` n `59` status `ready` deltaP `13.5068` edge `1387.9723` maxDD `-0.082`
- `news_risk_high->unknown_1h` score `397.7499` n `82` status `ready` deltaP `-5.3415` edge `33.2236` maxDD `-1.7068`
- `news_risk_high->crypto_major_24h` score `17.773` n `82` status `ready` deltaP `37.8512` edge `1.3758` maxDD `-9.098`
- `news_risk_high->crypto_alt_24h` score `17.7254` n `82` status `ready` deltaP `32.2371` edge `1.311` maxDD `-2.2369`
- `market_context_high->crypto_alt_24h` score `10.0057` n `59` status `ready` deltaP `22.1917` edge `0.7686` maxDD `-3.9523`
- `market_context_high->equity_24h` score `8.6497` n `59` status `ready` deltaP `43.0771` edge `0.5096` maxDD `-4.4114`
- `news_risk_high->equity_24h` score `7.3274` n `82` status `ready` deltaP `21.0639` edge `0.6482` maxDD `-6.5742`
- `news_risk_high->index_24h` score `6.5093` n `82` status `ready` deltaP `46.2153` edge `0.252` maxDD `-0.0797`
- `news_risk_high->metal_24h` score `4.5852` n `82` status `ready` deltaP `24.2431` edge `0.2659` maxDD `-0.6334`
- `market_context_high->commodity_24h` score `4.1798` n `59` status `ready` deltaP `41.2069` edge `0.0736` maxDD `0.0`
- `market_context_high->index_24h` score `3.66` n `59` status `ready` deltaP `40.0351` edge `0.0802` maxDD `-0.7014`
- `market_context_high->metal_24h` score `0.9162` n `59` status `ready` deltaP `13.5155` edge `0.1148` maxDD `-1.9958`
- `risk_on_high->crypto_alt_4h` score `0.4036` n `65` status `ready` deltaP `10.6061` edge `0.1485` maxDD `-6.7304`
- `risk_on_and_context->crypto_alt_4h` score `0.4036` n `65` status `ready` deltaP `10.6061` edge `0.1485` maxDD `-6.7304`
- `news_risk_high->index_4h` score `0.3936` n `82` status `ready` deltaP `12.1951` edge `0.032` maxDD `-0.6935`
- `risk_on_high->fx_1h` score `0.1021` n `65` status `ready` deltaP `4.6177` edge `0.0033` maxDD `-0.0464`
- `risk_on_and_context->fx_1h` score `0.1021` n `65` status `ready` deltaP `4.6177` edge `0.0033` maxDD `-0.0464`
- `risk_on_high->metal_1h` score `-0.0806` n `65` status `ready` deltaP `3.6753` edge `0.0018` maxDD `-0.3081`
- `risk_on_and_context->metal_1h` score `-0.0806` n `65` status `ready` deltaP `3.6753` edge `0.0018` maxDD `-0.3081`
- `market_context_high->fx_1h` score `-0.1515` n `138` status `ready` deltaP `3.0346` edge `-0.0012` maxDD `-0.5323`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

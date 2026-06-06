# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-06T16:22:21.648762+00:00`
- Price records: `672`
- Market context records: `3090`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6911`

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

- `market_context_high->crypto_alt_24h` score `17.0562` n `85` status `ready` deltaP `13.1495` edge `2.5402` maxDD `-26.6275`
- `market_context_high->commodity_24h` score `15.0856` n `85` status `ready` deltaP `45.4882` edge `0.9967` maxDD `-2.0927`
- `market_context_high->unknown_24h` score `14.4649` n `85` status `ready` deltaP `22.2263` edge `1.1037` maxDD `-1.7175`
- `market_context_high->index_24h` score `11.9655` n `85` status `ready` deltaP `34.6487` edge `0.9475` maxDD `-11.5093`
- `market_context_high->equity_24h` score `9.2453` n `85` status `ready` deltaP `22.3264` edge `1.4709` maxDD `-30.0893`
- `market_context_high->commodity_4h` score `2.9548` n `119` status `ready` deltaP `17.9301` edge `0.1725` maxDD `-1.9973`
- `market_context_high->unknown_4h` score `0.2973` n `119` status `ready` deltaP `4.0979` edge `0.0939` maxDD `-3.3825`
- `market_context_high->commodity_1h` score `-0.1609` n `125` status `ready` deltaP `0.6527` edge `0.0245` maxDD `-1.7142`
- `market_context_high->index_1h` score `-0.5223` n `125` status `ready` deltaP `3.497` edge `0.016` maxDD `-4.5023`
- `market_context_high->fx_1h` score `-0.7286` n `125` status `ready` deltaP `-8.1521` edge `-0.0018` maxDD `-0.3147`
- `market_context_high->crypto_alt_1h` score `-0.7624` n `125` status `ready` deltaP `3.6467` edge `0.0909` maxDD `-14.7034`
- `market_context_high->fx_24h` score `-0.9553` n `85` status `ready` deltaP `1.6074` edge `-0.0048` maxDD `-0.5088`
- `market_context_high->equity_1h` score `-1.2377` n `125` status `ready` deltaP `-1.4994` edge `-0.0001` maxDD `-8.8863`
- `market_context_high->fx_4h` score `-1.3515` n `119` status `ready` deltaP `-12.4193` edge `-0.0061` maxDD `-1.0829`
- `market_context_high->index_4h` score `-1.4616` n `119` status `ready` deltaP `8.9722` edge `0.0437` maxDD `-17.6057`
- `market_context_high->crypto_major_1h` score `-2.0228` n `125` status `ready` deltaP `-0.012` edge `0.0578` maxDD `-15.1032`
- `market_context_high->unknown_1h` score `-2.3166` n `125` status `ready` deltaP `1.3078` edge `-0.0578` maxDD `-9.1843`
- `market_context_high->metal_1h` score `-2.3324` n `125` status `ready` deltaP `-6.6599` edge `-0.0106` maxDD `-7.4828`
- `market_context_high->crypto_alt_4h` score `-3.3357` n `119` status `ready` deltaP `16.2034` edge `0.2688` maxDD `-58.6918`
- `market_context_high->equity_4h` score `-3.8584` n `119` status `ready` deltaP `7.6783` edge `-0.022` maxDD `-36.242`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-27T13:22:29.145325+00:00`
- Price records: `672`
- Market context records: `4937`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `9400`

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

- `market_context_high->unknown_1h` score `18.9547` n `97` status `ready` deltaP `11.672` edge `1.5435` maxDD `-1.674`
- `market_context_high->unknown_4h` score `11.9247` n `97` status `ready` deltaP `28.8518` edge `0.8528` maxDD `-1.7801`
- `market_context_high->crypto_major_4h` score `7.248` n `97` status `ready` deltaP `21.2424` edge `0.5848` maxDD `-7.1265`
- `market_context_high->crypto_alt_4h` score `7.18` n `97` status `ready` deltaP `22.6584` edge `0.5825` maxDD `-7.8181`
- `market_context_high->unknown_24h` score `6.0264` n `86` status `ready` deltaP `26.5141` edge `0.3597` maxDD `-1.4072`
- `market_context_high->equity_4h` score `1.8689` n `97` status `ready` deltaP `15.9432` edge `0.1876` maxDD `-6.3852`
- `market_context_high->metal_4h` score `1.5487` n `97` status `ready` deltaP `11.8038` edge `0.1166` maxDD `-1.9651`
- `market_context_high->crypto_major_1h` score `1.2871` n `97` status `ready` deltaP `7.7998` edge `0.1591` maxDD `-5.6406`
- `market_context_high->index_4h` score `0.9778` n `97` status `ready` deltaP `12.654` edge `0.0433` maxDD `-0.6938`
- `market_context_high->equity_1h` score `0.8737` n `97` status `ready` deltaP `7.5823` edge `0.0796` maxDD `-2.5875`
- `market_context_high->crypto_alt_1h` score `0.645` n `97` status `ready` deltaP `8.6302` edge `0.1274` maxDD `-5.5126`
- `market_context_high->metal_1h` score `0.1069` n `97` status `ready` deltaP `4.5743` edge `0.0364` maxDD `-1.3057`
- `market_context_high->commodity_1h` score `-0.4019` n `97` status `ready` deltaP `1.2979` edge `0.0058` maxDD `-1.278`
- `market_context_high->index_1h` score `-0.4219` n `97` status `ready` deltaP `1.3797` edge `0.0122` maxDD `-0.7054`
- `market_context_high->commodity_4h` score `-1.0058` n `97` status `ready` deltaP `5.843` edge `-0.0041` maxDD `-4.4933`
- `market_context_high->fx_4h` score `-1.0875` n `97` status `ready` deltaP `-5.7864` edge `-0.0038` maxDD `-1.0967`
- `market_context_high->fx_1h` score `-1.4418` n `97` status `ready` deltaP `-8.1132` edge `-0.0048` maxDD `-0.5675`
- `market_context_high->fx_24h` score `-1.6309` n `86` status `ready` deltaP `-3.0725` edge `-0.0144` maxDD `-2.749`
- `market_context_high->commodity_24h` score `-4.9788` n `86` status `ready` deltaP `13.9616` edge `0.0029` maxDD `-27.5371`
- `market_context_high->metal_24h` score `-7.4464` n `86` status `ready` deltaP `-12.2174` edge `0.0064` maxDD `-32.9721`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

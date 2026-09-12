# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-12T12:22:29.800789+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `12066`

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

- `market_context_high->unknown_24h` score `3840.1445` n `106` status `ready` deltaP `13.5646` edge `319.9268` maxDD `-0.082`
- `risk_on_high->unknown_24h` score `929.7253` n `57` status `ready` deltaP `15.4514` edge `77.3741` maxDD `0.0`
- `risk_on_and_context->unknown_24h` score `929.7253` n `57` status `ready` deltaP `15.4514` edge `77.3741` maxDD `0.0`
- `news_risk_high->unknown_1h` score `383.1002` n `82` status `ready` deltaP `-4.502` edge `31.9972` maxDD `-1.7068`
- `news_risk_high->crypto_major_24h` score `24.4034` n `59` status `ready` deltaP `54.505` edge `1.7603` maxDD `-5.8705`
- `risk_on_high->crypto_alt_24h` score `18.9229` n `57` status `ready` deltaP `39.8392` edge `1.3343` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `18.9229` n `57` status `ready` deltaP `39.8392` edge `1.3343` maxDD `-0.8386`
- `news_risk_high->crypto_alt_24h` score `17.527` n `59` status `ready` deltaP `29.967` edge `1.3096` maxDD `-2.2369`
- `market_context_high->crypto_alt_24h` score `16.3873` n `106` status `ready` deltaP `33.5168` edge `1.2249` maxDD `-3.9523`
- `news_risk_high->equity_24h` score `12.2687` n `59` status `ready` deltaP `33.9366` edge `0.806` maxDD `-0.1212`
- `risk_on_high->equity_24h` score `8.8673` n `57` status `ready` deltaP `37.3264` edge `0.4901` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `8.8673` n `57` status `ready` deltaP `37.3264` edge `0.4901` maxDD `0.0`
- `market_context_high->equity_24h` score `8.6141` n `106` status `ready` deltaP `37.3264` edge `0.469` maxDD `0.0`
- `risk_on_high->crypto_alt_4h` score `8.4856` n `57` status `ready` deltaP `41.6105` edge `0.4669` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `8.4856` n `57` status `ready` deltaP `41.6105` edge `0.4669` maxDD `-1.9733`
- `news_risk_high->metal_24h` score `8.3825` n `59` status `ready` deltaP `53.6458` edge `0.3409` maxDD `0.0`
- `news_risk_high->index_24h` score `7.9045` n `59` status `ready` deltaP `51.4713` edge `0.3249` maxDD `-0.0797`
- `risk_on_high->index_24h` score `4.8759` n `57` status `ready` deltaP `49.5979` edge `0.0799` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `4.8759` n `57` status `ready` deltaP `49.5979` edge `0.0799` maxDD `-0.0051`
- `risk_on_high->equity_4h` score `4.2201` n `57` status `ready` deltaP `37.7996` edge `0.109` maxDD `-0.079`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

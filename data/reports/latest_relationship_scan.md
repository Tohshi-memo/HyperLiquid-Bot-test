# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-12T08:07:26.731898+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11791`

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

- `market_context_high->unknown_24h` score `2150.9745` n `123` status `ready` deltaP `13.8254` edge `179.1609` maxDD `-0.082`
- `news_risk_high->unknown_1h` score `383.3028` n `82` status `ready` deltaP `-3.1547` edge `32.0051` maxDD `-1.7068`
- `news_risk_high->crypto_major_24h` score `24.2618` n `59` status `ready` deltaP `54.505` edge `1.7485` maxDD `-5.8705`
- `risk_on_high->crypto_alt_24h` score `22.2256` n `73` status `ready` deltaP `41.7618` edge `1.5967` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `22.2256` n `73` status `ready` deltaP `41.7618` edge `1.5967` maxDD `-0.8386`
- `market_context_high->crypto_alt_24h` score `18.725` n `123` status `ready` deltaP `35.603` edge `1.4058` maxDD `-3.9523`
- `news_risk_high->crypto_alt_24h` score `17.605` n `59` status `ready` deltaP `29.967` edge `1.3161` maxDD `-2.2369`
- `news_risk_high->equity_24h` score `12.1174` n `59` status `ready` deltaP `33.5894` edge `0.7957` maxDD `-0.1212`
- `risk_on_high->equity_24h` score `9.0195` n `73` status `ready` deltaP `36.9792` edge `0.5051` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `9.0195` n `73` status `ready` deltaP `36.9792` edge `0.5051` maxDD `0.0`
- `market_context_high->equity_24h` score `8.6847` n `123` status `ready` deltaP `36.9792` edge `0.4772` maxDD `0.0`
- `news_risk_high->metal_24h` score `8.2376` n `59` status `ready` deltaP `51.9097` edge `0.3404` maxDD `0.0`
- `risk_on_high->crypto_alt_4h` score `8.1659` n `73` status `ready` deltaP `43.1485` edge `0.43` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `8.1659` n `73` status `ready` deltaP `43.1485` edge `0.43` maxDD `-1.9733`
- `news_risk_high->index_24h` score `7.9153` n `59` status `ready` deltaP `51.4713` edge `0.3258` maxDD `-0.0797`
- `risk_on_high->crypto_major_4h` score `5.6841` n `73` status `ready` deltaP `28.0864` edge `0.3723` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `5.6841` n `73` status `ready` deltaP `28.0864` edge `0.3723` maxDD `-3.8693`
- `risk_on_high->index_24h` score `5.0774` n `73` status `ready` deltaP `50.7515` edge `0.089` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `5.0774` n `73` status `ready` deltaP `50.7515` edge `0.089` maxDD `-0.0051`
- `risk_on_high->crypto_major_24h` score `4.0303` n `73` status `ready` deltaP `16.0792` edge `0.8163` maxDD `-24.5429`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

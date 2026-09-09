# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-09T21:37:26.195882+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10146`

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

- `risk_on_high->crypto_alt_24h` score `12.2503` n `117` status `ready` deltaP `25.7612` edge `0.8721` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `12.2503` n `117` status `ready` deltaP `25.7612` edge `0.8721` maxDD `-0.8386`
- `market_context_high->crypto_alt_24h` score `7.2029` n `241` status `ready` deltaP `18.4164` edge `0.5602` maxDD `-3.9523`
- `risk_on_high->crypto_major_24h` score `6.5574` n `117` status `ready` deltaP `21.4477` edge `1.1045` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `6.5574` n `117` status `ready` deltaP `21.4477` edge `1.1045` maxDD `-24.5429`
- `risk_on_high->crypto_alt_4h` score `6.2121` n `117` status `ready` deltaP `34.446` edge `0.3252` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `6.2121` n `117` status `ready` deltaP `34.446` edge `0.3252` maxDD `-1.9733`
- `risk_on_high->crypto_major_4h` score `4.3283` n `117` status `ready` deltaP `24.6092` edge `0.2825` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `4.3283` n `117` status `ready` deltaP `24.6092` edge `0.2825` maxDD `-3.8693`
- `risk_on_high->index_24h` score `2.5986` n `117` status `ready` deltaP `26.0817` edge `0.0469` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `2.5986` n `117` status `ready` deltaP `26.0817` edge `0.0469` maxDD `-0.0051`
- `market_context_high->index_24h` score `1.8771` n `241` status `ready` deltaP `21.1769` edge `0.0546` maxDD `-0.1483`
- `market_context_high->equity_24h` score `1.6183` n `241` status `ready` deltaP `9.5486` edge `0.0712` maxDD `0.0`
- `risk_on_high->crypto_alt_1h` score `1.0365` n `117` status `ready` deltaP `4.097` edge `0.0943` maxDD `-1.1521`
- `risk_on_and_context->crypto_alt_1h` score `1.0365` n `117` status `ready` deltaP `4.097` edge `0.0943` maxDD `-1.1521`
- `risk_on_high->equity_24h` score `0.9331` n `117` status `ready` deltaP `9.5486` edge `0.0141` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `0.9331` n `117` status `ready` deltaP `9.5486` edge `0.0141` maxDD `0.0`
- `risk_on_high->metal_24h` score `0.7855` n `117` status `ready` deltaP `19.7383` edge `0.0847` maxDD `-0.9131`
- `risk_on_and_context->metal_24h` score `0.7855` n `117` status `ready` deltaP `19.7383` edge `0.0847` maxDD `-0.9131`
- `risk_on_high->equity_1h` score `0.4425` n `117` status `ready` deltaP `14.3726` edge `-0.0058` maxDD `-2.2516`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

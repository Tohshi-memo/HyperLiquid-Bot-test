# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-23T03:37:31.614427+00:00`
- Price records: `672`
- Market context records: `4478`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11059`

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

- `risk_on_high->unknown_4h` score `124.0716` n `49` status `ready` deltaP `3.2634` edge `10.5006` maxDD `-10.9781`
- `risk_on_and_context->unknown_4h` score `124.0716` n `49` status `ready` deltaP `3.2634` edge `10.5006` maxDD `-10.9781`
- `market_context_high->unknown_1h` score `32.6379` n `229` status `ready` deltaP `3.551` edge `2.8467` maxDD `-9.7103`
- `market_context_high->unknown_4h` score `14.832` n `229` status `ready` deltaP `3.8962` edge `1.7565` maxDD `-36.0512`
- `risk_on_high->equity_4h` score `4.1046` n `49` status `ready` deltaP `38.872` edge `0.0829` maxDD `0.0`
- `risk_on_and_context->equity_4h` score `4.1046` n `49` status `ready` deltaP `38.872` edge `0.0829` maxDD `0.0`
- `risk_on_high->metal_24h` score `3.3427` n `44` status `ready` deltaP `-13.0997` edge `0.5773` maxDD `-1.9133`
- `risk_on_and_context->metal_24h` score `3.3427` n `44` status `ready` deltaP `-13.0997` edge `0.5773` maxDD `-1.9133`
- `risk_on_high->equity_24h` score `2.8657` n `44` status `ready` deltaP `23.6111` edge `0.0814` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `2.8657` n `44` status `ready` deltaP `23.6111` edge `0.0814` maxDD `0.0`
- `risk_on_high->unknown_24h` score `2.7343` n `44` status `ready` deltaP `14.173` edge `0.2137` maxDD `-5.0928`
- `risk_on_and_context->unknown_24h` score `2.7343` n `44` status `ready` deltaP `14.173` edge `0.2137` maxDD `-5.0928`
- `risk_on_high->crypto_major_4h` score `2.5803` n `49` status `ready` deltaP `20.937` edge `0.142` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `2.5803` n `49` status `ready` deltaP `20.937` edge `0.142` maxDD `-2.6576`
- `risk_on_high->index_24h` score `2.3868` n `44` status `ready` deltaP `25.6944` edge `0.0276` maxDD `0.0`
- `risk_on_and_context->index_24h` score `2.3868` n `44` status `ready` deltaP `25.6944` edge `0.0276` maxDD `0.0`
- `risk_on_high->metal_4h` score `1.5264` n `49` status `ready` deltaP `12.7146` edge `0.076` maxDD `-1.3516`
- `risk_on_and_context->metal_4h` score `1.5264` n `49` status `ready` deltaP `12.7146` edge `0.076` maxDD `-1.3516`
- `risk_on_high->equity_1h` score `1.1169` n `49` status `ready` deltaP `14.6921` edge `0.0294` maxDD `-0.7415`
- `risk_on_and_context->equity_1h` score `1.1169` n `49` status `ready` deltaP `14.6921` edge `0.0294` maxDD `-0.7415`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

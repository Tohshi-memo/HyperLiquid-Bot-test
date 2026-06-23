# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-23T06:52:25.487957+00:00`
- Price records: `672`
- Market context records: `4492`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11169`

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

- `risk_on_high->unknown_4h` score `124.3031` n `49` status `ready` deltaP `4.1781` edge `10.5138` maxDD `-10.9781`
- `risk_on_and_context->unknown_4h` score `124.3031` n `49` status `ready` deltaP `4.1781` edge `10.5138` maxDD `-10.9781`
- `market_context_high->unknown_1h` score `36.1139` n `216` status `ready` deltaP `3.2602` edge `3.1383` maxDD `-9.7103`
- `market_context_high->unknown_4h` score `16.7128` n `216` status `ready` deltaP `2.7609` edge `1.9208` maxDD `-36.0512`
- `risk_on_high->equity_4h` score `4.6437` n `49` status `ready` deltaP `40.0915` edge `0.1197` maxDD `0.0`
- `risk_on_and_context->equity_4h` score `4.6437` n `49` status `ready` deltaP `40.0915` edge `0.1197` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `3.0095` n `49` status `ready` deltaP `22.4614` edge `0.1676` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `3.0095` n `49` status `ready` deltaP `22.4614` edge `0.1676` maxDD `-2.6576`
- `risk_on_high->metal_24h` score `2.1981` n `49` status `ready` deltaP `-14.7853` edge `0.4783` maxDD `-4.834`
- `risk_on_and_context->metal_24h` score `2.1981` n `49` status `ready` deltaP `-14.7853` edge `0.4783` maxDD `-4.834`
- `risk_on_high->unknown_24h` score `2.0736` n `49` status `ready` deltaP `12.8436` edge `0.1675` maxDD `-5.0928`
- `risk_on_and_context->unknown_24h` score `2.0736` n `49` status `ready` deltaP `12.8436` edge `0.1675` maxDD `-5.0928`
- `risk_on_high->metal_4h` score `1.802` n `49` status `ready` deltaP `14.239` edge `0.0888` maxDD `-1.3516`
- `risk_on_and_context->metal_4h` score `1.802` n `49` status `ready` deltaP `14.239` edge `0.0888` maxDD `-1.3516`
- `risk_on_high->equity_1h` score `1.3388` n `49` status `ready` deltaP `15.8897` edge `0.0399` maxDD `-0.7415`
- `risk_on_and_context->equity_1h` score `1.3388` n `49` status `ready` deltaP `15.8897` edge `0.0399` maxDD `-0.7415`
- `risk_on_high->fx_4h` score `0.6217` n `49` status `ready` deltaP `15.5519` edge `0.0072` maxDD `-0.3925`
- `risk_on_and_context->fx_4h` score `0.6217` n `49` status `ready` deltaP `15.5519` edge `0.0072` maxDD `-0.3925`
- `risk_on_high->index_24h` score `0.4681` n `49` status `ready` deltaP `17.7473` edge `-0.0276` maxDD `-2.4702`
- `risk_on_and_context->index_24h` score `0.4681` n `49` status `ready` deltaP `17.7473` edge `-0.0276` maxDD `-2.4702`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

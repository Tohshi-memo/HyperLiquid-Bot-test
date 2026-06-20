# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-20T12:52:25.889730+00:00`
- Price records: `672`
- Market context records: `4209`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9632`

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

- `risk_on_high->unknown_4h` score `145.6401` n `40` status `ready` deltaP `-7.2866` edge `12.3671` maxDD `-10.8809`
- `risk_on_and_context->unknown_4h` score `145.6401` n `40` status `ready` deltaP `-7.2866` edge `12.3671` maxDD `-10.8809`
- `market_context_high->unknown_1h` score `32.6966` n `209` status `ready` deltaP `1.7807` edge `2.8708` maxDD `-9.6361`
- `market_context_high->unknown_4h` score `9.4347` n `207` status `ready` deltaP `-3.4339` edge `1.3521` maxDD `-35.7719`
- `market_context_high->unknown_24h` score `7.7531` n `198` status `ready` deltaP `-12.3064` edge `1.1315` maxDD `-24.2693`
- `risk_on_high->commodity_24h` score `2.4431` n `40` status `ready` deltaP `4.6265` edge `0.4009` maxDD `-12.9187`
- `risk_on_and_context->commodity_24h` score `2.4431` n `40` status `ready` deltaP `4.6265` edge `0.4009` maxDD `-12.9187`
- `risk_on_high->equity_4h` score `2.1317` n `40` status `ready` deltaP `32.4085` edge `-0.0337` maxDD `-0.044`
- `risk_on_and_context->equity_4h` score `2.1317` n `40` status `ready` deltaP `32.4085` edge `-0.0337` maxDD `-0.044`
- `risk_on_high->crypto_major_4h` score `0.5762` n `40` status `ready` deltaP `13.811` edge `0.0225` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `0.5762` n `40` status `ready` deltaP `13.811` edge `0.0225` maxDD `-2.6576`
- `risk_on_high->metal_4h` score `0.0925` n `40` status `ready` deltaP `8.6585` edge `-0.0123` maxDD `-1.3516`
- `risk_on_and_context->metal_4h` score `0.0925` n `40` status `ready` deltaP `8.6585` edge `-0.0123` maxDD `-1.3516`
- `risk_on_high->equity_1h` score `0.0914` n `40` status `ready` deltaP `9.4162` edge `-0.0162` maxDD `-0.7834`
- `risk_on_and_context->equity_1h` score `0.0914` n `40` status `ready` deltaP `9.4162` edge `-0.0162` maxDD `-0.7834`
- `risk_on_high->crypto_major_1h` score `0.0372` n `40` status `ready` deltaP `9.012` edge `-0.0011` maxDD `-2.3372`
- `risk_on_and_context->crypto_major_1h` score `0.0372` n `40` status `ready` deltaP `9.012` edge `-0.0011` maxDD `-2.3372`
- `risk_on_high->fx_4h` score `0.0025` n `40` status `ready` deltaP `8.4146` edge `0.0033` maxDD `-0.3925`
- `risk_on_and_context->fx_4h` score `0.0025` n `40` status `ready` deltaP `8.4146` edge `0.0033` maxDD `-0.3925`
- `risk_on_high->fx_1h` score `-0.0156` n `40` status `ready` deltaP `3.0539` edge `0.0006` maxDD `-0.1704`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-16T03:37:43.019264+00:00`
- Price records: `672`
- Market context records: `4054`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10432`

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

- `risk_on_high->unknown_4h` score `144.9813` n `40` status `ready` deltaP `-7.439` edge `12.313` maxDD `-10.864`
- `risk_on_and_context->unknown_4h` score `144.9813` n `40` status `ready` deltaP `-7.439` edge `12.313` maxDD `-10.864`
- `market_context_high->unknown_24h` score `38.4209` n `143` status `ready` deltaP `-7.725` edge `3.6561` maxDD `-24.2289`
- `market_context_high->unknown_4h` score `20.0326` n `162` status `ready` deltaP `-0.1242` edge `2.2125` maxDD `-35.7161`
- `risk_on_high->equity_4h` score `3.8292` n `40` status `ready` deltaP `38.6585` edge `0.0661` maxDD `-0.0446`
- `risk_on_and_context->equity_4h` score `3.8292` n `40` status `ready` deltaP `38.6585` edge `0.0661` maxDD `-0.0446`
- `risk_on_high->equity_24h` score `3.5686` n `40` status `ready` deltaP `33.1023` edge `0.0767` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `3.5686` n `40` status `ready` deltaP `33.1023` edge `0.0767` maxDD `0.0`
- `market_context_high->index_24h` score `2.0458` n `143` status `ready` deltaP `20.0979` edge `0.0577` maxDD `-1.3629`
- `market_context_high->equity_4h` score `1.409` n `162` status `ready` deltaP `14.6153` edge `0.1689` maxDD `-6.9137`
- `risk_on_high->crypto_major_4h` score `1.3572` n `40` status `ready` deltaP `20.2134` edge `0.0449` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `1.3572` n `40` status `ready` deltaP `20.2134` edge `0.0449` maxDD `-2.6576`
- `market_context_high->equity_1h` score `0.8288` n `173` status `ready` deltaP `6.4397` edge `0.0821` maxDD `-2.144`
- `risk_on_high->equity_1h` score `0.4963` n `40` status `ready` deltaP `11.512` edge `0.0037` maxDD `-0.7937`
- `risk_on_and_context->equity_1h` score `0.4963` n `40` status `ready` deltaP `11.512` edge `0.0037` maxDD `-0.7937`
- `risk_on_high->crypto_major_1h` score `0.2201` n `40` status `ready` deltaP `12.7545` edge `-0.0026` maxDD `-2.3372`
- `risk_on_and_context->crypto_major_1h` score `0.2201` n `40` status `ready` deltaP `12.7545` edge `-0.0026` maxDD `-2.3372`
- `risk_on_high->metal_4h` score `0.1696` n `40` status `ready` deltaP `11.25` edge `-0.0197` maxDD `-1.3516`
- `risk_on_and_context->metal_4h` score `0.1696` n `40` status `ready` deltaP `11.25` edge `-0.0197` maxDD `-1.3516`
- `risk_on_high->fx_1h` score `0.003` n `40` status `ready` deltaP `3.503` edge `0.0` maxDD `-0.1704`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

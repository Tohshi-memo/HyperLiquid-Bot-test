# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-22T04:22:27.528802+00:00`
- Price records: `672`
- Market context records: `4382`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11143`

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

- `risk_on_high->unknown_4h` score `132.6006` n `44` status `ready` deltaP `-1.4413` edge `11.2415` maxDD `-10.8809`
- `risk_on_and_context->unknown_4h` score `132.6006` n `44` status `ready` deltaP `-1.4413` edge `11.2415` maxDD `-10.8809`
- `market_context_high->unknown_1h` score `36.3676` n `213` status `ready` deltaP `3.1732` edge `3.1591` maxDD `-9.6361`
- `market_context_high->unknown_4h` score `11.1976` n `213` status `ready` deltaP `3.3923` edge `1.4535` maxDD `-35.7719`
- `risk_on_high->equity_4h` score `3.2454` n `44` status `ready` deltaP `35.3797` edge `0.0393` maxDD `-0.044`
- `risk_on_and_context->equity_4h` score `3.2454` n `44` status `ready` deltaP `35.3797` edge `0.0393` maxDD `-0.044`
- `risk_on_high->metal_24h` score `2.9684` n `44` status `ready` deltaP `-15.183` edge `0.5432` maxDD `-1.9133`
- `risk_on_and_context->metal_24h` score `2.9684` n `44` status `ready` deltaP `-15.183` edge `0.5432` maxDD `-1.9133`
- `risk_on_high->crypto_major_4h` score `1.6629` n `44` status `ready` deltaP `17.2395` edge `0.0902` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `1.6629` n `44` status `ready` deltaP `17.2395` edge `0.0902` maxDD `-2.6576`
- `risk_on_high->equity_24h` score `1.6462` n `44` status `ready` deltaP `19.6181` edge `0.0064` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `1.6462` n `44` status `ready` deltaP `19.6181` edge `0.0064` maxDD `0.0`
- `risk_on_high->index_24h` score `1.0504` n `44` status `ready` deltaP `21.875` edge `-0.0583` maxDD `0.0`
- `risk_on_and_context->index_24h` score `1.0504` n `44` status `ready` deltaP `21.875` edge `-0.0583` maxDD `0.0`
- `risk_on_high->fx_1h` score `0.5284` n `44` status `ready` deltaP `9.54` edge `0.0034` maxDD `-0.1704`
- `risk_on_and_context->fx_1h` score `0.5284` n `44` status `ready` deltaP `9.54` edge `0.0034` maxDD `-0.1704`
- `risk_on_high->metal_4h` score `0.3529` n `44` status `ready` deltaP `6.1807` edge `0.0376` maxDD `-1.3516`
- `risk_on_and_context->metal_4h` score `0.3529` n `44` status `ready` deltaP `6.1807` edge `0.0376` maxDD `-1.3516`
- `risk_on_high->equity_1h` score `0.2975` n `44` status `ready` deltaP `8.8732` edge `0.0046` maxDD `-0.7834`
- `risk_on_and_context->equity_1h` score `0.2975` n `44` status `ready` deltaP `8.8732` edge `0.0046` maxDD `-0.7834`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

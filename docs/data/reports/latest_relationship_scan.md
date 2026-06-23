# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-23T06:37:31.297906+00:00`
- Price records: `672`
- Market context records: `4491`
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

- `risk_on_high->unknown_4h` score `124.2549` n `49` status `ready` deltaP `4.0256` edge `10.5108` maxDD `-10.9781`
- `risk_on_and_context->unknown_4h` score `124.2549` n `49` status `ready` deltaP `4.0256` edge `10.5108` maxDD `-10.9781`
- `market_context_high->unknown_1h` score `35.7744` n `217` status `ready` deltaP `3.2769` edge `3.1099` maxDD `-9.7103`
- `market_context_high->unknown_4h` score `16.5951` n `217` status `ready` deltaP `2.7748` edge `1.9109` maxDD `-36.0512`
- `risk_on_high->equity_4h` score `4.5979` n `49` status `ready` deltaP `39.939` edge `0.1169` maxDD `0.0`
- `risk_on_and_context->equity_4h` score `4.5979` n `49` status `ready` deltaP `39.939` edge `0.1169` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `2.9457` n `49` status `ready` deltaP `22.309` edge `0.1633` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `2.9457` n `49` status `ready` deltaP `22.309` edge `0.1633` maxDD `-2.6576`
- `risk_on_high->metal_24h` score `2.1641` n `49` status `ready` deltaP `-14.9589` edge `0.4751` maxDD `-4.834`
- `risk_on_and_context->metal_24h` score `2.1641` n `49` status `ready` deltaP `-14.9589` edge `0.4751` maxDD `-4.834`
- `risk_on_high->unknown_24h` score `2.1175` n `49` status `ready` deltaP `13.0173` edge `0.17` maxDD `-5.0928`
- `risk_on_and_context->unknown_24h` score `2.1175` n `49` status `ready` deltaP `13.0173` edge `0.17` maxDD `-5.0928`
- `risk_on_high->metal_4h` score `1.7778` n `49` status `ready` deltaP `14.0866` edge `0.0878` maxDD `-1.3516`
- `risk_on_and_context->metal_4h` score `1.7778` n `49` status `ready` deltaP `14.0866` edge `0.0878` maxDD `-1.3516`
- `risk_on_high->equity_1h` score `1.3352` n `49` status `ready` deltaP `15.8897` edge `0.0396` maxDD `-0.7415`
- `risk_on_and_context->equity_1h` score `1.3352` n `49` status `ready` deltaP `15.8897` edge `0.0396` maxDD `-0.7415`
- `risk_on_high->fx_4h` score `0.6205` n `49` status `ready` deltaP `15.5519` edge `0.0071` maxDD `-0.3925`
- `risk_on_and_context->fx_4h` score `0.6205` n `49` status `ready` deltaP `15.5519` edge `0.0071` maxDD `-0.3925`
- `risk_on_high->index_24h` score `0.4338` n `49` status `ready` deltaP `17.5737` edge `-0.0293` maxDD `-2.4702`
- `risk_on_and_context->index_24h` score `0.4338` n `49` status `ready` deltaP `17.5737` edge `-0.0293` maxDD `-2.4702`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

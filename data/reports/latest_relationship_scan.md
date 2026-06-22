# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-22T03:37:31.929575+00:00`
- Price records: `672`
- Market context records: `4379`
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

- `risk_on_high->unknown_4h` score `132.6066` n `44` status `ready` deltaP `-1.4413` edge `11.242` maxDD `-10.8809`
- `risk_on_and_context->unknown_4h` score `132.6066` n `44` status `ready` deltaP `-1.4413` edge `11.242` maxDD `-10.8809`
- `market_context_high->unknown_1h` score `35.7521` n `213` status `ready` deltaP `3.0235` edge `3.1088` maxDD `-9.6361`
- `market_context_high->unknown_4h` score `11.2036` n `213` status `ready` deltaP `3.3923` edge `1.454` maxDD `-35.7719`
- `risk_on_high->equity_4h` score `3.2346` n `44` status `ready` deltaP `35.3797` edge `0.0384` maxDD `-0.044`
- `risk_on_and_context->equity_4h` score `3.2346` n `44` status `ready` deltaP `35.3797` edge `0.0384` maxDD `-0.044`
- `risk_on_high->metal_24h` score `2.945` n `44` status `ready` deltaP `-15.183` edge `0.5402` maxDD `-1.9133`
- `risk_on_and_context->metal_24h` score `2.945` n `44` status `ready` deltaP `-15.183` edge `0.5402` maxDD `-1.9133`
- `risk_on_high->equity_24h` score `1.6318` n `44` status `ready` deltaP `19.6181` edge `0.0052` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `1.6318` n `44` status `ready` deltaP `19.6181` edge `0.0052` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `1.6305` n `44` status `ready` deltaP `17.2395` edge `0.0875` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `1.6305` n `44` status `ready` deltaP `17.2395` edge `0.0875` maxDD `-2.6576`
- `risk_on_high->index_24h` score `0.965` n `44` status `ready` deltaP `21.5278` edge `-0.0631` maxDD `0.0`
- `risk_on_and_context->index_24h` score `0.965` n `44` status `ready` deltaP `21.5278` edge `-0.0631` maxDD `0.0`
- `risk_on_high->fx_1h` score `0.5033` n `44` status `ready` deltaP `9.2406` edge `0.0033` maxDD `-0.1704`
- `risk_on_and_context->fx_1h` score `0.5033` n `44` status `ready` deltaP `9.2406` edge `0.0033` maxDD `-0.1704`
- `risk_on_high->equity_1h` score `0.3455` n `44` status `ready` deltaP `9.1726` edge `0.0066` maxDD `-0.7834`
- `risk_on_and_context->equity_1h` score `0.3455` n `44` status `ready` deltaP `9.1726` edge `0.0066` maxDD `-0.7834`
- `risk_on_high->metal_4h` score `0.3428` n `44` status `ready` deltaP `6.1807` edge `0.0363` maxDD `-1.3516`
- `risk_on_and_context->metal_4h` score `0.3428` n `44` status `ready` deltaP `6.1807` edge `0.0363` maxDD `-1.3516`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

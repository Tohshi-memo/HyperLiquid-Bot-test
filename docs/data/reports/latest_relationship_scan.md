# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-23T04:37:27.349977+00:00`
- Price records: `672`
- Market context records: `4482`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11089`

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

- `risk_on_high->unknown_4h` score `124.109` n `49` status `ready` deltaP `3.4159` edge `10.5027` maxDD `-10.9781`
- `risk_on_and_context->unknown_4h` score `124.109` n `49` status `ready` deltaP `3.4159` edge `10.5027` maxDD `-10.9781`
- `market_context_high->unknown_1h` score `33.6152` n `225` status `ready` deltaP `3.6614` edge `2.9274` maxDD `-9.7103`
- `market_context_high->unknown_4h` score `15.4066` n `225` status `ready` deltaP `3.4431` edge `1.8074` maxDD `-36.0512`
- `risk_on_high->equity_4h` score `4.2841` n `49` status `ready` deltaP `39.4817` edge `0.0938` maxDD `0.0`
- `risk_on_and_context->equity_4h` score `4.2841` n `49` status `ready` deltaP `39.4817` edge `0.0938` maxDD `0.0`
- `risk_on_high->metal_24h` score `2.9943` n `46` status `ready` deltaP `-14.0852` edge `0.5392` maxDD `-1.9133`
- `risk_on_and_context->metal_24h` score `2.9943` n `46` status `ready` deltaP `-14.0852` edge `0.5392` maxDD `-1.9133`
- `risk_on_high->crypto_major_4h` score `2.6225` n `49` status `ready` deltaP `21.0895` edge `0.1445` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `2.6225` n `49` status `ready` deltaP `21.0895` edge `0.1445` maxDD `-2.6576`
- `risk_on_high->unknown_24h` score `2.4032` n `46` status `ready` deltaP `13.8737` edge `0.1881` maxDD `-5.0928`
- `risk_on_and_context->unknown_24h` score `2.4032` n `46` status `ready` deltaP `13.8737` edge `0.1881` maxDD `-5.0928`
- `risk_on_high->index_24h` score `1.6204` n `46` status `ready` deltaP `22.0411` edge `0.0058` maxDD `-0.75`
- `risk_on_and_context->index_24h` score `1.6204` n `46` status `ready` deltaP `22.0411` edge `0.0058` maxDD `-0.75`
- `risk_on_high->metal_4h` score `1.611` n `49` status `ready` deltaP `13.172` edge `0.08` maxDD `-1.3516`
- `risk_on_and_context->metal_4h` score `1.611` n `49` status `ready` deltaP `13.172` edge `0.08` maxDD `-1.3516`
- `risk_on_high->equity_1h` score `1.1721` n `49` status `ready` deltaP `15.1412` edge `0.031` maxDD `-0.7415`
- `risk_on_and_context->equity_1h` score `1.1721` n `49` status `ready` deltaP `15.1412` edge `0.031` maxDD `-0.7415`
- `risk_on_high->fx_4h` score `0.6181` n `49` status `ready` deltaP `15.5519` edge `0.0069` maxDD `-0.3925`
- `risk_on_and_context->fx_4h` score `0.6181` n `49` status `ready` deltaP `15.5519` edge `0.0069` maxDD `-0.3925`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

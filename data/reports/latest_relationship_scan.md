# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-23T10:52:28.179892+00:00`
- Price records: `672`
- Market context records: `4509`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9771`

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

- `risk_on_high->unknown_4h` score `124.6169` n `49` status `ready` deltaP `4.6354` edge `10.5369` maxDD `-10.9781`
- `risk_on_and_context->unknown_4h` score `124.6169` n `49` status `ready` deltaP `4.6354` edge `10.5369` maxDD `-10.9781`
- `market_context_high->unknown_1h` score `41.5962` n `200` status `ready` deltaP `4.3683` edge `3.583` maxDD `-9.3285`
- `market_context_high->unknown_4h` score `22.5912` n `200` status `ready` deltaP `4.3293` edge `2.1556` maxDD `-19.1487`
- `risk_on_high->equity_4h` score `5.0863` n `49` status `ready` deltaP `41.7683` edge `0.1454` maxDD `0.0`
- `risk_on_and_context->equity_4h` score `5.0863` n `49` status `ready` deltaP `41.7683` edge `0.1454` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `3.9842` n `49` status `ready` deltaP `24.5956` edge `0.2346` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `3.9842` n `49` status `ready` deltaP `24.5956` edge `0.2346` maxDD `-2.6576`
- `risk_on_high->metal_24h` score `2.6814` n `49` status `ready` deltaP `-12.1811` edge `0.5229` maxDD `-4.834`
- `risk_on_and_context->metal_24h` score `2.6814` n `49` status `ready` deltaP `-12.1811` edge `0.5229` maxDD `-4.834`
- `risk_on_high->metal_4h` score `1.9979` n `49` status `ready` deltaP `15.4585` edge `0.097` maxDD `-1.3516`
- `risk_on_and_context->metal_4h` score `1.9979` n `49` status `ready` deltaP `15.4585` edge `0.097` maxDD `-1.3516`
- `risk_on_high->unknown_24h` score `1.876` n `49` status `ready` deltaP `10.2395` edge `0.1684` maxDD `-5.0928`
- `risk_on_and_context->unknown_24h` score `1.876` n `49` status `ready` deltaP `10.2395` edge `0.1684` maxDD `-5.0928`
- `risk_on_high->equity_1h` score `1.3735` n `49` status `ready` deltaP `16.1891` edge `0.0408` maxDD `-0.7415`
- `risk_on_and_context->equity_1h` score `1.3735` n `49` status `ready` deltaP `16.1891` edge `0.0408` maxDD `-0.7415`
- `risk_on_high->index_24h` score `1.0479` n `49` status `ready` deltaP `20.5251` edge `0.0022` maxDD `-2.4702`
- `risk_on_and_context->index_24h` score `1.0479` n `49` status `ready` deltaP `20.5251` edge `0.0022` maxDD `-2.4702`
- `risk_on_high->fx_4h` score `0.6435` n `49` status `ready` deltaP `15.7043` edge `0.008` maxDD `-0.3925`
- `risk_on_and_context->fx_4h` score `0.6435` n `49` status `ready` deltaP `15.7043` edge `0.008` maxDD `-0.3925`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-21T13:22:29.049066+00:00`
- Price records: `672`
- Market context records: `4316`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10794`

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

- `risk_on_high->unknown_4h` score `130.7483` n `44` status `ready` deltaP `-0.984` edge `11.0841` maxDD `-10.8809`
- `risk_on_and_context->unknown_4h` score `130.7483` n `44` status `ready` deltaP `-0.984` edge `11.0841` maxDD `-10.8809`
- `market_context_high->unknown_1h` score `28.4923` n `234` status `ready` deltaP `3.1962` edge `2.511` maxDD `-9.6361`
- `market_context_high->unknown_4h` score `9.3866` n `234` status `ready` deltaP `1.755` edge `1.3135` maxDD `-35.7719`
- `market_context_high->unknown_24h` score `4.3889` n `211` status `ready` deltaP `-7.2744` edge `0.8176` maxDD `-24.2693`
- `risk_on_high->metal_24h` score `2.2648` n `41` status `ready` deltaP `-19.4741` edge `0.4816` maxDD `-1.9133`
- `risk_on_and_context->metal_24h` score `2.2648` n `41` status `ready` deltaP `-19.4741` edge `0.4816` maxDD `-1.9133`
- `risk_on_high->equity_4h` score `2.2477` n `44` status `ready` deltaP `31.2639` edge `-0.0164` maxDD `-0.044`
- `risk_on_and_context->equity_4h` score `2.2477` n `44` status `ready` deltaP `31.2639` edge `-0.0164` maxDD `-0.044`
- `risk_on_high->equity_24h` score `1.9833` n `41` status `ready` deltaP `22.9167` edge `0.0125` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `1.9833` n `41` status `ready` deltaP `22.9167` edge `0.0125` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `1.4357` n `44` status `ready` deltaP `16.9346` edge `0.0733` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `1.4357` n `44` status `ready` deltaP `16.9346` edge `0.0733` maxDD `-2.6576`
- `risk_on_high->fx_1h` score `0.3931` n `44` status `ready` deltaP `7.8933` edge `0.0031` maxDD `-0.1704`
- `risk_on_and_context->fx_1h` score `0.3931` n `44` status `ready` deltaP `7.8933` edge `0.0031` maxDD `-0.1704`
- `risk_on_high->crypto_major_1h` score `0.1908` n `44` status `ready` deltaP `8.5466` edge `0.0217` maxDD `-2.3372`
- `risk_on_and_context->crypto_major_1h` score `0.1908` n `44` status `ready` deltaP `8.5466` edge `0.0217` maxDD `-2.3372`
- `risk_on_high->fx_4h` score `0.0203` n `44` status `ready` deltaP `8.786` edge `0.0031` maxDD `-0.3925`
- `risk_on_and_context->fx_4h` score `0.0203` n `44` status `ready` deltaP `8.786` edge `0.0031` maxDD `-0.3925`
- `risk_on_high->index_24h` score `0.0189` n `41` status `ready` deltaP `19.2708` edge `-0.1269` maxDD `0.0`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

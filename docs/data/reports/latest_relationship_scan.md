# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-22T10:22:30.040284+00:00`
- Price records: `672`
- Market context records: `7555`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14475`

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

- `risk_on_high->crypto_major_4h` score `7.485` n `33` status `ready` deltaP `41.6713` edge `0.3652` maxDD `-0.8742`
- `risk_on_and_context->crypto_major_4h` score `7.485` n `33` status `ready` deltaP `41.6713` edge `0.3652` maxDD `-0.8742`
- `risk_on_high->crypto_major_24h` score `6.1198` n `33` status `ready` deltaP `17.077` edge `0.4738` maxDD `-4.8796`
- `risk_on_and_context->crypto_major_24h` score `6.1198` n `33` status `ready` deltaP `17.077` edge `0.4738` maxDD `-4.8796`
- `risk_on_high->unknown_4h` score `4.8757` n `33` status `ready` deltaP `14.8929` edge `0.35` maxDD `-0.4384`
- `risk_on_and_context->unknown_4h` score `4.8757` n `33` status `ready` deltaP `14.8929` edge `0.35` maxDD `-0.4384`
- `risk_on_high->crypto_alt_4h` score `4.5578` n `33` status `ready` deltaP `30.3123` edge `0.2021` maxDD `-0.9492`
- `risk_on_and_context->crypto_alt_4h` score `4.5578` n `33` status `ready` deltaP `30.3123` edge `0.2021` maxDD `-0.9492`
- `risk_on_high->crypto_alt_24h` score `3.2177` n `33` status `ready` deltaP `16.5089` edge `0.2198` maxDD `-3.6039`
- `risk_on_and_context->crypto_alt_24h` score `3.2177` n `33` status `ready` deltaP `16.5089` edge `0.2198` maxDD `-3.6039`
- `risk_on_high->crypto_major_1h` score `1.5667` n `33` status `ready` deltaP `22.5776` edge `0.0748` maxDD `-0.957`
- `risk_on_and_context->crypto_major_1h` score `1.5667` n `33` status `ready` deltaP `22.5776` edge `0.0748` maxDD `-0.957`
- `risk_on_high->fx_24h` score `0.8177` n `32` status `ready` deltaP `20.0022` edge `0.0171` maxDD `-1.3162`
- `risk_on_and_context->fx_24h` score `0.8177` n `32` status `ready` deltaP `20.0022` edge `0.0171` maxDD `-1.3162`
- `risk_on_high->unknown_24h` score `0.6379` n `33` status `ready` deltaP `5.0348` edge `0.0418` maxDD `-0.4433`
- `risk_on_and_context->unknown_24h` score `0.6379` n `33` status `ready` deltaP `5.0348` edge `0.0418` maxDD `-0.4433`
- `risk_on_high->equity_1h` score `0.5865` n `33` status `ready` deltaP `8.5996` edge `0.0514` maxDD `-1.3497`
- `risk_on_and_context->equity_1h` score `0.5865` n `33` status `ready` deltaP `8.5996` edge `0.0514` maxDD `-1.3497`
- `risk_on_high->crypto_alt_1h` score `0.0493` n `33` status `ready` deltaP `-0.9164` edge `0.0495` maxDD `-0.9651`
- `risk_on_and_context->crypto_alt_1h` score `0.0493` n `33` status `ready` deltaP `-0.9164` edge `0.0495` maxDD `-0.9651`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

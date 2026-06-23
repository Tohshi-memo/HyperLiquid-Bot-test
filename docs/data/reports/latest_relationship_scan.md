# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-23T07:22:30.177223+00:00`
- Price records: `672`
- Market context records: `4494`
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

- `risk_on_high->unknown_4h` score `124.3611` n `49` status `ready` deltaP `4.4829` edge `10.5166` maxDD `-10.9781`
- `risk_on_and_context->unknown_4h` score `124.3611` n `49` status `ready` deltaP `4.4829` edge `10.5166` maxDD `-10.9781`
- `market_context_high->unknown_1h` score `36.8418` n `214` status `ready` deltaP `3.5397` edge `3.1971` maxDD `-9.7103`
- `market_context_high->unknown_4h` score `17.015` n `214` status `ready` deltaP `2.7282` edge `1.9462` maxDD `-36.0512`
- `risk_on_high->equity_4h` score `4.7027` n `49` status `ready` deltaP `40.2439` edge `0.1236` maxDD `0.0`
- `risk_on_and_context->equity_4h` score `4.7027` n `49` status `ready` deltaP `40.2439` edge `0.1236` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `3.1215` n `49` status `ready` deltaP `22.7663` edge `0.1749` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `3.1215` n `49` status `ready` deltaP `22.7663` edge `0.1749` maxDD `-2.6576`
- `risk_on_high->metal_24h` score `2.2606` n `49` status `ready` deltaP `-14.438` edge `0.484` maxDD `-4.834`
- `risk_on_and_context->metal_24h` score `2.2606` n `49` status `ready` deltaP `-14.438` edge `0.484` maxDD `-4.834`
- `risk_on_high->unknown_24h` score `1.9762` n `49` status `ready` deltaP `12.4964` edge `0.1617` maxDD `-5.0928`
- `risk_on_and_context->unknown_24h` score `1.9762` n `49` status `ready` deltaP `12.4964` edge `0.1617` maxDD `-5.0928`
- `risk_on_high->metal_4h` score `1.8408` n `49` status `ready` deltaP `14.5439` edge `0.09` maxDD `-1.3516`
- `risk_on_and_context->metal_4h` score `1.8408` n `49` status `ready` deltaP `14.5439` edge `0.09` maxDD `-1.3516`
- `risk_on_high->equity_1h` score `1.3076` n `49` status `ready` deltaP `15.74` edge `0.0383` maxDD `-0.7415`
- `risk_on_and_context->equity_1h` score `1.3076` n `49` status `ready` deltaP `15.74` edge `0.0383` maxDD `-0.7415`
- `risk_on_high->fx_4h` score `0.6351` n `49` status `ready` deltaP `15.7043` edge `0.0073` maxDD `-0.3925`
- `risk_on_and_context->fx_4h` score `0.6351` n `49` status `ready` deltaP `15.7043` edge `0.0073` maxDD `-0.3925`
- `risk_on_high->index_24h` score `0.5354` n `49` status `ready` deltaP `18.0945` edge `-0.0243` maxDD `-2.4702`
- `risk_on_and_context->index_24h` score `0.5354` n `49` status `ready` deltaP `18.0945` edge `-0.0243` maxDD `-2.4702`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

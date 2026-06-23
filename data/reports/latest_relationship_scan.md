# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-23T12:37:37.597670+00:00`
- Price records: `672`
- Market context records: `4516`
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

- `risk_on_high->unknown_4h` score `136.3314` n `46` status `ready` deltaP `8.742` edge `11.4301` maxDD `-7.5275`
- `risk_on_and_context->unknown_4h` score `136.3314` n `46` status `ready` deltaP `8.742` edge `11.4301` maxDD `-7.5275`
- `market_context_high->unknown_1h` score `45.7262` n `193` status `ready` deltaP `5.3357` edge `3.8466` maxDD `-3.3992`
- `market_context_high->unknown_4h` score `26.7188` n `193` status `ready` deltaP `6.5343` edge `2.3396` maxDD `-7.5275`
- `risk_on_high->equity_4h` score `5.1139` n `46` status `ready` deltaP `41.7683` edge `0.1477` maxDD `0.0`
- `risk_on_and_context->equity_4h` score `5.1139` n `46` status `ready` deltaP `41.7683` edge `0.1477` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `5.0679` n `46` status `ready` deltaP `29.2153` edge `0.2714` maxDD `-1.841`
- `risk_on_and_context->crypto_major_4h` score `5.0679` n `46` status `ready` deltaP `29.2153` edge `0.2714` maxDD `-1.841`
- `risk_on_high->unknown_24h` score `4.5918` n `46` status `ready` deltaP `15.1872` edge `0.3027` maxDD `-1.3704`
- `risk_on_and_context->unknown_24h` score `4.5918` n `46` status `ready` deltaP `15.1872` edge `0.3027` maxDD `-1.3704`
- `risk_on_high->metal_24h` score `2.9564` n `46` status `ready` deltaP `-11.5716` edge `0.5541` maxDD `-4.834`
- `risk_on_and_context->metal_24h` score `2.9564` n `46` status `ready` deltaP `-11.5716` edge `0.5541` maxDD `-4.834`
- `risk_on_high->metal_4h` score `2.0476` n `46` status `ready` deltaP `15.6747` edge `0.0997` maxDD `-1.3516`
- `risk_on_and_context->metal_4h` score `2.0476` n `46` status `ready` deltaP `15.6747` edge `0.0997` maxDD `-1.3516`
- `risk_on_high->index_24h` score `1.2827` n `46` status `ready` deltaP `21.0748` edge `0.0181` maxDD `-2.4702`
- `risk_on_and_context->index_24h` score `1.2827` n `46` status `ready` deltaP `21.0748` edge `0.0181` maxDD `-2.4702`
- `risk_on_high->equity_1h` score `1.1428` n `46` status `ready` deltaP `14.4754` edge `0.033` maxDD `-0.7415`
- `risk_on_and_context->equity_1h` score `1.1428` n `46` status `ready` deltaP `14.4754` edge `0.033` maxDD `-0.7415`
- `risk_on_high->fx_4h` score `0.496` n `46` status `ready` deltaP `14.0708` edge `0.0066` maxDD `-0.3925`
- `risk_on_and_context->fx_4h` score `0.496` n `46` status `ready` deltaP `14.0708` edge `0.0066` maxDD `-0.3925`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

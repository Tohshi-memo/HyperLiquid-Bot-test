# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-12T05:07:32.464025+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `9666`

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

- `market_context_high->unknown_4h` score `33.6749` n `119` status `ready` deltaP `-7.066` edge `2.9239` maxDD `-2.3109`
- `market_context_high->equity_24h` score `8.0136` n `54` status `ready` deltaP `25.1158` edge `0.5764` maxDD `-2.4161`
- `market_context_high->crypto_major_24h` score `7.1481` n `54` status `ready` deltaP `10.4745` edge `1.1274` maxDD `-15.1312`
- `market_context_high->index_24h` score `5.7509` n `54` status `ready` deltaP `49.0741` edge `0.1564` maxDD `-0.012`
- `risk_on_high->crypto_major_4h` score `5.6791` n `46` status `ready` deltaP `33.4836` edge `0.3353` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `5.6791` n `46` status `ready` deltaP `33.4836` edge `0.3353` maxDD `-4.1548`
- `risk_on_high->crypto_alt_4h` score `4.6797` n `46` status `ready` deltaP `20.7516` edge `0.2964` maxDD `-1.9151`
- `risk_on_and_context->crypto_alt_4h` score `4.6797` n `46` status `ready` deltaP `20.7516` edge `0.2964` maxDD `-1.9151`
- `risk_on_high->metal_4h` score `2.617` n `46` status `ready` deltaP `23.9529` edge `0.0816` maxDD `-0.1896`
- `risk_on_and_context->metal_4h` score `2.617` n `46` status `ready` deltaP `23.9529` edge `0.0816` maxDD `-0.1896`
- `risk_on_high->crypto_alt_1h` score `1.6538` n `58` status `ready` deltaP `9.7512` edge `0.1325` maxDD `-2.4421`
- `risk_on_and_context->crypto_alt_1h` score `1.6538` n `58` status `ready` deltaP `9.7512` edge `0.1325` maxDD `-2.4421`
- `risk_on_high->crypto_major_1h` score `1.339` n `58` status `ready` deltaP `9.8957` edge `0.1109` maxDD `-3.2233`
- `risk_on_and_context->crypto_major_1h` score `1.339` n `58` status `ready` deltaP `9.8957` edge `0.1109` maxDD `-3.2233`
- `market_context_high->crypto_major_4h` score `0.8345` n `119` status `ready` deltaP `11.032` edge `0.244` maxDD `-11.1784`
- `market_context_high->crypto_alt_24h` score `0.708` n `54` status `ready` deltaP `-11.2269` edge `0.6844` maxDD `-30.1698`
- `market_context_high->metal_4h` score `0.5981` n `119` status `ready` deltaP `13.4121` edge `0.0327` maxDD `-1.1153`
- `market_context_high->crypto_alt_1h` score `0.5781` n `131` status `ready` deltaP `6.2634` edge `0.1015` maxDD `-4.9401`
- `market_context_high->crypto_alt_4h` score `0.419` n `119` status `ready` deltaP `5.1688` edge `0.2563` maxDD `-13.8008`
- `risk_on_high->metal_1h` score `0.3544` n `58` status `ready` deltaP `8.249` edge `0.0161` maxDD `-0.3247`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-12T03:52:24.721656+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `9598`

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

- `market_context_high->unknown_24h` score `435.0214` n `54` status `ready` deltaP `-16.0879` edge `36.3954` maxDD `-1.2425`
- `market_context_high->unknown_4h` score `34.4165` n `119` status `ready` deltaP `-7.066` edge `2.9857` maxDD `-2.3109`
- `market_context_high->equity_24h` score `8.4649` n `54` status `ready` deltaP `25.1158` edge `0.5801` maxDD `-1.3705`
- `market_context_high->index_24h` score `5.9032` n `54` status `ready` deltaP `50.7523` edge `0.1579` maxDD `-0.012`
- `risk_on_high->crypto_major_4h` score `5.3752` n `41` status `ready` deltaP `31.8598` edge `0.3208` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `5.3752` n `41` status `ready` deltaP `31.8598` edge `0.3208` maxDD `-4.1548`
- `market_context_high->crypto_major_24h` score `5.0569` n `54` status `ready` deltaP `2.0833` edge `0.9465` maxDD `-17.6322`
- `risk_on_high->crypto_alt_4h` score `4.7544` n `41` status `ready` deltaP `23.1708` edge `0.2865` maxDD `-1.9151`
- `risk_on_and_context->crypto_alt_4h` score `4.7544` n `41` status `ready` deltaP `23.1708` edge `0.2865` maxDD `-1.9151`
- `risk_on_high->metal_4h` score `3.3432` n `41` status `ready` deltaP `30.9451` edge `0.0955` maxDD `-0.1896`
- `risk_on_and_context->metal_4h` score `3.3432` n `41` status `ready` deltaP `30.9451` edge `0.0955` maxDD `-0.1896`
- `risk_on_high->crypto_alt_1h` score `1.4544` n `53` status `ready` deltaP `10.2587` edge `0.1125` maxDD `-2.4421`
- `risk_on_and_context->crypto_alt_1h` score `1.4544` n `53` status `ready` deltaP `10.2587` edge `0.1125` maxDD `-2.4421`
- `risk_on_high->metal_1h` score `1.0804` n `53` status `ready` deltaP `13.9419` edge `0.021` maxDD `-0.2466`
- `risk_on_and_context->metal_1h` score `1.0804` n `53` status `ready` deltaP `13.9419` edge `0.021` maxDD `-0.2466`
- `risk_on_high->crypto_major_1h` score `1.0751` n `53` status `ready` deltaP `10.078` edge `0.0877` maxDD `-3.2233`
- `risk_on_and_context->crypto_major_1h` score `1.0751` n `53` status `ready` deltaP `10.078` edge `0.0877` maxDD `-3.2233`
- `market_context_high->metal_4h` score `0.5178` n `119` status `ready` deltaP `12.7242` edge `0.0306` maxDD `-1.1153`
- `market_context_high->crypto_major_4h` score `0.4052` n `119` status `ready` deltaP `7.5925` edge `0.2119` maxDD `-11.1784`
- `market_context_high->crypto_alt_1h` score `0.2706` n `131` status `ready` deltaP `5.6498` edge `0.0883` maxDD `-4.9401`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

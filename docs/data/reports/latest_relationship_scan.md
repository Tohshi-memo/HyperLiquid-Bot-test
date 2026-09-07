# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-07T11:52:30.167961+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10429`

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

- `risk_on_high->unknown_24h` score `406.9038` n `93` status `ready` deltaP `25.8681` edge `33.7362` maxDD `0.0`
- `risk_on_and_context->unknown_24h` score `406.9038` n `93` status `ready` deltaP `25.8681` edge `33.7362` maxDD `0.0`
- `market_context_high->unknown_1h` score `24.174` n `241` status `ready` deltaP `-2.2281` edge `2.1018` maxDD `-2.4626`
- `risk_on_high->crypto_major_24h` score `22.2214` n `93` status `ready` deltaP `38.0657` edge `1.6497` maxDD `-1.4687`
- `risk_on_and_context->crypto_major_24h` score `22.2214` n `93` status `ready` deltaP `38.0657` edge `1.6497` maxDD `-1.4687`
- `risk_on_high->crypto_alt_24h` score `15.1622` n `93` status `ready` deltaP `32.1181` edge `1.0494` maxDD `0.0`
- `risk_on_and_context->crypto_alt_24h` score `15.1622` n `93` status `ready` deltaP `32.1181` edge `1.0494` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `8.822` n `191` status `ready` deltaP `24.2647` edge `0.6309` maxDD `-2.5998`
- `market_context_high->equity_24h` score `5.891` n `191` status `ready` deltaP `20.3125` edge `0.3555` maxDD `0.0`
- `risk_on_high->crypto_alt_4h` score `5.4049` n `117` status `ready` deltaP `29.1106` edge `0.2935` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `5.4049` n `117` status `ready` deltaP `29.1106` edge `0.2935` maxDD `-1.9733`
- `risk_on_high->equity_24h` score `4.8782` n `93` status `ready` deltaP `20.3125` edge `0.2711` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `4.8782` n `93` status `ready` deltaP `20.3125` edge `0.2711` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `4.3737` n `117` status `ready` deltaP `24.4567` edge `0.2873` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `4.3737` n `117` status `ready` deltaP `24.4567` edge `0.2873` maxDD `-3.8693`
- `risk_on_high->index_24h` score `2.4473` n `93` status `ready` deltaP `20.9061` edge `0.0688` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `2.4473` n `93` status `ready` deltaP `20.9061` edge `0.0688` maxDD `-0.0051`
- `market_context_high->index_24h` score `2.0727` n `191` status `ready` deltaP `16.8021` edge `0.0825` maxDD `-0.0767`
- `risk_on_high->crypto_alt_1h` score `0.9249` n `117` status `ready` deltaP `4.3964` edge `0.083` maxDD `-1.1521`
- `risk_on_and_context->crypto_alt_1h` score `0.9249` n `117` status `ready` deltaP `4.3964` edge `0.083` maxDD `-1.1521`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

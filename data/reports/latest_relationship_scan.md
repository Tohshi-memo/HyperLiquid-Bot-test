# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-11T02:22:25.828922+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `11394`

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

- `news_risk_high->unknown_4h` score `1167.5588` n `34` status `ready` deltaP `-20.9917` edge `97.5009` maxDD `-2.1509`
- `news_risk_high->unknown_1h` score `1131.4823` n `46` status `ready` deltaP `-5.8058` edge `94.3643` maxDD `-1.1656`
- `risk_on_high->crypto_alt_24h` score `20.5599` n `91` status `ready` deltaP `36.3458` edge `1.494` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `20.5599` n `91` status `ready` deltaP `36.3458` edge `1.494` maxDD `-0.8386`
- `market_context_high->crypto_alt_24h` score `16.5164` n `196` status `ready` deltaP `29.5954` edge `1.2618` maxDD `-3.9523`
- `risk_on_high->crypto_alt_4h` score `9.0419` n `91` status `ready` deltaP `42.0983` edge `0.51` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `9.0419` n `91` status `ready` deltaP `42.0983` edge `0.51` maxDD `-1.9733`
- `market_context_high->equity_24h` score `8.2147` n `196` status `ready` deltaP `29.5139` edge `0.4878` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `7.8479` n `91` status `ready` deltaP `32.9637` edge `0.5201` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `7.8479` n `91` status `ready` deltaP `32.9637` edge `0.5201` maxDD `-3.8693`
- `risk_on_high->crypto_major_24h` score `7.2456` n `91` status `ready` deltaP `25.021` edge `1.1689` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `7.2456` n `91` status `ready` deltaP `25.021` edge `1.1689` maxDD `-24.5429`
- `risk_on_high->equity_24h` score `6.8335` n `91` status `ready` deltaP `29.5139` edge `0.3727` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `6.8335` n `91` status `ready` deltaP `29.5139` edge `0.3727` maxDD `0.0`
- `risk_on_high->index_24h` score `4.82` n `91` status `ready` deltaP `45.3144` edge `0.1038` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `4.82` n `91` status `ready` deltaP `45.3144` edge `0.1038` maxDD `-0.0051`
- `market_context_high->index_24h` score `3.9011` n `196` status `ready` deltaP `39.4274` edge `0.1016` maxDD `-0.1483`
- `risk_on_high->equity_4h` score `3.5854` n `91` status `ready` deltaP `33.3456` edge `0.0858` maxDD `-0.079`
- `risk_on_and_context->equity_4h` score `3.5854` n `91` status `ready` deltaP `33.3456` edge `0.0858` maxDD `-0.079`
- `market_context_high->equity_4h` score `2.3722` n `196` status `ready` deltaP `26.1635` edge `0.1088` maxDD `-2.843`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

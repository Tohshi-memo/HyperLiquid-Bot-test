# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-18T18:22:25.190552+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9270`

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

- `market_context_high->commodity_24h` score `2.02` n `117` status `ready` deltaP `18.7618` edge `0.1284` maxDD `-1.8119`
- `risk_on_high->commodity_24h` score `1.8822` n `84` status `ready` deltaP `20.8985` edge `0.0973` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `1.8822` n `84` status `ready` deltaP `20.8985` edge `0.0973` maxDD `-1.7154`
- `market_context_high->crypto_major_4h` score `1.695` n `118` status `ready` deltaP `19.4192` edge `0.4283` maxDD `-15.2359`
- `risk_on_high->crypto_major_4h` score `1.3466` n `85` status `ready` deltaP `20.2367` edge `0.2858` maxDD `-11.1788`
- `risk_on_and_context->crypto_major_4h` score `1.3466` n `85` status `ready` deltaP `20.2367` edge `0.2858` maxDD `-11.1788`
- `market_context_high->crypto_major_1h` score `0.4692` n `118` status `ready` deltaP `6.0819` edge `0.1085` maxDD `-3.7781`
- `risk_on_high->index_1h` score `0.2239` n `85` status `ready` deltaP `7.6453` edge `0.0061` maxDD `-0.7394`
- `risk_on_and_context->index_1h` score `0.2239` n `85` status `ready` deltaP `7.6453` edge `0.0061` maxDD `-0.7394`
- `risk_on_high->equity_1h` score `-0.2451` n `85` status `ready` deltaP `11.5492` edge `0.0322` maxDD `-5.3696`
- `risk_on_and_context->equity_1h` score `-0.2451` n `85` status `ready` deltaP `11.5492` edge `0.0322` maxDD `-5.3696`
- `market_context_high->crypto_alt_1h` score `-0.2906` n `118` status `ready` deltaP `2.9458` edge `0.0931` maxDD `-7.3329`
- `risk_on_high->metal_1h` score `-0.4883` n `85` status `ready` deltaP `0.951` edge `0.0042` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.4883` n `85` status `ready` deltaP `0.951` edge `0.0042` maxDD `-0.8513`
- `risk_on_high->crypto_major_1h` score `-0.493` n `85` status `ready` deltaP `0.7379` edge `0.0238` maxDD `-4.6876`
- `risk_on_and_context->crypto_major_1h` score `-0.493` n `85` status `ready` deltaP `0.7379` edge `0.0238` maxDD `-4.6876`
- `market_context_high->index_1h` score `-0.5781` n `118` status `ready` deltaP `3.6673` edge `0.0022` maxDD `-1.3195`
- `risk_on_high->fx_1h` score `-0.648` n `85` status `ready` deltaP `-1.9149` edge `-0.0032` maxDD `-0.376`
- `risk_on_and_context->fx_1h` score `-0.648` n `85` status `ready` deltaP `-1.9149` edge `-0.0032` maxDD `-0.376`
- `market_context_high->fx_1h` score `-0.6542` n `118` status `ready` deltaP `-4.3875` edge `-0.0025` maxDD `-0.503`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

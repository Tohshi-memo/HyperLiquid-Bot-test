# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-21T21:07:34.260556+00:00`
- Price records: `672`
- Market context records: `4351`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11234`

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

- `risk_on_high->unknown_4h` score `131.0221` n `44` status `ready` deltaP `-0.8315` edge `11.1059` maxDD `-10.8809`
- `risk_on_and_context->unknown_4h` score `131.0221` n `44` status `ready` deltaP `-0.8315` edge `11.1059` maxDD `-10.8809`
- `market_context_high->unknown_1h` score `32.5052` n `220` status `ready` deltaP `3.1683` edge `2.8456` maxDD `-9.6361`
- `market_context_high->unknown_4h` score `12.3426` n `218` status `ready` deltaP `3.8599` edge `1.5458` maxDD `-35.7719`
- `risk_on_high->equity_4h` score `3.1702` n `44` status `ready` deltaP `34.77` edge `0.0371` maxDD `-0.044`
- `risk_on_and_context->equity_4h` score `3.1702` n `44` status `ready` deltaP `34.77` edge `0.0371` maxDD `-0.044`
- `risk_on_high->metal_24h` score `2.7048` n `44` status `ready` deltaP `-17.2664` edge `0.5233` maxDD `-1.9133`
- `risk_on_and_context->metal_24h` score `2.7048` n `44` status `ready` deltaP `-17.2664` edge `0.5233` maxDD `-1.9133`
- `risk_on_high->equity_24h` score `1.8614` n `44` status `ready` deltaP `20.3125` edge `0.0197` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `1.8614` n `44` status `ready` deltaP `20.3125` edge `0.0197` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `1.7001` n `44` status `ready` deltaP `17.2395` edge `0.0933` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `1.7001` n `44` status `ready` deltaP `17.2395` edge `0.0933` maxDD `-2.6576`
- `risk_on_high->fx_1h` score `0.5368` n `44` status `ready` deltaP `9.54` edge `0.0041` maxDD `-0.1704`
- `risk_on_and_context->fx_1h` score `0.5368` n `44` status `ready` deltaP `9.54` edge `0.0041` maxDD `-0.1704`
- `risk_on_high->metal_4h` score `0.458` n `44` status `ready` deltaP `6.9429` edge `0.046` maxDD `-1.3516`
- `risk_on_and_context->metal_4h` score `0.458` n `44` status `ready` deltaP `6.9429` edge `0.046` maxDD `-1.3516`
- `risk_on_high->index_24h` score `0.4497` n `44` status `ready` deltaP `19.2708` edge `-0.091` maxDD `0.0`
- `risk_on_and_context->index_24h` score `0.4497` n `44` status `ready` deltaP `19.2708` edge `-0.091` maxDD `0.0`
- `risk_on_high->equity_1h` score `0.3707` n `44` status `ready` deltaP `9.1726` edge `0.0087` maxDD `-0.7834`
- `risk_on_and_context->equity_1h` score `0.3707` n `44` status `ready` deltaP `9.1726` edge `0.0087` maxDD `-0.7834`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

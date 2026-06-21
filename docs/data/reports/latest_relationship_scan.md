# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-21T12:52:33.266894+00:00`
- Price records: `672`
- Market context records: `4314`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10730`

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

- `risk_on_high->unknown_4h` score `130.7447` n `44` status `ready` deltaP `-0.984` edge `11.0838` maxDD `-10.8809`
- `risk_on_and_context->unknown_4h` score `130.7447` n `44` status `ready` deltaP `-0.984` edge `11.0838` maxDD `-10.8809`
- `market_context_high->unknown_1h` score `28.5306` n `234` status `ready` deltaP `3.4956` edge `2.5122` maxDD `-9.6361`
- `market_context_high->unknown_4h` score `9.383` n `234` status `ready` deltaP `1.755` edge `1.3132` maxDD `-35.7719`
- `market_context_high->unknown_24h` score `4.2829` n `209` status `ready` deltaP `-7.5782` edge `0.8108` maxDD `-24.2693`
- `risk_on_high->metal_24h` score `2.2952` n `40` status `ready` deltaP `-18.7847` edge `0.4809` maxDD `-1.9133`
- `risk_on_and_context->metal_24h` score `2.2952` n `40` status `ready` deltaP `-18.7847` edge `0.4809` maxDD `-1.9133`
- `risk_on_high->equity_4h` score `2.1635` n `44` status `ready` deltaP `31.1114` edge `-0.0224` maxDD `-0.044`
- `risk_on_and_context->equity_4h` score `2.1635` n `44` status `ready` deltaP `31.1114` edge `-0.0224` maxDD `-0.044`
- `risk_on_high->equity_24h` score `1.9173` n `40` status `ready` deltaP `22.9167` edge `0.007` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `1.9173` n `40` status `ready` deltaP `22.9167` edge `0.007` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `1.3575` n `44` status `ready` deltaP `16.7822` edge `0.0678` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `1.3575` n `44` status `ready` deltaP `16.7822` edge `0.0678` maxDD `-2.6576`
- `risk_on_high->fx_1h` score `0.3907` n `44` status `ready` deltaP `7.8933` edge `0.0029` maxDD `-0.1704`
- `risk_on_and_context->fx_1h` score `0.3907` n `44` status `ready` deltaP `7.8933` edge `0.0029` maxDD `-0.1704`
- `risk_on_high->crypto_major_1h` score `0.2189` n `44` status `ready` deltaP `8.846` edge `0.0233` maxDD `-2.3372`
- `risk_on_and_context->crypto_major_1h` score `0.2189` n `44` status `ready` deltaP `8.846` edge `0.0233` maxDD `-2.3372`
- `risk_on_high->equity_1h` score `0.0074` n `44` status `ready` deltaP `7.2265` edge `-0.0086` maxDD `-0.7834`
- `risk_on_and_context->equity_1h` score `0.0074` n `44` status `ready` deltaP `7.2265` edge `-0.0086` maxDD `-0.7834`
- `risk_on_high->index_24h` score `0.0033` n `40` status `ready` deltaP `19.2708` edge `-0.1282` maxDD `0.0`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

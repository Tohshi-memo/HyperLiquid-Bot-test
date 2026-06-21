# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-21T13:07:28.622626+00:00`
- Price records: `672`
- Market context records: `4315`
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

- `risk_on_high->unknown_4h` score `130.7459` n `44` status `ready` deltaP `-0.984` edge `11.0839` maxDD `-10.8809`
- `risk_on_and_context->unknown_4h` score `130.7459` n `44` status `ready` deltaP `-0.984` edge `11.0839` maxDD `-10.8809`
- `market_context_high->unknown_1h` score `28.5139` n `234` status `ready` deltaP `3.3459` edge `2.5118` maxDD `-9.6361`
- `market_context_high->unknown_4h` score `9.3842` n `234` status `ready` deltaP `1.755` edge `1.3133` maxDD `-35.7719`
- `market_context_high->unknown_24h` score `4.3516` n `210` status `ready` deltaP `-7.4256` edge `0.8155` maxDD `-24.2693`
- `risk_on_high->metal_24h` score `2.3448` n `40` status `ready` deltaP `-18.6111` edge `0.4861` maxDD `-1.9133`
- `risk_on_and_context->metal_24h` score `2.3448` n `40` status `ready` deltaP `-18.6111` edge `0.4861` maxDD `-1.9133`
- `risk_on_high->equity_4h` score `2.1959` n `44` status `ready` deltaP `31.1114` edge `-0.0197` maxDD `-0.044`
- `risk_on_and_context->equity_4h` score `2.1959` n `44` status `ready` deltaP `31.1114` edge `-0.0197` maxDD `-0.044`
- `risk_on_high->equity_24h` score `1.9701` n `40` status `ready` deltaP `22.9167` edge `0.0114` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `1.9701` n `40` status `ready` deltaP `22.9167` edge `0.0114` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `1.3887` n `44` status `ready` deltaP `16.7822` edge `0.0704` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `1.3887` n `44` status `ready` deltaP `16.7822` edge `0.0704` maxDD `-2.6576`
- `risk_on_high->fx_1h` score `0.3919` n `44` status `ready` deltaP `7.8933` edge `0.003` maxDD `-0.1704`
- `risk_on_and_context->fx_1h` score `0.3919` n `44` status `ready` deltaP `7.8933` edge `0.003` maxDD `-0.1704`
- `risk_on_high->crypto_major_1h` score `0.2064` n `44` status `ready` deltaP `8.6963` edge `0.0227` maxDD `-2.3372`
- `risk_on_and_context->crypto_major_1h` score `0.2064` n `44` status `ready` deltaP `8.6963` edge `0.0227` maxDD `-2.3372`
- `risk_on_high->index_24h` score `0.0453` n `40` status `ready` deltaP `19.2708` edge `-0.1247` maxDD `0.0`
- `risk_on_and_context->index_24h` score `0.0453` n `40` status `ready` deltaP `19.2708` edge `-0.1247` maxDD `0.0`
- `risk_on_high->fx_4h` score `0.0108` n `44` status `ready` deltaP `8.6336` edge `0.0029` maxDD `-0.3925`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

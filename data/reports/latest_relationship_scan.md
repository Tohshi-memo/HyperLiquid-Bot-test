# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-21T09:07:27.769993+00:00`
- Price records: `672`
- Market context records: `4297`
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

- `risk_on_high->unknown_4h` score `130.5244` n `44` status `ready` deltaP `-2.5084` edge `11.0756` maxDD `-10.8809`
- `risk_on_and_context->unknown_4h` score `130.5244` n `44` status `ready` deltaP `-2.5084` edge `11.0756` maxDD `-10.8809`
- `market_context_high->unknown_1h` score `27.8283` n `236` status `ready` deltaP `2.6059` edge `2.4596` maxDD `-9.6361`
- `market_context_high->unknown_4h` score `8.881` n `236` status `ready` deltaP `0.5348` edge `1.2795` maxDD `-35.7719`
- `market_context_high->unknown_24h` score `5.4921` n `206` status `ready` deltaP `-7.7332` edge `0.9126` maxDD `-24.2693`
- `risk_on_high->equity_4h` score `1.9359` n `44` status `ready` deltaP `30.5017` edge `-0.0373` maxDD `-0.044`
- `risk_on_and_context->equity_4h` score `1.9359` n `44` status `ready` deltaP `30.5017` edge `-0.0373` maxDD `-0.044`
- `risk_on_high->metal_24h` score `1.6033` n `40` status `ready` deltaP `-21.2153` edge `0.4084` maxDD `-1.9133`
- `risk_on_and_context->metal_24h` score `1.6033` n `40` status `ready` deltaP `-21.2153` edge `0.4084` maxDD `-1.9133`
- `risk_on_high->equity_24h` score `1.2693` n `40` status `ready` deltaP `22.9167` edge `-0.047` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `1.2693` n `40` status `ready` deltaP `22.9167` edge `-0.047` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `1.1228` n `44` status `ready` deltaP `16.1724` edge `0.0523` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `1.1228` n `44` status `ready` deltaP `16.1724` edge `0.0523` maxDD `-2.6576`
- `risk_on_high->fx_1h` score `0.4434` n `44` status `ready` deltaP `8.4921` edge `0.0033` maxDD `-0.1704`
- `risk_on_and_context->fx_1h` score `0.4434` n `44` status `ready` deltaP `8.4921` edge `0.0033` maxDD `-0.1704`
- `risk_on_high->crypto_major_1h` score `0.2158` n `44` status `ready` deltaP `8.6963` edge `0.0239` maxDD `-2.3372`
- `risk_on_and_context->crypto_major_1h` score `0.2158` n `44` status `ready` deltaP `8.6963` edge `0.0239` maxDD `-2.3372`
- `risk_on_high->fx_4h` score `0.0083` n `44` status `ready` deltaP `8.4811` edge `0.0036` maxDD `-0.3925`
- `risk_on_and_context->fx_4h` score `0.0083` n `44` status `ready` deltaP `8.4811` edge `0.0036` maxDD `-0.3925`
- `risk_on_high->equity_1h` score `-0.0177` n `44` status `ready` deltaP `6.9271` edge `-0.0087` maxDD `-0.7834`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

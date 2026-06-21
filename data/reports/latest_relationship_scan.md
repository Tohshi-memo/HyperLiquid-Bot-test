# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-21T14:22:25.951423+00:00`
- Price records: `672`
- Market context records: `4320`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10794`

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

- `risk_on_high->unknown_4h` score `130.7555` n `44` status `ready` deltaP `-0.984` edge `11.0847` maxDD `-10.8809`
- `risk_on_and_context->unknown_4h` score `130.7555` n `44` status `ready` deltaP `-0.984` edge `11.0847` maxDD `-10.8809`
- `market_context_high->unknown_1h` score `29.8289` n `230` status `ready` deltaP `3.8545` edge `2.618` maxDD `-9.6361`
- `market_context_high->unknown_4h` score `10.0398` n `230` status `ready` deltaP `1.5654` edge `1.3692` maxDD `-35.7719`
- `risk_on_high->equity_4h` score `2.4561` n `44` status `ready` deltaP `31.8736` edge `-0.0031` maxDD `-0.044`
- `risk_on_and_context->equity_4h` score `2.4561` n `44` status `ready` deltaP `31.8736` edge `-0.0031` maxDD `-0.044`
- `risk_on_high->metal_24h` score `2.0985` n `44` status `ready` deltaP `-21.6067` edge `0.4745` maxDD `-1.9133`
- `risk_on_and_context->metal_24h` score `2.0985` n `44` status `ready` deltaP `-21.6067` edge `0.4745` maxDD `-1.9133`
- `risk_on_high->equity_24h` score `2.0337` n `44` status `ready` deltaP `22.9167` edge `0.0167` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `2.0337` n `44` status `ready` deltaP `22.9167` edge `0.0167` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `1.6369` n `44` status `ready` deltaP `17.5444` edge `0.086` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `1.6369` n `44` status `ready` deltaP `17.5444` edge `0.086` maxDD `-2.6576`
- `risk_on_high->fx_1h` score `0.3644` n `44` status `ready` deltaP `7.5939` edge `0.0027` maxDD `-0.1704`
- `risk_on_and_context->fx_1h` score `0.3644` n `44` status `ready` deltaP `7.5939` edge `0.0027` maxDD `-0.1704`
- `risk_on_high->crypto_major_1h` score `0.1721` n `44` status `ready` deltaP `8.2472` edge `0.0213` maxDD `-2.3372`
- `risk_on_and_context->crypto_major_1h` score `0.1721` n `44` status `ready` deltaP `8.2472` edge `0.0213` maxDD `-2.3372`
- `risk_on_high->metal_4h` score `0.1167` n `44` status `ready` deltaP `4.5038` edge `0.0185` maxDD `-1.3516`
- `risk_on_and_context->metal_4h` score `0.1167` n `44` status `ready` deltaP `4.5038` edge `0.0185` maxDD `-1.3516`
- `risk_on_high->fx_4h` score `0.0211` n `44` status `ready` deltaP `8.786` edge `0.0032` maxDD `-0.3925`
- `risk_on_and_context->fx_4h` score `0.0211` n `44` status `ready` deltaP `8.786` edge `0.0032` maxDD `-0.3925`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-22T10:22:28.679976+00:00`
- Price records: `672`
- Market context records: `4406`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11123`

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

- `risk_on_high->unknown_4h` score `121.0113` n `49` status `ready` deltaP `3.8732` edge `10.2403` maxDD `-10.8809`
- `risk_on_and_context->unknown_4h` score `121.0113` n `49` status `ready` deltaP `3.8732` edge `10.2403` maxDD `-10.8809`
- `market_context_high->unknown_1h` score `30.603` n `231` status `ready` deltaP `2.2754` edge `2.6847` maxDD `-9.6361`
- `market_context_high->unknown_4h` score `13.4809` n `223` status `ready` deltaP `5.3832` edge `1.6305` maxDD `-35.7719`
- `risk_on_high->equity_4h` score `3.2108` n `49` status `ready` deltaP `33.4775` edge `0.0491` maxDD `-0.044`
- `risk_on_and_context->equity_4h` score `3.2108` n `49` status `ready` deltaP `33.4775` edge `0.0491` maxDD `-0.044`
- `risk_on_high->metal_24h` score `2.9906` n `44` status `ready` deltaP `-15.3567` edge `0.5472` maxDD `-1.9133`
- `risk_on_and_context->metal_24h` score `2.9906` n `44` status `ready` deltaP `-15.3567` edge `0.5472` maxDD `-1.9133`
- `risk_on_high->crypto_major_4h` score `2.5035` n `49` status `ready` deltaP `20.937` edge `0.1356` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `2.5035` n `49` status `ready` deltaP `20.937` edge `0.1356` maxDD `-2.6576`
- `risk_on_high->unknown_24h` score `2.194` n `44` status `ready` deltaP `20.0758` edge `0.1281` maxDD `-4.9954`
- `risk_on_and_context->unknown_24h` score `2.194` n `44` status `ready` deltaP `20.0758` edge `0.1281` maxDD `-4.9954`
- `risk_on_high->equity_24h` score `1.6713` n `44` status `ready` deltaP `20.4861` edge `0.0027` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `1.6713` n `44` status `ready` deltaP `20.4861` edge `0.0027` maxDD `0.0`
- `risk_on_high->index_24h` score `1.5558` n `44` status `ready` deltaP `23.4375` edge `-0.0266` maxDD `0.0`
- `risk_on_and_context->index_24h` score `1.5558` n `44` status `ready` deltaP `23.4375` edge `-0.0266` maxDD `0.0`
- `risk_on_high->metal_4h` score `0.8204` n `49` status `ready` deltaP `8.5988` edge `0.0446` maxDD `-1.3516`
- `risk_on_and_context->metal_4h` score `0.8204` n `49` status `ready` deltaP `8.5988` edge `0.0446` maxDD `-1.3516`
- `risk_on_high->equity_1h` score `0.6887` n `49` status `ready` deltaP `12.0525` edge `0.016` maxDD `-0.7834`
- `risk_on_and_context->equity_1h` score `0.6887` n `49` status `ready` deltaP `12.0525` edge `0.016` maxDD `-0.7834`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

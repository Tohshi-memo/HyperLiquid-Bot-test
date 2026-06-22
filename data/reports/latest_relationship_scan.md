# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-22T07:22:30.863256+00:00`
- Price records: `672`
- Market context records: `4394`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11119`

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

- `risk_on_high->unknown_4h` score `132.8983` n `44` status `ready` deltaP `-0.3742` edge `11.2592` maxDD `-10.8809`
- `risk_on_and_context->unknown_4h` score `132.8983` n `44` status `ready` deltaP `-0.3742` edge `11.2592` maxDD `-10.8809`
- `market_context_high->unknown_1h` score `33.0732` n `223` status `ready` deltaP `2.598` edge `2.8884` maxDD `-9.6361`
- `market_context_high->unknown_4h` score `11.4954` n `213` status `ready` deltaP `4.4594` edge `1.4712` maxDD `-35.7719`
- `risk_on_high->equity_4h` score `3.245` n `44` status `ready` deltaP `35.0749` edge `0.0413` maxDD `-0.044`
- `risk_on_and_context->equity_4h` score `3.245` n `44` status `ready` deltaP `35.0749` edge `0.0413` maxDD `-0.044`
- `risk_on_high->metal_24h` score `2.9968` n `44` status `ready` deltaP `-15.3567` edge `0.548` maxDD `-1.9133`
- `risk_on_and_context->metal_24h` score `2.9968` n `44` status `ready` deltaP `-15.3567` edge `0.548` maxDD `-1.9133`
- `risk_on_high->crypto_major_4h` score `2.0211` n `44` status `ready` deltaP `18.6114` edge `0.1109` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `2.0211` n `44` status `ready` deltaP `18.6114` edge `0.1109` maxDD `-2.6576`
- `risk_on_high->equity_24h` score `1.7925` n `44` status `ready` deltaP `20.4861` edge `0.0128` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `1.7925` n `44` status `ready` deltaP `20.4861` edge `0.0128` maxDD `0.0`
- `risk_on_high->index_24h` score `1.3895` n `44` status `ready` deltaP `23.2639` edge `-0.0393` maxDD `0.0`
- `risk_on_and_context->index_24h` score `1.3895` n `44` status `ready` deltaP `23.2639` edge `-0.0393` maxDD `0.0`
- `risk_on_high->equity_1h` score `0.8038` n `49` status `ready` deltaP `12.6513` edge `0.0216` maxDD `-0.7834`
- `risk_on_and_context->equity_1h` score `0.8038` n `49` status `ready` deltaP `12.6513` edge `0.0216` maxDD `-0.7834`
- `risk_on_high->metal_4h` score `0.3277` n `44` status `ready` deltaP `5.8758` edge `0.0364` maxDD `-1.3516`
- `risk_on_and_context->metal_4h` score `0.3277` n `44` status `ready` deltaP `5.8758` edge `0.0364` maxDD `-1.3516`
- `risk_on_high->fx_1h` score `0.2285` n `49` status `ready` deltaP `5.8505` edge `0.003` maxDD `-0.1704`
- `risk_on_and_context->fx_1h` score `0.2285` n `49` status `ready` deltaP `5.8505` edge `0.003` maxDD `-0.1704`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

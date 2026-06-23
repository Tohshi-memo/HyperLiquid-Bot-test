# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-23T01:07:27.098608+00:00`
- Price records: `672`
- Market context records: `4468`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11099`

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

- `risk_on_high->unknown_4h` score `123.9746` n `49` status `ready` deltaP `3.4159` edge `10.4915` maxDD `-10.9781`
- `risk_on_and_context->unknown_4h` score `123.9746` n `49` status `ready` deltaP `3.4159` edge `10.4915` maxDD `-10.9781`
- `market_context_high->unknown_1h` score `31.4958` n `233` status `ready` deltaP `3.4496` edge `2.7522` maxDD `-9.7103`
- `market_context_high->unknown_4h` score `14.1619` n `233` status `ready` deltaP `4.2042` edge `1.6986` maxDD `-36.0512`
- `risk_on_high->equity_4h` score `3.6622` n `49` status `ready` deltaP `37.3476` edge `0.0562` maxDD `0.0`
- `risk_on_and_context->equity_4h` score `3.6622` n `49` status `ready` deltaP `37.3476` edge `0.0562` maxDD `0.0`
- `risk_on_high->unknown_24h` score `3.1802` n `44` status `ready` deltaP `15.5619` edge `0.2416` maxDD `-5.0928`
- `risk_on_and_context->unknown_24h` score `3.1802` n `44` status `ready` deltaP `15.5619` edge `0.2416` maxDD `-5.0928`
- `risk_on_high->metal_24h` score `3.1245` n `44` status `ready` deltaP `-14.8358` edge `0.5609` maxDD `-1.9133`
- `risk_on_and_context->metal_24h` score `3.1245` n `44` status `ready` deltaP `-14.8358` edge `0.5609` maxDD `-1.9133`
- `risk_on_high->crypto_major_4h` score `2.3644` n `49` status `ready` deltaP `20.0224` edge `0.1301` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `2.3644` n `49` status `ready` deltaP `20.0224` edge `0.1301` maxDD `-2.6576`
- `risk_on_high->equity_24h` score `2.17` n `44` status `ready` deltaP `21.875` edge `0.035` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `2.17` n `44` status `ready` deltaP `21.875` edge `0.035` maxDD `0.0`
- `risk_on_high->index_24h` score `2.1339` n `44` status `ready` deltaP `23.9583` edge `0.0181` maxDD `0.0`
- `risk_on_and_context->index_24h` score `2.1339` n `44` status `ready` deltaP `23.9583` edge `0.0181` maxDD `0.0`
- `risk_on_high->metal_4h` score `1.2833` n `49` status `ready` deltaP `11.1902` edge `0.0659` maxDD `-1.3516`
- `risk_on_and_context->metal_4h` score `1.2833` n `49` status `ready` deltaP `11.1902` edge `0.0659` maxDD `-1.3516`
- `risk_on_high->equity_1h` score `1.021` n `49` status `ready` deltaP `14.5424` edge `0.0224` maxDD `-0.7415`
- `risk_on_and_context->equity_1h` score `1.021` n `49` status `ready` deltaP `14.5424` edge `0.0224` maxDD `-0.7415`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

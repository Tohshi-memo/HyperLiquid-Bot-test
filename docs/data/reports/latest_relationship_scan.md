# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-23T00:22:26.574741+00:00`
- Price records: `672`
- Market context records: `4465`
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

- `risk_on_high->unknown_4h` score `123.948` n `49` status `ready` deltaP `3.2634` edge `10.4903` maxDD `-10.9781`
- `risk_on_and_context->unknown_4h` score `123.948` n `49` status `ready` deltaP `3.2634` edge `10.4903` maxDD `-10.9781`
- `market_context_high->unknown_1h` score `31.4335` n `233` status `ready` deltaP `3.1502` edge `2.749` maxDD `-9.7103`
- `market_context_high->unknown_4h` score `14.1353` n `233` status `ready` deltaP `4.0517` edge `1.6974` maxDD `-36.0512`
- `risk_on_high->equity_4h` score `3.631` n `49` status `ready` deltaP `37.3476` edge `0.0536` maxDD `0.0`
- `risk_on_and_context->equity_4h` score `3.631` n `49` status `ready` deltaP `37.3476` edge `0.0536` maxDD `0.0`
- `risk_on_high->unknown_24h` score `3.2668` n `44` status `ready` deltaP `15.9091` edge `0.2465` maxDD `-5.0928`
- `risk_on_and_context->unknown_24h` score `3.2668` n `44` status `ready` deltaP `15.9091` edge `0.2465` maxDD `-5.0928`
- `risk_on_high->metal_24h` score `3.0764` n `44` status `ready` deltaP `-15.3567` edge `0.5582` maxDD `-1.9133`
- `risk_on_and_context->metal_24h` score `3.0764` n `44` status `ready` deltaP `-15.3567` edge `0.5582` maxDD `-1.9133`
- `risk_on_high->crypto_major_4h` score `2.3088` n `49` status `ready` deltaP `19.7175` edge `0.1275` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `2.3088` n `49` status `ready` deltaP `19.7175` edge `0.1275` maxDD `-2.6576`
- `risk_on_high->index_24h` score `2.073` n `44` status `ready` deltaP `23.4375` edge `0.0165` maxDD `0.0`
- `risk_on_and_context->index_24h` score `2.073` n `44` status `ready` deltaP `23.4375` edge `0.0165` maxDD `0.0`
- `risk_on_high->equity_24h` score `2.0491` n `44` status `ready` deltaP `21.3542` edge `0.0284` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `2.0491` n `44` status `ready` deltaP `21.3542` edge `0.0284` maxDD `0.0`
- `risk_on_high->metal_4h` score `1.2663` n `49` status `ready` deltaP `11.0378` edge `0.0655` maxDD `-1.3516`
- `risk_on_and_context->metal_4h` score `1.2663` n `49` status `ready` deltaP `11.0378` edge `0.0655` maxDD `-1.3516`
- `risk_on_high->equity_1h` score `1.0054` n `49` status `ready` deltaP `14.5424` edge `0.0211` maxDD `-0.7415`
- `risk_on_and_context->equity_1h` score `1.0054` n `49` status `ready` deltaP `14.5424` edge `0.0211` maxDD `-0.7415`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

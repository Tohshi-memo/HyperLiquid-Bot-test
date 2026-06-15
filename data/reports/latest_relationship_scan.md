# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-15T14:37:39.660311+00:00`
- Price records: `672`
- Market context records: `4000`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10252`

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

- `risk_on_high->unknown_4h` score `146.8786` n `40` status `ready` deltaP `-2.8659` edge `12.4402` maxDD `-10.8303`
- `risk_on_and_context->unknown_4h` score `146.8786` n `40` status `ready` deltaP `-2.8659` edge `12.4402` maxDD `-10.8303`
- `market_context_high->unknown_24h` score `46.7812` n `137` status `ready` deltaP `-3.3011` edge `4.3223` maxDD `-24.1486`
- `market_context_high->unknown_4h` score `25.5437` n `149` status `ready` deltaP `2.7213` edge `2.6514` maxDD `-35.6052`
- `risk_on_high->equity_24h` score `9.1463` n `40` status `ready` deltaP `42.0139` edge `0.4821` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `9.1463` n `40` status `ready` deltaP `42.0139` edge `0.4821` maxDD `0.0`
- `risk_on_high->equity_4h` score `4.0432` n `40` status `ready` deltaP `38.2012` edge `0.087` maxDD `-0.0458`
- `risk_on_and_context->equity_4h` score `4.0432` n `40` status `ready` deltaP `38.2012` edge `0.087` maxDD `-0.0458`
- `market_context_high->index_24h` score `3.0837` n `137` status `ready` deltaP `26.0379` edge `0.1925` maxDD `-7.0621`
- `market_context_high->metal_24h` score `2.7953` n `137` status `ready` deltaP `14.5568` edge `0.2874` maxDD `-9.1203`
- `risk_on_high->index_24h` score `2.6654` n `40` status `ready` deltaP `29.6875` edge `0.0242` maxDD `0.0`
- `risk_on_and_context->index_24h` score `2.6654` n `40` status `ready` deltaP `29.6875` edge `0.0242` maxDD `0.0`
- `market_context_high->equity_4h` score `2.0217` n `149` status `ready` deltaP `19.8958` edge `0.1661` maxDD `-7.0879`
- `market_context_high->equity_24h` score `1.7868` n `137` status `ready` deltaP `16.4665` edge `0.3421` maxDD `-14.5715`
- `risk_on_high->crypto_major_4h` score `1.5834` n `40` status `ready` deltaP `20.6707` edge `0.0607` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `1.5834` n `40` status `ready` deltaP `20.6707` edge `0.0607` maxDD `-2.6576`
- `market_context_high->metal_1h` score `1.2037` n `149` status `ready` deltaP `12.6432` edge `0.0635` maxDD `-1.7983`
- `market_context_high->crypto_major_1h` score `1.1086` n `149` status `ready` deltaP `10.7694` edge `0.0748` maxDD `-2.3372`
- `risk_on_high->commodity_24h` score `1.0503` n `40` status `ready` deltaP `4.1667` edge `0.2879` maxDD `-12.9187`
- `risk_on_and_context->commodity_24h` score `1.0503` n `40` status `ready` deltaP `4.1667` edge `0.2879` maxDD `-12.9187`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

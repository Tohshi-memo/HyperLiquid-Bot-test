# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-07T19:52:24.718870+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10225`

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

- `risk_on_high->unknown_24h` score `150.5821` n `109` status `ready` deltaP `22.3958` edge `12.3992` maxDD `0.0`
- `risk_on_and_context->unknown_24h` score `150.5821` n `109` status `ready` deltaP `22.3958` edge `12.3992` maxDD `0.0`
- `risk_on_high->crypto_major_24h` score `13.1609` n `109` status `ready` deltaP `26.3698` edge `1.1764` maxDD `-15.1034`
- `risk_on_and_context->crypto_major_24h` score `13.1609` n `109` status `ready` deltaP `26.3698` edge `1.1764` maxDD `-15.1034`
- `risk_on_high->crypto_alt_24h` score `11.5981` n `109` status `ready` deltaP `29.2415` edge `0.7777` maxDD `-0.1572`
- `risk_on_and_context->crypto_alt_24h` score `11.5981` n `109` status `ready` deltaP `29.2415` edge `0.7777` maxDD `-0.1572`
- `market_context_high->crypto_alt_24h` score `6.7616` n `223` status `ready` deltaP `23.0047` edge `0.4676` maxDD `-2.5998`
- `risk_on_high->crypto_alt_4h` score `5.7572` n `117` status `ready` deltaP `30.635` edge `0.3127` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `5.7572` n `117` status `ready` deltaP `30.635` edge `0.3127` maxDD `-1.9733`
- `risk_on_high->crypto_major_4h` score `4.9837` n `117` status `ready` deltaP `26.5909` edge `0.3239` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `4.9837` n `117` status `ready` deltaP `26.5909` edge `0.3239` maxDD `-3.8693`
- `market_context_high->equity_24h` score `3.6238` n `223` status `ready` deltaP `14.7569` edge `0.2036` maxDD `0.0`
- `risk_on_high->equity_24h` score `2.8342` n `109` status `ready` deltaP `14.7569` edge `0.1378` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `2.8342` n `109` status `ready` deltaP `14.7569` edge `0.1378` maxDD `0.0`
- `risk_on_high->index_24h` score `1.8359` n `109` status `ready` deltaP `16.5185` edge `0.0471` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `1.8359` n `109` status `ready` deltaP `16.5185` edge `0.0471` maxDD `-0.0051`
- `market_context_high->index_24h` score `1.0969` n `223` status `ready` deltaP `11.1991` edge `0.0561` maxDD `-0.1483`
- `risk_on_high->crypto_alt_1h` score `0.9813` n `117` status `ready` deltaP `4.5461` edge `0.0867` maxDD `-1.1521`
- `risk_on_and_context->crypto_alt_1h` score `0.9813` n `117` status `ready` deltaP `4.5461` edge `0.0867` maxDD `-1.1521`
- `risk_on_high->equity_1h` score `0.5229` n `117` status `ready` deltaP `14.3726` edge `0.0009` maxDD `-2.2516`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

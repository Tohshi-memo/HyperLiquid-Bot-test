# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-15T01:37:30.535620+00:00`
- Price records: `672`
- Market context records: `3947`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11355`

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

- `risk_on_high->unknown_4h` score `144.0816` n `41` status `ready` deltaP `2.8964` edge `12.1687` maxDD `-10.8303`
- `risk_on_and_context->unknown_4h` score `144.0816` n `41` status `ready` deltaP `2.8964` edge `12.1687` maxDD `-10.8303`
- `market_context_high->unknown_4h` score `17.6153` n `171` status `ready` deltaP `-2.4238` edge `2.025` maxDD `-35.6052`
- `market_context_high->unknown_24h` score `14.6228` n `160` status `ready` deltaP `-9.7569` edge `2.5257` maxDD `-87.0337`
- `risk_on_high->equity_24h` score `9.2495` n `41` status `ready` deltaP `42.0139` edge `0.4907` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `9.2495` n `41` status `ready` deltaP `42.0139` edge `0.4907` maxDD `0.0`
- `risk_on_high->equity_4h` score `3.51` n `41` status `ready` deltaP `36.8903` edge `0.0513` maxDD `-0.0458`
- `risk_on_and_context->equity_4h` score `3.51` n `41` status `ready` deltaP `36.8903` edge `0.0513` maxDD `-0.0458`
- `market_context_high->index_24h` score `3.4527` n `160` status `ready` deltaP `26.1111` edge `0.2276` maxDD `-7.1159`
- `market_context_high->metal_24h` score `3.4454` n `160` status `ready` deltaP `17.7778` edge `0.3201` maxDD `-9.1203`
- `market_context_high->equity_24h` score `3.415` n `160` status `ready` deltaP `20.1389` edge `0.4533` maxDD `-14.5715`
- `risk_on_high->index_24h` score `2.8665` n `41` status `ready` deltaP `29.8611` edge `0.0398` maxDD `0.0`
- `risk_on_and_context->index_24h` score `2.8665` n `41` status `ready` deltaP `29.8611` edge `0.0398` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `2.0464` n `41` status `ready` deltaP `22.4085` edge `0.0877` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `2.0464` n `41` status `ready` deltaP `22.4085` edge `0.0877` maxDD `-2.6576`
- `market_context_high->crypto_major_4h` score `1.8368` n `171` status `ready` deltaP `18.2436` edge `0.1881` maxDD `-7.8662`
- `market_context_high->equity_4h` score `1.5118` n `171` status `ready` deltaP `16.0373` edge `0.1535` maxDD `-7.0879`
- `market_context_high->crypto_major_1h` score `0.7624` n `171` status `ready` deltaP `11.5252` edge `0.0855` maxDD `-4.904`
- `market_context_high->metal_1h` score `0.6905` n `171` status `ready` deltaP `10.725` edge `0.0496` maxDD `-2.751`
- `risk_on_high->commodity_24h` score `0.6155` n `41` status `ready` deltaP `3.5569` edge `0.2685` maxDD `-13.9406`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

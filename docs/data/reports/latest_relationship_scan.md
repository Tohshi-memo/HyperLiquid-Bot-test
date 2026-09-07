# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-07T08:22:25.529097+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10451`

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

- `risk_on_high->unknown_24h` score `457.9817` n `93` status `ready` deltaP `26.7361` edge `37.9869` maxDD `0.0`
- `risk_on_and_context->unknown_24h` score `457.9817` n `93` status `ready` deltaP `26.7361` edge `37.9869` maxDD `0.0`
- `market_context_high->unknown_1h` score `24.174` n `241` status `ready` deltaP `-2.3778` edge `2.1028` maxDD `-2.4626`
- `risk_on_high->crypto_major_24h` score `21.9052` n `93` status `ready` deltaP `37.024` edge `1.6303` maxDD `-1.4687`
- `risk_on_and_context->crypto_major_24h` score `21.9052` n `93` status `ready` deltaP `37.024` edge `1.6303` maxDD `-1.4687`
- `risk_on_high->crypto_alt_24h` score `15.0102` n `93` status `ready` deltaP `31.5972` edge `1.0402` maxDD `0.0`
- `risk_on_and_context->crypto_alt_24h` score `15.0102` n `93` status `ready` deltaP `31.5972` edge `1.0402` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `9.2312` n `187` status `ready` deltaP `25.1801` edge `0.6589` maxDD `-2.5998`
- `market_context_high->equity_24h` score `6.5234` n `187` status `ready` deltaP `22.7431` edge `0.392` maxDD `0.0`
- `risk_on_high->crypto_alt_4h` score `5.6816` n `117` status `ready` deltaP `30.635` edge `0.3064` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `5.6816` n `117` status `ready` deltaP `30.635` edge `0.3064` maxDD `-1.9733`
- `risk_on_high->equity_24h` score `5.3534` n `93` status `ready` deltaP `22.7431` edge `0.2945` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `5.3534` n `93` status `ready` deltaP `22.7431` edge `0.2945` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `4.3735` n `117` status `ready` deltaP `24.3043` edge `0.2883` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `4.3735` n `117` status `ready` deltaP `24.3043` edge `0.2883` maxDD `-3.8693`
- `risk_on_high->index_24h` score `2.669` n `93` status `ready` deltaP `22.6423` edge `0.0757` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `2.669` n `93` status `ready` deltaP `22.6423` edge `0.0757` maxDD `-0.0051`
- `market_context_high->index_24h` score `2.4929` n `187` status `ready` deltaP `20.5205` edge `0.0924` maxDD `-0.0505`
- `risk_on_high->crypto_alt_1h` score `1.0388` n `117` status `ready` deltaP `4.9952` edge `0.0885` maxDD `-1.1521`
- `risk_on_and_context->crypto_alt_1h` score `1.0388` n `117` status `ready` deltaP `4.9952` edge `0.0885` maxDD `-1.1521`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

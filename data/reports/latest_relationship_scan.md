# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-11T20:52:27.203016+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11415`

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

- `news_risk_high->unknown_1h` score `546.7591` n `69` status `ready` deltaP `-5.3805` edge `45.6413` maxDD `-1.7068`
- `risk_on_high->crypto_alt_24h` score `23.9949` n `91` status `ready` deltaP `42.2486` edge `1.7409` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `23.9949` n `91` status `ready` deltaP `42.2486` edge `1.7409` maxDD `-0.8386`
- `market_context_high->crypto_alt_24h` score `21.0853` n `151` status `ready` deltaP `37.1471` edge `1.5922` maxDD `-3.9523`
- `risk_on_high->equity_24h` score `9.4947` n `91` status `ready` deltaP `36.9792` edge `0.5447` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `9.4947` n `91` status `ready` deltaP `36.9792` edge `0.5447` maxDD `0.0`
- `market_context_high->equity_24h` score `9.2055` n `151` status `ready` deltaP `36.9792` edge `0.5206` maxDD `0.0`
- `risk_on_high->crypto_alt_4h` score `8.4173` n `91` status `ready` deltaP `41.641` edge `0.461` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `8.4173` n `91` status `ready` deltaP `41.641` edge `0.461` maxDD `-1.9733`
- `risk_on_high->crypto_major_24h` score `7.556` n `91` status `ready` deltaP `25.021` edge `1.2087` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `7.556` n `91` status `ready` deltaP `25.021` edge `1.2087` maxDD `-24.5429`
- `risk_on_high->crypto_major_4h` score `6.5394` n `91` status `ready` deltaP `30.6771` edge `0.4263` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `6.5394` n `91` status `ready` deltaP `30.6771` edge `0.4263` maxDD `-3.8693`
- `risk_on_high->index_24h` score `5.4088` n `91` status `ready` deltaP `51.5644` edge `0.1112` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `5.4088` n `91` status `ready` deltaP `51.5644` edge `0.1112` maxDD `-0.0051`
- `market_context_high->index_24h` score `4.2352` n `151` status `ready` deltaP `43.6028` edge `0.1016` maxDD `-0.1483`
- `risk_on_high->equity_4h` score `3.8103` n `91` status `ready` deltaP `35.6322` edge `0.0893` maxDD `-0.079`
- `risk_on_and_context->equity_4h` score `3.8103` n `91` status `ready` deltaP `35.6322` edge `0.0893` maxDD `-0.079`
- `market_context_high->crypto_alt_4h` score `3.7849` n `151` status `ready` deltaP `24.8445` edge `0.3203` maxDD `-7.6417`
- `market_context_high->equity_4h` score `2.1602` n `151` status `ready` deltaP `28.3183` edge `0.0739` maxDD `-2.6138`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

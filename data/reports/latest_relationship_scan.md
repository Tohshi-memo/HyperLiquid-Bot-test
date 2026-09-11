# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-11T08:22:28.736721+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `12372`

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

- `news_risk_high->unknown_1h` score `750.9149` n `59` status `ready` deltaP `-6.3585` edge `62.6608` maxDD `-1.7068`
- `risk_on_high->crypto_alt_24h` score `21.8549` n `91` status `ready` deltaP `39.1236` edge `1.5834` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `21.8549` n `91` status `ready` deltaP `39.1236` edge `1.5834` maxDD `-0.8386`
- `market_context_high->crypto_alt_24h` score `19.0142` n `174` status `ready` deltaP `35.4227` edge `1.4311` maxDD `-3.9523`
- `market_context_high->equity_24h` score `9.0748` n `174` status `ready` deltaP `33.6806` edge `0.5317` maxDD `0.0`
- `risk_on_high->crypto_alt_4h` score `8.9653` n `91` status `ready` deltaP `41.3361` edge `0.5087` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `8.9653` n `91` status `ready` deltaP `41.3361` edge `0.5087` maxDD `-1.9733`
- `risk_on_high->equity_24h` score `8.5924` n `91` status `ready` deltaP `33.6806` edge `0.4915` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `8.5924` n `91` status `ready` deltaP `33.6806` edge `0.4915` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `7.6619` n `91` status `ready` deltaP `32.0491` edge `0.5107` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `7.6619` n `91` status `ready` deltaP `32.0491` edge `0.5107` maxDD `-3.8693`
- `risk_on_high->crypto_major_24h` score `7.3158` n `91` status `ready` deltaP `25.021` edge `1.1779` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `7.3158` n `91` status `ready` deltaP `25.021` edge `1.1779` maxDD `-24.5429`
- `risk_on_high->index_24h` score `5.3465` n `91` status `ready` deltaP `49.4811` edge `0.1199` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `5.3465` n `91` status `ready` deltaP `49.4811` edge `0.1199` maxDD `-0.0051`
- `market_context_high->index_24h` score `4.2796` n `174` status `ready` deltaP `42.433` edge `0.1131` maxDD `-0.1483`
- `risk_on_high->equity_4h` score `3.6662` n `91` status `ready` deltaP `34.5651` edge `0.0844` maxDD `-0.079`
- `risk_on_and_context->equity_4h` score `3.6662` n `91` status `ready` deltaP `34.5651` edge `0.0844` maxDD `-0.079`
- `market_context_high->equity_4h` score `2.2352` n `174` status `ready` deltaP `26.7907` edge `0.0932` maxDD `-2.843`
- `risk_on_high->equity_1h` score `1.637` n `91` status `ready` deltaP `21.3332` edge `0.022` maxDD `-0.2246`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

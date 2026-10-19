# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-19T02:07:26.364803+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8622`

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

- `market_context_high->commodity_24h` score `1.6388` n `87` status `ready` deltaP `15.3023` edge `0.1197` maxDD `-1.8119`
- `market_context_high->crypto_major_4h` score `1.1014` n `87` status `ready` deltaP `11.2577` edge `0.4066` maxDD `-15.2359`
- `risk_on_high->commodity_24h` score `0.7116` n `54` status `ready` deltaP `13.9613` edge `0.046` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `0.7116` n `54` status `ready` deltaP `13.9613` edge `0.046` maxDD `-1.7154`
- `market_context_high->crypto_major_1h` score `0.3669` n `87` status `ready` deltaP `3.4242` edge `0.1131` maxDD `-3.7781`
- `risk_on_high->equity_1h` score `0.1327` n `54` status `ready` deltaP `11.6117` edge `0.0091` maxDD `-3.3698`
- `risk_on_and_context->equity_1h` score `0.1327` n `54` status `ready` deltaP `11.6117` edge `0.0091` maxDD `-3.3698`
- `risk_on_high->index_1h` score `0.1254` n `54` status `ready` deltaP `6.3063` edge `0.0006` maxDD `-0.5754`
- `risk_on_and_context->index_1h` score `0.1254` n `54` status `ready` deltaP `6.3063` edge `0.0006` maxDD `-0.5754`
- `risk_on_high->fx_1h` score `-0.1121` n `54` status `ready` deltaP `3.1031` edge `-0.0004` maxDD `-0.1065`
- `risk_on_and_context->fx_1h` score `-0.1121` n `54` status `ready` deltaP `3.1031` edge `-0.0004` maxDD `-0.1065`
- `risk_on_high->crypto_major_4h` score `-0.146` n `54` status `ready` deltaP `6.5322` edge `0.1858` maxDD `-11.1788`
- `risk_on_and_context->crypto_major_4h` score `-0.146` n `54` status `ready` deltaP `6.5322` edge `0.1858` maxDD `-11.1788`
- `market_context_high->crypto_major_24h` score `-0.4907` n `87` status `ready` deltaP `2.8018` edge `0.5281` maxDD `-35.1086`
- `market_context_high->fx_1h` score `-0.5329` n `87` status `ready` deltaP `-2.3247` edge `-0.0007` maxDD `-0.503`
- `market_context_high->index_1h` score `-0.5383` n `87` status `ready` deltaP `1.1339` edge `-0.0038` maxDD `-1.1555`
- `risk_on_high->fx_4h` score `-0.555` n `54` status `ready` deltaP `-3.262` edge `0.0025` maxDD `-0.1603`
- `risk_on_and_context->fx_4h` score `-0.555` n `54` status `ready` deltaP `-3.262` edge `0.0025` maxDD `-0.1603`
- `market_context_high->crypto_alt_1h` score `-0.6157` n `87` status `ready` deltaP `-0.9808` edge `0.0776` maxDD `-7.3329`
- `market_context_high->fx_4h` score `-0.6174` n `87` status `ready` deltaP `-2.8788` edge `0.0031` maxDD `-0.7115`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

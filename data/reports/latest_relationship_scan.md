# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-17T14:37:30.815349+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9408`

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

- `risk_on_high->commodity_24h` score `6.9753` n `54` status `ready` deltaP `38.5017` edge `0.3246` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `6.9753` n `54` status `ready` deltaP `38.5017` edge `0.3246` maxDD `0.0`
- `market_context_high->crypto_major_4h` score `4.2068` n `158` status `ready` deltaP `17.9936` edge `0.4018` maxDD `-7.3621`
- `risk_on_high->crypto_major_4h` score `2.375` n `84` status `ready` deltaP `19.6211` edge `0.2383` maxDD `-7.3621`
- `risk_on_and_context->crypto_major_4h` score `2.375` n `84` status `ready` deltaP `19.6211` edge `0.2383` maxDD `-7.3621`
- `market_context_high->crypto_alt_4h` score `1.9838` n `158` status `ready` deltaP `10.3619` edge `0.456` maxDD `-18.7811`
- `market_context_high->crypto_major_1h` score `0.5416` n `170` status `ready` deltaP `5.7643` edge `0.0956` maxDD `-3.7781`
- `market_context_high->metal_4h` score `0.0834` n `158` status `ready` deltaP `9.9279` edge `0.0453` maxDD `-1.6961`
- `risk_on_high->index_1h` score `0.0363` n `90` status `ready` deltaP `5.4054` edge `0.0054` maxDD `-0.7394`
- `risk_on_and_context->index_1h` score `0.0363` n `90` status `ready` deltaP `5.4054` edge `0.0054` maxDD `-0.7394`
- `market_context_high->crypto_alt_1h` score `0.0042` n `170` status `ready` deltaP `6.8017` edge `0.105` maxDD `-7.3329`
- `market_context_high->index_1h` score `-0.1734` n `170` status `ready` deltaP `7.1701` edge `0.0048` maxDD `-1.3195`
- `market_context_high->metal_1h` score `-0.2589` n `170` status `ready` deltaP `6.8334` edge `0.0082` maxDD `-0.9556`
- `risk_on_high->fx_1h` score `-0.2599` n `90` status `ready` deltaP `1.1711` edge `-0.0031` maxDD `-0.376`
- `risk_on_and_context->fx_1h` score `-0.2599` n `90` status `ready` deltaP `1.1711` edge `-0.0031` maxDD `-0.376`
- `market_context_high->equity_1h` score `-0.3518` n `170` status `ready` deltaP `10.1731` edge `0.0385` maxDD `-7.1141`
- `market_context_high->equity_4h` score `-0.4564` n `158` status `ready` deltaP `12.4492` edge `0.2011` maxDD `-17.4086`
- `risk_on_high->equity_1h` score `-0.4819` n `90` status `ready` deltaP `9.5195` edge `0.026` maxDD `-5.3696`
- `risk_on_and_context->equity_1h` score `-0.4819` n `90` status `ready` deltaP `9.5195` edge `0.026` maxDD `-5.3696`
- `risk_on_high->metal_1h` score `-0.5126` n `90` status `ready` deltaP `0.5589` edge `0.0037` maxDD `-0.8513`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

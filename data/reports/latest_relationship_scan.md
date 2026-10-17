# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-17T16:22:29.980342+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9470`

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

- `risk_on_high->commodity_24h` score `6.9093` n `54` status `ready` deltaP `38.5017` edge `0.3191` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `6.9093` n `54` status `ready` deltaP `38.5017` edge `0.3191` maxDD `0.0`
- `market_context_high->crypto_major_4h` score `2.6934` n `165` status `ready` deltaP `15.3354` edge `0.3702` maxDD `-11.1723`
- `market_context_high->crypto_major_1h` score `0.4933` n `174` status `ready` deltaP `5.3703` edge `0.0942` maxDD `-3.7781`
- `risk_on_high->crypto_major_4h` score `0.4888` n `90` status `ready` deltaP `15.3354` edge `0.1974` maxDD `-10.6246`
- `risk_on_and_context->crypto_major_4h` score `0.4888` n `90` status `ready` deltaP `15.3354` edge `0.1974` maxDD `-10.6246`
- `risk_on_high->index_1h` score `0.0627` n `90` status `ready` deltaP `5.7057` edge `0.0056` maxDD `-0.7394`
- `risk_on_and_context->index_1h` score `0.0627` n `90` status `ready` deltaP `5.7057` edge `0.0056` maxDD `-0.7394`
- `market_context_high->crypto_alt_1h` score `0.0267` n `174` status `ready` deltaP `7.1426` edge `0.1046` maxDD `-7.3329`
- `market_context_high->metal_4h` score `-0.1428` n `165` status `ready` deltaP `7.4307` edge `0.0431` maxDD `-1.6961`
- `market_context_high->index_1h` score `-0.189` n `174` status `ready` deltaP `6.8551` edge `0.0049` maxDD `-1.3195`
- `market_context_high->crypto_alt_4h` score `-0.2011` n `165` status `ready` deltaP `8.9588` edge `0.4104` maxDD `-26.6171`
- `risk_on_high->fx_1h` score `-0.267` n `90` status `ready` deltaP `1.021` edge `-0.003` maxDD `-0.376`
- `risk_on_and_context->fx_1h` score `-0.267` n `90` status `ready` deltaP `1.021` edge `-0.003` maxDD `-0.376`
- `market_context_high->metal_1h` score `-0.3082` n `174` status `ready` deltaP `5.9157` edge `0.008` maxDD `-0.9556`
- `market_context_high->equity_1h` score `-0.3861` n `174` status `ready` deltaP `9.8581` edge `0.0385` maxDD `-7.2977`
- `risk_on_high->equity_1h` score `-0.4399` n `90` status `ready` deltaP `9.8198` edge `0.0275` maxDD `-5.3696`
- `risk_on_and_context->equity_1h` score `-0.4399` n `90` status `ready` deltaP `9.8198` edge `0.0275` maxDD `-5.3696`
- `risk_on_high->metal_1h` score `-0.4962` n `90` status `ready` deltaP `0.8583` edge `0.0038` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.4962` n `90` status `ready` deltaP `0.8583` edge `0.0038` maxDD `-0.8513`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

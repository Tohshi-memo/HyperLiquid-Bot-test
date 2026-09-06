# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-06T23:37:28.050438+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10593`

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

- `risk_on_high->unknown_24h` score `313.3325` n `108` status `ready` deltaP `26.7361` edge `25.9328` maxDD `0.0`
- `risk_on_and_context->unknown_24h` score `313.3325` n `108` status `ready` deltaP `26.7361` edge `25.9328` maxDD `0.0`
- `risk_on_high->crypto_major_24h` score `19.3471` n `108` status `ready` deltaP `34.0278` edge `1.4371` maxDD `-1.4687`
- `risk_on_and_context->crypto_major_24h` score `19.3471` n `108` status `ready` deltaP `34.0278` edge `1.4371` maxDD `-1.4687`
- `risk_on_high->crypto_alt_24h` score `13.6408` n `108` status `ready` deltaP `30.0347` edge `0.9365` maxDD `0.0`
- `risk_on_and_context->crypto_alt_24h` score `13.6408` n `108` status `ready` deltaP `30.0347` edge `0.9365` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `8.7962` n `196` status `ready` deltaP `23.9123` edge `0.6311` maxDD `-2.5998`
- `market_context_high->unknown_1h` score `8.0111` n `250` status `ready` deltaP `-4.3593` edge `0.7691` maxDD `-2.4626`
- `market_context_high->equity_24h` score `6.748` n `196` status `ready` deltaP `23.0903` edge `0.4084` maxDD `0.0`
- `risk_on_high->crypto_alt_4h` score `6.4656` n `124` status `ready` deltaP `29.8977` edge `0.3451` maxDD `-0.116`
- `risk_on_and_context->crypto_alt_4h` score `6.4656` n `124` status `ready` deltaP `29.8977` edge `0.3451` maxDD `-0.116`
- `risk_on_high->equity_24h` score `5.89` n `108` status `ready` deltaP `23.0903` edge `0.3369` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `5.89` n `108` status `ready` deltaP `23.0903` edge `0.3369` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `4.2385` n `124` status `ready` deltaP `24.0264` edge `0.2789` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `4.2385` n `124` status `ready` deltaP `24.0264` edge `0.2789` maxDD `-3.8693`
- `market_context_high->index_24h` score `2.7788` n `196` status `ready` deltaP `22.2967` edge `0.096` maxDD `-0.0463`
- `risk_on_high->index_24h` score `2.7601` n `108` status `ready` deltaP `23.0903` edge `0.0803` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `2.7601` n `108` status `ready` deltaP `23.0903` edge `0.0803` maxDD `-0.0051`
- `risk_on_high->crypto_alt_1h` score `0.843` n `131` status `ready` deltaP `4.0328` edge `0.0786` maxDD `-1.1521`
- `risk_on_and_context->crypto_alt_1h` score `0.843` n `131` status `ready` deltaP `4.0328` edge `0.0786` maxDD `-1.1521`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

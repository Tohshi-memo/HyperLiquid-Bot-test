# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-10T02:37:24.916810+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9978`

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

- `risk_on_high->crypto_alt_24h` score `13.816` n `108` status `ready` deltaP `28.8773` edge `0.9818` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `13.816` n `108` status `ready` deltaP `28.8773` edge `0.9818` maxDD `-0.8386`
- `market_context_high->crypto_alt_24h` score `9.1846` n `230` status `ready` deltaP `21.333` edge `0.7059` maxDD `-3.9523`
- `risk_on_high->crypto_alt_4h` score `7.2123` n `108` status `ready` deltaP `37.1387` edge `0.3906` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `7.2123` n `108` status `ready` deltaP `37.1387` edge `0.3906` maxDD `-1.9733`
- `risk_on_high->crypto_major_24h` score `6.5822` n `108` status `ready` deltaP `22.5694` edge `1.1002` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `6.5822` n `108` status `ready` deltaP `22.5694` edge `1.1002` maxDD `-24.5429`
- `risk_on_high->crypto_major_4h` score `5.0396` n `108` status `ready` deltaP `26.5696` edge `0.3287` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `5.0396` n `108` status `ready` deltaP `26.5696` edge `0.3287` maxDD `-3.8693`
- `risk_on_high->index_24h` score `2.9097` n `108` status `ready` deltaP `29.3403` edge `0.0511` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `2.9097` n `108` status `ready` deltaP `29.3403` edge `0.0511` maxDD `-0.0051`
- `market_context_high->equity_24h` score `2.4145` n `230` status `ready` deltaP `13.0208` edge `0.1144` maxDD `0.0`
- `market_context_high->index_24h` score `2.2247` n `230` status `ready` deltaP `24.292` edge `0.0628` maxDD `-0.1483`
- `risk_on_high->equity_24h` score `1.3381` n `108` status `ready` deltaP `13.0208` edge `0.0247` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `1.3381` n `108` status `ready` deltaP `13.0208` edge `0.0247` maxDD `0.0`
- `risk_on_high->crypto_alt_1h` score `1.0939` n `108` status `ready` deltaP `4.3192` edge `0.0976` maxDD `-1.1521`
- `risk_on_and_context->crypto_alt_1h` score `1.0939` n `108` status `ready` deltaP `4.3192` edge `0.0976` maxDD `-1.1521`
- `risk_on_high->metal_24h` score `0.365` n `108` status `ready` deltaP `17.2454` edge `0.0474` maxDD `-0.9131`
- `risk_on_and_context->metal_24h` score `0.365` n `108` status `ready` deltaP `17.2454` edge `0.0474` maxDD `-0.9131`
- `risk_on_high->equity_1h` score `0.2871` n `108` status `ready` deltaP `14.4378` edge `-0.0063` maxDD `-2.2516`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

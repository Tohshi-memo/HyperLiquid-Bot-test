# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-15T20:08:06.019094+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11123`

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

- `news_risk_high->unknown_4h` score `395.9863` n `78` status `ready` deltaP `-23.8274` edge `33.2471` maxDD `-4.1517`
- `news_risk_high->unknown_24h` score `25.368` n `78` status `ready` deltaP `21.1806` edge `1.9728` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `23.5554` n `78` status `ready` deltaP `47.7698` edge `1.6836` maxDD `-1.4626`
- `news_risk_high->crypto_major_24h` score `19.2001` n `78` status `ready` deltaP `39.7303` edge `1.4822` maxDD `-9.098`
- `news_risk_high->equity_24h` score `15.5861` n `78` status `ready` deltaP `49.8531` edge `1.1439` maxDD `-6.5262`
- `news_risk_high->index_24h` score `8.4009` n `78` status `ready` deltaP `59.6821` edge `0.3198` maxDD `-0.075`
- `news_risk_high->metal_24h` score `6.656` n `78` status `ready` deltaP `38.4882` edge `0.3435` maxDD `-0.6334`
- `risk_on_high->commodity_24h` score `5.9752` n `52` status `ready` deltaP `38.1944` edge `0.2433` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `5.9752` n `52` status `ready` deltaP `38.1944` edge `0.2433` maxDD `0.0`
- `market_context_high->commodity_24h` score `4.6782` n `137` status `ready` deltaP `30.8951` edge `0.2364` maxDD `-0.8682`
- `risk_on_high->fx_24h` score `2.9241` n `52` status `ready` deltaP `36.2713` edge `0.0061` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `2.9241` n `52` status `ready` deltaP `36.2713` edge `0.0061` maxDD `-0.0054`
- `market_context_high->fx_24h` score `2.5271` n `137` status `ready` deltaP `33.0849` edge `0.0116` maxDD `-0.0593`
- `risk_on_high->commodity_4h` score `1.6494` n `52` status `ready` deltaP `23.0886` edge `0.0185` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `1.6494` n `52` status `ready` deltaP `23.0886` edge `0.0185` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `1.5491` n `149` status `ready` deltaP `19.5909` edge `0.0403` maxDD `-0.345`
- `news_risk_high->index_4h` score `0.7043` n `78` status `ready` deltaP `17.2686` edge `0.038` maxDD `-0.6935`
- `market_context_high->commodity_1h` score `0.694` n `149` status `ready` deltaP `12.169` edge `0.0144` maxDD `-0.3491`
- `risk_on_high->metal_1h` score `0.1139` n `52` status `ready` deltaP `6.1147` edge `0.0044` maxDD `-0.1115`
- `risk_on_and_context->metal_1h` score `0.1139` n `52` status `ready` deltaP `6.1147` edge `0.0044` maxDD `-0.1115`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

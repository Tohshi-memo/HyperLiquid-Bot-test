# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-31T02:22:27.330637+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11636`

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

- `risk_on_high->crypto_alt_24h` score `20.8207` n `55` status `ready` deltaP `45.4955` edge `1.4798` maxDD `-3.1772`
- `risk_on_and_context->crypto_alt_24h` score `20.8207` n `55` status `ready` deltaP `45.4955` edge `1.4798` maxDD `-3.1772`
- `risk_on_high->unknown_4h` score `10.6083` n `92` status `ready` deltaP `31.6609` edge `0.7158` maxDD `-1.0945`
- `risk_on_and_context->unknown_4h` score `10.6083` n `92` status `ready` deltaP `31.6609` edge `0.7158` maxDD `-1.0945`
- `risk_on_high->crypto_major_24h` score `8.1732` n `55` status `ready` deltaP `26.6099` edge `0.6455` maxDD `-9.0103`
- `risk_on_and_context->crypto_major_24h` score `8.1732` n `55` status `ready` deltaP `26.6099` edge `0.6455` maxDD `-9.0103`
- `market_context_high->crypto_alt_24h` score `7.6455` n `107` status `ready` deltaP `22.9637` edge `0.903` maxDD `-27.517`
- `market_context_high->unknown_4h` score `6.8849` n `149` status `ready` deltaP `21.054` edge `0.4804` maxDD `-1.0945`
- `risk_on_high->fx_24h` score `6.0756` n `55` status `ready` deltaP `68.0556` edge `0.0526` maxDD `0.0`
- `risk_on_and_context->fx_24h` score `6.0756` n `55` status `ready` deltaP `68.0556` edge `0.0526` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `5.1855` n `107` status `ready` deltaP `20.4926` edge `0.5446` maxDD `-17.2607`
- `risk_on_high->metal_24h` score `4.301` n `55` status `ready` deltaP `40.2336` edge `0.1374` maxDD `-0.7767`
- `risk_on_and_context->metal_24h` score `4.301` n `55` status `ready` deltaP `40.2336` edge `0.1374` maxDD `-0.7767`
- `market_context_high->metal_24h` score `3.8249` n `107` status `ready` deltaP `30.429` edge `0.2178` maxDD `-3.1535`
- `risk_on_high->unknown_1h` score `3.641` n `98` status `ready` deltaP `10.4882` edge `0.2712` maxDD `-1.3497`
- `risk_on_and_context->unknown_1h` score `3.641` n `98` status `ready` deltaP `10.4882` edge `0.2712` maxDD `-1.3497`
- `market_context_high->unknown_1h` score `2.6396` n `161` status `ready` deltaP `7.5157` edge `0.2171` maxDD `-1.4454`
- `market_context_high->fx_24h` score `1.0408` n `107` status `ready` deltaP `37.2145` edge `0.0312` maxDD `-1.6688`
- `risk_on_high->commodity_24h` score `0.8686` n `55` status `ready` deltaP `9.6528` edge `0.1458` maxDD `-0.5706`
- `risk_on_and_context->commodity_24h` score `0.8686` n `55` status `ready` deltaP `9.6528` edge `0.1458` maxDD `-0.5706`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

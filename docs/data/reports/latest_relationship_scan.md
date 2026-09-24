# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-24T21:37:28.822651+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9645`

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

- `market_context_high->unknown_1h` score `84.6763` n `47` status `ready` deltaP `10.116` edge `6.996` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `45.7265` n `47` status `ready` deltaP `30.4226` edge `3.647` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `30.3268` n `47` status `ready` deltaP `24.782` edge `2.4` maxDD `-2.7051`
- `market_context_high->equity_24h` score `25.213` n `47` status `ready` deltaP `32.3323` edge `1.9211` maxDD `-2.1786`
- `market_context_high->index_24h` score `7.9559` n `47` status `ready` deltaP `35.9781` edge `0.4361` maxDD `-0.3705`
- `news_risk_high->unknown_1h` score `6.1701` n `114` status `ready` deltaP `-4.0498` edge `0.5656` maxDD `-0.9543`
- `market_context_high->metal_24h` score `4.1339` n `47` status `ready` deltaP `35.0584` edge `0.1346` maxDD `-0.2401`
- `news_risk_high->crypto_alt_1h` score `3.4396` n `114` status `ready` deltaP `16.8847` edge `0.2231` maxDD `-1.5895`
- `market_context_high->index_4h` score `2.9121` n `47` status `ready` deltaP `33.4166` edge `0.0353` maxDD `-0.2323`
- `news_risk_high->crypto_major_4h` score `2.6858` n `103` status `ready` deltaP `17.3203` edge `0.3215` maxDD `-13.719`
- `news_risk_high->crypto_alt_4h` score `2.5862` n `103` status `ready` deltaP `8.7512` edge `0.4023` maxDD `-15.9436`
- `news_risk_high->crypto_major_1h` score `2.5723` n `114` status `ready` deltaP `17.5255` edge `0.1452` maxDD `-1.8141`
- `news_risk_high->commodity_24h` score `2.4421` n `79` status `ready` deltaP `24.4946` edge `0.0917` maxDD `-1.7857`
- `market_context_high->equity_4h` score `2.3673` n `47` status `ready` deltaP `16.992` edge `0.1258` maxDD `-1.3444`
- `news_risk_high->fx_4h` score `1.6095` n `103` status `ready` deltaP `23.4326` edge `0.0415` maxDD `-0.421`
- `news_risk_high->metal_1h` score `1.52` n `114` status `ready` deltaP `19.511` edge `0.0251` maxDD `-0.6142`
- `market_context_high->index_1h` score `0.999` n `47` status `ready` deltaP `15.0592` edge `0.0107` maxDD `-0.2275`
- `market_context_high->equity_1h` score `0.939` n `47` status `ready` deltaP `11.6161` edge `0.0411` maxDD `-1.5564`
- `news_risk_high->crypto_major_24h` score `0.9035` n `79` status `ready` deltaP `-4.9666` edge `1.0532` maxDD `-63.6743`
- `news_risk_high->metal_24h` score `0.7179` n `79` status `ready` deltaP `22.6156` edge `0.0861` maxDD `-7.2536`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

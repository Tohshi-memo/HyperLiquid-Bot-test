# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-03T01:37:24.297220+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5935`

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

- `news_risk_high->unknown_24h` score `4674.2825` n `56` status `ready` deltaP `23.239` edge `389.4107` maxDD `-2.0332`
- `market_context_high->crypto_alt_24h` score `14.4891` n `40` status `ready` deltaP `51.4583` edge `0.9041` maxDD `-2.1786`
- `market_context_high->commodity_24h` score `11.2326` n `40` status `ready` deltaP `51.3194` edge `0.6067` maxDD `-0.6889`
- `news_risk_high->equity_4h` score `4.1565` n `56` status `ready` deltaP `11.5418` edge `0.3458` maxDD `-3.4427`
- `news_risk_high->index_4h` score `1.6716` n `56` status `ready` deltaP `15.9844` edge `0.0708` maxDD `-0.3783`
- `market_context_high->commodity_4h` score `0.8417` n `42` status `ready` deltaP `11.3168` edge `0.1171` maxDD `-2.7703`
- `news_risk_high->equity_1h` score `0.7478` n `56` status `ready` deltaP `9.645` edge `0.0803` maxDD `-2.916`
- `market_context_high->fx_4h` score `0.5213` n `42` status `ready` deltaP `18.7863` edge `0.0212` maxDD `-1.3685`
- `market_context_high->crypto_alt_4h` score `0.5208` n `42` status `ready` deltaP `6.6493` edge `0.113` maxDD `-4.9116`
- `market_context_high->commodity_1h` score `0.365` n `47` status `ready` deltaP `7.5646` edge `0.0338` maxDD `-1.3282`
- `news_risk_high->metal_4h` score `0.2459` n `56` status `ready` deltaP `7.0993` edge `0.0193` maxDD `-0.8085`
- `news_risk_high->index_1h` score `0.0752` n `56` status `ready` deltaP `4.8974` edge `0.0093` maxDD `-0.5845`
- `market_context_high->fx_1h` score `0.0079` n `47` status `ready` deltaP `7.2652` edge `-0.0085` maxDD `-0.7804`
- `news_risk_high->crypto_alt_1h` score `-0.096` n `56` status `ready` deltaP `6.1056` edge `0.0152` maxDD `-3.1233`
- `news_risk_high->fx_1h` score `-0.216` n `56` status `ready` deltaP `0.1604` edge `0.0035` maxDD `-0.2475`
- `news_risk_high->fx_4h` score `-0.2167` n `56` status `ready` deltaP `6.8815` edge `0.0221` maxDD `-0.6604`
- `news_risk_high->crypto_major_1h` score `-0.3255` n `56` status `ready` deltaP `2.9833` edge `0.0104` maxDD `-3.762`
- `news_risk_high->metal_1h` score `-0.3551` n `56` status `ready` deltaP `-0.8982` edge `0.0008` maxDD `-0.5599`
- `market_context_high->fx_24h` score `-0.7307` n `40` status `ready` deltaP `0.6597` edge `0.0327` maxDD `-2.506`
- `news_risk_high->commodity_1h` score `-0.8665` n `56` status `ready` deltaP `2.2455` edge `-0.0194` maxDD `-2.0891`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

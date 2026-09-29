# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-29T12:37:32.458192+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7522`

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

- `news_risk_high->unknown_24h` score `2593.2312` n `139` status `ready` deltaP `1.2153` edge `216.0945` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `16.9462` n `139` status `ready` deltaP `32.9349` edge `1.5878` maxDD `-29.2814`
- `news_risk_high->equity_24h` score `10.5657` n `139` status `ready` deltaP `35.6577` edge `0.8984` maxDD `-11.1179`
- `news_risk_high->crypto_major_24h` score `8.9309` n `139` status `ready` deltaP `26.8035` edge `1.009` maxDD `-26.1424`
- `news_risk_high->index_24h` score `4.3268` n `139` status `ready` deltaP `39.5534` edge `0.1664` maxDD `-2.2287`
- `news_risk_high->metal_24h` score `3.9276` n `139` status `ready` deltaP `31.9332` edge `0.2999` maxDD `-6.8392`
- `news_risk_high->equity_4h` score `2.7228` n `142` status `ready` deltaP `27.9801` edge `0.2013` maxDD `-9.2079`
- `news_risk_high->crypto_alt_4h` score `1.0571` n `142` status `ready` deltaP `8.6332` edge `0.2965` maxDD `-15.9436`
- `news_risk_high->crypto_alt_1h` score `0.7645` n `142` status `ready` deltaP `6.9706` edge `0.1083` maxDD `-4.2849`
- `news_risk_high->equity_1h` score `0.5799` n `142` status `ready` deltaP `7.5525` edge `0.0641` maxDD `-1.957`
- `news_risk_high->index_1h` score `0.4359` n `142` status `ready` deltaP `8.301` edge `0.01` maxDD `-0.3214`
- `news_risk_high->index_4h` score `0.0211` n `142` status `ready` deltaP `8.6826` edge `0.0292` maxDD `-1.493`
- `news_risk_high->crypto_major_1h` score `-0.4188` n `142` status `ready` deltaP `1.8407` edge `0.0623` maxDD `-7.2607`
- `news_risk_high->metal_1h` score `-0.5253` n `142` status `ready` deltaP `1.0141` edge `0.0124` maxDD `-0.7016`
- `news_risk_high->fx_4h` score `-1.3262` n `142` status `ready` deltaP `8.674` edge `-0.0065` maxDD `-3.0414`
- `news_risk_high->metal_4h` score `-1.3499` n `142` status `ready` deltaP `-7.8495` edge `0.0287` maxDD `-3.6214`
- `news_risk_high->crypto_major_4h` score `-1.7394` n `142` status `ready` deltaP `-4.6827` edge `0.0797` maxDD `-13.719`
- `news_risk_high->fx_1h` score `-1.781` n `142` status `ready` deltaP `-8.5456` edge `-0.0034` maxDD `-1.0436`
- `news_risk_high->commodity_1h` score `-1.9866` n `142` status `ready` deltaP `-10.9513` edge `-0.0142` maxDD `-3.3986`
- `news_risk_high->commodity_4h` score `-2.4984` n `142` status `ready` deltaP `-11.1366` edge `-0.0042` maxDD `-8.6825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

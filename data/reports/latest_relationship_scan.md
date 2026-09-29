# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-29T11:52:38.222479+00:00`
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

- `news_risk_high->unknown_24h` score `2597.364` n `139` status `ready` deltaP `1.2153` edge `216.4389` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `16.8298` n `139` status `ready` deltaP `32.9349` edge `1.5781` maxDD `-29.2814`
- `news_risk_high->equity_24h` score `10.4833` n `139` status `ready` deltaP `35.1368` edge `0.895` maxDD `-11.1179`
- `news_risk_high->crypto_major_24h` score `8.9959` n `139` status `ready` deltaP `27.1507` edge `1.0121` maxDD `-26.1424`
- `news_risk_high->index_24h` score `4.2839` n `139` status `ready` deltaP `39.0325` edge `0.1663` maxDD `-2.2287`
- `news_risk_high->metal_24h` score `3.9348` n `139` status `ready` deltaP `31.9332` edge `0.3005` maxDD `-6.8392`
- `news_risk_high->equity_4h` score `2.7012` n `142` status `ready` deltaP `27.9801` edge `0.1995` maxDD `-9.2079`
- `news_risk_high->crypto_alt_4h` score `1.0823` n `142` status `ready` deltaP `8.6332` edge `0.2986` maxDD `-15.9436`
- `news_risk_high->crypto_alt_1h` score `0.7465` n `142` status `ready` deltaP `6.9706` edge `0.1068` maxDD `-4.2849`
- `news_risk_high->equity_1h` score `0.5882` n `142` status `ready` deltaP `7.7022` edge `0.0638` maxDD `-1.957`
- `news_risk_high->index_1h` score `0.4227` n `142` status `ready` deltaP `8.1513` edge `0.0099` maxDD `-0.3214`
- `news_risk_high->index_4h` score `0.0211` n `142` status `ready` deltaP `8.6826` edge `0.0292` maxDD `-1.493`
- `news_risk_high->crypto_major_1h` score `-0.4133` n `142` status `ready` deltaP `1.8407` edge `0.063` maxDD `-7.2607`
- `news_risk_high->metal_1h` score `-0.5553` n `142` status `ready` deltaP `0.7147` edge `0.0119` maxDD `-0.7016`
- `news_risk_high->metal_4h` score `-1.327` n `142` status `ready` deltaP `-7.5446` edge `0.0296` maxDD `-3.6214`
- `news_risk_high->fx_4h` score `-1.3277` n `142` status `ready` deltaP `8.674` edge `-0.0067` maxDD `-3.0414`
- `news_risk_high->crypto_major_4h` score `-1.708` n `142` status `ready` deltaP `-4.3778` edge `0.0817` maxDD `-13.719`
- `news_risk_high->fx_1h` score `-1.8181` n `142` status `ready` deltaP `-8.9947` edge `-0.0035` maxDD `-1.0436`
- `news_risk_high->commodity_1h` score `-2.0053` n `142` status `ready` deltaP `-11.2507` edge `-0.0146` maxDD `-3.3986`
- `news_risk_high->commodity_4h` score `-2.5518` n `142` status `ready` deltaP `-11.5939` edge `-0.008` maxDD `-8.6825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-24T07:37:19.118867+00:00`
- Price records: `672`
- Market context records: `1713`
- Flow alert records: `6840`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8834`

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

- `market_context_high->metal_24h` score `6.5639` n `138` status `ready` deltaP `25.2445` edge `0.6213` maxDD `-12.7414`
- `market_context_high->unknown_24h` score `6.4889` n `138` status `ready` deltaP `17.622` edge `0.9553` maxDD `-35.8966`
- `market_context_high->crypto_alt_4h` score `6.072` n `196` status `ready` deltaP `22.0384` edge `0.5357` maxDD `-9.1295`
- `market_context_high->crypto_major_4h` score `4.5186` n `196` status `ready` deltaP `23.1769` edge `0.4626` maxDD `-10.9117`
- `market_context_high->index_24h` score `3.7756` n `138` status `ready` deltaP `16.4962` edge `0.3275` maxDD `-4.1604`
- `market_context_high->unknown_4h` score `3.1763` n `196` status `ready` deltaP `14.2514` edge `0.3968` maxDD `-11.1695`
- `market_context_high->equity_4h` score `2.9853` n `196` status `ready` deltaP `16.2643` edge `0.2498` maxDD `-5.0894`
- `market_context_high->equity_24h` score `1.2701` n `138` status `ready` deltaP `15.3277` edge `0.4935` maxDD `-33.1875`
- `market_context_high->crypto_alt_1h` score `0.7752` n `196` status `ready` deltaP `7.87` edge `0.1145` maxDD `-4.1892`
- `market_context_high->index_4h` score `0.4948` n `196` status `ready` deltaP `8.3593` edge `0.0944` maxDD `-3.7119`
- `market_context_high->crypto_major_1h` score `0.222` n `196` status `ready` deltaP `5.0471` edge `0.0922` maxDD `-3.9211`
- `market_context_high->crypto_alt_24h` score `0.1307` n `138` status `ready` deltaP `23.7752` edge `1.0333` maxDD `-88.8062`
- `market_context_high->equity_1h` score `0.0035` n `196` status `ready` deltaP `4.5216` edge `0.051` maxDD `-2.8014`
- `market_context_high->metal_4h` score `-0.2626` n `196` status `ready` deltaP `13.0538` edge `0.1485` maxDD `-12.5349`
- `market_context_high->index_1h` score `-0.4886` n `196` status `ready` deltaP `0.773` edge `0.0173` maxDD `-1.7205`
- `market_context_high->metal_1h` score `-0.5097` n `196` status `ready` deltaP `6.2447` edge `0.0266` maxDD `-6.3532`
- `market_context_high->fx_1h` score `-0.6716` n `196` status `ready` deltaP `-3.2659` edge `-0.0011` maxDD `-0.3914`
- `market_context_high->fx_24h` score `-0.8299` n `138` status `ready` deltaP `4.2676` edge `0.0073` maxDD `-1.3925`
- `market_context_high->crypto_major_24h` score `-1.082` n `138` status `ready` deltaP `21.9246` edge `0.5737` maxDD `-62.3533`
- `market_context_high->unknown_1h` score `-1.4413` n `196` status `ready` deltaP `1.8361` edge `0.0146` maxDD `-7.7558`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

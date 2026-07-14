# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-14T07:07:27.020817+00:00`
- Price records: `672`
- Market context records: `6686`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11784`

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

- `market_context_high->unknown_1h` score `2.4899` n `196` status `ready` deltaP `-4.8301` edge `0.3298` maxDD `-3.2083`
- `market_context_high->commodity_24h` score `0.887` n `196` status `ready` deltaP `11.3911` edge `0.1848` maxDD `-5.2791`
- `market_context_high->crypto_major_1h` score `0.302` n `196` status `ready` deltaP `8.9179` edge `0.0517` maxDD `-4.2122`
- `market_context_high->unknown_24h` score `0.1134` n `196` status `ready` deltaP `-2.5404` edge `0.4067` maxDD `-12.3511`
- `market_context_high->crypto_alt_1h` score `0.0665` n `196` status `ready` deltaP `5.6795` edge `0.0441` maxDD `-3.7803`
- `market_context_high->fx_1h` score `-0.2574` n `196` status `ready` deltaP `2.3891` edge `0.0013` maxDD `-0.6845`
- `market_context_high->index_1h` score `-0.4808` n `196` status `ready` deltaP `0.8371` edge `0.0042` maxDD `-0.7136`
- `market_context_high->equity_1h` score `-0.5528` n `196` status `ready` deltaP `3.7547` edge `0.0068` maxDD `-3.8827`
- `market_context_high->commodity_1h` score `-0.5674` n `196` status `ready` deltaP `0.5499` edge `-0.0081` maxDD `-2.1314`
- `market_context_high->metal_1h` score `-0.6042` n `196` status `ready` deltaP `-3.8158` edge `0.0005` maxDD `-1.2017`
- `market_context_high->index_4h` score `-0.8566` n `196` status `ready` deltaP `11.0783` edge `0.0043` maxDD `-5.7046`
- `market_context_high->fx_4h` score `-1.3998` n `196` status `ready` deltaP `6.3371` edge `-0.0005` maxDD `-3.3635`
- `market_context_high->unknown_4h` score `-1.4291` n `196` status `ready` deltaP `-14.4631` edge `0.2179` maxDD `-10.5788`
- `market_context_high->crypto_major_4h` score `-1.4499` n `196` status `ready` deltaP `8.6206` edge `0.0881` maxDD `-16.8495`
- `market_context_high->commodity_4h` score `-1.565` n `196` status `ready` deltaP `-2.7253` edge `-0.033` maxDD `-5.6246`
- `market_context_high->crypto_alt_4h` score `-1.7124` n `196` status `ready` deltaP `6.3807` edge `0.0781` maxDD `-19.2145`
- `market_context_high->metal_4h` score `-2.1324` n `196` status `ready` deltaP `-1.3564` edge `0.0217` maxDD `-5.2172`
- `market_context_high->equity_4h` score `-3.2129` n `196` status `ready` deltaP `7.7992` edge `-0.037` maxDD `-27.1529`
- `market_context_high->fx_24h` score `-5.8218` n `196` status `ready` deltaP `-11.4123` edge `-0.0092` maxDD `-9.6562`
- `market_context_high->metal_24h` score `-7.0018` n `196` status `ready` deltaP `-6.367` edge `-0.0067` maxDD `-28.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

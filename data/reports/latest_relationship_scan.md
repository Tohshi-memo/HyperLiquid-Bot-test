# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-22T05:52:25.080081+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `40`

- Symbol pattern count: `4590`

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

- `market_context_high->unknown_1h` score `10344.102` n `120` status `ready` deltaP `0.8433` edge `862.0227` maxDD `-0.9188`
- `market_context_high->unknown_4h` score `6308.2751` n `120` status `ready` deltaP `-1.0162` edge `525.7269` maxDD `-0.7759`
- `market_context_high->metal_1h` score `-0.2609` n `120` status `ready` deltaP `4.7904` edge `0.0128` maxDD `-2.6517`
- `market_context_high->index_1h` score `-0.3712` n `120` status `ready` deltaP `2.2455` edge `0.0028` maxDD `-1.2295`
- `market_context_high->metal_4h` score `-0.8587` n `120` status `ready` deltaP `7.7134` edge `0.0191` maxDD `-10.1161`
- `market_context_high->fx_1h` score `-1.5005` n `120` status `ready` deltaP `-10.1248` edge `-0.0016` maxDD `-0.4757`
- `market_context_high->fx_4h` score `-1.7642` n `120` status `ready` deltaP `-4.0244` edge `0.0018` maxDD `-1.7591`
- `market_context_high->equity_1h` score `-1.8547` n `120` status `ready` deltaP `5.6437` edge `0.0054` maxDD `-13.1399`
- `market_context_high->commodity_1h` score `-2.4533` n `120` status `ready` deltaP `-10.1048` edge `-0.0239` maxDD `-4.3877`
- `market_context_high->index_4h` score `-2.7364` n `120` status `ready` deltaP `-6.5752` edge `-0.0209` maxDD `-7.0639`
- `market_context_high->crypto_major_1h` score `-2.7652` n `120` status `ready` deltaP `1.2625` edge `-0.0237` maxDD `-13.8788`
- `market_context_high->crypto_alt_1h` score `-3.8456` n `120` status `ready` deltaP `-6.986` edge `-0.0545` maxDD `-13.8848`
- `market_context_high->crypto_major_4h` score `-5.4696` n `120` status `ready` deltaP `-2.8557` edge `0.0107` maxDD `-47.4317`
- `market_context_high->fx_24h` score `-5.6536` n `120` status `ready` deltaP `-7.6736` edge `-0.0013` maxDD `-6.8271`
- `market_context_high->crypto_alt_4h` score `-6.046` n `120` status `ready` deltaP `-3.0082` edge `-0.0738` maxDD `-46.5016`
- `market_context_high->commodity_4h` score `-6.9067` n `120` status `ready` deltaP `-18.8008` edge `-0.0821` maxDD `-15.4496`
- `market_context_high->metal_24h` score `-8.5823` n `120` status `ready` deltaP `1.1111` edge `0.087` maxDD `-52.1012`
- `market_context_high->crypto_major_24h` score `-13.511` n `120` status `ready` deltaP `12.0486` edge `0.2475` maxDD `-152.134`
- `market_context_high->index_24h` score `-15.3441` n `120` status `ready` deltaP `-29.5833` edge `-0.1379` maxDD `-40.151`
- `market_context_high->crypto_alt_24h` score `-16.1645` n `120` status `ready` deltaP `3.0209` edge `0.0257` maxDD `-156.7906`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

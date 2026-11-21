# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-21T06:07:37.352876+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `24`

- Symbol pattern count: `2704`

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

- `market_context_high->unknown_1h` score `10087.0769` n `126` status `ready` deltaP `1.1643` edge `840.6018` maxDD `-0.9188`
- `market_context_high->unknown_4h` score `6140.7645` n `126` status `ready` deltaP `-0.3145` edge `511.763` maxDD `-0.7759`
- `market_context_high->crypto_major_24h` score `3.417` n `108` status `ready` deltaP `26.794` edge `1.0662` maxDD `-57.8734`
- `market_context_high->metal_1h` score `-0.1914` n `126` status `ready` deltaP `3.9516` edge `0.0156` maxDD `-2.6517`
- `market_context_high->index_1h` score `-0.296` n `126` status `ready` deltaP `2.8585` edge `0.0042` maxDD `-1.2295`
- `market_context_high->metal_4h` score `-0.5227` n `126` status `ready` deltaP `11.491` edge `0.037` maxDD `-10.1161`
- `market_context_high->fx_1h` score `-1.407` n `126` status `ready` deltaP `-8.9559` edge `-0.0016` maxDD `-0.4757`
- `market_context_high->equity_1h` score `-1.7663` n `126` status `ready` deltaP `5.988` edge `0.0188` maxDD `-13.1399`
- `market_context_high->crypto_alt_24h` score `-1.9339` n `108` status `ready` deltaP `13.8311` edge `0.7367` maxDD `-72.5383`
- `market_context_high->fx_4h` score `-1.9349` n `126` status `ready` deltaP `-7.0315` edge `0.0004` maxDD `-1.794`
- `market_context_high->commodity_1h` score `-2.232` n `126` status `ready` deltaP `-7.6229` edge `-0.022` maxDD `-4.3877`
- `market_context_high->crypto_major_1h` score `-2.3072` n `126` status `ready` deltaP `3.0082` edge `0.0195` maxDD `-13.8788`
- `market_context_high->index_4h` score `-2.3593` n `126` status `ready` deltaP `-3.0318` edge `-0.0131` maxDD `-7.0639`
- `market_context_high->crypto_alt_1h` score `-3.0407` n `126` status `ready` deltaP `-3.5952` edge `-0.0017` maxDD `-13.8848`
- `market_context_high->crypto_major_4h` score `-4.1942` n `126` status `ready` deltaP `-0.4985` edge `0.1585` maxDD `-47.4317`
- `market_context_high->metal_24h` score `-5.8391` n `108` status `ready` deltaP `12.4422` edge `0.1198` maxDD `-45.1471`
- `market_context_high->fx_24h` score `-6.5318` n `108` status `ready` deltaP `-16.2616` edge `-0.0086` maxDD `-5.5179`
- `market_context_high->commodity_4h` score `-6.8712` n `126` status `ready` deltaP `-18.6629` edge `-0.0789` maxDD `-15.5426`
- `market_context_high->crypto_alt_4h` score `-7.3105` n `126` status `ready` deltaP `-0.6509` edge `0.0764` maxDD `-46.5016`
- `market_context_high->index_24h` score `-12.6852` n `108` status `ready` deltaP `-26.3888` edge `-0.1182` maxDD `-31.7046`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

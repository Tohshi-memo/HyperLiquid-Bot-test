# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-06T07:52:29.888920+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11781`

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

- `market_context_high->unknown_24h` score `11.7827` n `92` status `ready` deltaP `4.4686` edge `0.9564` maxDD `-0.0103`
- `market_context_high->unknown_4h` score `4.0848` n `109` status `ready` deltaP `-1.1929` edge `0.4479` maxDD `-3.6303`
- `market_context_high->commodity_4h` score `1.1996` n `109` status `ready` deltaP `13.9042` edge `0.0919` maxDD `-2.7703`
- `market_context_high->metal_24h` score `0.882` n `92` status `ready` deltaP `2.7626` edge `0.2115` maxDD `-2.6802`
- `market_context_high->fx_24h` score `0.5509` n `92` status `ready` deltaP `21.0598` edge `0.0508` maxDD `-4.3126`
- `market_context_high->commodity_1h` score `0.4491` n `109` status `ready` deltaP `8.0591` edge `0.0253` maxDD `-1.3282`
- `market_context_high->fx_1h` score `-0.0255` n `109` status `ready` deltaP `5.3837` edge `-0.003` maxDD `-0.8012`
- `market_context_high->fx_4h` score `-0.1889` n `109` status `ready` deltaP `8.2471` edge `0.0068` maxDD `-1.8797`
- `market_context_high->metal_1h` score `-0.5424` n `109` status `ready` deltaP `-1.8596` edge `-0.0077` maxDD `-1.6224`
- `market_context_high->index_1h` score `-0.7611` n `109` status `ready` deltaP `-3.656` edge `-0.0198` maxDD `-1.6054`
- `market_context_high->metal_4h` score `-0.776` n `109` status `ready` deltaP `2.9369` edge `0.0044` maxDD `-3.211`
- `market_context_high->index_24h` score `-1.2665` n `92` status `ready` deltaP `-3.1023` edge `0.0778` maxDD `-7.8922`
- `market_context_high->crypto_alt_24h` score `-1.3306` n `92` status `ready` deltaP `0.2868` edge `-0.0282` maxDD `-4.5445`
- `market_context_high->crypto_alt_1h` score `-1.5457` n `109` status `ready` deltaP `-5.4373` edge `-0.0215` maxDD `-3.0178`
- `market_context_high->equity_1h` score `-1.851` n `109` status `ready` deltaP `0.9697` edge `-0.0902` maxDD `-10.619`
- `market_context_high->index_4h` score `-2.0988` n `109` status `ready` deltaP `-12.5154` edge `-0.0602` maxDD `-4.7021`
- `market_context_high->crypto_alt_4h` score `-2.1573` n `109` status `ready` deltaP `1.2321` edge `-0.049` maxDD `-5.7857`
- `market_context_high->unknown_1h` score `-2.2012` n `109` status `ready` deltaP `1.2841` edge `-0.1473` maxDD `-1.2421`
- `market_context_high->crypto_major_1h` score `-3.345` n `109` status `ready` deltaP `-11.7481` edge `-0.0631` maxDD `-7.6533`
- `market_context_high->commodity_24h` score `-6.3868` n `92` status `ready` deltaP `7.4124` edge `-0.0361` maxDD `-51.2378`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

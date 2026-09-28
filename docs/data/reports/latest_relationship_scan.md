# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-28T21:07:31.747785+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7310`

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

- `news_risk_high->unknown_24h` score `2670.7164` n `139` status `ready` deltaP `1.2153` edge `222.5516` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `10.2377` n `139` status `ready` deltaP `26.1641` edge `1.0739` maxDD `-29.2814`
- `news_risk_high->equity_24h` score `6.6049` n `139` status `ready` deltaP `25.7618` edge `0.6343` maxDD `-11.1179`
- `news_risk_high->crypto_major_24h` score `6.268` n `139` status `ready` deltaP `21.9424` edge `0.8195` maxDD `-26.1424`
- `news_risk_high->index_24h` score `3.3788` n `139` status `ready` deltaP `31.3936` edge `0.1418` maxDD `-2.2287`
- `news_risk_high->metal_24h` score `2.5416` n `139` status `ready` deltaP `23.7735` edge `0.2388` maxDD `-6.8392`
- `news_risk_high->equity_4h` score `2.4761` n `139` status `ready` deltaP `26.4114` edge `0.1912` maxDD `-9.2079`
- `news_risk_high->crypto_alt_4h` score `0.8261` n `139` status `ready` deltaP `8.0409` edge `0.2812` maxDD `-15.9436`
- `news_risk_high->crypto_alt_1h` score `0.6171` n `139` status `ready` deltaP `6.7182` edge `0.0977` maxDD `-4.2849`
- `news_risk_high->equity_1h` score `0.538` n `139` status `ready` deltaP `7.554` edge `0.0606` maxDD `-1.957`
- `news_risk_high->index_1h` score `0.4695` n `139` status `ready` deltaP `8.9013` edge `0.0088` maxDD `-0.3214`
- `news_risk_high->index_4h` score `-0.1429` n `139` status `ready` deltaP `6.9629` edge `0.027` maxDD `-1.493`
- `news_risk_high->metal_1h` score `-0.4968` n `139` status `ready` deltaP `1.6402` edge `0.0106` maxDD `-0.7016`
- `news_risk_high->crypto_major_1h` score `-0.5669` n `139` status `ready` deltaP `0.4469` edge `0.0526` maxDD `-7.2607`
- `news_risk_high->fx_1h` score `-1.1889` n `139` status `ready` deltaP `-9.2675` edge `-0.0026` maxDD `-1.0436`
- `news_risk_high->fx_4h` score `-1.2792` n `139` status `ready` deltaP `9.0674` edge `-0.0031` maxDD `-3.0414`
- `news_risk_high->metal_4h` score `-1.4264` n `139` status `ready` deltaP `-9.1562` edge `0.0276` maxDD `-3.6214`
- `news_risk_high->crypto_major_4h` score `-1.8326` n `139` status `ready` deltaP `-5.2433` edge `0.0715` maxDD `-13.719`
- `news_risk_high->commodity_1h` score `-2.0661` n `139` status `ready` deltaP `-12.465` edge `-0.0143` maxDD `-3.3986`
- `news_risk_high->commodity_4h` score `-3.7934` n `139` status `ready` deltaP `-11.0173` edge `-0.0008` maxDD `-8.6825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-28T20:37:49.800705+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7314`

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

- `news_risk_high->unknown_24h` score `2671.764` n `139` status `ready` deltaP `1.2153` edge `222.6389` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `9.9675` n `139` status `ready` deltaP `25.8169` edge `1.0537` maxDD `-29.2814`
- `news_risk_high->equity_24h` score `6.3983` n `139` status `ready` deltaP `25.4146` edge `0.6194` maxDD `-11.1179`
- `news_risk_high->crypto_major_24h` score `6.1605` n `139` status `ready` deltaP `21.7688` edge `0.8117` maxDD `-26.1424`
- `news_risk_high->index_24h` score `3.333` n `139` status `ready` deltaP `31.0464` edge `0.1403` maxDD `-2.2287`
- `news_risk_high->metal_24h` score `2.4538` n `139` status `ready` deltaP `23.4263` edge `0.2338` maxDD `-6.8392`
- `news_risk_high->equity_4h` score `2.4265` n `139` status `ready` deltaP `26.1066` edge `0.1891` maxDD `-9.2079`
- `news_risk_high->crypto_alt_4h` score `0.7827` n `139` status `ready` deltaP `7.8884` edge `0.2786` maxDD `-15.9436`
- `news_risk_high->crypto_alt_1h` score `0.6387` n `139` status `ready` deltaP `6.8679` edge `0.0985` maxDD `-4.2849`
- `news_risk_high->equity_1h` score `0.5224` n `139` status `ready` deltaP `7.4043` edge `0.0603` maxDD `-1.957`
- `news_risk_high->index_1h` score `0.4695` n `139` status `ready` deltaP `8.9013` edge `0.0088` maxDD `-0.3214`
- `news_risk_high->index_4h` score `-0.1575` n `139` status `ready` deltaP `6.8104` edge `0.0268` maxDD `-1.493`
- `news_risk_high->metal_1h` score `-0.5112` n `139` status `ready` deltaP `1.4905` edge `0.0104` maxDD `-0.7016`
- `news_risk_high->crypto_major_1h` score `-0.5607` n `139` status `ready` deltaP `0.5966` edge `0.0524` maxDD `-7.2607`
- `news_risk_high->fx_1h` score `-1.1889` n `139` status `ready` deltaP `-9.2675` edge `-0.0026` maxDD `-1.0436`
- `news_risk_high->fx_4h` score `-1.2674` n `139` status `ready` deltaP `9.2198` edge `-0.0026` maxDD `-3.0414`
- `news_risk_high->metal_4h` score `-1.4485` n `139` status `ready` deltaP `-9.461` edge `0.0268` maxDD `-3.6214`
- `news_risk_high->crypto_major_4h` score `-1.8318` n `139` status `ready` deltaP `-5.2433` edge `0.0716` maxDD `-13.719`
- `news_risk_high->commodity_1h` score `-2.0466` n `139` status `ready` deltaP `-12.1656` edge `-0.0138` maxDD `-3.3986`
- `news_risk_high->commodity_4h` score `-3.7946` n `139` status `ready` deltaP `-11.0173` edge `-0.0009` maxDD `-8.6825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

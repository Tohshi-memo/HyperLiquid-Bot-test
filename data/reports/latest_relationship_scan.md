# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-29T06:52:32.353599+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7376`

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

- `news_risk_high->unknown_24h` score `2618.5224` n `139` status `ready` deltaP `1.2153` edge `218.2021` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `15.961` n `139` status `ready` deltaP `32.9349` edge `1.5057` maxDD `-29.2814`
- `news_risk_high->equity_24h` score `9.7601` n `139` status `ready` deltaP `32.5327` edge `0.8521` maxDD `-11.1179`
- `news_risk_high->crypto_major_24h` score `9.0405` n `139` status `ready` deltaP `27.498` edge `1.0135` maxDD `-26.1424`
- `news_risk_high->index_24h` score `4.0668` n `139` status `ready` deltaP `36.9492` edge `0.1621` maxDD `-2.2287`
- `news_risk_high->metal_24h` score `3.751` n `139` status `ready` deltaP `30.3707` edge `0.2956` maxDD `-6.8392`
- `news_risk_high->equity_4h` score `2.5123` n `139` status `ready` deltaP `27.4785` edge `0.1871` maxDD `-9.2079`
- `news_risk_high->crypto_alt_4h` score `1.2057` n `139` status `ready` deltaP `9.2604` edge `0.3047` maxDD `-15.9436`
- `news_risk_high->crypto_alt_1h` score `0.9264` n `142` status `ready` deltaP `7.7191` edge `0.1168` maxDD `-4.2849`
- `news_risk_high->equity_1h` score `0.7176` n `142` status `ready` deltaP `8.8998` edge `0.0666` maxDD `-1.957`
- `news_risk_high->index_1h` score `0.4994` n `142` status `ready` deltaP `9.0495` edge `0.0103` maxDD `-0.3214`
- `news_risk_high->index_4h` score `-0.0831` n `139` status `ready` deltaP `7.7251` edge `0.0269` maxDD `-1.493`
- `news_risk_high->crypto_major_1h` score `-0.4367` n `142` status `ready` deltaP `1.3916` edge `0.063` maxDD `-7.2607`
- `news_risk_high->metal_1h` score `-0.5134` n `142` status `ready` deltaP `1.3135` edge `0.0114` maxDD `-0.7016`
- `news_risk_high->fx_4h` score `-1.3272` n `139` status `ready` deltaP `8.61` edge `-0.0062` maxDD `-3.0414`
- `news_risk_high->metal_4h` score `-1.4514` n `139` status `ready` deltaP `-9.1562` edge `0.0244` maxDD `-3.6214`
- `news_risk_high->crypto_major_4h` score `-1.8348` n `139` status `ready` deltaP `-5.0908` edge `0.0702` maxDD `-13.719`
- `news_risk_high->fx_1h` score `-1.8876` n `142` status `ready` deltaP `-9.8929` edge `-0.0033` maxDD `-1.0436`
- `news_risk_high->commodity_1h` score `-2.0606` n `142` status `ready` deltaP `-12.2986` edge `-0.0147` maxDD `-3.3986`
- `news_risk_high->commodity_4h` score `-3.9905` n `139` status `ready` deltaP `-12.2368` edge `-0.0091` maxDD `-8.6825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

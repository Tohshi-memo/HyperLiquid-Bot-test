# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-29T03:52:28.427316+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7190`

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

- `news_risk_high->unknown_24h` score `2626.746` n `139` status `ready` deltaP `1.2153` edge `218.8874` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `14.3471` n `139` status `ready` deltaP `30.8516` edge `1.3851` maxDD `-29.2814`
- `news_risk_high->equity_24h` score `8.8183` n `139` status `ready` deltaP `30.4493` edge `0.7875` maxDD `-11.1179`
- `news_risk_high->crypto_major_24h` score `8.2454` n `139` status `ready` deltaP `26.1091` edge `0.9565` maxDD `-26.1424`
- `news_risk_high->index_24h` score `3.8198` n `139` status `ready` deltaP `34.8659` edge `0.1554` maxDD `-2.2287`
- `news_risk_high->metal_24h` score `3.4283` n `139` status `ready` deltaP `28.2874` edge `0.2826` maxDD `-6.8392`
- `news_risk_high->equity_4h` score `2.4723` n `139` status `ready` deltaP `27.1736` edge `0.1858` maxDD `-9.2079`
- `news_risk_high->crypto_alt_4h` score `1.2115` n `139` status `ready` deltaP `9.108` edge `0.3062` maxDD `-15.9436`
- `news_risk_high->crypto_alt_1h` score `0.7898` n `139` status `ready` deltaP `7.4667` edge `0.1071` maxDD `-4.2849`
- `news_risk_high->equity_1h` score `0.6194` n `139` status `ready` deltaP `8.3025` edge `0.0624` maxDD `-1.957`
- `news_risk_high->index_1h` score `0.4611` n `139` status `ready` deltaP `8.7516` edge `0.0091` maxDD `-0.3214`
- `news_risk_high->index_4h` score `-0.1269` n `139` status `ready` deltaP `7.2678` edge `0.0263` maxDD `-1.493`
- `news_risk_high->crypto_major_1h` score `-0.5513` n `139` status `ready` deltaP `0.5966` edge `0.0536` maxDD `-7.2607`
- `news_risk_high->metal_1h` score `-0.5747` n `139` status `ready` deltaP `0.742` edge `0.0101` maxDD `-0.7016`
- `news_risk_high->fx_1h` score `-1.2419` n `139` status `ready` deltaP `-10.1657` edge `-0.0034` maxDD `-1.0436`
- `news_risk_high->fx_4h` score `-1.3233` n `139` status `ready` deltaP `8.61` edge `-0.0057` maxDD `-3.0414`
- `news_risk_high->metal_4h` score `-1.4585` n `139` status `ready` deltaP `-9.3086` edge `0.0245` maxDD `-3.6214`
- `news_risk_high->crypto_major_4h` score `-1.8123` n `139` status `ready` deltaP `-5.2433` edge `0.0741` maxDD `-13.719`
- `news_risk_high->commodity_1h` score `-2.0116` n `139` status `ready` deltaP `-11.5668` edge `-0.0133` maxDD `-3.3986`
- `news_risk_high->commodity_4h` score `-3.7424` n `139` status `ready` deltaP `-10.56` edge `0.0004` maxDD `-8.6825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

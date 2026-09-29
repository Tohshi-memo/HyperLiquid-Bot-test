# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-29T04:22:28.420084+00:00`
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

- `news_risk_high->unknown_24h` score `2626.44` n `139` status `ready` deltaP `1.2153` edge `218.8619` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `14.6281` n `139` status `ready` deltaP `31.1988` edge `1.4062` maxDD `-29.2814`
- `news_risk_high->equity_24h` score `8.9684` n `139` status `ready` deltaP `30.7966` edge `0.7977` maxDD `-11.1179`
- `news_risk_high->crypto_major_24h` score `8.3967` n `139` status `ready` deltaP `26.4563` edge `0.9668` maxDD `-26.1424`
- `news_risk_high->index_24h` score `3.8595` n `139` status `ready` deltaP `35.2131` edge `0.1564` maxDD `-2.2287`
- `news_risk_high->metal_24h` score `3.4849` n `139` status `ready` deltaP `28.6346` edge `0.285` maxDD `-6.8392`
- `news_risk_high->equity_4h` score `2.4591` n `139` status `ready` deltaP `27.1736` edge `0.1847` maxDD `-9.2079`
- `news_risk_high->crypto_alt_4h` score `1.2571` n `139` status `ready` deltaP `9.108` edge `0.31` maxDD `-15.9436`
- `news_risk_high->crypto_alt_1h` score `0.7238` n `139` status `ready` deltaP `7.1673` edge `0.1036` maxDD `-4.2849`
- `news_risk_high->equity_1h` score `0.6062` n `139` status `ready` deltaP `8.3025` edge `0.0613` maxDD `-1.957`
- `news_risk_high->index_1h` score `0.4611` n `139` status `ready` deltaP `8.7516` edge `0.0091` maxDD `-0.3214`
- `news_risk_high->index_4h` score `-0.1281` n `139` status `ready` deltaP `7.2678` edge `0.0262` maxDD `-1.493`
- `news_risk_high->metal_1h` score `-0.5591` n `139` status `ready` deltaP `0.8917` edge `0.0104` maxDD `-0.7016`
- `news_risk_high->crypto_major_1h` score `-0.5957` n `139` status `ready` deltaP `0.2972` edge `0.0499` maxDD `-7.2607`
- `news_risk_high->fx_1h` score `-1.2419` n `139` status `ready` deltaP `-10.1657` edge `-0.0034` maxDD `-1.0436`
- `news_risk_high->fx_4h` score `-1.3138` n `139` status `ready` deltaP `8.7625` edge `-0.0055` maxDD `-3.0414`
- `news_risk_high->metal_4h` score `-1.4624` n `139` status `ready` deltaP `-9.3086` edge `0.024` maxDD `-3.6214`
- `news_risk_high->crypto_major_4h` score `-1.817` n `139` status `ready` deltaP `-5.2433` edge `0.0735` maxDD `-13.719`
- `news_risk_high->commodity_1h` score `-2.0116` n `139` status `ready` deltaP `-11.5668` edge `-0.0133` maxDD `-3.3986`
- `news_risk_high->commodity_4h` score `-3.7728` n `139` status `ready` deltaP `-10.8649` edge `-0.0001` maxDD `-8.6825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

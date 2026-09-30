# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-30T01:52:25.661491+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7026`

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

- `news_risk_high->unknown_24h` score `1518.67` n `135` status `ready` deltaP `1.9097` edge `126.5431` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `17.5812` n `135` status `ready` deltaP `29.6296` edge `1.434` maxDD `-12.3145`
- `news_risk_high->equity_24h` score `8.8325` n `135` status `ready` deltaP `29.6297` edge `0.7734` maxDD `-9.4579`
- `news_risk_high->crypto_major_24h` score `8.5963` n `135` status `ready` deltaP `25.1158` edge `0.8643` maxDD `-15.8971`
- `news_risk_high->index_24h` score `3.9792` n `135` status `ready` deltaP `35.8218` edge `0.1459` maxDD `-0.9159`
- `news_risk_high->metal_24h` score `3.4942` n `135` status `ready` deltaP `27.9977` edge `0.2515` maxDD `-3.7574`
- `news_risk_high->equity_4h` score `2.9118` n `138` status `ready` deltaP `29.3655` edge `0.207` maxDD `-9.143`
- `news_risk_high->crypto_alt_4h` score `2.3131` n `138` status `ready` deltaP `12.6635` edge `0.3743` maxDD `-15.9436`
- `news_risk_high->crypto_alt_1h` score `1.2578` n `138` status `ready` deltaP `9.672` edge `0.1314` maxDD `-4.2849`
- `news_risk_high->equity_1h` score `0.8376` n `138` status `ready` deltaP `8.8215` edge `0.0733` maxDD `-1.6514`
- `news_risk_high->index_1h` score `0.5427` n `138` status `ready` deltaP `9.4203` edge `0.0112` maxDD `-0.302`
- `news_risk_high->index_4h` score `-0.0463` n `138` status `ready` deltaP `7.9312` edge `0.0286` maxDD `-1.493`
- `news_risk_high->crypto_major_1h` score `-0.2141` n `138` status `ready` deltaP `3.467` edge `0.0777` maxDD `-7.2607`
- `news_risk_high->metal_1h` score `-0.5082` n `138` status `ready` deltaP `0.8678` edge `0.0148` maxDD `-0.7016`
- `news_risk_high->metal_4h` score `-1.3006` n `138` status `ready` deltaP `-7.9777` edge `0.0293` maxDD `-3.0957`
- `news_risk_high->crypto_major_4h` score `-1.3031` n `138` status `ready` deltaP `-2.291` edge `0.1197` maxDD `-13.719`
- `news_risk_high->fx_4h` score `-1.4422` n `138` status `ready` deltaP `6.7427` edge `-0.0085` maxDD `-3.0414`
- `news_risk_high->commodity_1h` score `-1.861` n `138` status `ready` deltaP `-9.2706` edge `-0.0093` maxDD `-3.3986`
- `news_risk_high->fx_1h` score `-1.9119` n `138` status `ready` deltaP `-10.0018` edge `-0.0046` maxDD `-1.0436`
- `news_risk_high->commodity_4h` score `-2.2673` n `138` status `ready` deltaP `-9.153` edge `0.0122` maxDD `-8.6825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

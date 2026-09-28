# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-28T13:22:28.591314+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7922`

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

- `news_risk_high->unknown_24h` score `1227.3` n `139` status `ready` deltaP `1.2153` edge `102.2669` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `6.6753` n `139` status `ready` deltaP `21.1294` edge `0.8106` maxDD `-29.2814`
- `news_risk_high->crypto_major_24h` score `4.0185` n `139` status `ready` deltaP `16.9077` edge `0.6656` maxDD `-26.1424`
- `news_risk_high->equity_24h` score `3.5211` n `139` status `ready` deltaP `20.3799` edge `0.4132` maxDD `-11.1179`
- `news_risk_high->index_24h` score `2.659` n `139` status `ready` deltaP `26.0117` edge `0.1177` maxDD `-2.2287`
- `news_risk_high->equity_4h` score `1.8236` n `139` status `ready` deltaP `22.9053` edge `0.1602` maxDD `-9.2079`
- `news_risk_high->metal_24h` score `1.5246` n `139` status `ready` deltaP `20.3013` edge `0.1772` maxDD `-6.8392`
- `news_risk_high->crypto_alt_4h` score `0.603` n `139` status `ready` deltaP `7.1262` edge `0.2687` maxDD `-15.9436`
- `news_risk_high->crypto_alt_1h` score `0.5007` n `139` status `ready` deltaP `6.5685` edge `0.089` maxDD `-4.2849`
- `news_risk_high->index_1h` score `0.3126` n `139` status `ready` deltaP `7.2546` edge `0.0067` maxDD `-0.3214`
- `news_risk_high->equity_1h` score `0.2718` n `139` status `ready` deltaP `5.9073` edge `0.0494` maxDD `-1.957`
- `news_risk_high->index_4h` score `-0.398` n `139` status `ready` deltaP `4.5239` edge `0.022` maxDD `-1.493`
- `news_risk_high->metal_1h` score `-0.5172` n `139` status `ready` deltaP `1.4905` edge `0.0099` maxDD `-0.7016`
- `news_risk_high->crypto_major_1h` score `-0.7329` n `139` status `ready` deltaP `-0.4513` edge `0.0373` maxDD `-7.2607`
- `news_risk_high->fx_4h` score `-1.1534` n `139` status `ready` deltaP `11.2015` edge `-0.0012` maxDD `-3.0414`
- `news_risk_high->fx_1h` score `-1.1555` n `139` status `ready` deltaP `-8.6687` edge `-0.0023` maxDD `-1.0436`
- `news_risk_high->metal_4h` score `-1.5605` n `139` status `ready` deltaP `-10.9854` edge `0.0226` maxDD `-3.6214`
- `news_risk_high->commodity_1h` score `-2.024` n `139` status `ready` deltaP `-11.7165` edge `-0.0139` maxDD `-3.3986`
- `news_risk_high->crypto_major_4h` score `-2.1318` n `139` status `ready` deltaP `-6.7677` edge `0.0433` maxDD `-13.719`
- `news_risk_high->commodity_4h` score `-4.0755` n `139` status `ready` deltaP `-12.999` edge `-0.0111` maxDD `-8.6825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

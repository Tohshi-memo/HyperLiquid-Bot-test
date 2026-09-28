# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-28T08:37:32.191849+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7872`

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

- `news_risk_high->unknown_24h` score `786.2232` n `139` status `ready` deltaP `1.2153` edge `65.5105` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `4.7856` n `139` status `ready` deltaP `18.178` edge `0.6728` maxDD `-29.2814`
- `news_risk_high->index_24h` score `2.2007` n `139` status `ready` deltaP `22.7131` edge `0.1015` maxDD `-2.2287`
- `news_risk_high->crypto_major_24h` score `2.0842` n `139` status `ready` deltaP `13.6091` edge `0.5264` maxDD `-26.1424`
- `news_risk_high->equity_24h` score `1.8604` n `139` status `ready` deltaP `17.0813` edge `0.2968` maxDD `-11.1179`
- `news_risk_high->equity_4h` score `1.3329` n `139` status `ready` deltaP `21.0761` edge `0.1315` maxDD `-9.2079`
- `news_risk_high->metal_24h` score `1.221` n `139` status `ready` deltaP `20.3013` edge `0.1519` maxDD `-6.8392`
- `news_risk_high->crypto_alt_1h` score `0.5667` n `139` status `ready` deltaP `6.5685` edge `0.0945` maxDD `-4.2849`
- `news_risk_high->crypto_alt_4h` score `0.415` n `139` status `ready` deltaP `6.5165` edge `0.2571` maxDD `-15.9436`
- `news_risk_high->equity_1h` score `0.2658` n `139` status `ready` deltaP `5.9073` edge `0.0489` maxDD `-1.957`
- `news_risk_high->index_1h` score `0.2395` n `139` status `ready` deltaP `6.3564` edge `0.0066` maxDD `-0.3214`
- `news_risk_high->metal_1h` score `-0.5472` n `139` status `ready` deltaP `1.1911` edge `0.0094` maxDD `-0.7016`
- `news_risk_high->index_4h` score `-0.5874` n `139` status `ready` deltaP `2.847` edge `0.0174` maxDD `-1.493`
- `news_risk_high->crypto_major_1h` score `-0.7259` n `139` status `ready` deltaP `-0.9004` edge `0.0412` maxDD `-7.2607`
- `news_risk_high->fx_1h` score `-1.157` n `139` status `ready` deltaP `-8.6687` edge `-0.0025` maxDD `-1.0436`
- `news_risk_high->fx_4h` score `-1.2444` n `139` status `ready` deltaP `9.6771` edge `-0.0027` maxDD `-3.0414`
- `news_risk_high->metal_4h` score `-1.5763` n `139` status `ready` deltaP `-11.1379` edge `0.0216` maxDD `-3.6214`
- `news_risk_high->commodity_1h` score `-1.9664` n `139` status `ready` deltaP `-10.8183` edge `-0.0125` maxDD `-3.3986`
- `news_risk_high->crypto_major_4h` score `-2.2737` n `139` status `ready` deltaP `-7.6823` edge `0.0312` maxDD `-13.719`
- `news_risk_high->commodity_4h` score `-3.7558` n `139` status `ready` deltaP `-10.7124` edge `0.0003` maxDD `-8.6825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

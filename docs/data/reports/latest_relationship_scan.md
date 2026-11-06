# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-06T21:37:27.561236+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4126`

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

- `news_risk_high->equity_4h` score `1.4805` n `84` status `ready` deltaP `12.9719` edge `0.1939` maxDD `-4.2454`
- `news_risk_high->index_4h` score `0.6863` n `84` status `ready` deltaP `12.7903` edge `0.0197` maxDD `-0.4888`
- `news_risk_high->index_1h` score `0.3422` n `84` status `ready` deltaP `12.6604` edge `0.0048` maxDD `-0.2931`
- `news_risk_high->equity_1h` score `0.2734` n `84` status `ready` deltaP `4.9045` edge `0.0573` maxDD `-1.396`
- `news_risk_high->fx_4h` score `-0.0205` n `84` status `ready` deltaP `6.054` edge `0.0016` maxDD `-0.2336`
- `news_risk_high->index_24h` score `-0.207` n `84` status `ready` deltaP `0.0413` edge `0.14` maxDD `-6.6786`
- `news_risk_high->fx_1h` score `-0.2866` n `84` status `ready` deltaP `0.4206` edge `0.0` maxDD `-0.1641`
- `news_risk_high->metal_1h` score `-0.3041` n `84` status `ready` deltaP `0.1426` edge `-0.0042` maxDD `-0.5256`
- `news_risk_high->fx_24h` score `-0.4554` n `84` status `ready` deltaP `-3.4187` edge `0.0291` maxDD `-0.2073`
- `news_risk_high->crypto_alt_1h` score `-0.7543` n `84` status `ready` deltaP `2.2455` edge `0.0111` maxDD `-5.8225`
- `news_risk_high->crypto_major_1h` score `-0.858` n `84` status `ready` deltaP `-3.1081` edge `0.0046` maxDD `-4.1772`
- `news_risk_high->crypto_major_4h` score `-0.8605` n `84` status `ready` deltaP `-0.8275` edge `0.0638` maxDD `-9.1553`
- `news_risk_high->metal_4h` score `-1.0979` n `84` status `ready` deltaP `-2.2213` edge `-0.0354` maxDD `-1.5773`
- `news_risk_high->equity_24h` score `-1.6928` n `84` status `ready` deltaP `25.5014` edge `0.7716` maxDD `-86.0244`
- `news_risk_high->crypto_alt_4h` score `-2.1728` n `84` status `ready` deltaP `-4.457` edge `0.0148` maxDD `-14.0916`
- `news_risk_high->commodity_1h` score `-2.7719` n `84` status `ready` deltaP `-16.2247` edge `-0.0051` maxDD `-1.7518`
- `news_risk_high->metal_24h` score `-2.9903` n `84` status `ready` deltaP `3.8603` edge `-0.2195` maxDD `-8.5019`
- `news_risk_high->commodity_4h` score `-4.0353` n `84` status `ready` deltaP `-26.009` edge `-0.0014` maxDD `-4.252`
- `news_risk_high->commodity_24h` score `-9.2793` n `84` status `ready` deltaP `-25.9821` edge `-0.025` maxDD `-28.6715`
- `news_risk_high->crypto_major_24h` score `-11.3985` n `84` status `ready` deltaP `-22.2683` edge `0.0489` maxDD `-50.6925`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

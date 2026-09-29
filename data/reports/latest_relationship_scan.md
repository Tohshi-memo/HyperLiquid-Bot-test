# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-29T07:07:30.640814+00:00`
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

- `news_risk_high->unknown_24h` score `2617.368` n `139` status `ready` deltaP `1.2153` edge `218.1059` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `16.0414` n `139` status `ready` deltaP `32.9349` edge `1.5124` maxDD `-29.2814`
- `news_risk_high->equity_24h` score `9.8184` n `139` status `ready` deltaP `32.7063` edge `0.8558` maxDD `-11.1179`
- `news_risk_high->crypto_major_24h` score `9.0609` n `139` status `ready` deltaP `27.498` edge `1.0152` maxDD `-26.1424`
- `news_risk_high->index_24h` score `4.0855` n `139` status `ready` deltaP `37.1228` edge `0.1625` maxDD `-2.2287`
- `news_risk_high->metal_24h` score `3.7721` n `139` status `ready` deltaP `30.5444` edge `0.2962` maxDD `-6.8392`
- `news_risk_high->equity_4h` score `2.5111` n `139` status `ready` deltaP `27.4785` edge `0.187` maxDD `-9.2079`
- `news_risk_high->crypto_alt_4h` score `1.1359` n `139` status `ready` deltaP `9.108` edge `0.2999` maxDD `-15.9436`
- `news_risk_high->crypto_alt_1h` score `0.9096` n `142` status `ready` deltaP `7.7191` edge `0.1154` maxDD `-4.2849`
- `news_risk_high->equity_1h` score `0.6925` n `142` status `ready` deltaP `8.7501` edge `0.0655` maxDD `-1.957`
- `news_risk_high->index_1h` score `0.485` n `142` status `ready` deltaP `8.8998` edge `0.0101` maxDD `-0.3214`
- `news_risk_high->index_4h` score `-0.0831` n `139` status `ready` deltaP `7.7251` edge `0.0269` maxDD `-1.493`
- `news_risk_high->crypto_major_1h` score `-0.4522` n `142` status `ready` deltaP `1.2419` edge `0.062` maxDD `-7.2607`
- `news_risk_high->metal_1h` score `-0.5277` n `142` status `ready` deltaP `1.1638` edge `0.0112` maxDD `-0.7016`
- `news_risk_high->fx_4h` score `-1.328` n `139` status `ready` deltaP `8.61` edge `-0.0063` maxDD `-3.0414`
- `news_risk_high->metal_4h` score `-1.4506` n `139` status `ready` deltaP `-9.1562` edge `0.0245` maxDD `-3.6214`
- `news_risk_high->crypto_major_4h` score `-1.8638` n `139` status `ready` deltaP `-5.2433` edge `0.0675` maxDD `-13.719`
- `news_risk_high->fx_1h` score `-1.8876` n `142` status `ready` deltaP `-9.8929` edge `-0.0033` maxDD `-1.0436`
- `news_risk_high->commodity_1h` score `-2.0613` n `142` status `ready` deltaP `-12.2986` edge `-0.0148` maxDD `-3.3986`
- `news_risk_high->commodity_4h` score `-4.0001` n `139` status `ready` deltaP `-12.2368` edge `-0.0099` maxDD `-8.6825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

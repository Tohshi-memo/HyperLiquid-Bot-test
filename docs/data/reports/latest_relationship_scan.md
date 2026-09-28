# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-28T08:52:27.294290+00:00`
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

- `news_risk_high->unknown_24h` score `809.5452` n `139` status `ready` deltaP `1.2153` edge `67.454` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `4.9267` n `139` status `ready` deltaP `18.3516` edge `0.6834` maxDD `-29.2814`
- `news_risk_high->index_24h` score `2.2254` n `139` status `ready` deltaP `22.8867` edge `0.1024` maxDD `-2.2287`
- `news_risk_high->crypto_major_24h` score `2.2133` n `139` status `ready` deltaP `13.7827` edge `0.536` maxDD `-26.1424`
- `news_risk_high->equity_24h` score `1.9487` n `139` status `ready` deltaP `17.2549` edge `0.303` maxDD `-11.1179`
- `news_risk_high->equity_4h` score `1.3727` n `139` status `ready` deltaP `21.2285` edge `0.1338` maxDD `-9.2079`
- `news_risk_high->metal_24h` score `1.2402` n `139` status `ready` deltaP `20.3013` edge `0.1535` maxDD `-6.8392`
- `news_risk_high->crypto_alt_1h` score `0.5643` n `139` status `ready` deltaP `6.5685` edge `0.0943` maxDD `-4.2849`
- `news_risk_high->crypto_alt_4h` score `0.486` n `139` status `ready` deltaP `6.6689` edge `0.262` maxDD `-15.9436`
- `news_risk_high->equity_1h` score `0.2874` n `139` status `ready` deltaP `6.057` edge `0.0497` maxDD `-1.957`
- `news_risk_high->index_1h` score `0.2527` n `139` status `ready` deltaP `6.5061` edge `0.0067` maxDD `-0.3214`
- `news_risk_high->metal_1h` score `-0.5472` n `139` status `ready` deltaP `1.1911` edge `0.0094` maxDD `-0.7016`
- `news_risk_high->index_4h` score `-0.5728` n `139` status `ready` deltaP `2.9995` edge `0.0176` maxDD `-1.493`
- `news_risk_high->crypto_major_1h` score `-0.7274` n `139` status `ready` deltaP `-0.9004` edge `0.041` maxDD `-7.2607`
- `news_risk_high->fx_1h` score `-1.1477` n `139` status `ready` deltaP `-8.519` edge `-0.0023` maxDD `-1.0436`
- `news_risk_high->fx_4h` score `-1.2357` n `139` status `ready` deltaP `9.8296` edge `-0.0026` maxDD `-3.0414`
- `news_risk_high->metal_4h` score `-1.5629` n `139` status `ready` deltaP `-10.9854` edge `0.0223` maxDD `-3.6214`
- `news_risk_high->commodity_1h` score `-1.9758` n `139` status `ready` deltaP `-10.968` edge `-0.0127` maxDD `-3.3986`
- `news_risk_high->crypto_major_4h` score `-2.2463` n `139` status `ready` deltaP `-7.5298` edge `0.0337` maxDD `-13.719`
- `news_risk_high->commodity_4h` score `-3.774` n `139` status `ready` deltaP `-10.8649` edge `-0.0002` maxDD `-8.6825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

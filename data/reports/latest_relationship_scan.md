# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-29T14:37:42.633798+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7466`

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

- `news_risk_high->unknown_24h` score `2584.2` n `139` status `ready` deltaP `1.2153` edge `215.3419` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `16.8759` n `139` status `ready` deltaP `32.7613` edge `1.5831` maxDD `-29.2814`
- `news_risk_high->equity_24h` score `10.43` n `139` status `ready` deltaP `35.3105` edge `0.8894` maxDD `-11.1179`
- `news_risk_high->crypto_major_24h` score `8.5198` n `139` status `ready` deltaP `25.4146` edge `0.984` maxDD `-26.1424`
- `news_risk_high->index_24h` score `4.3052` n `139` status `ready` deltaP `39.5534` edge `0.1646` maxDD `-2.2287`
- `news_risk_high->metal_24h` score `3.8628` n `139` status `ready` deltaP `31.9332` edge `0.2945` maxDD `-6.8392`
- `news_risk_high->equity_4h` score `2.718` n `142` status `ready` deltaP `27.9801` edge `0.2009` maxDD `-9.2079`
- `news_risk_high->crypto_alt_4h` score `1.0379` n `142` status `ready` deltaP `8.6332` edge `0.2949` maxDD `-15.9436`
- `news_risk_high->crypto_alt_1h` score `0.7333` n `142` status `ready` deltaP `6.8209` edge `0.1067` maxDD `-4.2849`
- `news_risk_high->equity_1h` score `0.6015` n `142` status `ready` deltaP `7.5525` edge `0.0659` maxDD `-1.957`
- `news_risk_high->index_1h` score `0.479` n `142` status `ready` deltaP `8.7501` edge `0.0106` maxDD `-0.3214`
- `news_risk_high->index_4h` score `0.0223` n `142` status `ready` deltaP `8.6826` edge `0.0293` maxDD `-1.493`
- `news_risk_high->crypto_major_1h` score `-0.3977` n `142` status `ready` deltaP `2.1401` edge `0.063` maxDD `-7.2607`
- `news_risk_high->metal_1h` score `-0.5385` n `142` status `ready` deltaP `0.8644` edge `0.0123` maxDD `-0.7016`
- `news_risk_high->fx_4h` score `-1.3103` n `142` status `ready` deltaP `8.9789` edge `-0.0065` maxDD `-3.0414`
- `news_risk_high->metal_4h` score `-1.3619` n `142` status `ready` deltaP `-8.1544` edge `0.0292` maxDD `-3.6214`
- `news_risk_high->crypto_major_4h` score `-1.7873` n `142` status `ready` deltaP `-4.9876` edge `0.0756` maxDD `-13.719`
- `news_risk_high->fx_1h` score `-1.8325` n `142` status `ready` deltaP `-9.1444` edge `-0.0037` maxDD `-1.0436`
- `news_risk_high->commodity_1h` score `-1.9219` n `142` status `ready` deltaP `-10.2028` edge `-0.0109` maxDD `-3.3986`
- `news_risk_high->commodity_4h` score `-2.3836` n `142` status `ready` deltaP `-10.0695` edge `0.0034` maxDD `-8.6825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

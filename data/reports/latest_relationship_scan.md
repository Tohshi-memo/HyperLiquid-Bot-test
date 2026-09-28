# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-28T03:22:30.435317+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7628`

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

- `news_risk_high->unknown_24h` score `591.0696` n `139` status `ready` deltaP `1.2153` edge `49.2477` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `2.2404` n `139` status `ready` deltaP `14.5321` edge `0.485` maxDD `-29.2814`
- `news_risk_high->index_24h` score `1.6775` n `139` status `ready` deltaP `19.0673` edge `0.0822` maxDD `-2.2287`
- `news_risk_high->metal_24h` score `0.927` n `139` status `ready` deltaP `20.3013` edge `0.1274` maxDD `-6.8392`
- `news_risk_high->equity_4h` score `0.4708` n `139` status `ready` deltaP `17.8749` edge `0.081` maxDD `-9.2079`
- `news_risk_high->crypto_alt_1h` score `0.1338` n `139` status `ready` deltaP `5.0715` edge `0.0684` maxDD `-4.2849`
- `news_risk_high->equity_24h` score `0.0916` n `139` status `ready` deltaP `13.4355` edge `0.1737` maxDD `-11.1179`
- `news_risk_high->index_1h` score `0.0694` n `139` status `ready` deltaP `4.4103` edge `0.0054` maxDD `-0.3214`
- `news_risk_high->equity_1h` score `-0.0015` n `139` status `ready` deltaP `4.2606` edge `0.0376` maxDD `-1.957`
- `news_risk_high->metal_1h` score `-0.6143` n `139` status `ready` deltaP `0.5923` edge `0.0078` maxDD `-0.7016`
- `news_risk_high->crypto_major_24h` score `-0.8607` n `139` status `ready` deltaP `9.9632` edge `0.3053` maxDD `-26.1424`
- `news_risk_high->index_4h` score `-0.9155` n `139` status `ready` deltaP `-0.3542` edge `0.0114` maxDD `-1.493`
- `news_risk_high->crypto_major_1h` score `-0.9987` n `139` status `ready` deltaP `-2.6968` edge `0.0182` maxDD `-7.2607`
- `news_risk_high->fx_1h` score `-1.1321` n `139` status `ready` deltaP `-8.2196` edge `-0.0023` maxDD `-1.0436`
- `news_risk_high->fx_4h` score `-1.1519` n `139` status `ready` deltaP `11.2015` edge `-0.001` maxDD `-3.0414`
- `news_risk_high->crypto_alt_4h` score `-1.2451` n `139` status `ready` deltaP `3.3153` edge `0.1401` maxDD `-15.9436`
- `news_risk_high->metal_4h` score `-1.7612` n `139` status `ready` deltaP `-13.1196` edge `0.0111` maxDD `-3.6214`
- `news_risk_high->commodity_1h` score `-1.9508` n `139` status `ready` deltaP `-10.6686` edge `-0.0115` maxDD `-3.3986`
- `news_risk_high->crypto_major_4h` score `-3.2623` n `139` status `ready` deltaP `-10.8835` edge `-0.0742` maxDD `-13.719`
- `news_risk_high->commodity_4h` score `-3.5094` n `139` status `ready` deltaP `-8.5783` edge `0.0066` maxDD `-8.6825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

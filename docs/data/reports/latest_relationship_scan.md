# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-28T13:07:29.559691+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7916`

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

- `news_risk_high->unknown_24h` score `1204.2912` n `139` status `ready` deltaP `1.2153` edge `100.3495` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `6.5931` n `139` status `ready` deltaP `20.9558` edge `0.8049` maxDD `-29.2814`
- `news_risk_high->crypto_major_24h` score `3.9386` n `139` status `ready` deltaP `16.7341` edge `0.6601` maxDD `-26.1424`
- `news_risk_high->equity_24h` score `3.4412` n `139` status `ready` deltaP `20.2063` edge `0.4077` maxDD `-11.1179`
- `news_risk_high->index_24h` score `2.6355` n `139` status `ready` deltaP `25.8381` edge `0.1169` maxDD `-2.2287`
- `news_risk_high->equity_4h` score `1.8164` n `139` status `ready` deltaP `22.9053` edge `0.1596` maxDD `-9.2079`
- `news_risk_high->metal_24h` score `1.5078` n `139` status `ready` deltaP `20.3013` edge `0.1758` maxDD `-6.8392`
- `news_risk_high->crypto_alt_4h` score `0.644` n `139` status `ready` deltaP `7.2787` edge `0.2711` maxDD `-15.9436`
- `news_risk_high->crypto_alt_1h` score `0.5031` n `139` status `ready` deltaP `6.5685` edge `0.0892` maxDD `-4.2849`
- `news_risk_high->index_1h` score `0.2982` n `139` status `ready` deltaP `7.1049` edge `0.0065` maxDD `-0.3214`
- `news_risk_high->equity_1h` score `0.2527` n `139` status `ready` deltaP `5.7576` edge `0.0488` maxDD `-1.957`
- `news_risk_high->index_4h` score `-0.4016` n `139` status `ready` deltaP `4.5239` edge `0.0217` maxDD `-1.493`
- `news_risk_high->metal_1h` score `-0.5172` n `139` status `ready` deltaP `1.4905` edge `0.0099` maxDD `-0.7016`
- `news_risk_high->crypto_major_1h` score `-0.7306` n `139` status `ready` deltaP `-0.4513` edge `0.0376` maxDD `-7.2607`
- `news_risk_high->fx_1h` score `-1.1477` n `139` status `ready` deltaP `-8.519` edge `-0.0023` maxDD `-1.0436`
- `news_risk_high->fx_4h` score `-1.1534` n `139` status `ready` deltaP `11.2015` edge `-0.0012` maxDD `-3.0414`
- `news_risk_high->metal_4h` score `-1.5574` n `139` status `ready` deltaP `-10.9854` edge `0.023` maxDD `-3.6214`
- `news_risk_high->commodity_1h` score `-2.0248` n `139` status `ready` deltaP `-11.7165` edge `-0.014` maxDD `-3.3986`
- `news_risk_high->crypto_major_4h` score `-2.1248` n `139` status `ready` deltaP `-6.7677` edge `0.0442` maxDD `-13.719`
- `news_risk_high->commodity_4h` score `-4.0767` n `139` status `ready` deltaP `-12.999` edge `-0.0112` maxDD `-8.6825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

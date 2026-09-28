# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-28T12:07:29.279247+00:00`
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

- `news_risk_high->unknown_24h` score `1112.268` n `139` status `ready` deltaP `1.2153` edge `92.6809` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `6.2879` n `139` status `ready` deltaP `20.2613` edge `0.7841` maxDD `-29.2814`
- `news_risk_high->crypto_major_24h` score `3.5914` n `139` status `ready` deltaP `16.0396` edge `0.6358` maxDD `-26.1424`
- `news_risk_high->equity_24h` score `3.1169` n `139` status `ready` deltaP `19.5118` edge `0.3853` maxDD `-11.1179`
- `news_risk_high->index_24h` score `2.5452` n `139` status `ready` deltaP `25.1436` edge `0.114` maxDD `-2.2287`
- `news_risk_high->equity_4h` score `1.784` n `139` status `ready` deltaP `22.9053` edge `0.1569` maxDD `-9.2079`
- `news_risk_high->metal_24h` score `1.4442` n `139` status `ready` deltaP `20.3013` edge `0.1705` maxDD `-6.8392`
- `news_risk_high->crypto_alt_4h` score `0.8065` n `139` status `ready` deltaP `7.736` edge `0.2816` maxDD `-15.9436`
- `news_risk_high->crypto_alt_1h` score `0.6363` n `139` status `ready` deltaP `7.0176` edge `0.0973` maxDD `-4.2849`
- `news_risk_high->index_1h` score `0.3006` n `139` status `ready` deltaP `7.1049` edge `0.0067` maxDD `-0.3214`
- `news_risk_high->equity_1h` score `0.2587` n `139` status `ready` deltaP `5.7576` edge `0.0493` maxDD `-1.957`
- `news_risk_high->index_4h` score `-0.4124` n `139` status `ready` deltaP `4.5239` edge `0.0208` maxDD `-1.493`
- `news_risk_high->metal_1h` score `-0.528` n `139` status `ready` deltaP `1.3408` edge `0.01` maxDD `-0.7016`
- `news_risk_high->crypto_major_1h` score `-0.694` n `139` status `ready` deltaP `-0.3016` edge `0.0413` maxDD `-7.2607`
- `news_risk_high->fx_1h` score `-1.1235` n `139` status `ready` deltaP `-8.0699` edge `-0.0022` maxDD `-1.0436`
- `news_risk_high->fx_4h` score `-1.136` n `139` status `ready` deltaP `11.5064` edge `-0.001` maxDD `-3.0414`
- `news_risk_high->metal_4h` score `-1.5132` n `139` status `ready` deltaP `-10.3757` edge `0.0246` maxDD `-3.6214`
- `news_risk_high->commodity_1h` score `-2.0381` n `139` status `ready` deltaP `-11.8662` edge `-0.0147` maxDD `-3.3986`
- `news_risk_high->crypto_major_4h` score `-2.0904` n `139` status `ready` deltaP `-6.7677` edge `0.0486` maxDD `-13.719`
- `news_risk_high->commodity_4h` score `-4.0477` n `139` status `ready` deltaP `-12.8466` edge `-0.0098` maxDD `-8.6825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

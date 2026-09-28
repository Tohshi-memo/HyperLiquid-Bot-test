# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-28T11:07:28.173729+00:00`
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

- `news_risk_high->unknown_24h` score `1019.5668` n `139` status `ready` deltaP `1.2153` edge `84.9558` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `5.9486` n `139` status `ready` deltaP `19.7405` edge `0.7593` maxDD `-29.2814`
- `news_risk_high->crypto_major_24h` score `3.2227` n `139` status `ready` deltaP `15.3452` edge `0.6097` maxDD `-26.1424`
- `news_risk_high->equity_24h` score `2.7769` n `139` status `ready` deltaP `18.8174` edge `0.3616` maxDD `-11.1179`
- `news_risk_high->index_24h` score `2.4512` n `139` status `ready` deltaP `24.4492` edge `0.1108` maxDD `-2.2287`
- `news_risk_high->equity_4h` score `1.6779` n `139` status `ready` deltaP `22.448` edge `0.1511` maxDD `-9.2079`
- `news_risk_high->metal_24h` score `1.3914` n `139` status `ready` deltaP `20.3013` edge `0.1661` maxDD `-6.8392`
- `news_risk_high->crypto_alt_4h` score `0.8607` n `139` status `ready` deltaP `7.8884` edge `0.2851` maxDD `-15.9436`
- `news_risk_high->crypto_alt_1h` score `0.6447` n `139` status `ready` deltaP `7.0176` edge `0.098` maxDD `-4.2849`
- `news_risk_high->index_1h` score `0.3162` n `139` status `ready` deltaP `7.2546` edge `0.007` maxDD `-0.3214`
- `news_risk_high->equity_1h` score `0.285` n `139` status `ready` deltaP `5.9073` edge `0.0505` maxDD `-1.957`
- `news_risk_high->index_4h` score `-0.4378` n `139` status `ready` deltaP `4.3714` edge `0.0197` maxDD `-1.493`
- `news_risk_high->metal_1h` score `-0.5699` n `139` status `ready` deltaP `0.8917` edge `0.0095` maxDD `-0.7016`
- `news_risk_high->crypto_major_1h` score `-0.6924` n `139` status `ready` deltaP `-0.4513` edge `0.0425` maxDD `-7.2607`
- `news_risk_high->fx_1h` score `-1.1399` n `139` status `ready` deltaP `-8.3693` edge `-0.0023` maxDD `-1.0436`
- `news_risk_high->fx_4h` score `-1.155` n `139` status `ready` deltaP `11.2015` edge `-0.0014` maxDD `-3.0414`
- `news_risk_high->metal_4h` score `-1.4832` n `139` status `ready` deltaP `-9.9184` edge `0.0254` maxDD `-3.6214`
- `news_risk_high->commodity_1h` score `-2.0396` n `139` status `ready` deltaP `-11.8662` edge `-0.0149` maxDD `-3.3986`
- `news_risk_high->crypto_major_4h` score `-2.092` n `139` status `ready` deltaP `-6.7677` edge `0.0484` maxDD `-13.719`
- `news_risk_high->commodity_4h` score `-3.9689` n `139` status `ready` deltaP `-12.2368` edge `-0.0073` maxDD `-8.6825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-28T00:52:25.238870+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7638`

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

- `news_risk_high->unknown_24h` score `720.6408` n `136` status `ready` deltaP `1.2153` edge `60.0453` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `1.9278` n `136` status `ready` deltaP `14.6446` edge `0.4582` maxDD `-29.2814`
- `news_risk_high->index_24h` score `1.5978` n `136` status `ready` deltaP `19.0768` edge `0.0755` maxDD `-2.2287`
- `news_risk_high->metal_24h` score `1.0667` n `136` status `ready` deltaP `21.5074` edge `0.131` maxDD `-6.8392`
- `news_risk_high->equity_4h` score `0.19` n `139` status `ready` deltaP `16.9602` edge `0.0637` maxDD `-9.2079`
- `news_risk_high->index_1h` score `-0.0276` n `139` status `ready` deltaP `3.3624` edge `0.0043` maxDD `-0.3214`
- `news_risk_high->crypto_alt_1h` score `-0.0953` n `139` status `ready` deltaP `4.1733` edge `0.0553` maxDD `-4.2849`
- `news_risk_high->equity_1h` score `-0.1298` n `139` status `ready` deltaP `3.6618` edge `0.0309` maxDD `-1.957`
- `news_risk_high->equity_24h` score `-0.332` n `136` status `ready` deltaP `13.2863` edge `0.1394` maxDD `-11.1179`
- `news_risk_high->metal_1h` score `-0.649` n `139` status `ready` deltaP `0.4426` edge `0.0059` maxDD `-0.7016`
- `news_risk_high->index_4h` score `-1.0626` n `139` status `ready` deltaP `-1.8786` edge `0.0093` maxDD `-1.493`
- `news_risk_high->fx_4h` score `-1.0736` n `139` status `ready` deltaP `12.421` edge `0.0009` maxDD `-3.0414`
- `news_risk_high->crypto_major_1h` score `-1.0774` n `139` status `ready` deltaP `-3.4453` edge `0.0131` maxDD `-7.2607`
- `news_risk_high->fx_1h` score `-1.1064` n `139` status `ready` deltaP `-7.7705` edge `-0.002` maxDD `-1.0436`
- `news_risk_high->crypto_major_24h` score `-1.5878` n `136` status `ready` deltaP `9.8141` edge `0.2457` maxDD `-26.1424`
- `news_risk_high->crypto_alt_4h` score `-1.6415` n `139` status `ready` deltaP `2.0958` edge `0.1152` maxDD `-15.9436`
- `news_risk_high->metal_4h` score `-1.8199` n `139` status `ready` deltaP `-13.272` edge `0.0046` maxDD `-3.6214`
- `news_risk_high->commodity_1h` score `-1.9275` n `139` status `ready` deltaP `-10.2195` edge `-0.0115` maxDD `-3.3986`
- `news_risk_high->crypto_major_4h` score `-3.4262` n `139` status `ready` deltaP `-11.9506` edge `-0.0881` maxDD `-13.719`
- `news_risk_high->commodity_4h` score `-3.6502` n `139` status `ready` deltaP `-9.7978` edge `0.003` maxDD `-8.6825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

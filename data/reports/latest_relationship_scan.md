# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-28T01:07:30.704588+00:00`
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

- `news_risk_high->unknown_24h` score `720.6852` n `136` status `ready` deltaP `1.2153` edge `60.049` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `1.9698` n `136` status `ready` deltaP `14.6446` edge `0.4617` maxDD `-29.2814`
- `news_risk_high->index_24h` score `1.6237` n `136` status `ready` deltaP `19.2505` edge `0.0765` maxDD `-2.2287`
- `news_risk_high->metal_24h` score `1.0763` n `136` status `ready` deltaP `21.5074` edge `0.1318` maxDD `-6.8392`
- `news_risk_high->equity_4h` score `0.1984` n `139` status `ready` deltaP `16.9602` edge `0.0644` maxDD `-9.2079`
- `news_risk_high->index_1h` score `-0.0264` n `139` status `ready` deltaP `3.3624` edge `0.0044` maxDD `-0.3214`
- `news_risk_high->equity_1h` score `-0.125` n `139` status `ready` deltaP `3.6618` edge `0.0313` maxDD `-1.957`
- `news_risk_high->crypto_alt_1h` score `-0.13` n `139` status `ready` deltaP `4.0236` edge `0.0534` maxDD `-4.2849`
- `news_risk_high->equity_24h` score `-0.2617` n `136` status `ready` deltaP `13.46` edge `0.1441` maxDD `-11.1179`
- `news_risk_high->metal_1h` score `-0.6454` n `139` status `ready` deltaP `0.4426` edge `0.0062` maxDD `-0.7016`
- `news_risk_high->index_4h` score `-1.0492` n `139` status `ready` deltaP `-1.7261` edge `0.0094` maxDD `-1.493`
- `news_risk_high->fx_4h` score `-1.0831` n `139` status `ready` deltaP `12.2686` edge `0.0007` maxDD `-3.0414`
- `news_risk_high->crypto_major_1h` score `-1.0883` n `139` status `ready` deltaP `-3.4453` edge `0.0117` maxDD `-7.2607`
- `news_risk_high->fx_1h` score `-1.115` n `139` status `ready` deltaP `-7.9202` edge `-0.0021` maxDD `-1.0436`
- `news_risk_high->crypto_major_24h` score `-1.4923` n `136` status `ready` deltaP `9.9877` edge `0.2525` maxDD `-26.1424`
- `news_risk_high->crypto_alt_4h` score `-1.6427` n `139` status `ready` deltaP `2.0958` edge `0.1151` maxDD `-15.9436`
- `news_risk_high->metal_4h` score `-1.816` n `139` status `ready` deltaP `-13.272` edge `0.0051` maxDD `-3.6214`
- `news_risk_high->commodity_1h` score `-1.9267` n `139` status `ready` deltaP `-10.2195` edge `-0.0114` maxDD `-3.3986`
- `news_risk_high->crypto_major_4h` score `-3.4301` n `139` status `ready` deltaP `-11.9506` edge `-0.0886` maxDD `-13.719`
- `news_risk_high->commodity_4h` score `-3.6284` n `139` status `ready` deltaP `-9.6454` edge `0.0038` maxDD `-8.6825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

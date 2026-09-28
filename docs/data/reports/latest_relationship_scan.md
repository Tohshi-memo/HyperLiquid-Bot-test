# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-28T04:37:31.884429+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7786`

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

- `news_risk_high->unknown_24h` score `590.6304` n `139` status `ready` deltaP `1.2153` edge `49.2111` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `2.7478` n `139` status `ready` deltaP `15.4002` edge `0.5215` maxDD `-29.2814`
- `news_risk_high->index_24h` score `1.8093` n `139` status `ready` deltaP `19.9353` edge `0.0874` maxDD `-2.2287`
- `news_risk_high->metal_24h` score `0.9918` n `139` status `ready` deltaP `20.3013` edge `0.1328` maxDD `-6.8392`
- `news_risk_high->equity_4h` score `0.6962` n `139` status `ready` deltaP `18.637` edge `0.0947` maxDD `-9.2079`
- `news_risk_high->equity_24h` score `0.5402` n `139` status `ready` deltaP `14.3035` edge `0.2053` maxDD `-11.1179`
- `news_risk_high->crypto_alt_1h` score `0.2117` n `139` status `ready` deltaP `5.3709` edge `0.0729` maxDD `-4.2849`
- `news_risk_high->index_1h` score `0.0682` n `139` status `ready` deltaP `4.4103` edge `0.0053` maxDD `-0.3214`
- `news_risk_high->equity_1h` score `-0.0267` n `139` status `ready` deltaP `3.9612` edge `0.0375` maxDD `-1.957`
- `news_risk_high->crypto_major_24h` score `-0.1733` n `139` status `ready` deltaP `10.8313` edge `0.3568` maxDD `-26.1424`
- `news_risk_high->metal_1h` score `-0.6286` n `139` status `ready` deltaP `0.4426` edge `0.0076` maxDD `-0.7016`
- `news_risk_high->index_4h` score `-0.8341` n `139` status `ready` deltaP `0.408` edge `0.0131` maxDD `-1.493`
- `news_risk_high->crypto_alt_4h` score `-0.9225` n `139` status `ready` deltaP `4.0775` edge `0.1619` maxDD `-15.9436`
- `news_risk_high->crypto_major_1h` score `-0.9675` n `139` status `ready` deltaP `-2.3974` edge `0.0202` maxDD `-7.2607`
- `news_risk_high->fx_1h` score `-1.0994` n `139` status `ready` deltaP `-7.6208` edge `-0.0021` maxDD `-1.0436`
- `news_risk_high->fx_4h` score `-1.1811` n `139` status `ready` deltaP `10.7442` edge `-0.0017` maxDD `-3.0414`
- `news_risk_high->metal_4h` score `-1.7355` n `139` status `ready` deltaP `-13.1196` edge `0.0144` maxDD `-3.6214`
- `news_risk_high->commodity_1h` score `-1.9524` n `139` status `ready` deltaP `-10.6686` edge `-0.0117` maxDD `-3.3986`
- `news_risk_high->crypto_major_4h` score `-3.0846` n `139` status `ready` deltaP `-10.1213` edge `-0.0565` maxDD `-13.719`
- `news_risk_high->commodity_4h` score `-3.5264` n `139` status `ready` deltaP `-8.7307` edge `0.0062` maxDD `-8.6825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

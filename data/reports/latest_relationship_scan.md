# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-28T01:22:31.909523+00:00`
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

- `news_risk_high->unknown_24h` score `720.7092` n `136` status `ready` deltaP `1.2153` edge `60.051` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `2.007` n `136` status `ready` deltaP `14.6446` edge `0.4648` maxDD `-29.2814`
- `news_risk_high->index_24h` score `1.6496` n `136` status `ready` deltaP `19.4241` edge `0.0775` maxDD `-2.2287`
- `news_risk_high->metal_24h` score `1.0871` n `136` status `ready` deltaP `21.5074` edge `0.1327` maxDD `-6.8392`
- `news_risk_high->equity_4h` score `0.2116` n `139` status `ready` deltaP `16.9602` edge `0.0655` maxDD `-9.2079`
- `news_risk_high->index_1h` score `-0.024` n `139` status `ready` deltaP `3.3624` edge `0.0046` maxDD `-0.3214`
- `news_risk_high->equity_1h` score `-0.1142` n `139` status `ready` deltaP `3.6618` edge `0.0322` maxDD `-1.957`
- `news_risk_high->crypto_alt_1h` score `-0.1372` n `139` status `ready` deltaP `4.0236` edge `0.0528` maxDD `-4.2849`
- `news_risk_high->equity_24h` score `-0.189` n `136` status `ready` deltaP `13.6336` edge `0.149` maxDD `-11.1179`
- `news_risk_high->metal_1h` score `-0.6406` n `139` status `ready` deltaP `0.4426` edge `0.0066` maxDD `-0.7016`
- `news_risk_high->index_4h` score `-1.0346` n `139` status `ready` deltaP `-1.5737` edge `0.0096` maxDD `-1.493`
- `news_risk_high->fx_4h` score `-1.0847` n `139` status `ready` deltaP `12.2686` edge `0.0005` maxDD `-3.0414`
- `news_risk_high->crypto_major_1h` score `-1.0899` n `139` status `ready` deltaP `-3.4453` edge `0.0115` maxDD `-7.2607`
- `news_risk_high->fx_1h` score `-1.115` n `139` status `ready` deltaP `-7.9202` edge `-0.0021` maxDD `-1.0436`
- `news_risk_high->crypto_major_24h` score `-1.4065` n `136` status `ready` deltaP `10.1613` edge `0.2585` maxDD `-26.1424`
- `news_risk_high->crypto_alt_4h` score `-1.6391` n `139` status `ready` deltaP `2.0958` edge `0.1154` maxDD `-15.9436`
- `news_risk_high->metal_4h` score `-1.8113` n `139` status `ready` deltaP `-13.272` edge `0.0057` maxDD `-3.6214`
- `news_risk_high->commodity_1h` score `-1.9259` n `139` status `ready` deltaP `-10.2195` edge `-0.0113` maxDD `-3.3986`
- `news_risk_high->crypto_major_4h` score `-3.434` n `139` status `ready` deltaP `-11.9506` edge `-0.0891` maxDD `-13.719`
- `news_risk_high->commodity_4h` score `-3.6078` n `139` status `ready` deltaP `-9.4929` edge `0.0045` maxDD `-8.6825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

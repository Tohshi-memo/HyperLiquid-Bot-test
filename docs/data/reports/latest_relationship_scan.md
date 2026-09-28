# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-28T00:07:31.202525+00:00`
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

- `news_risk_high->unknown_24h` score `720.4896` n `136` status `ready` deltaP `1.2153` edge `60.0327` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `1.7814` n `136` status `ready` deltaP `14.6446` edge `0.446` maxDD `-29.2814`
- `news_risk_high->index_24h` score `1.5492` n `136` status `ready` deltaP `18.9032` edge `0.0726` maxDD `-2.2287`
- `news_risk_high->metal_24h` score `0.9962` n `136` status `ready` deltaP `20.9866` edge `0.1286` maxDD `-6.8392`
- `news_risk_high->equity_4h` score `0.1514` n `139` status `ready` deltaP `16.8078` edge `0.0615` maxDD `-9.2079`
- `news_risk_high->index_1h` score `-0.0264` n `139` status `ready` deltaP `3.3624` edge `0.0044` maxDD `-0.3214`
- `news_risk_high->crypto_alt_1h` score `-0.0317` n `139` status `ready` deltaP `4.4727` edge `0.0586` maxDD `-4.2849`
- `news_risk_high->equity_1h` score `-0.1538` n `139` status `ready` deltaP `3.5121` edge `0.0299` maxDD `-1.957`
- `news_risk_high->equity_24h` score `-0.535` n `136` status `ready` deltaP `12.9391` edge `0.1248` maxDD `-11.1179`
- `news_risk_high->metal_1h` score `-0.6982` n `139` status `ready` deltaP `-0.0065` edge `0.0048` maxDD `-0.7016`
- `news_risk_high->fx_4h` score `-1.0475` n `139` status `ready` deltaP `12.8783` edge `0.0012` maxDD `-3.0414`
- `news_risk_high->crypto_major_1h` score `-1.0626` n `139` status `ready` deltaP `-3.4453` edge `0.015` maxDD `-7.2607`
- `news_risk_high->index_4h` score `-1.0918` n `139` status `ready` deltaP `-2.1835` edge `0.0089` maxDD `-1.493`
- `news_risk_high->fx_1h` score `-1.0955` n `139` status `ready` deltaP `-7.6208` edge `-0.0016` maxDD `-1.0436`
- `news_risk_high->crypto_alt_4h` score `-1.6367` n `139` status `ready` deltaP `2.0958` edge `0.1156` maxDD `-15.9436`
- `news_risk_high->metal_4h` score `-1.8482` n `139` status `ready` deltaP `-13.5769` edge `0.003` maxDD `-3.6214`
- `news_risk_high->crypto_major_24h` score `-1.8801` n `136` status `ready` deltaP `9.6405` edge `0.2225` maxDD `-26.1424`
- `news_risk_high->commodity_1h` score `-1.922` n `139` status `ready` deltaP `-10.2195` edge `-0.0108` maxDD `-3.3986`
- `news_risk_high->crypto_major_4h` score `-3.3988` n `139` status `ready` deltaP `-11.7981` edge `-0.0856` maxDD `-13.719`
- `news_risk_high->commodity_4h` score `-3.6622` n `139` status `ready` deltaP `-9.7978` edge `0.002` maxDD `-8.6825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

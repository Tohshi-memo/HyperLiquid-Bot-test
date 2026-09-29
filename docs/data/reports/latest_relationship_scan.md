# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-29T16:52:28.781089+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7160`

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

- `news_risk_high->unknown_24h` score `2588.2584` n `139` status `ready` deltaP `1.2153` edge `215.6801` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `16.1936` n `139` status `ready` deltaP `31.3724` edge `1.5355` maxDD `-29.2814`
- `news_risk_high->equity_24h` score `9.9256` n `139` status `ready` deltaP `33.748` edge `0.8568` maxDD `-11.039`
- `news_risk_high->crypto_major_24h` score `7.9741` n `139` status `ready` deltaP `24.8938` edge `0.942` maxDD `-26.1424`
- `news_risk_high->index_24h` score `4.1654` n `139` status `ready` deltaP `38.5117` edge `0.1599` maxDD `-2.2287`
- `news_risk_high->metal_24h` score `3.751` n `139` status `ready` deltaP `31.586` edge `0.2875` maxDD `-6.8392`
- `news_risk_high->equity_4h` score `2.8355` n `142` status `ready` deltaP `28.7423` edge `0.2048` maxDD `-9.143`
- `news_risk_high->crypto_alt_4h` score `1.4233` n `142` status `ready` deltaP `9.7003` edge `0.3199` maxDD `-15.9436`
- `news_risk_high->crypto_alt_1h` score `0.9744` n `142` status `ready` deltaP `7.7191` edge `0.1208` maxDD `-4.2849`
- `news_risk_high->equity_1h` score `0.6886` n `142` status `ready` deltaP `8.1513` edge `0.069` maxDD `-1.9431`
- `news_risk_high->index_1h` score `0.5221` n `142` status `ready` deltaP `9.1992` edge `0.0112` maxDD `-0.3214`
- `news_risk_high->index_4h` score `0.145` n `142` status `ready` deltaP `9.9021` edge `0.0314` maxDD `-1.493`
- `news_risk_high->crypto_major_1h` score `-0.2738` n `142` status `ready` deltaP `2.8886` edge `0.0739` maxDD `-7.2607`
- `news_risk_high->metal_1h` score `-0.5025` n `142` status `ready` deltaP `1.1638` edge `0.0133` maxDD `-0.7016`
- `news_risk_high->metal_4h` score `-1.2485` n `142` status `ready` deltaP `-6.9349` edge `0.0356` maxDD `-3.6214`
- `news_risk_high->fx_4h` score `-1.285` n `142` status `ready` deltaP `9.4362` edge `-0.0063` maxDD `-3.0414`
- `news_risk_high->crypto_major_4h` score `-1.5538` n `142` status `ready` deltaP `-3.7681` edge `0.0974` maxDD `-13.719`
- `news_risk_high->fx_1h` score `-1.8061` n `142` status `ready` deltaP `-8.845` edge `-0.0035` maxDD `-1.0436`
- `news_risk_high->commodity_1h` score `-1.8955` n `142` status `ready` deltaP `-9.7537` edge `-0.0105` maxDD `-3.3986`
- `news_risk_high->commodity_4h` score `-2.3521` n `142` status `ready` deltaP `-9.6122` edge `0.0044` maxDD `-8.6825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

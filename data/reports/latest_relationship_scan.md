# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-29T19:52:31.392337+00:00`
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

- `news_risk_high->unknown_24h` score `2591.7014` n `139` status `ready` deltaP `1.5625` edge `215.9647` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `15.3176` n `139` status `ready` deltaP `30.1571` edge `1.4706` maxDD `-29.2814`
- `news_risk_high->equity_24h` score `9.3389` n `139` status `ready` deltaP `31.6646` edge `0.8218` maxDD `-11.039`
- `news_risk_high->crypto_major_24h` score `7.3111` n `139` status `ready` deltaP `24.7202` edge `0.8879` maxDD `-26.1424`
- `news_risk_high->index_24h` score `4.0084` n `139` status `ready` deltaP `37.6436` edge `0.1526` maxDD `-2.2287`
- `news_risk_high->metal_24h` score `3.4877` n `139` status `ready` deltaP `30.5444` edge `0.2725` maxDD `-6.8392`
- `news_risk_high->equity_4h` score `3.0705` n `142` status `ready` deltaP `30.4191` edge `0.2132` maxDD `-9.143`
- `news_risk_high->crypto_alt_4h` score `2.094` n `142` status `ready` deltaP `11.5296` edge `0.3636` maxDD `-15.9436`
- `news_risk_high->crypto_alt_1h` score `1.0319` n `142` status `ready` deltaP `8.1682` edge `0.1226` maxDD `-4.2849`
- `news_risk_high->equity_1h` score `0.7054` n `142` status `ready` deltaP `8.1513` edge `0.0704` maxDD `-1.9431`
- `news_risk_high->index_1h` score `0.5078` n `142` status `ready` deltaP `9.0495` edge `0.011` maxDD `-0.3214`
- `news_risk_high->index_4h` score `0.2254` n `142` status `ready` deltaP `10.8167` edge `0.032` maxDD `-1.493`
- `news_risk_high->crypto_major_1h` score `-0.2722` n `142` status `ready` deltaP `3.0383` edge `0.0731` maxDD `-7.2607`
- `news_risk_high->metal_1h` score `-0.5013` n `142` status `ready` deltaP `1.1638` edge `0.0134` maxDD `-0.7016`
- `news_risk_high->metal_4h` score `-1.228` n `142` status `ready` deltaP `-6.63` edge `0.0362` maxDD `-3.6214`
- `news_risk_high->fx_4h` score `-1.2834` n `142` status `ready` deltaP `9.4362` edge `-0.0061` maxDD `-3.0414`
- `news_risk_high->crypto_major_4h` score `-1.2929` n `142` status `ready` deltaP `-2.3961` edge `0.1217` maxDD `-13.719`
- `news_risk_high->fx_1h` score `-1.8193` n `142` status `ready` deltaP `-8.9947` edge `-0.0036` maxDD `-1.0436`
- `news_risk_high->commodity_1h` score `-1.855` n `142` status `ready` deltaP `-9.1549` edge `-0.0093` maxDD `-3.3986`
- `news_risk_high->commodity_4h` score `-2.3129` n `142` status `ready` deltaP `-9.4598` edge `0.0084` maxDD `-8.6825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

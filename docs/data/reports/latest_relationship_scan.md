# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-29T20:22:31.297889+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6958`

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

- `news_risk_high->unknown_24h` score `2592.052` n `139` status `ready` deltaP `1.9097` edge `215.9916` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `15.117` n `139` status `ready` deltaP `29.8099` edge `1.4562` maxDD `-29.2814`
- `news_risk_high->equity_24h` score `9.2151` n `139` status `ready` deltaP `31.3174` edge `0.8138` maxDD `-11.039`
- `news_risk_high->crypto_major_24h` score `7.1863` n `139` status `ready` deltaP `24.7202` edge `0.8775` maxDD `-26.1424`
- `news_risk_high->index_24h` score `3.9626` n `139` status `ready` deltaP `37.2964` edge `0.1511` maxDD `-2.2287`
- `news_risk_high->metal_24h` score `3.4155` n `139` status `ready` deltaP `30.1971` edge `0.2688` maxDD `-6.8392`
- `news_risk_high->equity_4h` score `3.1021` n `142` status `ready` deltaP `30.724` edge `0.2138` maxDD `-9.143`
- `news_risk_high->crypto_alt_4h` score `2.1856` n `142` status `ready` deltaP `11.8345` edge `0.3692` maxDD `-15.9436`
- `news_risk_high->crypto_alt_1h` score `1.0739` n `142` status `ready` deltaP `8.4676` edge `0.1241` maxDD `-4.2849`
- `news_risk_high->equity_1h` score `0.7318` n `142` status `ready` deltaP `8.4507` edge `0.0706` maxDD `-1.9431`
- `news_risk_high->index_1h` score `0.4958` n `142` status `ready` deltaP `8.8998` edge `0.011` maxDD `-0.3214`
- `news_risk_high->index_4h` score `0.1986` n `142` status `ready` deltaP `10.5118` edge `0.0318` maxDD `-1.493`
- `news_risk_high->crypto_major_1h` score `-0.2582` n `142` status `ready` deltaP `3.188` edge `0.0739` maxDD `-7.2607`
- `news_risk_high->metal_1h` score `-0.5277` n `142` status `ready` deltaP `0.8644` edge `0.0132` maxDD `-0.7016`
- `news_risk_high->metal_4h` score `-1.2334` n `142` status `ready` deltaP `-6.63` edge `0.0355` maxDD `-3.6214`
- `news_risk_high->crypto_major_4h` score `-1.2631` n `142` status `ready` deltaP `-2.0913` edge `0.1235` maxDD `-13.719`
- `news_risk_high->fx_4h` score `-1.3008` n `142` status `ready` deltaP `9.1313` edge `-0.0063` maxDD `-3.0414`
- `news_risk_high->fx_1h` score `-1.8325` n `142` status `ready` deltaP `-9.1444` edge `-0.0037` maxDD `-1.0436`
- `news_risk_high->commodity_1h` score `-1.837` n `142` status `ready` deltaP `-8.8555` edge `-0.009` maxDD `-3.3986`
- `news_risk_high->commodity_4h` score `-2.2869` n `142` status `ready` deltaP `-9.1549` edge `0.0097` maxDD `-8.6825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

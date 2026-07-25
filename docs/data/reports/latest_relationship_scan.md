# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-25T15:37:45.992752+00:00`
- Price records: `672`
- Market context records: `7892`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14713`

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

- `market_context_high->equity_24h` score `14.3902` n `106` status `ready` deltaP `30.0252` edge `1.1332` maxDD `-6.0681`
- `market_context_high->equity_4h` score `5.0506` n `108` status `ready` deltaP `16.0093` edge `0.4076` maxDD `-5.1426`
- `market_context_high->metal_24h` score `4.9288` n `106` status `ready` deltaP `24.4467` edge `0.3212` maxDD `-0.542`
- `market_context_high->commodity_24h` score `1.8006` n `106` status `ready` deltaP `21.8992` edge `0.1624` maxDD `-7.0012`
- `market_context_high->crypto_alt_4h` score `1.7072` n `108` status `ready` deltaP `14.1425` edge `0.1597` maxDD `-3.9374`
- `market_context_high->crypto_major_4h` score `1.5743` n `108` status `ready` deltaP `15.8549` edge `0.1973` maxDD `-6.7444`
- `market_context_high->equity_1h` score `1.3058` n `112` status `ready` deltaP `11.5911` edge `0.1133` maxDD `-4.2072`
- `market_context_high->fx_24h` score `1.2776` n `106` status `ready` deltaP `33.5928` edge `0.0486` maxDD `-3.0343`
- `market_context_high->crypto_major_1h` score `1.1332` n `112` status `ready` deltaP `12.9438` edge `0.049` maxDD `-1.6021`
- `market_context_high->index_4h` score `1.0447` n `108` status `ready` deltaP `16.3146` edge `0.0609` maxDD `-0.9419`
- `market_context_high->metal_4h` score `0.8444` n `108` status `ready` deltaP `10.8701` edge `0.1018` maxDD `-0.979`
- `market_context_high->index_1h` score `0.6267` n `112` status `ready` deltaP `11.4651` edge `0.0188` maxDD `-0.7743`
- `market_context_high->commodity_4h` score `0.623` n `108` status `ready` deltaP `10.0452` edge `0.0443` maxDD `-1.0817`
- `market_context_high->crypto_alt_1h` score `0.3773` n `112` status `ready` deltaP `4.9187` edge `0.0419` maxDD `-1.4603`
- `market_context_high->index_24h` score `0.1954` n `106` status `ready` deltaP `1.6284` edge `0.1234` maxDD `-1.4379`
- `market_context_high->metal_1h` score `-0.0019` n `112` status `ready` deltaP `3.8815` edge `0.0243` maxDD `-0.6936`
- `market_context_high->commodity_1h` score `-0.254` n `112` status `ready` deltaP `3.239` edge `0.0027` maxDD `-1.5486`
- `market_context_high->fx_1h` score `-0.2867` n `112` status `ready` deltaP `0.3164` edge `-0.0004` maxDD `-0.4102`
- `market_context_high->fx_4h` score `-0.5332` n `108` status `ready` deltaP `2.0017` edge `0.0017` maxDD `-1.3386`
- `market_context_high->crypto_alt_24h` score `-1.7697` n `106` status `ready` deltaP `11.151` edge `0.2283` maxDD `-28.3623`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

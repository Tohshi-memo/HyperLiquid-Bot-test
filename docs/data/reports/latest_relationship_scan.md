# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-10T23:52:24.324185+00:00`
- Price records: `672`
- Market context records: `6335`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11134`

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

- `news_risk_high->crypto_alt_24h` score `15.3815` n `32` status `ready` deltaP `43.0556` edge `1.0095` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `6.0812` n `32` status `ready` deltaP `50.6944` edge `0.1688` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `4.4019` n `32` status `ready` deltaP `16.6667` edge `0.5312` maxDD `-4.2368`
- `news_risk_high->fx_4h` score `4.2289` n `32` status `ready` deltaP `44.1311` edge `0.0628` maxDD `-0.0345`
- `news_risk_high->commodity_24h` score `3.473` n `32` status `ready` deltaP `30.7292` edge `0.1051` maxDD `-0.3101`
- `news_risk_high->fx_1h` score `2.4123` n `32` status `ready` deltaP `29.0419` edge `0.0213` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `1.5271` n `32` status `ready` deltaP `14.8765` edge `0.1433` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.9673` n `32` status `ready` deltaP `12.0696` edge `0.0897` maxDD `-1.6923`
- `market_context_high->metal_4h` score `0.3269` n `196` status `ready` deltaP `11.1498` edge `0.0409` maxDD `-2.7056`
- `market_context_high->index_4h` score `0.0186` n `196` status `ready` deltaP `6.4118` edge `0.0215` maxDD `-0.6158`
- `market_context_high->unknown_1h` score `-0.1335` n `208` status `ready` deltaP `-8.5819` edge `0.1469` maxDD `-3.7317`
- `market_context_high->metal_1h` score `-0.3692` n `208` status `ready` deltaP `4.2492` edge `0.0021` maxDD `-1.8877`
- `market_context_high->metal_24h` score `-0.4467` n `142` status `ready` deltaP `17.0065` edge `0.0862` maxDD `-11.8809`
- `market_context_high->commodity_1h` score `-0.5522` n `208` status `ready` deltaP `-0.4174` edge `0.0003` maxDD `-2.1314`
- `market_context_high->index_1h` score `-0.5751` n `208` status `ready` deltaP `-3.1207` edge `0.0024` maxDD `-0.7596`
- `news_risk_high->index_24h` score `-0.6556` n `32` status `ready` deltaP `1.2153` edge `-0.005` maxDD `-2.3058`
- `news_risk_high->unknown_1h` score `-0.7` n `32` status `ready` deltaP `6.0816` edge `-0.0644` maxDD `-0.7581`
- `news_risk_high->metal_1h` score `-0.7628` n `32` status `ready` deltaP `-3.4431` edge `-0.0251` maxDD `-1.6464`
- `market_context_high->fx_1h` score `-0.7632` n `208` status `ready` deltaP `-1.2466` edge `-0.0019` maxDD `-0.9376`
- `market_context_high->equity_4h` score `-0.7673` n `196` status `ready` deltaP `4.2466` edge `0.0432` maxDD `-8.2573`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

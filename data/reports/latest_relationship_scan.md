# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-25T12:37:34.994189+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3780`

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

- `market_context_high->unknown_1h` score `32214.0949` n `45` status `ready` deltaP `2.0159` edge `2684.5039` maxDD `-0.4209`
- `market_context_high->unknown_4h` score `21949.6117` n `45` status `ready` deltaP `3.1776` edge `1829.127` maxDD `-0.7765`
- `news_risk_high->unknown_1h` score `979.14` n `31` status `ready` deltaP `2.231` edge `81.5977` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `696.6642` n `31` status `ready` deltaP `4.3962` edge `58.0317` maxDD `-0.1191`
- `news_risk_high->unknown_24h` score `602.1215` n `31` status `ready` deltaP `5.7292` edge `50.1386` maxDD `0.0`
- `news_risk_high->equity_24h` score `43.5294` n `31` status `ready` deltaP `49.1319` edge `3.2999` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `40.8968` n `31` status `ready` deltaP `50.6944` edge `3.0701` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `37.7031` n `31` status `ready` deltaP `53.2986` edge `2.7866` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `11.8217` n `31` status `ready` deltaP `27.3701` edge `0.8897` maxDD `-5.2957`
- `news_risk_high->metal_24h` score `11.7062` n `31` status `ready` deltaP `41.2355` edge `0.7281` maxDD `-0.1986`
- `news_risk_high->equity_4h` score `11.1823` n `31` status `ready` deltaP `37.682` edge `0.7287` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `7.49` n `31` status `ready` deltaP `18.9123` edge `0.9759` maxDD `-7.6714`
- `news_risk_high->index_24h` score `6.8877` n `31` status `ready` deltaP `49.8264` edge `0.2418` maxDD `0.0`
- `news_risk_high->fx_24h` score `5.1959` n `31` status `ready` deltaP `43.9684` edge `0.1527` maxDD `-0.0262`
- `news_risk_high->equity_1h` score `4.0098` n `31` status `ready` deltaP `20.7359` edge `0.2146` maxDD `-0.1621`
- `news_risk_high->index_4h` score `3.382` n `31` status `ready` deltaP `36.1576` edge `0.0668` maxDD `-0.4146`
- `news_risk_high->crypto_major_1h` score `2.7588` n `31` status `ready` deltaP `11.9567` edge `0.3201` maxDD `-1.6897`
- `news_risk_high->index_1h` score `2.7202` n `31` status `ready` deltaP `31.9925` edge `0.0219` maxDD `-0.0136`
- `market_context_high->fx_4h` score `2.5626` n `45` status `ready` deltaP `31.3076` edge `0.0333` maxDD `-0.2774`
- `news_risk_high->crypto_alt_1h` score `2.4702` n `31` status `ready` deltaP `13.304` edge `0.2637` maxDD `-1.5232`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

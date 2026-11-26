# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-26T02:52:28.879334+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3899`

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

- `market_context_high->unknown_1h` score `34681.4225` n `42` status `ready` deltaP `0.9409` edge `2890.1217` maxDD `-0.4209`
- `news_risk_high->unknown_4h` score `3200.1941` n `31` status `ready` deltaP `3.3291` edge `266.6663` maxDD `-0.1191`
- `news_risk_high->unknown_1h` score `889.7341` n `31` status `ready` deltaP `1.6322` edge `74.1512` maxDD `-0.7395`
- `news_risk_high->equity_24h` score `43.7337` n `31` status `ready` deltaP `49.8264` edge `3.3123` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `40.8644` n `31` status `ready` deltaP `50.6944` edge `3.0674` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `35.6836` n `31` status `ready` deltaP `50.0` edge `2.6403` maxDD `0.0`
- `news_risk_high->unknown_24h` score `35.0293` n `31` status `ready` deltaP `6.0764` edge `2.8786` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `10.8271` n `31` status `ready` deltaP `26.6079` edge `0.8119` maxDD `-5.2957`
- `news_risk_high->metal_24h` score `10.8194` n `31` status `ready` deltaP `36.3744` edge `0.6866` maxDD `-0.1986`
- `news_risk_high->equity_4h` score `10.1713` n `31` status `ready` deltaP `37.2247` edge `0.6475` maxDD `-2.178`
- `news_risk_high->index_24h` score `7.1416` n `31` status `ready` deltaP `51.2153` edge `0.2537` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `6.7562` n `31` status `ready` deltaP `17.2354` edge `0.893` maxDD `-7.6714`
- `news_risk_high->fx_24h` score `5.3317` n `31` status `ready` deltaP `45.5309` edge `0.1536` maxDD `-0.0262`
- `news_risk_high->equity_1h` score `3.5527` n `31` status `ready` deltaP `19.688` edge `0.1835` maxDD `-0.1621`
- `news_risk_high->index_4h` score `3.3172` n `31` status `ready` deltaP `36.1576` edge `0.0614` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.6387` n `31` status `ready` deltaP `31.3937` edge `0.0191` maxDD `-0.0136`
- `market_context_high->fx_4h` score `2.5149` n `42` status `ready` deltaP `30.7418` edge `0.0331` maxDD `-0.2774`
- `news_risk_high->crypto_major_1h` score `2.3753` n `31` status `ready` deltaP `9.5615` edge `0.2869` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `2.1785` n `31` status `ready` deltaP `12.2561` edge `0.2333` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.4565` n `31` status `ready` deltaP `28.8342` edge `0.0224` maxDD `-0.2315`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

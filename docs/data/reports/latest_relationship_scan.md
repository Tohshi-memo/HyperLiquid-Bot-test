# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-29T06:37:18.752992+00:00`
- Price records: `672`
- Market context records: `2220`
- Flow alert records: `8282`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9178`

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

- `news_risk_high->crypto_alt_24h` score `26.2343` n `30` status `ready` deltaP `57.743` edge `1.8601` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `14.2335` n `30` status `ready` deltaP `48.4028` edge `0.9074` maxDD `-3.1836`
- `market_context_high->crypto_alt_4h` score `13.0103` n `132` status `ready` deltaP `37.7587` edge `0.9261` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `11.7897` n `132` status `ready` deltaP `42.2811` edge `0.7536` maxDD `-1.9063`
- `news_risk_high->equity_24h` score `10.8557` n `30` status `ready` deltaP `39.375` edge `0.6736` maxDD `-2.1831`
- `news_risk_high->unknown_24h` score `10.1825` n `30` status `ready` deltaP `38.6458` edge `0.6135` maxDD `-1.4744`
- `news_risk_high->crypto_major_24h` score `6.8436` n `30` status `ready` deltaP `17.257` edge `0.8204` maxDD `-3.3119`
- `market_context_high->unknown_4h` score `5.4961` n `132` status `ready` deltaP `21.5263` edge `0.3824` maxDD `-2.4317`
- `news_risk_high->commodity_4h` score `3.908` n `43` status `ready` deltaP `32.7673` edge `0.3497` maxDD `-3.0367`
- `market_context_high->equity_4h` score `3.393` n `132` status `ready` deltaP `23.4156` edge `0.2361` maxDD `-5.0894`
- `market_context_high->index_4h` score `3.2246` n `132` status `ready` deltaP `26.6214` edge `0.1596` maxDD `-1.8022`
- `market_context_high->crypto_major_1h` score `3.2155` n `133` status `ready` deltaP `17.5161` edge `0.1989` maxDD `-1.817`
- `market_context_high->crypto_alt_1h` score `3.0191` n `133` status `ready` deltaP `16.4648` edge `0.2282` maxDD `-4.9097`
- `news_risk_high->fx_24h` score `2.6126` n `30` status `ready` deltaP `28.3333` edge `0.0473` maxDD `-0.1442`
- `news_risk_high->fx_4h` score `2.2194` n `43` status `ready` deltaP `28.0416` edge `0.0164` maxDD `-0.1382`
- `market_context_high->unknown_24h` score `2.1424` n `132` status `ready` deltaP `24.858` edge `0.4943` maxDD `-32.8525`
- `market_context_high->index_24h` score `1.9004` n `132` status `ready` deltaP `9.6906` edge `0.2166` maxDD `-4.1604`
- `news_risk_high->commodity_24h` score `1.7759` n `30` status `ready` deltaP `-6.5278` edge `0.2732` maxDD `-3.202`
- `news_risk_high->unknown_1h` score `1.4803` n `43` status `ready` deltaP `21.4942` edge `0.027` maxDD `-1.7548`
- `news_risk_high->unknown_4h` score `1.3325` n `43` status `ready` deltaP `14.62` edge `0.0859` maxDD `-2.7857`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-10T02:52:28.257050+00:00`
- Price records: `672`
- Market context records: `6242`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11100`

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

- `news_risk_high->crypto_alt_24h` score `14.0978` n `32` status `ready` deltaP `42.2194` edge `0.9081` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `6.1637` n `32` status `ready` deltaP `52.551` edge `0.1633` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.2169` n `32` status `ready` deltaP `44.1311` edge `0.0618` maxDD `-0.0345`
- `news_risk_high->crypto_major_24h` score `3.1809` n `32` status `ready` deltaP `15.625` edge `0.3816` maxDD `-4.2368`
- `news_risk_high->fx_1h` score `2.3524` n `32` status `ready` deltaP `28.2934` edge `0.0213` maxDD `-0.1113`
- `market_context_high->unknown_1h` score `2.2435` n `192` status `ready` deltaP `2.2611` edge `0.2727` maxDD `-3.7317`
- `news_risk_high->commodity_24h` score `2.0624` n `32` status `ready` deltaP `24.5111` edge `0.029` maxDD `-0.3101`
- `market_context_high->unknown_4h` score `1.8784` n `192` status `ready` deltaP `0.4446` edge `0.4068` maxDD `-11.925`
- `news_risk_high->crypto_major_1h` score `1.3329` n `32` status `ready` deltaP `14.128` edge `0.1234` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.7491` n `32` status `ready` deltaP `10.4229` edge `0.0727` maxDD `-1.6923`
- `market_context_high->metal_24h` score `-0.079` n `192` status `ready` deltaP `19.8023` edge `0.1147` maxDD `-11.8809`
- `news_risk_high->index_24h` score `-0.1754` n `32` status `ready` deltaP `8.801` edge `0.006` maxDD `-2.3058`
- `market_context_high->fx_1h` score `-0.2879` n `192` status `ready` deltaP `1.2101` edge `-0.0004` maxDD `-0.5659`
- `market_context_high->metal_4h` score `-0.507` n `192` status `ready` deltaP `4.281` edge `0.0252` maxDD `-3.4996`
- `market_context_high->equity_4h` score `-0.658` n `192` status `ready` deltaP `2.6677` edge `0.0191` maxDD `-2.671`
- `market_context_high->commodity_1h` score `-0.6841` n `192` status `ready` deltaP `-2.0958` edge `0.0016` maxDD `-0.5708`
- `news_risk_high->metal_1h` score `-0.7886` n `32` status `ready` deltaP `-3.5928` edge `-0.0274` maxDD `-1.6464`
- `market_context_high->metal_1h` score `-0.8724` n `192` status `ready` deltaP `1.6155` edge `-0.0036` maxDD `-2.0564`
- `market_context_high->crypto_alt_1h` score `-0.9146` n `192` status `ready` deltaP `4.6937` edge `0.0267` maxDD `-9.3536`
- `market_context_high->crypto_major_1h` score `-0.9667` n `192` status `ready` deltaP `4.2322` edge `0.0246` maxDD `-9.807`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

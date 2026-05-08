# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-08T03:37:09.805941+00:00`
- Price records: `610`
- Market context records: `714`
- Flow alert records: `2018`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `901`

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

- `market_context_high->crypto_major_24h` score `11.276` n `146` status `ready` deltaP `27.3839` edge `0.7905` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `6.426` n `146` status `ready` deltaP `8.07` edge `0.4865` maxDD `-0.0508`
- `market_context_high->fx_4h` score `-0.2709` n `149` status `ready` deltaP `6.3622` edge `0.01` maxDD `-1.6381`
- `market_context_high->fx_1h` score `-0.2837` n `149` status `ready` deltaP `2.9008` edge `0.0021` maxDD `-0.291`
- `market_context_high->commodity_1h` score `-0.4344` n `149` status `ready` deltaP `2.6478` edge `0.0436` maxDD `-3.7959`
- `market_context_high->index_1h` score `-0.6212` n `149` status `ready` deltaP `0.4359` edge `0.0028` maxDD `-2.8282`
- `market_context_high->index_24h` score `-0.7568` n `146` status `ready` deltaP `-1.8077` edge `0.1485` maxDD `-5.9609`
- `market_context_high->crypto_major_4h` score `-1.0632` n `149` status `ready` deltaP `16.9344` edge `0.1214` maxDD `-22.648`
- `market_context_high->equity_1h` score `-1.1635` n `149` status `ready` deltaP `-1.5642` edge `-0.0055` maxDD `-4.4826`
- `market_context_high->unknown_1h` score `-1.1703` n `149` status `ready` deltaP `-3.9881` edge `-0.0106` maxDD `-2.1602`
- `market_context_high->crypto_alt_1h` score `-1.3551` n `149` status `ready` deltaP `4.6714` edge `-0.0126` maxDD `-8.1842`
- `market_context_high->crypto_major_1h` score `-1.5717` n `149` status `ready` deltaP `6.4091` edge `-0.0014` maxDD `-11.4508`
- `market_context_high->equity_24h` score `-1.7519` n `146` status `ready` deltaP `-3.6771` edge `0.139` maxDD `-10.5047`
- `market_context_high->index_4h` score `-1.7877` n `149` status `ready` deltaP `1.7245` edge `-0.0082` maxDD `-6.5149`
- `market_context_high->crypto_alt_4h` score `-1.9613` n `149` status `ready` deltaP `3.8008` edge `0.0682` maxDD `-15.2248`
- `market_context_high->equity_4h` score `-2.7258` n `149` status `ready` deltaP `-1.3263` edge `-0.0031` maxDD `-10.5498`
- `market_context_high->metal_1h` score `-3.3666` n `149` status `ready` deltaP `-4.9228` edge `-0.0518` maxDD `-9.0076`
- `market_context_high->commodity_4h` score `-3.7103` n `149` status `ready` deltaP `-5.9549` edge `0.0806` maxDD `-13.0076`
- `market_context_high->unknown_4h` score `-4.2003` n `149` status `ready` deltaP `3.4935` edge `-0.1855` maxDD `-8.3588`
- `market_context_high->fx_24h` score `-5.117` n `146` status `ready` deltaP `-12.8015` edge `-0.0535` maxDD `-21.0414`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

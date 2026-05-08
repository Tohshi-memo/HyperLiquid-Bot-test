# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-08T01:37:14.863665+00:00`
- Price records: `602`
- Market context records: `706`
- Flow alert records: `1994`
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

- `market_context_high->crypto_major_24h` score `10.8513` n `146` status `ready` deltaP `26.3658` edge `0.7619` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `6.5307` n `146` status `ready` deltaP `8.2084` edge `0.4943` maxDD `-0.0508`
- `market_context_high->fx_4h` score `-0.2229` n `149` status `ready` deltaP `7.0308` edge `0.0117` maxDD `-1.6381`
- `market_context_high->fx_1h` score `-0.287` n `149` status `ready` deltaP `2.8359` edge `0.0021` maxDD `-0.291`
- `market_context_high->commodity_1h` score `-0.479` n `149` status `ready` deltaP `2.3603` edge `0.0418` maxDD `-3.7959`
- `market_context_high->index_1h` score `-0.6282` n `149` status `ready` deltaP `0.3017` edge `0.0028` maxDD `-2.8282`
- `market_context_high->index_24h` score `-1.0775` n `146` status `ready` deltaP `-2.9826` edge `0.1296` maxDD `-5.9609`
- `market_context_high->crypto_major_4h` score `-1.1394` n `149` status `ready` deltaP `16.2036` edge `0.1165` maxDD `-22.648`
- `market_context_high->unknown_1h` score `-1.1837` n `149` status `ready` deltaP `-4.1863` edge `-0.0104` maxDD `-2.1602`
- `market_context_high->equity_1h` score `-1.2` n `149` status `ready` deltaP `-1.8847` edge `-0.0064` maxDD `-4.4826`
- `market_context_high->crypto_alt_1h` score `-1.3761` n `149` status `ready` deltaP `4.5588` edge `-0.0136` maxDD `-8.1842`
- `market_context_high->crypto_major_1h` score `-1.615` n `149` status `ready` deltaP `6.0482` edge `-0.0026` maxDD `-11.4508`
- `market_context_high->index_4h` score `-1.6919` n `149` status `ready` deltaP `2.2464` edge `-0.0037` maxDD `-6.5149`
- `market_context_high->crypto_alt_4h` score `-1.9937` n `149` status `ready` deltaP `3.9054` edge `0.0648` maxDD `-15.2248`
- `market_context_high->equity_24h` score `-2.191` n `146` status `ready` deltaP `-4.9364` edge `0.1108` maxDD `-10.5047`
- `market_context_high->equity_4h` score `-2.5914` n `149` status `ready` deltaP `-0.8464` edge `0.0049` maxDD `-10.5498`
- `market_context_high->metal_1h` score `-3.375` n `149` status `ready` deltaP `-5.1783` edge `-0.0508` maxDD `-9.0076`
- `market_context_high->commodity_4h` score `-3.8256` n `149` status `ready` deltaP `-6.5257` edge `0.0748` maxDD `-13.0076`
- `market_context_high->unknown_4h` score `-4.2866` n `149` status `ready` deltaP `3.0304` edge `-0.1896` maxDD `-8.3588`
- `market_context_high->fx_24h` score `-5.0366` n `146` status `ready` deltaP `-11.8704` edge `-0.0494` maxDD `-21.0414`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-08T04:22:20.120466+00:00`
- Price records: `613`
- Market context records: `717`
- Flow alert records: `2027`
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

- `market_context_high->crypto_major_24h` score `11.4175` n `146` status `ready` deltaP `27.7576` edge `0.7998` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `6.3487` n `146` status `ready` deltaP `8.0192` edge `0.4804` maxDD `-0.0508`
- `market_context_high->fx_4h` score `-0.2876` n `149` status `ready` deltaP `6.1161` edge `0.0095` maxDD `-1.6381`
- `market_context_high->fx_1h` score `-0.2969` n `149` status `ready` deltaP `2.6768` edge `0.0019` maxDD `-0.291`
- `market_context_high->commodity_1h` score `-0.446` n `149` status `ready` deltaP `2.547` edge `0.0433` maxDD `-3.7959`
- `market_context_high->index_1h` score `-0.6316` n `149` status `ready` deltaP `0.2374` edge `0.0028` maxDD `-2.8282`
- `market_context_high->index_24h` score `-0.6395` n `146` status `ready` deltaP `-1.3765` edge `0.1554` maxDD `-5.9609`
- `market_context_high->crypto_major_4h` score `-1.032` n `149` status `ready` deltaP `17.2035` edge `0.1236` maxDD `-22.648`
- `market_context_high->unknown_1h` score `-1.1353` n `149` status `ready` deltaP `-3.7304` edge `-0.0094` maxDD `-2.1602`
- `market_context_high->equity_1h` score `-1.1849` n `149` status `ready` deltaP `-1.7561` edge `-0.006` maxDD `-4.4826`
- `market_context_high->crypto_alt_1h` score `-1.3979` n `149` status `ready` deltaP `4.4665` edge `-0.0148` maxDD `-8.1842`
- `market_context_high->equity_24h` score `-1.5877` n `146` status `ready` deltaP `-3.215` edge `0.1496` maxDD `-10.5047`
- `market_context_high->crypto_major_1h` score `-1.5978` n `149` status `ready` deltaP `6.1726` edge `-0.002` maxDD `-11.4508`
- `market_context_high->index_4h` score `-1.8114` n `149` status `ready` deltaP `1.5324` edge `-0.0089` maxDD `-6.5149`
- `market_context_high->crypto_alt_4h` score `-1.9648` n `149` status `ready` deltaP `3.6367` edge `0.069` maxDD `-15.2248`
- `market_context_high->equity_4h` score `-2.7543` n `149` status `ready` deltaP `-1.503` edge `-0.0043` maxDD `-10.5498`
- `market_context_high->metal_1h` score `-3.3921` n `149` status `ready` deltaP `-5.1365` edge `-0.0525` maxDD `-9.0076`
- `market_context_high->commodity_4h` score `-3.6719` n `149` status `ready` deltaP `-5.7448` edge `0.0824` maxDD `-13.0076`
- `market_context_high->unknown_4h` score `-4.1407` n `149` status `ready` deltaP `3.7896` edge `-0.1825` maxDD `-8.3588`
- `market_context_high->fx_24h` score `-5.1457` n `146` status `ready` deltaP `-13.1432` edge `-0.0549` maxDD `-21.0414`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

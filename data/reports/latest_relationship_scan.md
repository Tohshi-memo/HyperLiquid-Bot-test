# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-07T15:52:34.646335+00:00`
- Price records: `672`
- Market context records: `5995`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11120`

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

- `news_risk_high->fx_24h` score `7.5407` n `30` status `ready` deltaP `68.9236` edge `0.1689` maxDD `0.0`
- `news_risk_high->commodity_24h` score `4.2586` n `30` status `ready` deltaP `32.6736` edge `0.1576` maxDD `-0.3101`
- `news_risk_high->fx_4h` score `4.1409` n `30` status `ready` deltaP `42.8963` edge `0.0637` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.2298` n `30` status `ready` deltaP `26.7764` edge `0.0212` maxDD `-0.1113`
- `market_context_high->equity_4h` score `1.1233` n `226` status `ready` deltaP `7.4479` edge `0.1534` maxDD `-4.0887`
- `news_risk_high->crypto_major_1h` score `0.7312` n `30` status `ready` deltaP `9.5908` edge `0.0765` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.146` n `30` status `ready` deltaP `5.02` edge `0.0314` maxDD `-1.6923`
- `news_risk_high->index_24h` score `0.1078` n `30` status `ready` deltaP `9.2361` edge `0.0394` maxDD `-2.3058`
- `market_context_high->equity_24h` score `-0.3376` n `199` status `ready` deltaP `22.5084` edge `0.3586` maxDD `-31.2762`
- `news_risk_high->metal_1h` score `-0.3939` n `30` status `ready` deltaP `1.8363` edge `-0.0261` maxDD `-1.2643`
- `market_context_high->equity_1h` score `-0.4564` n `226` status `ready` deltaP `3.3504` edge `0.032` maxDD `-4.3608`
- `market_context_high->metal_1h` score `-0.5176` n `226` status `ready` deltaP `2.0428` edge `-0.0001` maxDD `-2.0564`
- `market_context_high->commodity_1h` score `-0.5982` n `226` status `ready` deltaP `-0.5856` edge `0.002` maxDD `-0.8358`
- `market_context_high->fx_1h` score `-0.7428` n `226` status `ready` deltaP `-1.4242` edge `-0.0016` maxDD `-0.7314`
- `news_risk_high->index_1h` score `-1.008` n `30` status `ready` deltaP `-8.9521` edge `-0.0181` maxDD `-1.1161`
- `market_context_high->commodity_4h` score `-1.0514` n `226` status `ready` deltaP `-0.1417` edge `-0.0003` maxDD `-3.3508`
- `market_context_high->crypto_major_1h` score `-1.1474` n `226` status `ready` deltaP `2.4522` edge `0.0133` maxDD `-9.807`
- `market_context_high->index_1h` score `-1.1875` n `226` status `ready` deltaP `-1.607` edge `0.0031` maxDD `-1.3078`
- `market_context_high->index_4h` score `-1.2047` n `226` status `ready` deltaP `-0.1673` edge `0.0154` maxDD `-3.165`
- `market_context_high->crypto_alt_1h` score `-1.2213` n `226` status `ready` deltaP `1.4506` edge `0.009` maxDD `-9.3536`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-07T16:22:26.678274+00:00`
- Price records: `672`
- Market context records: `5997`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11122`

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

- `news_risk_high->fx_24h` score `7.5503` n `30` status `ready` deltaP `68.9236` edge `0.1697` maxDD `0.0`
- `news_risk_high->commodity_24h` score `4.178` n `30` status `ready` deltaP `32.3264` edge `0.1532` maxDD `-0.3101`
- `news_risk_high->fx_4h` score `4.1665` n `30` status `ready` deltaP `43.2012` edge `0.0638` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.231` n `30` status `ready` deltaP `26.7764` edge `0.0213` maxDD `-0.1113`
- `market_context_high->equity_4h` score `1.137` n `224` status `ready` deltaP `7.3933` edge `0.1549` maxDD `-4.0887`
- `news_risk_high->crypto_major_1h` score `0.7288` n `30` status `ready` deltaP `9.5908` edge `0.0762` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.1374` n `30` status `ready` deltaP `5.02` edge `0.0303` maxDD `-1.6923`
- `news_risk_high->index_24h` score `0.1156` n `30` status `ready` deltaP `9.2361` edge `0.0404` maxDD `-2.3058`
- `market_context_high->equity_24h` score `-0.1349` n `197` status `ready` deltaP `23.2022` edge `0.3692` maxDD `-31.1432`
- `news_risk_high->metal_1h` score `-0.404` n `30` status `ready` deltaP `1.6866` edge `-0.0264` maxDD `-1.2643`
- `market_context_high->metal_1h` score `-0.4958` n `224` status `ready` deltaP `2.3712` edge `0.0005` maxDD `-2.0564`
- `market_context_high->equity_1h` score `-0.4993` n `224` status `ready` deltaP `2.9593` edge `0.0291` maxDD `-4.3608`
- `market_context_high->commodity_1h` score `-0.5637` n `224` status `ready` deltaP `-0.4464` edge `0.0024` maxDD `-0.7117`
- `market_context_high->fx_1h` score `-0.7082` n `224` status `ready` deltaP `-1.0212` edge `-0.0014` maxDD `-0.7314`
- `news_risk_high->index_1h` score `-1.0103` n `30` status `ready` deltaP `-8.9521` edge `-0.0184` maxDD `-1.1161`
- `market_context_high->commodity_4h` score `-1.0209` n `224` status `ready` deltaP `-0.0436` edge `-0.0009` maxDD `-3.0418`
- `market_context_high->crypto_major_1h` score `-1.1857` n `224` status `ready` deltaP `2.0611` edge `0.011` maxDD `-9.807`
- `market_context_high->index_4h` score `-1.1919` n `224` status `ready` deltaP `-0.0109` edge `0.0158` maxDD `-3.1499`
- `market_context_high->index_1h` score `-1.2323` n `224` status `ready` deltaP `-2.0771` edge `0.0025` maxDD `-1.3078`
- `market_context_high->crypto_alt_1h` score `-1.2556` n `224` status `ready` deltaP `1.0319` edge `0.0074` maxDD `-9.3536`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

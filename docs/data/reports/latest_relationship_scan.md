# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-07T13:07:34.182900+00:00`
- Price records: `672`
- Market context records: `5983`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11220`

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

- `news_risk_high->fx_24h` score `7.3955` n `30` status `ready` deltaP `67.7083` edge `0.1649` maxDD `0.0`
- `news_risk_high->commodity_24h` score `4.667` n `30` status `ready` deltaP `34.5834` edge `0.1789` maxDD `-0.3101`
- `news_risk_high->fx_4h` score `4.0716` n `30` status `ready` deltaP `42.1341` edge `0.063` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.1891` n `30` status `ready` deltaP `26.3273` edge `0.0208` maxDD `-0.1113`
- `market_context_high->equity_4h` score `1.1212` n `236` status `ready` deltaP `7.901` edge `0.1502` maxDD `-4.0887`
- `news_risk_high->crypto_major_1h` score `0.7421` n `30` status `ready` deltaP `9.5908` edge `0.0779` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.1054` n `30` status `ready` deltaP `4.7206` edge `0.0282` maxDD `-1.6923`
- `news_risk_high->index_24h` score `0.0555` n `30` status `ready` deltaP `9.2361` edge `0.0327` maxDD `-2.3058`
- `market_context_high->commodity_1h` score `-0.4078` n `237` status `ready` deltaP `-0.7011` edge `0.0042` maxDD `-1.1447`
- `news_risk_high->metal_1h` score `-0.4398` n `30` status `ready` deltaP `1.2375` edge `-0.028` maxDD `-1.2643`
- `market_context_high->equity_1h` score `-0.4772` n `237` status `ready` deltaP `3.3692` edge `0.0292` maxDD `-4.3608`
- `market_context_high->metal_1h` score `-0.5321` n `237` status `ready` deltaP `1.9126` edge `-0.0011` maxDD `-2.0564`
- `market_context_high->fx_1h` score `-0.711` n `237` status `ready` deltaP `-1.0144` edge `-0.0008` maxDD `-0.8015`
- `market_context_high->equity_24h` score `-1.0569` n `210` status `ready` deltaP `21.0466` edge `0.3084` maxDD `-31.2762`
- `news_risk_high->index_1h` score `-1.0976` n `30` status `ready` deltaP `-10.2994` edge `-0.0206` maxDD `-1.1161`
- `market_context_high->index_1h` score `-1.1324` n `237` status `ready` deltaP `-0.9323` edge `0.0032` maxDD `-1.3078`
- `market_context_high->index_4h` score `-1.1521` n `236` status `ready` deltaP `0.6795` edge `0.0165` maxDD `-3.165`
- `market_context_high->crypto_major_1h` score `-1.1773` n `237` status `ready` deltaP `1.9537` edge `0.0128` maxDD `-9.807`
- `market_context_high->crypto_alt_1h` score `-1.2326` n `237` status `ready` deltaP `1.2185` edge `0.0091` maxDD `-9.3536`
- `market_context_high->commodity_4h` score `-1.3226` n `236` status `ready` deltaP `-0.6821` edge `-0.0033` maxDD `-5.6038`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

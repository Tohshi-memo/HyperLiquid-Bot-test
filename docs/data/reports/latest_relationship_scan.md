# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-07T12:37:32.871089+00:00`
- Price records: `672`
- Market context records: `5981`
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

- `news_risk_high->fx_24h` score `7.3569` n `30` status `ready` deltaP `67.3611` edge `0.164` maxDD `0.0`
- `news_risk_high->commodity_24h` score `4.7307` n `30` status `ready` deltaP `34.9306` edge `0.1819` maxDD `-0.3101`
- `news_risk_high->fx_4h` score `4.0412` n `30` status `ready` deltaP `41.8293` edge `0.0625` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.1639` n `30` status `ready` deltaP `26.0279` edge `0.0207` maxDD `-0.1113`
- `market_context_high->equity_4h` score `1.1848` n `238` status `ready` deltaP `7.9166` edge `0.1554` maxDD `-4.0887`
- `news_risk_high->crypto_major_1h` score `0.7125` n `30` status `ready` deltaP `9.4411` edge `0.0751` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.0719` n `30` status `ready` deltaP `4.5709` edge `0.0249` maxDD `-1.6923`
- `news_risk_high->index_24h` score `0.0477` n `30` status `ready` deltaP `9.2361` edge `0.0317` maxDD `-2.3058`
- `market_context_high->commodity_1h` score `-0.4369` n `239` status `ready` deltaP `-1.1037` edge `0.0037` maxDD `-1.1887`
- `market_context_high->equity_1h` score `-0.446` n `239` status `ready` deltaP `3.5797` edge `0.0318` maxDD `-4.3608`
- `news_risk_high->metal_1h` score `-0.4492` n `30` status `ready` deltaP `1.0878` edge `-0.0282` maxDD `-1.2643`
- `market_context_high->metal_1h` score `-0.5152` n `239` status `ready` deltaP `2.1478` edge `-0.0005` maxDD `-2.0564`
- `market_context_high->fx_1h` score `-0.6988` n `239` status `ready` deltaP `-0.8619` edge `-0.0008` maxDD `-0.8015`
- `market_context_high->index_1h` score `-0.7155` n `239` status `ready` deltaP `-0.6583` edge `0.004` maxDD `-1.3078`
- `market_context_high->equity_24h` score `-1.099` n `212` status `ready` deltaP `21.0004` edge `0.3052` maxDD `-31.2762`
- `news_risk_high->index_1h` score `-1.1069` n `30` status `ready` deltaP `-10.4491` edge `-0.0208` maxDD `-1.1161`
- `market_context_high->index_4h` score `-1.1364` n `238` status `ready` deltaP `0.7698` edge `0.0179` maxDD `-3.165`
- `market_context_high->crypto_major_1h` score `-1.1416` n `239` status `ready` deltaP `2.1747` edge `0.0159` maxDD `-9.807`
- `market_context_high->crypto_alt_1h` score `-1.1959` n `239` status `ready` deltaP `1.4607` edge `0.0122` maxDD `-9.3536`
- `market_context_high->commodity_4h` score `-1.386` n `238` status `ready` deltaP `-1.0453` edge `-0.005` maxDD `-5.925`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-07T19:22:45.506602+00:00`
- Price records: `672`
- Market context records: `6010`
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

- `news_risk_high->fx_24h` score `7.6242` n `30` status `ready` deltaP `69.0972` edge `0.1747` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.1749` n `30` status `ready` deltaP `43.2012` edge `0.0645` maxDD `-0.0345`
- `news_risk_high->commodity_24h` score `3.7077` n `30` status `ready` deltaP `30.2431` edge `0.1279` maxDD `-0.3101`
- `news_risk_high->fx_1h` score `2.2442` n `30` status `ready` deltaP `26.9261` edge `0.0214` maxDD `-0.1113`
- `market_context_high->equity_4h` score `1.1057` n `217` status `ready` deltaP `7.3023` edge `0.1529` maxDD `-4.0887`
- `news_risk_high->crypto_major_1h` score `0.8481` n `30` status `ready` deltaP `10.6387` edge `0.0845` maxDD `-2.0691`
- `market_context_high->equity_24h` score `0.5737` n `191` status `ready` deltaP `25.3709` edge `0.4238` maxDD `-31.6107`
- `news_risk_high->crypto_alt_1h` score `0.2153` n `30` status `ready` deltaP `5.4691` edge `0.0373` maxDD `-1.6923`
- `news_risk_high->index_24h` score `0.1288` n `30` status `ready` deltaP `9.2361` edge `0.0421` maxDD `-2.3058`
- `news_risk_high->metal_1h` score `-0.404` n `30` status `ready` deltaP `1.5369` edge `-0.0254` maxDD `-1.2643`
- `market_context_high->metal_1h` score `-0.443` n `217` status `ready` deltaP `3.0423` edge `0.0028` maxDD `-2.0564`
- `market_context_high->equity_1h` score `-0.5665` n `217` status `ready` deltaP `1.9827` edge `0.027` maxDD `-4.3608`
- `market_context_high->commodity_1h` score `-0.6513` n `217` status `ready` deltaP `-1.3018` edge `0.0008` maxDD `-0.7117`
- `market_context_high->fx_1h` score `-0.6905` n `217` status `ready` deltaP `-0.7851` edge `-0.0015` maxDD `-0.7314`
- `news_risk_high->index_1h` score `-1.0353` n `30` status `ready` deltaP `-9.4012` edge `-0.0186` maxDD `-1.1161`
- `market_context_high->index_4h` score `-1.1419` n `217` status `ready` deltaP `0.5493` edge `0.0155` maxDD `-2.9119`
- `market_context_high->crypto_major_1h` score `-1.158` n `217` status `ready` deltaP `2.1441` edge `0.014` maxDD `-9.807`
- `market_context_high->crypto_alt_1h` score `-1.1581` n `217` status `ready` deltaP `1.7978` edge `0.0148` maxDD `-9.3536`
- `market_context_high->commodity_4h` score `-1.1731` n `217` status `ready` deltaP `-2.1019` edge `-0.0068` maxDD `-3.0339`
- `market_context_high->index_1h` score `-1.2867` n `217` status `ready` deltaP `-2.8574` edge `0.0023` maxDD `-1.2381`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

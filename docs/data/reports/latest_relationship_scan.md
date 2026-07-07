# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-07T23:22:25.036083+00:00`
- Price records: `672`
- Market context records: `6029`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11125`

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

- `news_risk_high->fx_24h` score `7.8706` n `30` status `ready` deltaP `71.0069` edge `0.1825` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.3063` n `30` status `ready` deltaP `44.5732` edge `0.0663` maxDD `-0.0345`
- `news_risk_high->commodity_24h` score `2.9743` n `30` status `ready` deltaP `27.4653` edge `0.0853` maxDD `-0.3101`
- `news_risk_high->fx_1h` score `2.2574` n `30` status `ready` deltaP `27.0758` edge `0.0215` maxDD `-0.1113`
- `market_context_high->equity_4h` score `1.6747` n `206` status `ready` deltaP `9.2514` edge `0.1696` maxDD `-2.671`
- `market_context_high->equity_24h` score `1.6685` n `180` status `ready` deltaP `29.7223` edge `0.5609` maxDD `-31.6107`
- `news_risk_high->crypto_major_1h` score `0.8278` n `30` status `ready` deltaP `10.1896` edge `0.0849` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.2302` n `30` status `ready` deltaP `5.4691` edge `0.0392` maxDD `-1.6923`
- `news_risk_high->index_24h` score `0.1522` n `30` status `ready` deltaP `9.2361` edge `0.0451` maxDD `-2.3058`
- `market_context_high->metal_1h` score `-0.3854` n `206` status `ready` deltaP `3.7294` edge `0.0056` maxDD `-2.0564`
- `news_risk_high->metal_1h` score `-0.4219` n `30` status `ready` deltaP `1.2375` edge `-0.0257` maxDD `-1.2643`
- `market_context_high->index_24h` score `-0.4273` n `180` status `ready` deltaP `5.3472` edge `0.0796` maxDD `-5.6021`
- `news_risk_high->crypto_alt_24h` score `-0.5289` n `30` status `ready` deltaP `23.0208` edge `-0.1828` maxDD `-0.5131`
- `market_context_high->fx_1h` score `-0.575` n `206` status `ready` deltaP `-0.141` edge `-0.0013` maxDD `-0.6538`
- `market_context_high->commodity_1h` score `-0.6379` n `206` status `ready` deltaP `-1.2339` edge `-0.0003` maxDD `-0.5708`
- `market_context_high->index_4h` score `-0.9118` n `206` status `ready` deltaP `2.7203` edge `0.0183` maxDD `-1.9335`
- `market_context_high->metal_4h` score `-0.9189` n `206` status `ready` deltaP `5.0956` edge `0.0082` maxDD `-3.4996`
- `market_context_high->equity_1h` score `-0.9354` n `206` status `ready` deltaP `1.2296` edge `0.0267` maxDD `-4.3608`
- `market_context_high->crypto_alt_1h` score `-0.9764` n `206` status `ready` deltaP `3.6568` edge `0.0257` maxDD `-9.3536`
- `market_context_high->crypto_major_1h` score `-0.9899` n `206` status `ready` deltaP `3.6524` edge `0.0255` maxDD `-9.807`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

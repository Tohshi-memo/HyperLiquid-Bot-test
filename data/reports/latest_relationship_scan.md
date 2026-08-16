# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-16T10:22:30.775661+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11798`

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

- `market_context_high->unknown_24h` score `195.129` n `88` status `ready` deltaP `-21.512` edge `25.4283` maxDD `-7.8016`
- `news_risk_high->equity_24h` score `12.573` n `35` status `ready` deltaP `20.0099` edge `0.9523` maxDD `-1.0358`
- `news_risk_high->equity_4h` score `7.5254` n `35` status `ready` deltaP `36.7378` edge `0.3822` maxDD `0.0`
- `market_context_high->commodity_24h` score `7.4941` n `88` status `ready` deltaP `41.3037` edge `0.3549` maxDD `-0.1266`
- `news_risk_high->index_24h` score `3.7224` n `35` status `ready` deltaP `30.5556` edge `0.1065` maxDD `0.0`
- `market_context_high->commodity_4h` score `1.9323` n `111` status `ready` deltaP `18.095` edge `0.0875` maxDD `-0.7687`
- `news_risk_high->index_4h` score `1.8512` n `35` status `ready` deltaP `21.2326` edge `0.0259` maxDD `-0.0546`
- `news_risk_high->equity_1h` score `1.6142` n `35` status `ready` deltaP `6.2832` edge `0.1245` maxDD `-0.5496`
- `news_risk_high->fx_4h` score `0.0491` n `35` status `ready` deltaP `5.2351` edge `-0.0067` maxDD `-0.0863`
- `market_context_high->commodity_1h` score `0.0199` n `123` status `ready` deltaP `3.2533` edge `0.0211` maxDD `-0.624`
- `market_context_high->fx_4h` score `-0.0279` n `111` status `ready` deltaP `7.2429` edge `0.0086` maxDD `-0.504`
- `news_risk_high->index_1h` score `-0.0551` n `35` status `ready` deltaP `0.5561` edge `0.0143` maxDD `-0.141`
- `market_context_high->fx_1h` score `-0.1345` n `123` status `ready` deltaP `1.413` edge `0.0015` maxDD `-0.2527`
- `news_risk_high->fx_1h` score `-0.1477` n `35` status `ready` deltaP `2.0402` edge `-0.0016` maxDD `-0.1414`
- `market_context_high->metal_1h` score `-0.5684` n `123` status `ready` deltaP `0.7497` edge `-0.0063` maxDD `-1.7257`
- `news_risk_high->metal_1h` score `-0.6272` n `35` status `ready` deltaP `-6.3815` edge `-0.011` maxDD `-0.8156`
- `market_context_high->index_1h` score `-0.7501` n `123` status `ready` deltaP `-6.1803` edge `-0.0028` maxDD `-0.5064`
- `news_risk_high->commodity_1h` score `-0.963` n `35` status `ready` deltaP `-4.2729` edge `-0.021` maxDD `-0.7946`
- `news_risk_high->metal_4h` score `-1.1177` n `35` status `ready` deltaP `-3.7152` edge `-0.0292` maxDD `-2.4791`
- `market_context_high->metal_4h` score `-1.1691` n `111` status `ready` deltaP `3.5693` edge `-0.0163` maxDD `-4.5909`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

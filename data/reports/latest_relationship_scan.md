# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-07T10:37:29.952296+00:00`
- Price records: `672`
- Market context records: `5972`
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

- `news_risk_high->fx_24h` score `7.199` n `30` status `ready` deltaP `65.9722` edge `0.1601` maxDD `0.0`
- `news_risk_high->commodity_24h` score `4.9762` n `30` status `ready` deltaP `36.3195` edge `0.1931` maxDD `-0.3101`
- `news_risk_high->fx_4h` score `3.9148` n `30` status `ready` deltaP `40.6098` edge `0.0601` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.1615` n `30` status `ready` deltaP `26.0279` edge `0.0205` maxDD `-0.1113`
- `market_context_high->equity_4h` score `1.4127` n `234` status `ready` deltaP `8.9197` edge `0.1677` maxDD `-4.0887`
- `news_risk_high->crypto_major_1h` score `0.8232` n `30` status `ready` deltaP `10.0399` edge `0.0853` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.1764` n `30` status `ready` deltaP `5.1697` edge `0.0343` maxDD `-1.6923`
- `news_risk_high->index_24h` score `-0.0411` n `30` status `ready` deltaP `8.368` edge `0.0261` maxDD `-2.3058`
- `news_risk_high->metal_1h` score `-0.3806` n `30` status `ready` deltaP `1.986` edge `-0.0254` maxDD `-1.2643`
- `market_context_high->equity_1h` score `-0.4482` n `242` status `ready` deltaP `3.432` edge `0.0325` maxDD `-4.3608`
- `market_context_high->metal_1h` score `-0.4888` n `242` status `ready` deltaP `2.3717` edge `0.0014` maxDD `-2.0564`
- `market_context_high->commodity_1h` score `-0.5098` n `242` status `ready` deltaP `-1.5811` edge `0.0009` maxDD `-1.4578`
- `market_context_high->fx_1h` score `-0.6787` n `242` status `ready` deltaP `-0.6112` edge `-0.0008` maxDD `-0.8015`
- `market_context_high->index_1h` score `-0.7184` n `242` status `ready` deltaP `-0.7126` edge `0.004` maxDD `-1.3078`
- `market_context_high->equity_24h` score `-0.9301` n `212` status `ready` deltaP `21.0266` edge `0.3066` maxDD `-31.2762`
- `news_risk_high->index_1h` score `-1.0999` n `30` status `ready` deltaP `-10.2994` edge `-0.0209` maxDD `-1.1161`
- `market_context_high->crypto_major_1h` score `-1.1138` n `242` status `ready` deltaP `2.0785` edge `0.0201` maxDD `-9.807`
- `market_context_high->index_4h` score `-1.1185` n `234` status `ready` deltaP `0.9198` edge `0.0192` maxDD `-3.165`
- `market_context_high->crypto_alt_1h` score `-1.1302` n `242` status `ready` deltaP `1.8088` edge `0.0183` maxDD `-9.3536`
- `market_context_high->commodity_4h` score `-1.4394` n `234` status `ready` deltaP `-1.3199` edge `-0.0044` maxDD `-6.3734`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

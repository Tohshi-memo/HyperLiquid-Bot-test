# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-07T04:52:25.130807+00:00`
- Price records: `672`
- Market context records: `5948`
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

- `news_risk_high->fx_24h` score `6.8746` n `30` status `ready` deltaP `62.8472` edge `0.1539` maxDD `0.0`
- `news_risk_high->commodity_24h` score `5.468` n `30` status `ready` deltaP `39.2709` edge `0.2144` maxDD `-0.3101`
- `news_risk_high->fx_4h` score `3.7615` n `30` status `ready` deltaP `38.9329` edge `0.0585` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.0933` n `30` status `ready` deltaP `25.2794` edge `0.0198` maxDD `-0.1113`
- `market_context_high->equity_4h` score `1.6083` n `221` status `ready` deltaP `10.5852` edge `0.1729` maxDD `-4.0887`
- `news_risk_high->crypto_major_1h` score `0.9252` n `30` status `ready` deltaP `11.2375` edge `0.0904` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.2636` n `30` status `ready` deltaP `5.9182` edge `0.0405` maxDD `-1.6923`
- `news_risk_high->index_24h` score `-0.2132` n `30` status `ready` deltaP `6.9791` edge `0.0133` maxDD `-2.3058`
- `market_context_high->equity_1h` score `-0.2894` n `229` status `ready` deltaP `5.2219` edge `0.0326` maxDD `-4.3608`
- `market_context_high->metal_1h` score `-0.3832` n `229` status `ready` deltaP `2.6639` edge `0.0002` maxDD `-2.0339`
- `news_risk_high->metal_1h` score `-0.39` n `30` status `ready` deltaP `2.2854` edge `-0.0286` maxDD `-1.2643`
- `market_context_high->index_1h` score `-0.6225` n `229` status `ready` deltaP `0.8171` edge `0.0045` maxDD `-1.1808`
- `market_context_high->commodity_1h` score `-0.6555` n `229` status `ready` deltaP `-4.2733` edge `-0.004` maxDD `-1.4578`
- `market_context_high->fx_1h` score `-0.8052` n `229` status `ready` deltaP `-2.2024` edge `-0.0013` maxDD `-0.756`
- `market_context_high->equity_24h` score `-0.833` n `213` status `ready` deltaP `19.0532` edge `0.2738` maxDD `-31.2762`
- `market_context_high->crypto_alt_1h` score `-0.9994` n `229` status `ready` deltaP `1.6532` edge `0.0186` maxDD `-8.6202`
- `news_risk_high->index_1h` score `-1.0462` n `30` status `ready` deltaP `-9.4012` edge `-0.02` maxDD `-1.1161`
- `market_context_high->crypto_major_1h` score `-1.0564` n `229` status `ready` deltaP `2.0527` edge `0.0203` maxDD `-9.2206`
- `market_context_high->metal_4h` score `-1.5976` n `221` status `ready` deltaP `-2.0989` edge `-0.0276` maxDD `-5.725`
- `market_context_high->index_4h` score `-1.6694` n `221` status `ready` deltaP `1.3974` edge `0.0203` maxDD `-3.165`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

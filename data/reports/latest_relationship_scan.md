# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-07T05:37:33.472313+00:00`
- Price records: `672`
- Market context records: `5951`
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

- `news_risk_high->fx_24h` score `6.8818` n `30` status `ready` deltaP `62.8472` edge `0.1545` maxDD `0.0`
- `news_risk_high->commodity_24h` score `5.462` n `30` status `ready` deltaP `39.2709` edge `0.2139` maxDD `-0.3101`
- `news_risk_high->fx_4h` score `3.8052` n `30` status `ready` deltaP `39.3902` edge `0.0591` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.0933` n `30` status `ready` deltaP `25.2794` edge `0.0198` maxDD `-0.1113`
- `market_context_high->equity_4h` score `1.6359` n `221` status `ready` deltaP `10.5852` edge `0.1752` maxDD `-4.0887`
- `news_risk_high->crypto_major_1h` score `0.933` n `30` status `ready` deltaP `11.2375` edge `0.0914` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.2933` n `30` status `ready` deltaP `6.2176` edge `0.0423` maxDD `-1.6923`
- `news_risk_high->index_24h` score `-0.1999` n `30` status `ready` deltaP `6.9791` edge `0.015` maxDD `-2.3058`
- `news_risk_high->metal_1h` score `-0.3604` n `30` status `ready` deltaP `2.5848` edge `-0.0268` maxDD `-1.2643`
- `market_context_high->equity_1h` score `-0.3923` n `232` status `ready` deltaP `4.7466` edge `0.0309` maxDD `-4.3608`
- `market_context_high->metal_1h` score `-0.4386` n `232` status `ready` deltaP `2.2687` edge `-0.0001` maxDD `-2.0339`
- `market_context_high->index_1h` score `-0.6587` n `232` status `ready` deltaP `0.4491` edge `0.0039` maxDD `-1.3078`
- `market_context_high->commodity_1h` score `-0.6883` n `232` status `ready` deltaP `-4.2923` edge `-0.0039` maxDD `-1.4578`
- `market_context_high->equity_24h` score `-0.7155` n `213` status `ready` deltaP `19.5741` edge `0.2854` maxDD `-31.2762`
- `market_context_high->fx_1h` score `-0.7456` n `232` status `ready` deltaP `-1.5022` edge `-0.001` maxDD `-0.756`
- `news_risk_high->index_1h` score `-1.0547` n `30` status `ready` deltaP `-9.5509` edge `-0.0201` maxDD `-1.1161`
- `market_context_high->crypto_major_1h` score `-1.1416` n `232` status `ready` deltaP `1.7835` edge `0.0185` maxDD `-9.807`
- `market_context_high->crypto_alt_1h` score `-1.148` n `232` status `ready` deltaP `1.7061` edge `0.0167` maxDD `-9.3536`
- `market_context_high->metal_4h` score `-1.5512` n `221` status `ready` deltaP `-1.6416` edge `-0.0247` maxDD `-5.725`
- `market_context_high->index_4h` score `-1.6634` n `221` status `ready` deltaP `1.3974` edge `0.0208` maxDD `-3.165`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

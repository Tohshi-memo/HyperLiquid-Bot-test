# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-07T04:37:29.625958+00:00`
- Price records: `672`
- Market context records: `5947`
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

- `news_risk_high->fx_24h` score `6.8571` n `30` status `ready` deltaP `62.6736` edge `0.1536` maxDD `0.0`
- `news_risk_high->commodity_24h` score `5.4704` n `30` status `ready` deltaP `39.2709` edge `0.2146` maxDD `-0.3101`
- `news_risk_high->fx_4h` score `3.7469` n `30` status `ready` deltaP `38.7805` edge `0.0583` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.0933` n `30` status `ready` deltaP `25.2794` edge `0.0198` maxDD `-0.1113`
- `market_context_high->equity_4h` score `1.5963` n `221` status `ready` deltaP `10.5852` edge `0.1719` maxDD `-4.0887`
- `news_risk_high->crypto_major_1h` score `0.9221` n `30` status `ready` deltaP `11.2375` edge `0.09` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.2636` n `30` status `ready` deltaP `5.9182` edge `0.0405` maxDD `-1.6923`
- `news_risk_high->index_24h` score `-0.2178` n `30` status `ready` deltaP `6.9791` edge `0.0127` maxDD `-2.3058`
- `market_context_high->equity_1h` score `-0.2357` n `228` status `ready` deltaP `5.4785` edge `0.0336` maxDD `-4.3608`
- `market_context_high->metal_1h` score `-0.3686` n `228` status `ready` deltaP `2.8995` edge `0.0005` maxDD `-2.0339`
- `news_risk_high->metal_1h` score `-0.3877` n `30` status `ready` deltaP `2.2854` edge `-0.0283` maxDD `-1.2643`
- `market_context_high->index_1h` score `-0.6072` n `228` status `ready` deltaP `1.0374` edge `0.0046` maxDD `-1.1486`
- `market_context_high->commodity_1h` score `-0.6445` n `228` status `ready` deltaP `-4.0761` edge `-0.0039` maxDD `-1.4578`
- `market_context_high->fx_1h` score `-0.7891` n `228` status `ready` deltaP `-2.0013` edge `-0.0013` maxDD `-0.756`
- `market_context_high->equity_24h` score `-0.874` n `213` status `ready` deltaP `18.8796` edge `0.2697` maxDD `-31.2762`
- `market_context_high->crypto_alt_1h` score `-0.9648` n `228` status `ready` deltaP `1.8831` edge `0.0195` maxDD `-8.4597`
- `market_context_high->crypto_major_1h` score `-1.0086` n `228` status `ready` deltaP `2.2902` edge `0.0214` maxDD `-8.9448`
- `news_risk_high->index_1h` score `-1.0462` n `30` status `ready` deltaP `-9.4012` edge `-0.02` maxDD `-1.1161`
- `market_context_high->metal_4h` score `-1.6118` n `221` status `ready` deltaP `-2.2514` edge `-0.0284` maxDD `-5.725`
- `market_context_high->index_4h` score `-1.673` n `221` status `ready` deltaP `1.3974` edge `0.02` maxDD `-3.165`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

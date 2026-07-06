# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-06T09:37:26.063086+00:00`
- Price records: `672`
- Market context records: `5866`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `10106`

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

- `news_risk_high->fx_4h` score `3.7035` n `30` status `ready` deltaP `38.628` edge `0.0557` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `1.9759` n `30` status `ready` deltaP `23.9321` edge `0.019` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `0.9361` n `30` status `ready` deltaP `12.1357` edge `0.0858` maxDD `-2.0691`
- `market_context_high->equity_4h` score `0.6093` n `242` status `ready` deltaP `6.6003` edge `0.1519` maxDD `-6.9437`
- `news_risk_high->crypto_alt_1h` score `0.3112` n `30` status `ready` deltaP `5.9182` edge `0.0466` maxDD `-1.6923`
- `market_context_high->fx_1h` score `-0.3729` n `242` status `ready` deltaP `0.1856` edge `-0.0005` maxDD `-0.5499`
- `market_context_high->metal_1h` score `-0.3881` n `242` status `ready` deltaP `4.2522` edge `0.0064` maxDD `-2.0339`
- `market_context_high->equity_1h` score `-0.438` n `242` status `ready` deltaP `4.4985` edge `0.0342` maxDD `-5.0555`
- `news_risk_high->metal_1h` score `-0.4391` n `30` status `ready` deltaP `1.3872` edge `-0.0289` maxDD `-1.2643`
- `market_context_high->commodity_1h` score `-0.5687` n `242` status `ready` deltaP `-1.737` edge `-0.0029` maxDD `-2.0076`
- `market_context_high->index_1h` score `-0.6194` n `242` status `ready` deltaP `0.2338` edge `0.0038` maxDD `-0.7819`
- `market_context_high->crypto_major_1h` score `-0.7779` n `242` status `ready` deltaP `3.7611` edge `0.0422` maxDD `-6.2348`
- `market_context_high->crypto_alt_1h` score `-0.9264` n `242` status `ready` deltaP `2.5573` edge `0.0392` maxDD `-6.6758`
- `news_risk_high->index_1h` score `-1.2245` n `30` status `ready` deltaP `-12.2455` edge `-0.0239` maxDD `-1.1161`
- `market_context_high->index_4h` score `-1.2444` n `242` status `ready` deltaP `-0.4208` edge `0.012` maxDD `-3.165`
- `news_risk_high->commodity_4h` score `-1.8174` n `30` status `ready` deltaP `-13.8821` edge `-0.0529` maxDD `-2.3372`
- `market_context_high->fx_24h` score `-1.8296` n `228` status `ready` deltaP `4.8794` edge `0.0147` maxDD `-5.5435`
- `market_context_high->fx_4h` score `-1.8807` n `242` status `ready` deltaP `-6.3307` edge `-0.004` maxDD `-2.2593`
- `market_context_high->equity_24h` score `-1.9457` n `228` status `ready` deltaP `13.8524` edge `0.2534` maxDD `-31.6316`
- `news_risk_high->index_4h` score `-2.2344` n `30` status `ready` deltaP `-15.7927` edge `-0.0778` maxDD `-2.9371`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

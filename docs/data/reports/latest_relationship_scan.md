# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-06T06:07:31.153706+00:00`
- Price records: `672`
- Market context records: `5851`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `10126`

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

- `news_risk_high->fx_4h` score `3.6743` n `30` status `ready` deltaP `38.3232` edge `0.0553` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `1.989` n `30` status `ready` deltaP `24.0818` edge `0.0191` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `0.8877` n `30` status `ready` deltaP `11.6866` edge `0.0826` maxDD `-2.0691`
- `market_context_high->equity_4h` score `0.7407` n `254` status `ready` deltaP `7.8464` edge `0.1552` maxDD `-6.9958`
- `news_risk_high->crypto_alt_1h` score `0.266` n `30` status `ready` deltaP `5.3194` edge `0.0448` maxDD `-1.6923`
- `market_context_high->fx_1h` score `-0.3192` n `254` status `ready` deltaP `1.1422` edge `0.0` maxDD `-0.5499`
- `news_risk_high->metal_1h` score `-0.3869` n `30` status `ready` deltaP `1.986` edge `-0.0262` maxDD `-1.2643`
- `market_context_high->equity_1h` score `-0.4422` n `254` status `ready` deltaP `4.326` edge `0.035` maxDD `-5.0555`
- `market_context_high->metal_1h` score `-0.5025` n `254` status `ready` deltaP `3.3771` edge `0.0027` maxDD `-2.0339`
- `market_context_high->commodity_1h` score `-0.548` n `254` status `ready` deltaP `-1.1481` edge `-0.0025` maxDD `-2.1412`
- `market_context_high->index_1h` score `-0.5799` n `254` status `ready` deltaP `0.9041` edge `0.0044` maxDD `-0.7819`
- `market_context_high->equity_24h` score `-0.8381` n `226` status `ready` deltaP `17.4379` edge `0.3218` maxDD `-31.6316`
- `market_context_high->crypto_major_1h` score `-0.8407` n `254` status `ready` deltaP `3.4714` edge `0.0389` maxDD `-6.2348`
- `market_context_high->crypto_alt_1h` score `-0.9937` n `254` status `ready` deltaP `2.196` edge `0.036` maxDD `-6.6758`
- `market_context_high->index_4h` score `-1.1944` n `254` status `ready` deltaP `0.2401` edge `0.014` maxDD `-3.165`
- `news_risk_high->index_1h` score `-1.2229` n `30` status `ready` deltaP `-12.2455` edge `-0.0237` maxDD `-1.1161`
- `news_risk_high->commodity_4h` score `-1.7361` n `30` status `ready` deltaP `-12.815` edge `-0.0496` maxDD `-2.3372`
- `market_context_high->fx_4h` score `-1.749` n `254` status `ready` deltaP `-4.039` edge `-0.0024` maxDD `-2.2593`
- `market_context_high->fx_24h` score `-1.8439` n `226` status `ready` deltaP `4.3787` edge `0.0162` maxDD `-5.5435`
- `market_context_high->metal_4h` score `-2.0417` n `254` status `ready` deltaP `-4.2179` edge `-0.0373` maxDD `-8.3735`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

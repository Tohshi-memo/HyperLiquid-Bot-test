# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-06T20:07:32.876061+00:00`
- Price records: `672`
- Market context records: `5911`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11166`

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

- `news_risk_high->fx_4h` score `3.6059` n `30` status `ready` deltaP `37.4085` edge `0.0557` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.025` n `30` status `ready` deltaP `24.5309` edge `0.0191` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `0.9089` n `30` status `ready` deltaP `10.9381` edge `0.0903` maxDD `-2.0691`
- `market_context_high->equity_4h` score `0.8833` n `220` status `ready` deltaP `7.9878` edge `0.1298` maxDD `-4.0887`
- `news_risk_high->crypto_alt_1h` score `0.199` n `30` status `ready` deltaP `4.8703` edge `0.0392` maxDD `-1.6923`
- `market_context_high->equity_1h` score `-0.2164` n `221` status `ready` deltaP `4.7952` edge `0.0323` maxDD `-4.3608`
- `market_context_high->metal_1h` score `-0.3272` n `221` status `ready` deltaP `3.2609` edge `0.0034` maxDD `-2.0339`
- `news_risk_high->metal_1h` score `-0.4632` n `30` status `ready` deltaP `0.9381` edge `-0.029` maxDD `-1.2643`
- `market_context_high->commodity_1h` score `-0.5008` n `221` status `ready` deltaP `-1.5973` edge `-0.002` maxDD `-1.4578`
- `market_context_high->crypto_major_1h` score `-0.5503` n `221` status `ready` deltaP `3.7134` edge `0.0368` maxDD `-6.2348`
- `market_context_high->crypto_alt_1h` score `-0.6698` n `221` status `ready` deltaP `2.5022` edge `0.0309` maxDD `-6.6758`
- `market_context_high->fx_1h` score `-0.7752` n `221` status `ready` deltaP `-2.1961` edge `-0.0011` maxDD `-0.5751`
- `market_context_high->index_1h` score `-0.9681` n `221` status `ready` deltaP `0.0901` edge `0.0035` maxDD `-0.7819`
- `news_risk_high->index_1h` score `-1.2074` n `30` status `ready` deltaP `-11.9461` edge `-0.0237` maxDD `-1.1161`
- `market_context_high->commodity_4h` score `-1.6305` n `220` status `ready` deltaP `-2.985` edge `-0.0178` maxDD `-6.3734`
- `market_context_high->metal_4h` score `-1.7408` n `220` status `ready` deltaP `-3.8331` edge `-0.0344` maxDD `-5.725`
- `news_risk_high->commodity_4h` score `-1.9485` n `30` status `ready` deltaP `-15.8638` edge `-0.0565` maxDD `-2.3372`
- `market_context_high->index_4h` score `-1.9897` n `220` status `ready` deltaP `-0.9423` edge `0.0092` maxDD `-3.165`
- `market_context_high->equity_24h` score `-2.0928` n `213` status `ready` deltaP `12.9768` edge `0.1528` maxDD `-31.2762`
- `market_context_high->fx_24h` score `-2.1359` n `213` status `ready` deltaP `0.8949` edge `0.002` maxDD `-5.5435`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

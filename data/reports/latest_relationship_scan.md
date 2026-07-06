# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-06T21:52:30.093350+00:00`
- Price records: `672`
- Market context records: `5918`
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

- `news_risk_high->fx_4h` score `3.6765` n `30` status `ready` deltaP `38.1707` edge `0.0565` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.0621` n `30` status `ready` deltaP `24.98` edge `0.0192` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `0.8855` n `30` status `ready` deltaP `10.9381` edge `0.0873` maxDD `-2.0691`
- `market_context_high->equity_4h` score `0.8711` n `220` status `ready` deltaP `7.8354` edge `0.1298` maxDD `-4.0887`
- `news_risk_high->crypto_alt_1h` score `0.1647` n `30` status `ready` deltaP `4.7206` edge `0.0358` maxDD `-1.6923`
- `market_context_high->equity_1h` score `-0.1961` n `221` status `ready` deltaP `5.0946` edge `0.0329` maxDD `-4.3608`
- `market_context_high->metal_1h` score `-0.3194` n `221` status `ready` deltaP `3.4106` edge `0.0034` maxDD `-2.0339`
- `news_risk_high->metal_1h` score `-0.4554` n `30` status `ready` deltaP `1.0878` edge `-0.029` maxDD `-1.2643`
- `market_context_high->commodity_1h` score `-0.5257` n `221` status `ready` deltaP `-2.0464` edge `-0.0022` maxDD `-1.4578`
- `market_context_high->crypto_major_1h` score `-0.5737` n `221` status `ready` deltaP `3.7134` edge `0.0338` maxDD `-6.2348`
- `market_context_high->crypto_alt_1h` score `-0.7041` n `221` status `ready` deltaP `2.3525` edge `0.0275` maxDD `-6.6758`
- `market_context_high->fx_1h` score `-0.738` n `221` status `ready` deltaP `-1.747` edge `-0.001` maxDD `-0.5751`
- `market_context_high->index_1h` score `-0.9825` n `221` status `ready` deltaP `-0.0596` edge `0.0033` maxDD `-0.7819`
- `news_risk_high->index_1h` score `-1.2167` n `30` status `ready` deltaP `-12.0958` edge `-0.0239` maxDD `-1.1161`
- `market_context_high->commodity_4h` score `-1.6992` n `220` status `ready` deltaP `-4.0521` edge `-0.0195` maxDD `-6.3734`
- `market_context_high->metal_4h` score `-1.8361` n `220` status `ready` deltaP `-4.9002` edge `-0.0395` maxDD `-5.725`
- `market_context_high->equity_24h` score `-1.8572` n `213` status `ready` deltaP `14.1921` edge `0.1749` maxDD `-31.2762`
- `news_risk_high->commodity_4h` score `-2.0172` n `30` status `ready` deltaP `-16.9309` edge `-0.0582` maxDD `-2.3372`
- `market_context_high->index_4h` score `-2.0383` n `220` status `ready` deltaP `-1.3996` edge `0.0082` maxDD `-3.165`
- `market_context_high->fx_24h` score `-2.1429` n `213` status `ready` deltaP `0.8949` edge `0.0011` maxDD `-5.5435`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

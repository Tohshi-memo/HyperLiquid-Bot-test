# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-06T20:37:30.002275+00:00`
- Price records: `672`
- Market context records: `5913`
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

- `news_risk_high->fx_4h` score `3.6205` n `30` status `ready` deltaP `37.561` edge `0.0559` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.025` n `30` status `ready` deltaP `24.5309` edge `0.0191` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `0.9206` n `30` status `ready` deltaP `11.0878` edge `0.0908` maxDD `-2.0691`
- `market_context_high->equity_4h` score `0.8929` n `220` status `ready` deltaP `7.9878` edge `0.1306` maxDD `-4.0887`
- `news_risk_high->crypto_alt_1h` score `0.1982` n `30` status `ready` deltaP `4.8703` edge `0.0391` maxDD `-1.6923`
- `market_context_high->equity_1h` score `-0.1969` n `221` status `ready` deltaP `5.0946` edge `0.0328` maxDD `-4.3608`
- `market_context_high->metal_1h` score `-0.3109` n `221` status `ready` deltaP `3.5603` edge `0.0035` maxDD `-2.0339`
- `news_risk_high->metal_1h` score `-0.4468` n `30` status `ready` deltaP `1.2375` edge `-0.0289` maxDD `-1.2643`
- `market_context_high->commodity_1h` score `-0.5086` n `221` status `ready` deltaP `-1.747` edge `-0.002` maxDD `-1.4578`
- `market_context_high->crypto_major_1h` score `-0.5386` n `221` status `ready` deltaP `3.8631` edge `0.0373` maxDD `-6.2348`
- `market_context_high->crypto_alt_1h` score `-0.6705` n `221` status `ready` deltaP `2.5022` edge `0.0308` maxDD `-6.6758`
- `market_context_high->fx_1h` score `-0.7752` n `221` status `ready` deltaP `-2.1961` edge `-0.0011` maxDD `-0.5751`
- `market_context_high->index_1h` score `-0.9429` n `221` status `ready` deltaP `0.3895` edge `0.0036` maxDD `-0.7819`
- `news_risk_high->index_1h` score `-1.191` n `30` status `ready` deltaP `-11.6467` edge `-0.0236` maxDD `-1.1161`
- `market_context_high->commodity_4h` score `-1.6494` n `220` status `ready` deltaP `-3.2899` edge `-0.0182` maxDD `-6.3734`
- `market_context_high->metal_4h` score `-1.7637` n `220` status `ready` deltaP `-4.138` edge `-0.0353` maxDD `-5.725`
- `news_risk_high->commodity_4h` score `-1.9675` n `30` status `ready` deltaP `-16.1687` edge `-0.0569` maxDD `-2.3372`
- `market_context_high->index_4h` score `-1.9909` n `220` status `ready` deltaP `-0.9423` edge `0.0091` maxDD `-3.165`
- `market_context_high->equity_24h` score `-2.024` n `213` status `ready` deltaP `13.3241` edge `0.1593` maxDD `-31.2762`
- `market_context_high->fx_24h` score `-2.1374` n `213` status `ready` deltaP `0.8949` edge `0.0018` maxDD `-5.5435`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

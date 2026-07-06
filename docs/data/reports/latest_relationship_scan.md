# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-06T22:22:29.682137+00:00`
- Price records: `672`
- Market context records: `5920`
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

- `news_risk_high->fx_4h` score `3.6777` n `30` status `ready` deltaP `38.1707` edge `0.0566` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.0489` n `30` status `ready` deltaP `24.8303` edge `0.0191` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `0.8676` n `30` status `ready` deltaP `10.7884` edge `0.086` maxDD `-2.0691`
- `market_context_high->equity_4h` score `0.8522` n `221` status `ready` deltaP `7.6889` edge `0.1292` maxDD `-4.0887`
- `news_risk_high->crypto_alt_1h` score `0.1437` n `30` status `ready` deltaP `4.5709` edge `0.0341` maxDD `-1.6923`
- `market_context_high->equity_1h` score `-0.2047` n `221` status `ready` deltaP `4.9449` edge `0.0328` maxDD `-4.3608`
- `market_context_high->metal_1h` score `-0.3101` n `221` status `ready` deltaP `3.5603` edge `0.0036` maxDD `-2.0339`
- `news_risk_high->metal_1h` score `-0.4461` n `30` status `ready` deltaP `1.2375` edge `-0.0288` maxDD `-1.2643`
- `market_context_high->commodity_1h` score `-0.5421` n `221` status `ready` deltaP `-2.3458` edge `-0.0023` maxDD `-1.4578`
- `market_context_high->crypto_major_1h` score `-0.5916` n `221` status `ready` deltaP `3.5637` edge `0.0325` maxDD `-6.2348`
- `market_context_high->crypto_alt_1h` score `-0.7251` n `221` status `ready` deltaP `2.2028` edge `0.0258` maxDD `-6.6758`
- `market_context_high->fx_1h` score `-0.7512` n `221` status `ready` deltaP `-1.8967` edge `-0.0011` maxDD `-0.5751`
- `market_context_high->index_1h` score `-0.9825` n `221` status `ready` deltaP `-0.0596` edge `0.0033` maxDD `-0.7819`
- `news_risk_high->index_1h` score `-1.2167` n `30` status `ready` deltaP `-12.0958` edge `-0.0239` maxDD `-1.1161`
- `market_context_high->commodity_4h` score `-1.6834` n `221` status `ready` deltaP `-3.7786` edge `-0.0193` maxDD `-6.3734`
- `market_context_high->equity_24h` score `-1.7892` n `213` status `ready` deltaP `14.5393` edge `0.1813` maxDD `-31.2762`
- `market_context_high->metal_4h` score `-1.844` n `221` status `ready` deltaP `-4.8428` edge `-0.0409` maxDD `-5.725`
- `news_risk_high->commodity_4h` score `-2.0188` n `30` status `ready` deltaP `-16.9309` edge `-0.0584` maxDD `-2.3372`
- `market_context_high->index_4h` score `-2.0475` n `221` status `ready` deltaP `-1.4989` edge `0.0081` maxDD `-3.165`
- `market_context_high->fx_24h` score `-2.1429` n `213` status `ready` deltaP `0.8949` edge `0.0011` maxDD `-5.5435`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

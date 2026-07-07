# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-07T00:52:25.743607+00:00`
- Price records: `672`
- Market context records: `5931`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11237`

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

- `news_risk_high->fx_4h` score `3.6265` n `30` status `ready` deltaP `37.561` edge `0.0564` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.1016` n `30` status `ready` deltaP `25.4291` edge `0.0195` maxDD `-0.1113`
- `market_context_high->equity_4h` score `1.0734` n `221` status `ready` deltaP `8.9084` edge `0.1395` maxDD `-4.0887`
- `news_risk_high->crypto_major_1h` score `0.827` n `30` status `ready` deltaP `10.489` edge `0.0828` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.1359` n `30` status `ready` deltaP `4.7206` edge `0.0321` maxDD `-1.6923`
- `market_context_high->equity_1h` score `-0.1564` n `221` status `ready` deltaP `5.5437` edge `0.035` maxDD `-4.3608`
- `market_context_high->metal_1h` score `-0.3218` n `221` status `ready` deltaP `3.71` edge `0.0011` maxDD `-2.0339`
- `news_risk_high->metal_1h` score `-0.4578` n `30` status `ready` deltaP `1.3872` edge `-0.0313` maxDD `-1.2643`
- `market_context_high->commodity_1h` score `-0.5833` n `221` status `ready` deltaP `-3.0943` edge `-0.0026` maxDD `-1.4578`
- `market_context_high->crypto_major_1h` score `-0.6321` n `221` status `ready` deltaP `3.2643` edge `0.0293` maxDD `-6.2348`
- `market_context_high->fx_1h` score `-0.6985` n `221` status `ready` deltaP `-1.2979` edge `-0.0007` maxDD `-0.5751`
- `market_context_high->crypto_alt_1h` score `-0.7329` n `221` status `ready` deltaP `2.3525` edge `0.0238` maxDD `-6.6758`
- `market_context_high->index_1h` score `-0.9261` n `221` status `ready` deltaP `0.5392` edge `0.004` maxDD `-0.7819`
- `news_risk_high->index_1h` score `-1.1801` n `30` status `ready` deltaP `-11.497` edge `-0.0232` maxDD `-1.1161`
- `market_context_high->equity_24h` score `-1.3729` n `213` status `ready` deltaP `16.2754` edge `0.2231` maxDD `-31.2762`
- `market_context_high->commodity_4h` score `-1.7103` n `221` status `ready` deltaP `-4.2359` edge `-0.0197` maxDD `-6.3734`
- `market_context_high->metal_4h` score `-1.8602` n `221` status `ready` deltaP `-4.5379` edge `-0.045` maxDD `-5.725`
- `market_context_high->index_4h` score `-1.9175` n `221` status `ready` deltaP `-0.2794` edge `0.0108` maxDD `-3.165`
- `news_risk_high->commodity_4h` score `-2.0457` n `30` status `ready` deltaP `-17.3882` edge `-0.0588` maxDD `-2.3372`
- `market_context_high->fx_24h` score `-2.1437` n `213` status `ready` deltaP `0.8949` edge `0.001` maxDD `-5.5435`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

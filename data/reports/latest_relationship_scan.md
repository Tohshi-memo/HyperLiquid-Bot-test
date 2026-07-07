# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-07T00:22:25.955364+00:00`
- Price records: `672`
- Market context records: `5929`
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

- `news_risk_high->fx_4h` score `3.6533` n `30` status `ready` deltaP `37.8659` edge `0.0566` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.1016` n `30` status `ready` deltaP `25.4291` edge `0.0195` maxDD `-0.1113`
- `market_context_high->equity_4h` score `0.9866` n `221` status `ready` deltaP `8.6035` edge `0.1343` maxDD `-4.0887`
- `news_risk_high->crypto_major_1h` score `0.8403` n `30` status `ready` deltaP `10.6387` edge `0.0835` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.139` n `30` status `ready` deltaP `4.7206` edge `0.0325` maxDD `-1.6923`
- `market_context_high->equity_1h` score `-0.1845` n `221` status `ready` deltaP `5.2443` edge `0.0334` maxDD `-4.3608`
- `market_context_high->metal_1h` score `-0.3202` n `221` status `ready` deltaP `3.71` edge `0.0013` maxDD `-2.0339`
- `news_risk_high->metal_1h` score `-0.4562` n `30` status `ready` deltaP `1.3872` edge `-0.0311` maxDD `-1.2643`
- `market_context_high->commodity_1h` score `-0.5833` n `221` status `ready` deltaP `-3.0943` edge `-0.0026` maxDD `-1.4578`
- `market_context_high->crypto_major_1h` score `-0.6189` n `221` status `ready` deltaP `3.414` edge `0.03` maxDD `-6.2348`
- `market_context_high->fx_1h` score `-0.6985` n `221` status `ready` deltaP `-1.2979` edge `-0.0007` maxDD `-0.5751`
- `market_context_high->crypto_alt_1h` score `-0.7298` n `221` status `ready` deltaP `2.3525` edge `0.0242` maxDD `-6.6758`
- `market_context_high->index_1h` score `-0.9573` n `221` status `ready` deltaP `0.2398` edge `0.0034` maxDD `-0.7819`
- `news_risk_high->index_1h` score `-1.2004` n `30` status `ready` deltaP `-11.7964` edge `-0.0238` maxDD `-1.1161`
- `market_context_high->equity_24h` score `-1.4682` n `213` status `ready` deltaP `15.9282` edge `0.2132` maxDD `-31.2762`
- `market_context_high->commodity_4h` score `-1.7008` n `221` status `ready` deltaP `-4.0834` edge `-0.0195` maxDD `-6.3734`
- `market_context_high->metal_4h` score `-1.8815` n `221` status `ready` deltaP `-4.8428` edge `-0.0457` maxDD `-5.725`
- `market_context_high->index_4h` score `-1.9599` n `221` status `ready` deltaP `-0.5843` edge `0.0093` maxDD `-3.165`
- `news_risk_high->commodity_4h` score `-2.0362` n `30` status `ready` deltaP `-17.2357` edge `-0.0586` maxDD `-2.3372`
- `market_context_high->fx_24h` score `-2.1444` n `213` status `ready` deltaP `0.8949` edge `0.0009` maxDD `-5.5435`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

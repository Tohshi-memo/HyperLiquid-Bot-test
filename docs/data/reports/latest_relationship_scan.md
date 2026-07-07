# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-07T01:52:25.119721+00:00`
- Price records: `672`
- Market context records: `5935`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11219`

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

- `news_risk_high->fx_4h` score `3.5997` n `30` status `ready` deltaP `37.2561` edge `0.0562` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.1016` n `30` status `ready` deltaP `25.4291` edge `0.0195` maxDD `-0.1113`
- `market_context_high->equity_4h` score `1.2542` n `221` status `ready` deltaP `9.5182` edge `0.1505` maxDD `-4.0887`
- `news_risk_high->crypto_major_1h` score `0.8473` n `30` status `ready` deltaP `10.6387` edge `0.0844` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.1764` n `30` status `ready` deltaP `5.02` edge `0.0353` maxDD `-1.6923`
- `market_context_high->equity_1h` score `-0.0933` n `221` status `ready` deltaP `6.1425` edge `0.0391` maxDD `-4.3608`
- `market_context_high->metal_1h` score `-0.3054` n `221` status `ready` deltaP `3.8597` edge `0.0022` maxDD `-2.0339`
- `news_risk_high->metal_1h` score `-0.4414` n `30` status `ready` deltaP `1.5369` edge `-0.0302` maxDD `-1.2643`
- `market_context_high->commodity_1h` score `-0.5576` n `221` status `ready` deltaP `-2.6452` edge `-0.0023` maxDD `-1.4578`
- `market_context_high->crypto_major_1h` score `-0.6118` n `221` status `ready` deltaP `3.414` edge `0.0309` maxDD `-6.2348`
- `market_context_high->crypto_alt_1h` score `-0.6924` n `221` status `ready` deltaP `2.6519` edge `0.027` maxDD `-6.6758`
- `market_context_high->fx_1h` score `-0.6985` n `221` status `ready` deltaP `-1.2979` edge `-0.0007` maxDD `-0.5751`
- `market_context_high->index_1h` score `-0.865` n `221` status `ready` deltaP `1.138` edge `0.0051` maxDD `-0.7819`
- `news_risk_high->index_1h` score `-1.1404` n `30` status `ready` deltaP `-10.8982` edge `-0.0221` maxDD `-1.1161`
- `market_context_high->equity_24h` score `-1.2206` n `213` status `ready` deltaP `16.9699` edge `0.238` maxDD `-31.2762`
- `market_context_high->commodity_4h` score `-1.7459` n `221` status `ready` deltaP `-4.8456` edge `-0.0202` maxDD `-6.3734`
- `market_context_high->metal_4h` score `-1.8058` n `221` status `ready` deltaP `-3.9282` edge `-0.0421` maxDD `-5.725`
- `market_context_high->index_4h` score `-1.8315` n `221` status `ready` deltaP `0.3304` edge `0.0139` maxDD `-3.165`
- `news_risk_high->commodity_4h` score `-2.0813` n `30` status `ready` deltaP `-17.9979` edge `-0.0593` maxDD `-2.3372`
- `news_risk_high->index_4h` score `-2.1241` n `30` status `ready` deltaP `-14.4207` edge `-0.0728` maxDD `-2.9371`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

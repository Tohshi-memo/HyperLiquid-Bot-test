# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-06T04:07:32.332835+00:00`
- Price records: `672`
- Market context records: `5843`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `10128`

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

- `news_risk_high->fx_1h` score `1.9387` n `30` status `ready` deltaP `23.483` edge `0.0189` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `0.816` n `30` status `ready` deltaP `11.2375` edge `0.0764` maxDD `-2.0691`
- `market_context_high->equity_4h` score `0.7502` n `261` status `ready` deltaP `7.8293` edge `0.1561` maxDD `-6.9958`
- `news_risk_high->crypto_alt_1h` score `0.1686` n `30` status `ready` deltaP `4.5709` edge `0.0373` maxDD `-1.6923`
- `market_context_high->fx_1h` score `-0.3226` n `261` status `ready` deltaP `1.1076` edge `-0.0002` maxDD `-0.5499`
- `market_context_high->equity_1h` score `-0.3453` n `261` status `ready` deltaP `4.6677` edge `0.0408` maxDD `-5.0555`
- `news_risk_high->metal_1h` score `-0.4274` n `30` status `ready` deltaP `1.3872` edge `-0.0274` maxDD `-1.2643`
- `market_context_high->metal_1h` score `-0.5014` n `261` status `ready` deltaP `3.2263` edge `0.0038` maxDD `-2.0339`
- `market_context_high->commodity_1h` score `-0.514` n `261` status `ready` deltaP `-0.6458` edge `-0.0015` maxDD `-2.1412`
- `market_context_high->index_1h` score `-0.5282` n `261` status `ready` deltaP `1.6278` edge `0.0062` maxDD `-0.7819`
- `market_context_high->equity_24h` score `-0.6584` n `233` status `ready` deltaP `16.4744` edge `0.3432` maxDD `-31.6316`
- `market_context_high->crypto_major_1h` score `-0.8104` n `261` status `ready` deltaP `3.4598` edge `0.0415` maxDD `-6.2348`
- `market_context_high->crypto_alt_1h` score `-1.026` n `261` status `ready` deltaP `1.9272` edge `0.0351` maxDD `-6.6758`
- `market_context_high->index_4h` score `-1.1747` n `261` status `ready` deltaP `0.5291` edge `0.0146` maxDD `-3.165`
- `news_risk_high->index_1h` score `-1.2354` n `30` status `ready` deltaP `-12.3952` edge `-0.0243` maxDD `-1.1161`
- `market_context_high->fx_4h` score `-1.7007` n `261` status `ready` deltaP `-3.1703` edge `-0.002` maxDD `-2.2593`
- `market_context_high->fx_24h` score `-1.736` n `233` status `ready` deltaP `6.0935` edge `0.0186` maxDD `-5.5435`
- `market_context_high->metal_4h` score `-2.1004` n `261` status `ready` deltaP `-4.2169` edge `-0.0408` maxDD `-8.6964`
- `market_context_high->commodity_4h` score `-2.361` n `261` status `ready` deltaP `-0.1747` edge `-0.0131` maxDD `-7.2653`
- `market_context_high->crypto_major_4h` score `-2.8875` n `261` status `ready` deltaP `7.2774` edge `0.1481` maxDD `-25.6458`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

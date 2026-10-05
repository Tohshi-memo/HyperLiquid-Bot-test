# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-05T01:22:27.573968+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5392`

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

- `market_context_high->unknown_1h` score `103.9337` n `96` status `ready` deltaP `-0.0436` edge `8.7029` maxDD `-0.9839`
- `market_context_high->unknown_4h` score `82.9762` n `96` status `ready` deltaP `2.6168` edge `6.9284` maxDD `-0.4928`
- `news_risk_high->crypto_major_4h` score `9.6022` n `65` status `ready` deltaP `33.4662` edge `0.5974` maxDD `-0.6258`
- `market_context_high->crypto_major_24h` score `9.2627` n `50` status `ready` deltaP `28.8056` edge `0.6169` maxDD `-2.2971`
- `market_context_high->crypto_alt_24h` score `8.5113` n `50` status `ready` deltaP `23.0625` edge `0.6322` maxDD `-4.1339`
- `news_risk_high->crypto_alt_4h` score `6.5912` n `65` status `ready` deltaP `21.311` edge `0.5416` maxDD `-6.4195`
- `news_risk_high->equity_24h` score `4.9332` n `65` status `ready` deltaP `16.9365` edge `0.3082` maxDD `-0.1344`
- `market_context_high->crypto_major_4h` score `4.202` n `96` status `ready` deltaP `18.2418` edge `0.2989` maxDD `-3.294`
- `news_risk_high->index_24h` score `3.519` n `65` status `ready` deltaP `24.6528` edge `0.1289` maxDD `0.0`
- `news_risk_high->equity_4h` score `2.9942` n `65` status `ready` deltaP `21.9489` edge `0.1642` maxDD `-2.881`
- `news_risk_high->index_4h` score `2.9594` n `65` status `ready` deltaP `32.5235` edge `0.056` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.6379` n `65` status `ready` deltaP `10.9143` edge `0.1826` maxDD `-1.5096`
- `news_risk_high->metal_4h` score `2.1609` n `65` status `ready` deltaP `19.6881` edge `0.0904` maxDD `-0.993`
- `news_risk_high->index_1h` score `2.1105` n `65` status `ready` deltaP `26.0663` edge `0.0171` maxDD `-0.1997`
- `market_context_high->crypto_major_1h` score `2.0962` n `96` status `ready` deltaP `14.5522` edge `0.1227` maxDD `-2.2692`
- `market_context_high->fx_4h` score `1.4549` n `96` status `ready` deltaP `25.3811` edge `0.0277` maxDD `-0.3868`
- `news_risk_high->crypto_alt_1h` score `1.4371` n `65` status `ready` deltaP `4.719` edge `0.1402` maxDD `-2.4854`
- `market_context_high->fx_24h` score `1.432` n `50` status `ready` deltaP `26.6667` edge `0.1028` maxDD `-1.7589`
- `market_context_high->crypto_alt_4h` score `1.0787` n `96` status `ready` deltaP `3.811` edge `0.2434` maxDD `-7.6465`
- `market_context_high->fx_1h` score `0.9704` n `96` status `ready` deltaP `15.0574` edge `0.0069` maxDD `-0.113`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-04T07:07:24.491172+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5004`

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

- `market_context_high->unknown_4h` score `249.8279` n `58` status `ready` deltaP `7.4327` edge `20.7838` maxDD `-0.4822`
- `market_context_high->unknown_1h` score `194.5884` n `70` status `ready` deltaP `1.5826` edge `16.2466` maxDD `-0.983`
- `market_context_high->crypto_alt_24h` score `14.3397` n `46` status `ready` deltaP `32.0812` edge `1.1084` maxDD `-8.1838`
- `market_context_high->crypto_major_24h` score `13.0943` n `46` status `ready` deltaP `38.5238` edge `0.8996` maxDD `-4.5519`
- `news_risk_high->equity_24h` score `11.2175` n `59` status `ready` deltaP `28.9222` edge `0.752` maxDD `-0.1353`
- `news_risk_high->crypto_major_4h` score `11.1108` n `65` status `ready` deltaP `40.1736` edge `0.6784` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `7.5662` n `65` status `ready` deltaP `24.6646` edge `0.6005` maxDD `-6.4195`
- `market_context_high->crypto_major_4h` score `6.2131` n `58` status `ready` deltaP `20.2797` edge `0.4529` maxDD `-3.294`
- `news_risk_high->index_24h` score `4.7966` n `59` status `ready` deltaP `32.5823` edge `0.1825` maxDD `0.0`
- `market_context_high->equity_24h` score `4.2434` n `46` status `ready` deltaP `9.6149` edge `0.3892` maxDD `-6.3081`
- `news_risk_high->equity_4h` score `3.9397` n `65` status `ready` deltaP `27.1318` edge `0.2087` maxDD `-2.9013`
- `market_context_high->crypto_alt_4h` score `3.3902` n `58` status `ready` deltaP `18.8025` edge `0.4382` maxDD `-7.6465`
- `news_risk_high->index_4h` score `3.1696` n `65` status `ready` deltaP `34.5052` edge `0.0603` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.9903` n `65` status `ready` deltaP `13.1598` edge `0.197` maxDD `-1.5096`
- `market_context_high->crypto_major_1h` score `2.6525` n `70` status `ready` deltaP `17.006` edge `0.1527` maxDD `-2.2692`
- `news_risk_high->metal_4h` score `2.578` n `65` status `ready` deltaP `22.1271` edge `0.1089` maxDD `-0.993`
- `news_risk_high->index_1h` score `2.1453` n `65` status `ready` deltaP `26.3657` edge `0.018` maxDD `-0.1997`
- `market_context_high->crypto_alt_1h` score `2.1249` n `70` status `ready` deltaP `12.1215` edge `0.1709` maxDD `-3.6376`
- `market_context_high->fx_4h` score `1.7492` n `58` status `ready` deltaP `22.4349` edge `0.0324` maxDD `-0.229`
- `news_risk_high->crypto_alt_1h` score `1.5583` n `65` status `ready` deltaP `4.8687` edge `0.1493` maxDD `-2.4854`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

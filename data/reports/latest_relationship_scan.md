# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-17T20:07:33.459196+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4041`

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

- `market_context_high->unknown_24h` score `1491.0126` n `98` status `ready` deltaP `3.4722` edge `124.2279` maxDD `0.0`
- `news_risk_high->equity_24h` score `55.5396` n `37` status `ready` deltaP `66.7699` edge `4.2538` maxDD `-3.6503`
- `news_risk_high->equity_4h` score `20.1292` n `37` status `ready` deltaP `55.6402` edge `1.3065` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `16.0844` n `37` status `ready` deltaP `31.1609` edge `1.9687` maxDD `-6.8139`
- `market_context_high->crypto_major_24h` score `15.3909` n `98` status `ready` deltaP `46.1912` edge `1.9923` maxDD `-22.8301`
- `market_context_high->crypto_alt_24h` score `14.5713` n `98` status `ready` deltaP `32.4263` edge `1.8643` maxDD `-13.3222`
- `news_risk_high->index_24h` score `9.0026` n `37` status `ready` deltaP `58.0894` edge `0.3933` maxDD `-0.4279`
- `news_risk_high->commodity_24h` score `7.8617` n `37` status `ready` deltaP `54.8611` edge `0.2894` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `7.488` n `37` status `ready` deltaP `31.0523` edge `0.4937` maxDD `-4.137`
- `news_risk_high->metal_4h` score `6.785` n `37` status `ready` deltaP `55.529` edge `0.1997` maxDD `-0.0246`
- `news_risk_high->crypto_alt_24h` score `5.8549` n `37` status `ready` deltaP `12.7627` edge `1.1161` maxDD `-29.0448`
- `news_risk_high->equity_1h` score `5.6532` n `37` status `ready` deltaP `25.8173` edge `0.3208` maxDD `-0.4122`
- `news_risk_high->crypto_major_4h` score `5.3876` n `37` status `ready` deltaP `22.9442` edge `0.3387` maxDD `-1.7491`
- `news_risk_high->index_4h` score `4.3545` n `37` status `ready` deltaP `37.5536` edge `0.135` maxDD `-0.1319`
- `news_risk_high->metal_1h` score `2.6265` n `37` status `ready` deltaP `28.0709` edge `0.0535` maxDD `-0.0743`
- `news_risk_high->commodity_4h` score `2.5686` n `37` status `ready` deltaP `27.8098` edge `0.054` maxDD `-0.3611`
- `news_risk_high->crypto_major_1h` score `2.4988` n `37` status `ready` deltaP `16.811` edge `0.1313` maxDD `-1.4777`
- `news_risk_high->crypto_alt_1h` score `2.3459` n `37` status `ready` deltaP `18.0086` edge `0.1281` maxDD `-2.5469`
- `news_risk_high->index_1h` score `1.9959` n `37` status `ready` deltaP `23.414` edge `0.032` maxDD `-0.0751`
- `news_risk_high->commodity_1h` score `-0.0277` n `37` status `ready` deltaP `1.0438` edge `0.0242` maxDD `-0.3438`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

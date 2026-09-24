# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-24T03:22:33.051934+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9858`

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

- `market_context_high->unknown_1h` score `72.0282` n `47` status `ready` deltaP `10.5651` edge `5.939` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `37.0961` n `46` status `ready` deltaP `24.4716` edge `2.9438` maxDD `-0.5817`
- `market_context_high->crypto_alt_24h` score `21.5584` n `46` status `ready` deltaP `19.4444` edge `1.6669` maxDD `0.0`
- `market_context_high->equity_24h` score `21.5079` n `46` status `ready` deltaP `21.8675` edge `1.6566` maxDD `-0.1382`
- `market_context_high->index_24h` score `7.2151` n `46` status `ready` deltaP `30.8953` edge `0.404` maxDD `-0.03`
- `news_risk_high->crypto_alt_4h` score `4.9743` n `103` status `ready` deltaP `14.6889` edge `0.4164` maxDD `-5.9838`
- `news_risk_high->crypto_major_4h` score `4.6612` n `103` status `ready` deltaP `17.8902` edge `0.3269` maxDD `-2.619`
- `news_risk_high->crypto_major_24h` score `3.3549` n `103` status `ready` deltaP `-3.2194` edge `1.2053` maxDD `-63.6743`
- `news_risk_high->crypto_alt_1h` score `2.5557` n `103` status `ready` deltaP `13.6068` edge `0.1713` maxDD `-1.5895`
- `market_context_high->index_4h` score `2.5294` n `47` status `ready` deltaP `29.758` edge `0.0278` maxDD `-0.2323`
- `news_risk_high->commodity_24h` score `2.4362` n `103` status `ready` deltaP `23.4004` edge `0.1649` maxDD `-2.431`
- `market_context_high->metal_24h` score `2.2647` n `46` status `ready` deltaP `24.8717` edge `0.0463` maxDD `-0.2042`
- `news_risk_high->crypto_major_1h` score `2.0696` n `103` status `ready` deltaP `16.002` edge `0.1093` maxDD `-1.8141`
- `news_risk_high->fx_4h` score `1.5722` n `103` status `ready` deltaP `23.0716` edge `0.0408` maxDD `-0.421`
- `market_context_high->equity_4h` score `1.5527` n `47` status `ready` deltaP `12.4189` edge `0.0884` maxDD `-1.3444`
- `news_risk_high->fx_24h` score `1.2187` n `103` status `ready` deltaP `29.6639` edge `0.1216` maxDD `-1.7159`
- `market_context_high->index_1h` score `0.8313` n `47` status `ready` deltaP `13.2628` edge `0.0087` maxDD `-0.2275`
- `news_risk_high->metal_1h` score `0.6673` n `103` status `ready` deltaP `15.502` edge `0.0116` maxDD `-0.7468`
- `market_context_high->equity_1h` score `0.649` n `47` status `ready` deltaP `9.3706` edge `0.0319` maxDD `-1.5564`
- `news_risk_high->metal_4h` score `0.3716` n `103` status `ready` deltaP `14.8798` edge `0.0442` maxDD `-1.9941`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

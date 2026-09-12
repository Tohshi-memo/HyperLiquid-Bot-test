# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-12T04:37:29.883841+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11361`

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

- `market_context_high->unknown_24h` score `977.1538` n `137` status `ready` deltaP `13.9915` edge `81.3414` maxDD `-0.082`
- `news_risk_high->unknown_1h` score `383.3569` n `82` status `ready` deltaP `-3.6038` edge `32.0126` maxDD `-1.7068`
- `risk_on_high->crypto_alt_24h` score `24.1389` n `85` status `ready` deltaP `42.7287` edge `1.7497` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `24.1389` n `85` status `ready` deltaP `42.7287` edge `1.7497` maxDD `-0.8386`
- `news_risk_high->crypto_major_24h` score `23.7893` n `58` status `ready` deltaP `54.3881` edge `1.7099` maxDD `-5.8705`
- `market_context_high->crypto_alt_24h` score `20.1897` n `137` status `ready` deltaP `36.9323` edge `1.519` maxDD `-3.9523`
- `news_risk_high->crypto_alt_24h` score `17.2277` n `58` status `ready` deltaP `29.6456` edge `1.2868` maxDD `-2.2369`
- `news_risk_high->equity_24h` score `12.0803` n `58` status `ready` deltaP `33.5309` edge `0.793` maxDD `-0.1212`
- `risk_on_high->equity_24h` score `9.0627` n `85` status `ready` deltaP `36.9792` edge `0.5087` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `9.0627` n `85` status `ready` deltaP `36.9792` edge `0.5087` maxDD `0.0`
- `market_context_high->equity_24h` score `8.7531` n `137` status `ready` deltaP `36.9792` edge `0.4829` maxDD `0.0`
- `risk_on_high->crypto_alt_4h` score `8.5202` n `85` status `ready` deltaP `43.6173` edge `0.4564` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `8.5202` n `85` status `ready` deltaP `43.6173` edge `0.4564` maxDD `-1.9733`
- `news_risk_high->metal_24h` score `8.1837` n `58` status `ready` deltaP `51.0417` edge `0.3417` maxDD `0.0`
- `news_risk_high->index_24h` score `7.9503` n `58` status `ready` deltaP `51.4128` edge `0.3291` maxDD `-0.0797`
- `risk_on_high->crypto_major_24h` score `6.7973` n `85` status `ready` deltaP `22.4612` edge `1.1285` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `6.7973` n `85` status `ready` deltaP `22.4612` edge `1.1285` maxDD `-24.5429`
- `risk_on_high->crypto_major_4h` score `6.5158` n `85` status `ready` deltaP `30.6528` edge `0.4245` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `6.5158` n `85` status `ready` deltaP `30.6528` edge `0.4245` maxDD `-3.8693`
- `risk_on_high->index_24h` score `5.2018` n `85` status `ready` deltaP `51.3317` edge `0.0955` maxDD `-0.0051`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

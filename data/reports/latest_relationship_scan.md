# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-12T08:52:26.309937+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11791`

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

- `market_context_high->unknown_24h` score `2417.8249` n `120` status `ready` deltaP `13.7847` edge `201.3987` maxDD `-0.082`
- `news_risk_high->unknown_1h` score `383.2572` n `82` status `ready` deltaP `-3.3044` edge `32.0023` maxDD `-1.7068`
- `news_risk_high->crypto_major_24h` score `24.3182` n `59` status `ready` deltaP `54.505` edge `1.7532` maxDD `-5.8705`
- `risk_on_high->crypto_alt_24h` score `22.0433` n `71` status `ready` deltaP `41.5688` edge `1.5828` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `22.0433` n `71` status `ready` deltaP `41.5688` edge `1.5828` maxDD `-0.8386`
- `market_context_high->crypto_alt_24h` score `18.4842` n `120` status `ready` deltaP `35.2778` edge `1.3879` maxDD `-3.9523`
- `news_risk_high->crypto_alt_24h` score `17.6218` n `59` status `ready` deltaP `29.967` edge `1.3175` maxDD `-2.2369`
- `news_risk_high->equity_24h` score `12.1517` n `59` status `ready` deltaP `33.763` edge `0.7974` maxDD `-0.1212`
- `risk_on_high->equity_24h` score `9.0442` n `71` status `ready` deltaP `37.1528` edge `0.506` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `9.0442` n `71` status `ready` deltaP `37.1528` edge `0.506` maxDD `0.0`
- `market_context_high->equity_24h` score `8.6998` n `120` status `ready` deltaP `37.1528` edge `0.4773` maxDD `0.0`
- `news_risk_high->metal_24h` score `8.269` n `59` status `ready` deltaP `52.2569` edge `0.3407` maxDD `0.0`
- `risk_on_high->crypto_alt_4h` score `8.0959` n `71` status `ready` deltaP `42.9942` edge `0.4252` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `8.0959` n `71` status `ready` deltaP `42.9942` edge `0.4252` maxDD `-1.9733`
- `news_risk_high->index_24h` score `7.9129` n `59` status `ready` deltaP `51.4713` edge `0.3256` maxDD `-0.0797`
- `risk_on_high->crypto_major_4h` score `5.5541` n `71` status `ready` deltaP `27.3918` edge `0.3661` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `5.5541` n `71` status `ready` deltaP `27.3918` edge `0.3661` maxDD `-3.8693`
- `risk_on_high->index_24h` score `5.0549` n `71` status `ready` deltaP `50.6357` edge `0.0879` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `5.0549` n `71` status `ready` deltaP `50.6357` edge `0.0879` maxDD `-0.0051`
- `risk_on_high->equity_4h` score `4.0508` n `71` status `ready` deltaP `37.3175` edge `0.0981` maxDD `-0.079`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

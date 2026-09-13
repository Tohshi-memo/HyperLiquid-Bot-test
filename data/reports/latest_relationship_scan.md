# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-13T17:22:34.848845+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `12966`

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

- `market_context_high->unknown_24h` score `17765.3592` n `56` status `ready` deltaP `10.2093` edge `1480.3987` maxDD `-0.613`
- `risk_on_high->unknown_24h` score `7900.8687` n `37` status `ready` deltaP `11.0298` edge `658.3387` maxDD `-0.1869`
- `risk_on_and_context->unknown_24h` score `7900.8687` n `37` status `ready` deltaP `11.0298` edge `658.3387` maxDD `-0.1869`
- `news_risk_high->unknown_1h` score `424.4307` n `82` status `ready` deltaP `-5.1008` edge `35.4454` maxDD `-1.7068`
- `news_risk_high->crypto_alt_24h` score `18.6301` n `82` status `ready` deltaP `36.0302` edge `1.3611` maxDD `-2.2369`
- `news_risk_high->crypto_major_24h` score `18.394` n `82` status `ready` deltaP `38.0236` edge `1.4264` maxDD `-9.098`
- `news_risk_high->equity_24h` score `9.0558` n `82` status `ready` deltaP `26.4088` edge `0.7566` maxDD `-6.5742`
- `news_risk_high->index_24h` score `7.0209` n `82` status `ready` deltaP `50.1808` edge `0.2682` maxDD `-0.0797`
- `news_risk_high->metal_24h` score `4.656` n `82` status `ready` deltaP `25.2776` edge `0.2649` maxDD `-0.6334`
- `risk_on_high->commodity_24h` score `4.3778` n `37` status `ready` deltaP `39.8276` edge `0.0993` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `4.3778` n `37` status `ready` deltaP `39.8276` edge `0.0993` maxDD `0.0`
- `market_context_high->commodity_24h` score `4.319` n `56` status `ready` deltaP `39.8276` edge `0.0944` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `3.0663` n `37` status `ready` deltaP `7.1575` edge `0.4724` maxDD `-6.8265`
- `risk_on_and_context->crypto_alt_24h` score `3.0663` n `37` status `ready` deltaP `7.1575` edge `0.4724` maxDD `-6.8265`
- `market_context_high->crypto_alt_24h` score `2.8491` n `56` status `ready` deltaP `6.6748` edge `0.4803` maxDD `-9.4287`
- `market_context_high->metal_24h` score `0.5476` n `56` status `ready` deltaP `7.3769` edge `0.1195` maxDD `-1.5447`
- `news_risk_high->index_4h` score `0.3958` n `82` status `ready` deltaP `12.0427` edge `0.0333` maxDD `-0.6935`
- `risk_on_high->metal_1h` score `0.2333` n `71` status `ready` deltaP `7.4745` edge `0.0031` maxDD `-0.3456`
- `risk_on_and_context->metal_1h` score `0.2333` n `71` status `ready` deltaP `7.4745` edge `0.0031` maxDD `-0.3456`
- `market_context_high->commodity_4h` score `0.1904` n `131` status `ready` deltaP `8.9358` edge `0.0069` maxDD `-0.7148`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

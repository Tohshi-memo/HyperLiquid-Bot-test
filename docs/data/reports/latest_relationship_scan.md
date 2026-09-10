# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-10T01:37:30.497532+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9978`

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

- `risk_on_high->crypto_alt_24h` score `13.8277` n `112` status `ready` deltaP `28.3482` edge `0.9863` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `13.8277` n `112` status `ready` deltaP `28.3482` edge `0.9863` maxDD `-0.8386`
- `market_context_high->crypto_alt_24h` score `8.9441` n `234` status `ready` deltaP `20.8467` edge `0.6891` maxDD `-3.9523`
- `risk_on_high->crypto_alt_4h` score `7.1431` n `112` status `ready` deltaP `36.6942` edge `0.3878` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `7.1431` n `112` status `ready` deltaP `36.6942` edge `0.3878` maxDD `-1.9733`
- `risk_on_high->crypto_major_24h` score `7.0584` n `112` status `ready` deltaP `22.9663` edge `1.1586` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `7.0584` n `112` status `ready` deltaP `22.9663` edge `1.1586` maxDD `-24.5429`
- `risk_on_high->crypto_major_4h` score `5.0206` n `112` status `ready` deltaP `26.8728` edge `0.3251` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `5.0206` n `112` status `ready` deltaP `26.8728` edge `0.3251` maxDD `-3.8693`
- `risk_on_high->index_24h` score `2.8704` n `112` status `ready` deltaP `28.745` edge `0.0518` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `2.8704` n `112` status `ready` deltaP `28.745` edge `0.0518` maxDD `-0.0051`
- `market_context_high->equity_24h` score `2.2785` n `234` status `ready` deltaP `12.3264` edge `0.1077` maxDD `0.0`
- `market_context_high->index_24h` score `2.1607` n `234` status `ready` deltaP `23.7313` edge `0.0612` maxDD `-0.1483`
- `risk_on_high->equity_24h` score `1.4145` n `112` status `ready` deltaP `12.3264` edge `0.0357` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `1.4145` n `112` status `ready` deltaP `12.3264` edge `0.0357` maxDD `0.0`
- `risk_on_high->crypto_alt_1h` score `1.1665` n `112` status `ready` deltaP `4.5819` edge `0.1019` maxDD `-1.1521`
- `risk_on_and_context->crypto_alt_1h` score `1.1665` n `112` status `ready` deltaP `4.5819` edge `0.1019` maxDD `-1.1521`
- `risk_on_high->metal_24h` score `0.5632` n `112` status `ready` deltaP `18.4028` edge `0.0651` maxDD `-0.9131`
- `risk_on_and_context->metal_24h` score `0.5632` n `112` status `ready` deltaP `18.4028` edge `0.0651` maxDD `-0.9131`
- `risk_on_high->equity_1h` score `0.5271` n `112` status `ready` deltaP `14.9808` edge `-0.0028` maxDD `-2.2516`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

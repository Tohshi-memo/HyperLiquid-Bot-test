# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-10T18:52:31.243999+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `12090`

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

- `risk_on_high->crypto_alt_24h` score `19.7708` n `91` status `ready` deltaP `36.1722` edge `1.4294` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `19.7708` n `91` status `ready` deltaP `36.1722` edge `1.4294` maxDD `-0.8386`
- `market_context_high->crypto_alt_24h` score `15.1821` n `201` status `ready` deltaP `27.7364` edge `1.163` maxDD `-3.9523`
- `risk_on_high->crypto_alt_4h` score `9.1704` n `91` status `ready` deltaP `43.1654` edge `0.5136` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `9.1704` n `91` status `ready` deltaP `43.1654` edge `0.5136` maxDD `-1.9733`
- `risk_on_high->crypto_major_4h` score `7.8713` n `91` status `ready` deltaP `33.421` edge `0.519` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `7.8713` n `91` status `ready` deltaP `33.421` edge `0.519` maxDD `-3.8693`
- `risk_on_high->crypto_major_24h` score `7.2245` n `91` status `ready` deltaP `25.021` edge `1.1662` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `7.2245` n `91` status `ready` deltaP `25.021` edge `1.1662` maxDD `-24.5429`
- `market_context_high->equity_24h` score `5.8564` n `201` status `ready` deltaP `24.3056` edge `0.326` maxDD `0.0`
- `risk_on_high->equity_24h` score `4.2628` n `91` status `ready` deltaP `24.3056` edge `0.1932` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `4.2628` n `91` status `ready` deltaP `24.3056` edge `0.1932` maxDD `0.0`
- `risk_on_high->index_24h` score `4.0961` n `91` status `ready` deltaP `40.1061` edge `0.0782` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `4.0961` n `91` status `ready` deltaP `40.1061` edge `0.0782` maxDD `-0.0051`
- `market_context_high->index_24h` score `3.2244` n `201` status `ready` deltaP `34.4476` edge `0.0784` maxDD `-0.1483`
- `risk_on_high->equity_4h` score `2.9748` n `91` status `ready` deltaP `29.8395` edge `0.0583` maxDD `-0.0796`
- `risk_on_and_context->equity_4h` score `2.9748` n `91` status `ready` deltaP `29.8395` edge `0.0583` maxDD `-0.0796`
- `market_context_high->equity_4h` score `1.8492` n `201` status `ready` deltaP `23.0001` edge `0.0863` maxDD `-2.843`
- `risk_on_high->crypto_alt_1h` score `1.5585` n `91` status `ready` deltaP `6.4964` edge `0.1218` maxDD `-1.1521`
- `risk_on_and_context->crypto_alt_1h` score `1.5585` n `91` status `ready` deltaP `6.4964` edge `0.1218` maxDD `-1.1521`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

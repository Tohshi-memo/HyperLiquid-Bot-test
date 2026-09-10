# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-10T20:52:36.029704+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `11770`

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

- `risk_on_high->crypto_alt_24h` score `20.0792` n `91` status `ready` deltaP `36.1722` edge `1.4551` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `20.0792` n `91` status `ready` deltaP `36.1722` edge `1.4551` maxDD `-0.8386`
- `market_context_high->crypto_alt_24h` score `15.4905` n `201` status `ready` deltaP `27.7364` edge `1.1887` maxDD `-3.9523`
- `risk_on_high->crypto_alt_4h` score `9.0075` n `91` status `ready` deltaP `42.4032` edge `0.5051` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `9.0075` n `91` status `ready` deltaP `42.4032` edge `0.5051` maxDD `-1.9733`
- `risk_on_high->crypto_major_4h` score `7.7095` n `91` status `ready` deltaP `32.6588` edge `0.5106` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `7.7095` n `91` status `ready` deltaP `32.6588` edge `0.5106` maxDD `-3.8693`
- `risk_on_high->crypto_major_24h` score `7.2549` n `91` status `ready` deltaP `25.021` edge `1.1701` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `7.2549` n `91` status `ready` deltaP `25.021` edge `1.1701` maxDD `-24.5429`
- `market_context_high->equity_24h` score `6.5616` n `201` status `ready` deltaP `25.6944` edge `0.3755` maxDD `0.0`
- `risk_on_high->equity_24h` score `4.9656` n `91` status `ready` deltaP `25.6944` edge `0.2425` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `4.9656` n `91` status `ready` deltaP `25.6944` edge `0.2425` maxDD `0.0`
- `risk_on_high->index_24h` score `4.2936` n `91` status `ready` deltaP `41.495` edge `0.0854` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `4.2936` n `91` status `ready` deltaP `41.495` edge `0.0854` maxDD `-0.0051`
- `market_context_high->index_24h` score `3.4219` n `201` status `ready` deltaP `35.8365` edge `0.0856` maxDD `-0.1483`
- `risk_on_high->equity_4h` score `3.1221` n `91` status `ready` deltaP `30.4493` edge `0.0665` maxDD `-0.079`
- `risk_on_and_context->equity_4h` score `3.1221` n `91` status `ready` deltaP `30.4493` edge `0.0665` maxDD `-0.079`
- `market_context_high->equity_4h` score `1.9975` n `201` status `ready` deltaP `23.6099` edge `0.0946` maxDD `-2.843`
- `risk_on_high->equity_1h` score `1.5196` n `91` status `ready` deltaP `20.1356` edge `0.0202` maxDD `-0.2246`
- `risk_on_and_context->equity_1h` score `1.5196` n `91` status `ready` deltaP `20.1356` edge `0.0202` maxDD `-0.2246`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

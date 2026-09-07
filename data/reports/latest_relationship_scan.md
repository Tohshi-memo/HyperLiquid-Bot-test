# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-07T18:37:24.964735+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10225`

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

- `risk_on_high->unknown_24h` score `187.418` n `106` status `ready` deltaP `22.5694` edge `15.4677` maxDD `0.0`
- `risk_on_and_context->unknown_24h` score `187.418` n `106` status `ready` deltaP `22.5694` edge `15.4677` maxDD `0.0`
- `risk_on_high->crypto_major_24h` score `14.9459` n `106` status `ready` deltaP `28.5509` edge `1.265` maxDD `-12.4546`
- `risk_on_and_context->crypto_major_24h` score `14.9459` n `106` status `ready` deltaP `28.5509` edge `1.265` maxDD `-12.4546`
- `risk_on_high->crypto_alt_24h` score `12.2898` n `106` status `ready` deltaP `30.0576` edge `0.8299` maxDD `-0.1572`
- `risk_on_and_context->crypto_alt_24h` score `12.2898` n `106` status `ready` deltaP `30.0576` edge `0.8299` maxDD `-0.1572`
- `market_context_high->crypto_alt_24h` score `7.2062` n `218` status `ready` deltaP `23.6875` edge `0.5001` maxDD `-2.5998`
- `risk_on_high->crypto_alt_4h` score `5.7534` n `117` status `ready` deltaP `30.4826` edge `0.3134` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `5.7534` n `117` status `ready` deltaP `30.4826` edge `0.3134` maxDD `-1.9733`
- `risk_on_high->crypto_major_4h` score `5.0621` n `117` status `ready` deltaP `26.8957` edge `0.3284` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `5.0621` n `117` status `ready` deltaP `26.8957` edge `0.3284` maxDD `-3.8693`
- `market_context_high->equity_24h` score `3.9992` n `218` status `ready` deltaP `15.625` edge `0.2291` maxDD `0.0`
- `risk_on_high->equity_24h` score `3.2132` n `106` status `ready` deltaP `15.625` edge `0.1636` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `3.2132` n `106` status `ready` deltaP `15.625` edge `0.1636` maxDD `0.0`
- `risk_on_high->index_24h` score `1.9447` n `106` status `ready` deltaP `17.3087` edge `0.0509` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `1.9447` n `106` status `ready` deltaP `17.3087` edge `0.0509` maxDD `-0.0051`
- `market_context_high->index_24h` score `1.1995` n `218` status `ready` deltaP `11.882` edge `0.0601` maxDD `-0.1483`
- `risk_on_high->crypto_alt_1h` score `1.01` n `117` status `ready` deltaP `4.6958` edge `0.0881` maxDD `-1.1521`
- `risk_on_and_context->crypto_alt_1h` score `1.01` n `117` status `ready` deltaP `4.6958` edge `0.0881` maxDD `-1.1521`
- `risk_on_high->metal_24h` score `0.5065` n `106` status `ready` deltaP `16.1884` edge `0.0726` maxDD `-0.9131`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

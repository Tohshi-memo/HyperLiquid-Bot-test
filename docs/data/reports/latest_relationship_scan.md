# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-07T17:52:25.905104+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10463`

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

- `risk_on_high->unknown_24h` score `240.8913` n `103` status `ready` deltaP `22.9167` edge `19.9215` maxDD `0.0`
- `risk_on_and_context->unknown_24h` score `240.8913` n `103` status `ready` deltaP `22.9167` edge `19.9215` maxDD `0.0`
- `risk_on_high->crypto_major_24h` score `16.8692` n `103` status `ready` deltaP `30.859` edge `1.3576` maxDD `-9.2714`
- `risk_on_and_context->crypto_major_24h` score `16.8692` n `103` status `ready` deltaP `30.859` edge `1.3576` maxDD `-9.2714`
- `risk_on_high->crypto_alt_24h` score `13.0701` n `103` status `ready` deltaP `31.3208` edge `0.8865` maxDD `-0.1572`
- `risk_on_and_context->crypto_alt_24h` score `13.0701` n `103` status `ready` deltaP `31.3208` edge `0.8865` maxDD `-0.1572`
- `market_context_high->crypto_alt_24h` score `7.562` n `215` status `ready` deltaP `24.3847` edge `0.5251` maxDD `-2.5998`
- `risk_on_high->crypto_alt_4h` score `5.7052` n `117` status `ready` deltaP `30.3302` edge `0.3104` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `5.7052` n `117` status `ready` deltaP `30.3302` edge `0.3104` maxDD `-1.9733`
- `risk_on_high->crypto_major_4h` score `5.0331` n `117` status `ready` deltaP `26.7433` edge `0.327` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `5.0331` n `117` status `ready` deltaP `26.7433` edge `0.327` maxDD `-3.8693`
- `market_context_high->equity_24h` score `4.2209` n `215` status `ready` deltaP `16.1458` edge `0.2441` maxDD `0.0`
- `risk_on_high->equity_24h` score `3.4649` n `103` status `ready` deltaP `16.1458` edge `0.1811` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `3.4649` n `103` status `ready` deltaP `16.1458` edge `0.1811` maxDD `0.0`
- `risk_on_high->index_24h` score `2.0122` n `103` status `ready` deltaP `17.7471` edge `0.0536` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `2.0122` n `103` status `ready` deltaP `17.7471` edge `0.0536` maxDD `-0.0051`
- `market_context_high->index_24h` score `1.2608` n `215` status `ready` deltaP `12.2876` edge `0.0625` maxDD `-0.1483`
- `risk_on_high->crypto_alt_1h` score `1.0028` n `117` status `ready` deltaP `4.6958` edge `0.0875` maxDD `-1.1521`
- `risk_on_and_context->crypto_alt_1h` score `1.0028` n `117` status `ready` deltaP `4.6958` edge `0.0875` maxDD `-1.1521`
- `risk_on_high->metal_24h` score `0.6288` n `103` status `ready` deltaP `17.3695` edge `0.0804` maxDD `-0.9131`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

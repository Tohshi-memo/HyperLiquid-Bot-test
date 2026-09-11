# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-11T18:52:32.680806+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11845`

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

- `news_risk_high->unknown_1h` score `582.6004` n `67` status `ready` deltaP `-4.5603` edge `48.6226` maxDD `-1.7068`
- `risk_on_high->crypto_alt_24h` score `23.5694` n `91` status `ready` deltaP `42.0749` edge `1.7066` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `23.5694` n `91` status `ready` deltaP `42.0749` edge `1.7066` maxDD `-0.8386`
- `market_context_high->crypto_alt_24h` score `20.6598` n `151` status `ready` deltaP `36.9734` edge `1.5579` maxDD `-3.9523`
- `risk_on_high->equity_24h` score `9.5487` n `91` status `ready` deltaP `36.9792` edge `0.5492` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `9.5487` n `91` status `ready` deltaP `36.9792` edge `0.5492` maxDD `0.0`
- `market_context_high->equity_24h` score `9.2595` n `151` status `ready` deltaP `36.9792` edge `0.5251` maxDD `0.0`
- `risk_on_high->crypto_alt_4h` score `8.1173` n `91` status `ready` deltaP `40.7264` edge `0.4421` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `8.1173` n `91` status `ready` deltaP `40.7264` edge `0.4421` maxDD `-1.9733`
- `risk_on_high->crypto_major_24h` score `7.4008` n `91` status `ready` deltaP `25.021` edge `1.1888` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `7.4008` n `91` status `ready` deltaP `25.021` edge `1.1888` maxDD `-24.5429`
- `risk_on_high->crypto_major_4h` score `6.3628` n `91` status `ready` deltaP `30.5247` edge `0.4126` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `6.3628` n `91` status `ready` deltaP `30.5247` edge `0.4126` maxDD `-3.8693`
- `risk_on_high->index_24h` score `5.4544` n `91` status `ready` deltaP `51.5644` edge `0.115` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `5.4544` n `91` status `ready` deltaP `51.5644` edge `0.115` maxDD `-0.0051`
- `market_context_high->index_24h` score `4.2808` n `151` status `ready` deltaP `43.6028` edge `0.1054` maxDD `-0.1483`
- `risk_on_high->equity_4h` score `3.6917` n `91` status `ready` deltaP `34.87` edge `0.0845` maxDD `-0.079`
- `risk_on_and_context->equity_4h` score `3.6917` n `91` status `ready` deltaP `34.87` edge `0.0845` maxDD `-0.079`
- `market_context_high->crypto_alt_4h` score `3.4849` n `151` status `ready` deltaP `23.9299` edge `0.3014` maxDD `-7.6417`
- `market_context_high->equity_4h` score `2.0416` n `151` status `ready` deltaP `27.5561` edge `0.0691` maxDD `-2.6138`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

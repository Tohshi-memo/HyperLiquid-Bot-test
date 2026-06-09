# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-09T22:52:30.072028+00:00`
- Price records: `672`
- Market context records: `3426`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13160`

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

- `risk_on_high->crypto_alt_24h` score `56.4313` n `32` status `ready` deltaP `59.7222` edge `4.3196` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `56.4313` n `32` status `ready` deltaP `59.7222` edge `4.3196` maxDD `-0.8779`
- `risk_on_high->crypto_major_24h` score `56.2209` n `32` status `ready` deltaP `58.5069` edge `4.2993` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `56.2209` n `32` status `ready` deltaP `58.5069` edge `4.2993` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `45.5393` n `32` status `ready` deltaP `56.0764` edge `3.4211` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `45.5393` n `32` status `ready` deltaP `56.0764` edge `3.4211` maxDD `0.0`
- `risk_on_high->index_24h` score `23.9399` n `32` status `ready` deltaP `51.3889` edge `1.6524` maxDD `0.0`
- `risk_on_and_context->index_24h` score `23.9399` n `32` status `ready` deltaP `51.3889` edge `1.6524` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `22.657` n `154` status `ready` deltaP `20.6394` edge `2.5464` maxDD `-56.6728`
- `market_context_high->crypto_major_24h` score `21.3434` n `154` status `ready` deltaP `24.6189` edge `2.3876` maxDD `-54.8486`
- `market_context_high->equity_24h` score `20.3205` n `154` status `ready` deltaP `33.3491` edge `2.1123` maxDD `-40.9667`
- `risk_on_high->crypto_major_4h` score `14.6842` n `32` status `ready` deltaP `26.372` edge `1.1601` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `14.6842` n `32` status `ready` deltaP `26.372` edge `1.1601` maxDD `-5.9781`
- `risk_on_high->metal_24h` score `13.311` n `32` status `ready` deltaP `28.9931` edge `0.9421` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `13.311` n `32` status `ready` deltaP `28.9931` edge `0.9421` maxDD `-0.7574`
- `market_context_high->index_24h` score `12.7472` n `154` status `ready` deltaP `36.4538` edge `1.0409` maxDD `-15.0661`
- `risk_on_high->crypto_alt_4h` score `6.3126` n `32` status `ready` deltaP `6.3262` edge `0.6683` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `6.3126` n `32` status `ready` deltaP `6.3262` edge `0.6683` maxDD `-11.7537`
- `market_context_high->metal_24h` score `4.3913` n `154` status `ready` deltaP `23.8795` edge `0.8578` maxDD `-25.9879`
- `risk_on_high->equity_4h` score `4.2594` n `32` status `ready` deltaP `16.2348` edge `0.5513` maxDD `-5.7426`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

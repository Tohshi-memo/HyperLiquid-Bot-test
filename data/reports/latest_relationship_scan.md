# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-22T16:37:41.757093+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9738`

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

- `market_context_high->unknown_4h` score `46.5018` n `46` status `ready` deltaP `7.0122` edge `3.8284` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `30.2346` n `46` status `ready` deltaP `14.2286` edge `2.4403` maxDD `-0.5817`
- `market_context_high->equity_24h` score `16.268` n `46` status `ready` deltaP `12.3189` edge `1.2836` maxDD `-0.1382`
- `market_context_high->crypto_alt_24h` score `15.3544` n `46` status `ready` deltaP `13.7153` edge `1.1881` maxDD `0.0`
- `market_context_high->index_24h` score `5.5608` n `46` status `ready` deltaP `20.1314` edge `0.3379` maxDD `-0.03`
- `news_risk_high->commodity_24h` score `3.0979` n `101` status `ready` deltaP `37.4329` edge `0.2782` maxDD `-3.4467`
- `news_risk_high->crypto_major_24h` score `2.5175` n `101` status `ready` deltaP `-11.1266` edge `0.9698` maxDD `-46.1999`
- `news_risk_high->crypto_alt_1h` score `2.0723` n `101` status `ready` deltaP `12.938` edge `0.133` maxDD `-2.058`
- `market_context_high->index_4h` score `1.8728` n `46` status `ready` deltaP `22.2494` edge `0.0211` maxDD `-0.0692`
- `news_risk_high->crypto_alt_4h` score `1.8321` n `101` status `ready` deltaP `10.3824` edge `0.2044` maxDD `-7.675`
- `news_risk_high->crypto_major_1h` score `1.3494` n `101` status `ready` deltaP `14.1356` edge `0.0705` maxDD `-2.8494`
- `news_risk_high->crypto_major_4h` score `1.1957` n `101` status `ready` deltaP `13.2788` edge `0.1369` maxDD `-8.0625`
- `market_context_high->metal_24h` score `1.1773` n `46` status `ready` deltaP `23.3092` edge `-0.0339` maxDD `-0.2042`
- `news_risk_high->fx_4h` score `1.1318` n `101` status `ready` deltaP `18.0919` edge `0.0373` maxDD `-0.421`
- `market_context_high->equity_1h` score `0.8556` n `46` status `ready` deltaP `7.5111` edge `0.0455` maxDD `-0.2751`
- `market_context_high->equity_4h` score `0.6944` n `46` status `ready` deltaP `6.0048` edge `0.0485` maxDD `-0.4529`
- `market_context_high->index_1h` score `0.671` n `46` status `ready` deltaP `10.6548` edge `0.0102` maxDD `-0.0249`
- `news_risk_high->metal_1h` score `0.67` n `101` status `ready` deltaP `15.3465` edge `0.0137` maxDD `-0.8144`
- `news_risk_high->metal_24h` score `0.5661` n `101` status `ready` deltaP `19.4994` edge `0.027` maxDD `-2.4203`
- `news_risk_high->fx_24h` score `0.4124` n `101` status `ready` deltaP `18.7672` edge `0.0867` maxDD `-1.7159`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

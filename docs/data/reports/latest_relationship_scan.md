# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-25T10:51:22.213824+00:00`
- Price records: `672`
- Market context records: `7870`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14667`

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

- `market_context_high->equity_24h` score `12.5406` n `119` status `ready` deltaP `29.1648` edge `0.9848` maxDD `-6.0681`
- `market_context_high->metal_24h` score `2.6437` n `120` status `ready` deltaP `15.0679` edge `0.2671` maxDD `-1.7794`
- `market_context_high->equity_4h` score `2.3879` n `120` status `ready` deltaP `9.8318` edge `0.36` maxDD `-5.5523`
- `market_context_high->crypto_major_4h` score `1.5893` n `120` status `ready` deltaP `17.0326` edge `0.1907` maxDD `-6.7444`
- `market_context_high->crypto_alt_4h` score `1.3823` n `120` status `ready` deltaP `12.5711` edge `0.1431` maxDD `-3.9374`
- `market_context_high->commodity_24h` score `1.3793` n `119` status `ready` deltaP `21.2232` edge `0.1318` maxDD `-7.0012`
- `market_context_high->crypto_major_1h` score `1.2553` n `120` status `ready` deltaP `14.017` edge `0.0511` maxDD `-1.5286`
- `market_context_high->fx_24h` score `1.0515` n `119` status `ready` deltaP `29.2612` edge `0.0485` maxDD `-3.0343`
- `market_context_high->equity_1h` score `0.7232` n `120` status `ready` deltaP `10.4655` edge `0.1047` maxDD `-4.2072`
- `market_context_high->crypto_alt_1h` score `0.3546` n `120` status `ready` deltaP `4.98` edge `0.0396` maxDD `-1.4603`
- `market_context_high->commodity_4h` score `0.2928` n `120` status `ready` deltaP `6.7279` edge `0.0389` maxDD `-1.0817`
- `market_context_high->index_1h` score `0.2203` n `120` status `ready` deltaP `8.1682` edge `0.0168` maxDD `-0.7743`
- `market_context_high->commodity_1h` score `-0.0207` n `120` status `ready` deltaP `4.6622` edge `0.0131` maxDD `-0.6722`
- `market_context_high->index_4h` score `-0.1711` n `120` status `ready` deltaP `10.4435` edge `0.0534` maxDD `-1.263`
- `market_context_high->fx_1h` score `-0.2894` n `120` status `ready` deltaP `0.2853` edge `-0.0003` maxDD `-0.4292`
- `market_context_high->metal_4h` score `-0.5615` n `120` status `ready` deltaP `4.939` edge `0.087` maxDD `-1.3374`
- `market_context_high->metal_1h` score `-0.9632` n `120` status `ready` deltaP `-0.2745` edge `0.0219` maxDD `-0.6936`
- `market_context_high->index_24h` score `-1.1106` n `119` status `ready` deltaP `-2.9097` edge `0.1052` maxDD `-1.9345`
- `market_context_high->fx_4h` score `-1.2556` n `120` status `ready` deltaP `-2.3547` edge `0.0002` maxDD `-1.6382`
- `market_context_high->crypto_alt_24h` score `-1.5444` n `120` status `ready` deltaP `14.2388` edge `0.2366` maxDD `-28.3623`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-24T03:37:25.429568+00:00`
- Price records: `672`
- Market context records: `7737`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14676`

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

- `market_context_high->equity_24h` score `4.1596` n `132` status `ready` deltaP `20.2671` edge `0.3457` maxDD `-6.0681`
- `market_context_high->crypto_major_1h` score `1.013` n `133` status `ready` deltaP `13.0082` edge `0.0418` maxDD `-1.5286`
- `market_context_high->crypto_major_4h` score `0.8559` n `133` status `ready` deltaP `14.194` edge `0.1485` maxDD `-6.7444`
- `market_context_high->crypto_alt_4h` score `0.6082` n `133` status `ready` deltaP `8.5045` edge `0.1057` maxDD `-3.9374`
- `market_context_high->equity_1h` score `0.5846` n `133` status `ready` deltaP `8.6466` edge `0.077` maxDD `-4.2072`
- `market_context_high->index_1h` score `0.4263` n `133` status `ready` deltaP `9.3952` edge `0.0159` maxDD `-0.7743`
- `market_context_high->equity_4h` score `0.4157` n `133` status `ready` deltaP `1.6636` edge `0.2335` maxDD `-6.9701`
- `market_context_high->fx_24h` score `0.262` n `132` status `ready` deltaP `16.8224` edge `0.0302` maxDD `-3.0343`
- `market_context_high->metal_24h` score `0.1861` n `133` status `ready` deltaP `6.327` edge `0.1824` maxDD `-2.3927`
- `market_context_high->crypto_alt_1h` score `0.1053` n `133` status `ready` deltaP `3.8292` edge `0.0265` maxDD `-1.4603`
- `market_context_high->commodity_1h` score `-0.2433` n `133` status `ready` deltaP `2.9443` edge `0.006` maxDD `-0.6722`
- `market_context_high->index_4h` score `-0.26` n `133` status `ready` deltaP `10.5585` edge `0.0421` maxDD `-1.3325`
- `market_context_high->commodity_4h` score `-0.2956` n `133` status `ready` deltaP `3.2581` edge `0.013` maxDD `-1.0817`
- `market_context_high->fx_1h` score `-0.4387` n `133` status `ready` deltaP `0.3737` edge `-0.0003` maxDD `-0.4331`
- `market_context_high->metal_1h` score `-0.7357` n `133` status `ready` deltaP `2.7644` edge `0.0206` maxDD `-0.6936`
- `market_context_high->metal_4h` score `-1.4855` n `133` status `ready` deltaP `0.9857` edge `0.0751` maxDD `-1.4368`
- `market_context_high->fx_4h` score `-1.5237` n `133` status `ready` deltaP `-4.6205` edge `-0.0017` maxDD `-1.6936`
- `market_context_high->commodity_24h` score `-1.7093` n `132` status `ready` deltaP `5.6858` edge `-0.022` maxDD `-7.0012`
- `market_context_high->unknown_1h` score `-2.1385` n `133` status `ready` deltaP `-0.9747` edge `-0.1127` maxDD `-1.054`
- `market_context_high->index_24h` score `-2.518` n `132` status `ready` deltaP `-18.2795` edge `0.0093` maxDD `-2.1544`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

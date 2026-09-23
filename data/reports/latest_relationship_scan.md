# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-23T21:07:27.252833+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9697`

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

- `market_context_high->unknown_1h` score `72.1411` n `47` status `ready` deltaP `9.8166` edge `5.9534` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `33.7369` n `46` status `ready` deltaP `20.1314` edge `2.6928` maxDD `-0.5817`
- `market_context_high->equity_24h` score `19.4002` n `46` status `ready` deltaP `17.5272` edge `1.5099` maxDD `-0.1382`
- `market_context_high->crypto_alt_24h` score `16.9283` n `46` status `ready` deltaP `15.1042` edge `1.31` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `8.0807` n `97` status `ready` deltaP `-3.3559` edge `1.3816` maxDD `-46.1999`
- `market_context_high->index_24h` score `6.5451` n `46` status `ready` deltaP `26.555` edge `0.3771` maxDD `-0.03`
- `news_risk_high->crypto_major_4h` score `4.4634` n `103` status `ready` deltaP `17.128` edge `0.3155` maxDD `-2.619`
- `news_risk_high->crypto_alt_4h` score `4.4346` n `103` status `ready` deltaP `13.0121` edge `0.3826` maxDD `-5.9838`
- `news_risk_high->crypto_alt_24h` score `3.0376` n `97` status `ready` deltaP `-5.5144` edge `0.778` maxDD `-32.7147`
- `news_risk_high->commodity_24h` score `2.7941` n `97` status `ready` deltaP `26.2994` edge `0.1754` maxDD `-2.431`
- `news_risk_high->crypto_alt_1h` score `2.5006` n `103` status `ready` deltaP `13.3074` edge `0.1687` maxDD `-1.5895`
- `market_context_high->index_4h` score `2.3896` n `47` status `ready` deltaP `28.3861` edge `0.0253` maxDD `-0.2323`
- `news_risk_high->crypto_major_1h` score `2.0193` n `103` status `ready` deltaP `15.7026` edge `0.1071` maxDD `-1.8141`
- `news_risk_high->fx_4h` score `1.4418` n `103` status `ready` deltaP `21.5472` edge `0.0401` maxDD `-0.421`
- `market_context_high->metal_24h` score `1.2503` n `46` status `ready` deltaP `20.5314` edge `-0.0093` maxDD `-0.2042`
- `news_risk_high->fx_24h` score `1.1275` n `97` status `ready` deltaP `27.9693` edge `0.1212` maxDD `-1.7159`
- `market_context_high->equity_4h` score `1.1034` n `47` status `ready` deltaP `9.2177` edge `0.0723` maxDD `-1.3444`
- `market_context_high->index_1h` score `0.6959` n `47` status `ready` deltaP `11.7658` edge `0.0074` maxDD `-0.2275`
- `news_risk_high->metal_1h` score `0.5942` n `103` status `ready` deltaP `14.9032` edge `0.0095` maxDD `-0.7468`
- `news_risk_high->metal_24h` score `0.4747` n `97` status `ready` deltaP `16.6093` edge `0.0419` maxDD `-3.0086`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

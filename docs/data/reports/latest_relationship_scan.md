# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-23T04:22:29.230056+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9794`

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

- `market_context_high->unknown_4h` score `46.249` n `46` status `ready` deltaP `7.3171` edge `3.8053` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `29.5347` n `46` status `ready` deltaP `13.5341` edge `2.3866` maxDD `-0.5817`
- `market_context_high->equity_24h` score `16.6693` n `46` status `ready` deltaP `12.1453` edge `1.3182` maxDD `-0.1382`
- `market_context_high->crypto_alt_24h` score `12.7056` n `46` status `ready` deltaP `10.5903` edge `0.9882` maxDD `0.0`
- `market_context_high->index_24h` score `5.6524` n `46` status `ready` deltaP `20.8258` edge `0.3409` maxDD `-0.03`
- `news_risk_high->crypto_major_24h` score `4.8411` n `96` status `ready` deltaP `-9.2014` edge `1.1506` maxDD `-46.1999`
- `news_risk_high->commodity_24h` score `4.491` n `96` status `ready` deltaP `34.8958` edge `0.2595` maxDD `-2.431`
- `news_risk_high->crypto_major_4h` score `2.6814` n `97` status `ready` deltaP `13.3031` edge `0.1925` maxDD `-2.619`
- `news_risk_high->crypto_alt_4h` score `2.1128` n `97` status `ready` deltaP `8.425` edge `0.2197` maxDD `-5.9838`
- `market_context_high->index_4h` score `2.1063` n `46` status `ready` deltaP `24.6884` edge `0.0243` maxDD `-0.0692`
- `news_risk_high->crypto_alt_1h` score `1.8841` n `103` status `ready` deltaP `11.0618` edge `0.1323` maxDD `-1.5895`
- `news_risk_high->crypto_major_1h` score `1.4341` n `103` status `ready` deltaP `13.1577` edge `0.0753` maxDD `-1.8141`
- `news_risk_high->fx_4h` score `1.3985` n `97` status `ready` deltaP `20.661` edge `0.0424` maxDD `-0.421`
- `news_risk_high->fx_24h` score `0.9223` n `96` status `ready` deltaP `24.4792` edge `0.114` maxDD `-1.7159`
- `market_context_high->equity_1h` score `0.7622` n `46` status `ready` deltaP `6.4632` edge `0.0447` maxDD `-0.2751`
- `market_context_high->equity_4h` score `0.6609` n `46` status `ready` deltaP `5.0902` edge `0.0518` maxDD `-0.4529`
- `market_context_high->index_1h` score `0.6543` n `46` status `ready` deltaP `10.3554` edge `0.0108` maxDD `-0.0249`
- `news_risk_high->metal_4h` score `0.4383` n `97` status `ready` deltaP `13.6928` edge `0.041` maxDD `-1.9941`
- `news_risk_high->metal_1h` score `0.4301` n `103` status `ready` deltaP `12.9571` edge `0.0088` maxDD `-0.7468`
- `market_context_high->metal_24h` score `0.3473` n `46` status `ready` deltaP `17.0592` edge `-0.0614` maxDD `-0.2042`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

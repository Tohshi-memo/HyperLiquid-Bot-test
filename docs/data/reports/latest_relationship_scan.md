# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-23T01:52:28.826637+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9740`

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

- `market_context_high->unknown_4h` score `45.9918` n `46` status `ready` deltaP `7.0122` edge `3.7859` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `29.7039` n `46` status `ready` deltaP `13.5341` edge `2.4007` maxDD `-0.5817`
- `market_context_high->equity_24h` score `16.4809` n `46` status `ready` deltaP `12.1453` edge `1.3025` maxDD `-0.1382`
- `market_context_high->crypto_alt_24h` score `13.0128` n `46` status `ready` deltaP `10.5903` edge `1.0138` maxDD `0.0`
- `market_context_high->index_24h` score `5.5474` n `46` status `ready` deltaP `19.7841` edge `0.3391` maxDD `-0.03`
- `news_risk_high->crypto_major_24h` score `5.0103` n `96` status `ready` deltaP `-9.2014` edge `1.1647` maxDD `-46.1999`
- `news_risk_high->commodity_24h` score `4.5769` n `96` status `ready` deltaP `35.0694` edge `0.2655` maxDD `-2.431`
- `news_risk_high->crypto_major_4h` score `2.9216` n `97` status `ready` deltaP `14.3701` edge `0.2054` maxDD `-2.619`
- `news_risk_high->crypto_alt_4h` score `2.3362` n `97` status `ready` deltaP `9.4921` edge `0.2312` maxDD `-5.9838`
- `market_context_high->index_4h` score `1.9665` n `46` status `ready` deltaP `23.3165` edge `0.0218` maxDD `-0.0692`
- `news_risk_high->crypto_alt_1h` score `1.5791` n `98` status `ready` deltaP `9.8741` edge `0.1148` maxDD `-1.5895`
- `news_risk_high->fx_4h` score `1.3827` n `97` status `ready` deltaP `20.5086` edge `0.0421` maxDD `-0.421`
- `news_risk_high->crypto_major_1h` score `1.2191` n `98` status `ready` deltaP `12.1197` edge `0.0643` maxDD `-1.8141`
- `news_risk_high->fx_24h` score `0.8318` n `96` status `ready` deltaP `23.2639` edge `0.1105` maxDD `-1.7159`
- `market_context_high->equity_1h` score `0.6819` n `46` status `ready` deltaP `6.0141` edge `0.041` maxDD `-0.2751`
- `market_context_high->index_1h` score `0.6375` n `46` status `ready` deltaP `10.2057` edge `0.0104` maxDD `-0.0249`
- `news_risk_high->metal_1h` score `0.5989` n `98` status `ready` deltaP `14.857` edge `0.0102` maxDD `-0.7468`
- `market_context_high->metal_24h` score `0.5347` n `46` status `ready` deltaP `18.6217` edge `-0.0562` maxDD `-0.2042`
- `market_context_high->equity_4h` score `0.3973` n `46` status `ready` deltaP `3.5658` edge `0.04` maxDD `-0.4529`
- `news_risk_high->metal_4h` score `0.3039` n `97` status `ready` deltaP `12.7782` edge `0.0359` maxDD `-1.9941`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

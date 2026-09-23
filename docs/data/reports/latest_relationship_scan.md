# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-23T00:52:33.583135+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9542`

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

- `market_context_high->unknown_4h` score `45.797` n `46` status `ready` deltaP `6.7073` edge `3.7717` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `29.7075` n `46` status `ready` deltaP `13.5341` edge `2.401` maxDD `-0.5817`
- `market_context_high->equity_24h` score `16.3777` n `46` status `ready` deltaP `12.1453` edge `1.2939` maxDD `-0.1382`
- `market_context_high->crypto_alt_24h` score `13.08` n `46` status `ready` deltaP `10.5903` edge `1.0194` maxDD `0.0`
- `market_context_high->index_24h` score `5.5179` n `46` status `ready` deltaP `19.6105` edge `0.3378` maxDD `-0.03`
- `news_risk_high->crypto_major_24h` score `5.0139` n `96` status `ready` deltaP `-9.2014` edge `1.165` maxDD `-46.1999`
- `news_risk_high->commodity_24h` score `4.6865` n `96` status `ready` deltaP `35.7639` edge `0.27` maxDD `-2.431`
- `news_risk_high->crypto_major_4h` score `2.9001` n `96` status `ready` deltaP `14.1768` edge `0.2049` maxDD `-2.619`
- `news_risk_high->crypto_alt_4h` score `2.3015` n `96` status `ready` deltaP `9.2988` edge `0.2296` maxDD `-5.9838`
- `market_context_high->index_4h` score `1.907` n `46` status `ready` deltaP `22.7067` edge `0.0209` maxDD `-0.0692`
- `news_risk_high->crypto_alt_1h` score `1.8138` n `97` status `ready` deltaP `10.4713` edge `0.1209` maxDD `-1.1645`
- `news_risk_high->fx_4h` score `1.4411` n `96` status `ready` deltaP `21.1637` edge `0.0426` maxDD `-0.421`
- `news_risk_high->crypto_major_1h` score `1.3816` n `97` status `ready` deltaP `12.8666` edge `0.0687` maxDD `-1.8141`
- `news_risk_high->fx_24h` score `0.8225` n `96` status `ready` deltaP `23.2639` edge `0.1093` maxDD `-1.7159`
- `market_context_high->equity_1h` score `0.6351` n `46` status `ready` deltaP `5.7147` edge `0.0391` maxDD `-0.2751`
- `news_risk_high->metal_1h` score `0.6229` n `97` status `ready` deltaP `15.0812` edge `0.0107` maxDD `-0.7468`
- `market_context_high->index_1h` score `0.6088` n `46` status `ready` deltaP `9.9063` edge `0.01` maxDD `-0.0249`
- `market_context_high->metal_24h` score `0.5371` n `46` status `ready` deltaP `18.6217` edge `-0.056` maxDD `-0.2042`
- `news_risk_high->fx_1h` score `0.3431` n `97` status `ready` deltaP `9.2459` edge `0.0113` maxDD `-0.2147`
- `market_context_high->equity_4h` score `0.3189` n `46` status `ready` deltaP `3.2609` edge `0.0355` maxDD `-0.4529`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

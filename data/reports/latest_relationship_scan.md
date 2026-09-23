# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-23T12:07:44.986384+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9810`

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

- `market_context_high->unknown_4h` score `47.2757` n `46` status `ready` deltaP `7.9268` edge `3.8868` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `29.5841` n `46` status `ready` deltaP `13.8814` edge `2.3884` maxDD `-0.5817`
- `market_context_high->equity_24h` score `16.7893` n `46` status `ready` deltaP `12.1453` edge `1.3282` maxDD `-0.1382`
- `market_context_high->crypto_alt_24h` score `12.2016` n `46` status `ready` deltaP `10.5903` edge `0.9462` maxDD `0.0`
- `market_context_high->index_24h` score `5.6651` n `46` status `ready` deltaP `20.9994` edge `0.3408` maxDD `-0.03`
- `news_risk_high->crypto_major_24h` score `4.8905` n `96` status `ready` deltaP `-8.8541` edge `1.1524` maxDD `-46.1999`
- `news_risk_high->commodity_24h` score `3.7442` n `96` status `ready` deltaP `31.7708` edge `0.2181` maxDD `-2.431`
- `news_risk_high->crypto_major_4h` score `3.0581` n `103` status `ready` deltaP `14.2316` edge `0.2177` maxDD `-2.619`
- `market_context_high->index_4h` score `2.4008` n `46` status `ready` deltaP `27.8897` edge `0.0275` maxDD `-0.0692`
- `news_risk_high->crypto_alt_4h` score `2.2791` n `103` status `ready` deltaP `9.0487` edge `0.2294` maxDD `-5.9838`
- `news_risk_high->crypto_alt_1h` score `2.0064` n `103` status `ready` deltaP `11.8104` edge `0.1375` maxDD `-1.5895`
- `news_risk_high->crypto_major_1h` score `1.7003` n `103` status `ready` deltaP `14.6547` edge `0.0875` maxDD `-1.8141`
- `news_risk_high->fx_4h` score `1.2543` n `103` status `ready` deltaP `19.4131` edge `0.0387` maxDD `-0.421`
- `market_context_high->equity_4h` score `1.1512` n `46` status `ready` deltaP `8.4438` edge `0.0703` maxDD `-0.4529`
- `news_risk_high->fx_24h` score `1.1084` n `96` status `ready` deltaP `27.0833` edge `0.1205` maxDD `-1.7159`
- `market_context_high->equity_1h` score `0.9935` n `46` status `ready` deltaP `8.4093` edge `0.051` maxDD `-0.2751`
- `market_context_high->index_1h` score `0.8364` n `46` status `ready` deltaP `12.4512` edge `0.012` maxDD `-0.0249`
- `news_risk_high->metal_1h` score `0.617` n `103` status `ready` deltaP `14.9032` edge `0.0114` maxDD `-0.7468`
- `news_risk_high->metal_4h` score `0.2151` n `103` status `ready` deltaP `12.4408` edge `0.0404` maxDD `-1.9941`
- `news_risk_high->fx_1h` score `0.2112` n `103` status `ready` deltaP `7.8077` edge `0.0099` maxDD `-0.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

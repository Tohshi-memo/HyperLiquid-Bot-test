# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-21T21:52:31.219570+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9868`

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

- `market_context_high->unknown_4h` score `25.1359` n `58` status `ready` deltaP `1.6874` edge `2.0984` maxDD `-0.5326`
- `news_risk_high->crypto_major_24h` score `13.3092` n `101` status `ready` deltaP `1.8942` edge `1.7823` maxDD `-46.1999`
- `news_risk_high->crypto_alt_24h` score `8.2847` n `101` status `ready` deltaP `2.2793` edge `1.1633` maxDD `-32.7147`
- `news_risk_high->crypto_alt_4h` score `3.4529` n `101` status `ready` deltaP `16.6324` edge `0.2978` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `2.53` n `101` status `ready` deltaP `17.8519` edge `0.2176` maxDD `-8.0625`
- `news_risk_high->crypto_alt_1h` score `2.492` n `101` status `ready` deltaP `15.3332` edge `0.152` maxDD `-2.058`
- `news_risk_high->commodity_24h` score `2.2633` n `101` status `ready` deltaP `29.2732` edge `0.2256` maxDD `-3.4467`
- `news_risk_high->crypto_major_1h` score `1.7366` n `101` status `ready` deltaP `16.6805` edge `0.0858` maxDD `-2.8494`
- `market_context_high->index_24h` score `1.1477` n `45` status `ready` deltaP `-2.2917` edge `0.1898` maxDD `-1.644`
- `market_context_high->equity_24h` score `0.7743` n `45` status `ready` deltaP `-6.2847` edge `0.4209` maxDD `-17.7117`
- `market_context_high->equity_1h` score `0.6222` n `58` status `ready` deltaP `4.362` edge `0.0481` maxDD `-0.36`
- `news_risk_high->metal_1h` score `0.5394` n `101` status `ready` deltaP `13.8495` edge `0.0128` maxDD `-0.8144`
- `market_context_high->index_1h` score `0.5076` n `58` status `ready` deltaP `8.3316` edge `0.0123` maxDD `-0.0435`
- `market_context_high->fx_1h` score `0.4337` n `58` status `ready` deltaP `9.8235` edge `0.0063` maxDD `-0.1854`
- `market_context_high->crypto_major_24h` score `0.387` n `45` status `ready` deltaP `0.4861` edge `0.7122` maxDD `-48.5989`
- `news_risk_high->fx_4h` score `0.3694` n `101` status `ready` deltaP `10.3175` edge `0.0256` maxDD `-0.421`
- `market_context_high->metal_1h` score `0.2615` n `58` status `ready` deltaP `5.3996` edge `0.0166` maxDD `-0.1314`
- `news_risk_high->metal_4h` score `0.1919` n `101` status `ready` deltaP `13.4403` edge `0.0318` maxDD `-2.0994`
- `market_context_high->index_4h` score `0.0816` n `58` status `ready` deltaP `11.1228` edge `0.0` maxDD `-1.0949`
- `market_context_high->metal_24h` score `0.0657` n `45` status `ready` deltaP `14.4097` edge `-0.0672` maxDD `-0.2042`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-15T06:37:32.759791+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11184`

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

- `news_risk_high->unknown_4h` score `399.7142` n `78` status `ready` deltaP `-21.9981` edge `33.5455` maxDD `-4.1464`
- `news_risk_high->unknown_24h` score `22.4782` n `78` status `ready` deltaP `18.4028` edge `1.7505` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `21.1659` n `78` status `ready` deltaP `43.7767` edge `1.5111` maxDD `-1.4626`
- `news_risk_high->crypto_major_24h` score `15.7611` n `78` status `ready` deltaP `33.133` edge `1.2396` maxDD `-9.098`
- `news_risk_high->equity_24h` score `14.6041` n `78` status `ready` deltaP `46.7281` edge `1.0835` maxDD `-6.5742`
- `news_risk_high->index_24h` score `8.5611` n `78` status `ready` deltaP `60.7238` edge `0.3262` maxDD `-0.075`
- `news_risk_high->metal_24h` score `6.4181` n `78` status `ready` deltaP `37.7938` edge `0.3283` maxDD `-0.6334`
- `risk_on_high->commodity_24h` score `6.1384` n `52` status `ready` deltaP `39.4097` edge `0.2488` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `6.1384` n `52` status `ready` deltaP `39.4097` edge `0.2488` maxDD `0.0`
- `market_context_high->commodity_24h` score `4.8414` n `137` status `ready` deltaP `32.1104` edge `0.2419` maxDD `-0.8682`
- `risk_on_high->fx_24h` score `4.0101` n `52` status `ready` deltaP `45.6463` edge `0.0341` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `4.0101` n `52` status `ready` deltaP `45.6463` edge `0.0341` maxDD `-0.0054`
- `market_context_high->fx_24h` score `3.6131` n `137` status `ready` deltaP `42.4599` edge `0.0396` maxDD `-0.0593`
- `risk_on_high->commodity_4h` score `1.9761` n `52` status `ready` deltaP `25.2228` edge `0.0315` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `1.9761` n `52` status `ready` deltaP `25.2228` edge `0.0315` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `1.8759` n `149` status `ready` deltaP `21.7251` edge `0.0533` maxDD `-0.345`
- `market_context_high->commodity_1h` score `0.8246` n `149` status `ready` deltaP `13.3666` edge `0.0173` maxDD `-0.3491`
- `news_risk_high->index_4h` score `0.63` n `78` status `ready` deltaP `16.2015` edge `0.0356` maxDD `-0.6935`
- `risk_on_high->metal_1h` score `0.2206` n `52` status `ready` deltaP `7.7614` edge `0.0071` maxDD `-0.1115`
- `risk_on_and_context->metal_1h` score `0.2206` n `52` status `ready` deltaP `7.7614` edge `0.0071` maxDD `-0.1115`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

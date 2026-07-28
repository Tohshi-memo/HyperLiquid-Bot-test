# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-28T18:22:38.129651+00:00`
- Price records: `672`
- Market context records: `8222`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5936`

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

- `news_risk_high->unknown_24h` score `7956.9696` n `43` status `ready` deltaP `37.5` edge `662.8308` maxDD `0.0`
- `market_context_high->equity_24h` score `21.7688` n `30` status `ready` deltaP `38.2639` edge `1.65` maxDD `-4.9489`
- `market_context_high->crypto_major_24h` score `18.4585` n `30` status `ready` deltaP `36.875` edge `1.3818` maxDD `-4.8208`
- `market_context_high->crypto_alt_24h` score `17.3784` n `30` status `ready` deltaP `38.2639` edge `1.2601` maxDD `-3.0264`
- `market_context_high->equity_4h` score `8.9551` n `30` status `ready` deltaP `47.8862` edge `0.4313` maxDD `-0.0094`
- `market_context_high->metal_24h` score `8.2366` n `30` status `ready` deltaP `46.6667` edge `0.3854` maxDD `-0.4771`
- `news_risk_high->equity_4h` score `7.43` n `54` status `ready` deltaP `27.1454` edge `0.4979` maxDD `-3.4427`
- `market_context_high->crypto_major_4h` score `6.6049` n `30` status `ready` deltaP `28.9533` edge `0.3753` maxDD `-0.433`
- `market_context_high->index_24h` score `5.8667` n `30` status `ready` deltaP `37.743` edge `0.2766` maxDD `-0.8132`
- `market_context_high->crypto_alt_4h` score `4.9568` n `30` status `ready` deltaP `23.5061` edge `0.2766` maxDD `-0.6195`
- `market_context_high->metal_4h` score `3.8285` n `30` status `ready` deltaP `37.4085` edge `0.0827` maxDD `-0.0438`
- `market_context_high->index_4h` score `3.5525` n `30` status `ready` deltaP `35.8841` edge `0.0611` maxDD `-0.0092`
- `news_risk_high->equity_1h` score `3.1984` n `54` status `ready` deltaP `22.8765` edge `0.1449` maxDD `-1.1366`
- `market_context_high->fx_24h` score `2.7383` n `30` status `ready` deltaP `45.3819` edge `0.0816` maxDD `-0.3134`
- `news_risk_high->index_4h` score `2.6129` n `54` status `ready` deltaP `21.81` edge `0.0914` maxDD `-0.191`
- `news_risk_high->crypto_major_4h` score `2.3603` n `54` status `ready` deltaP `11.5459` edge `0.295` maxDD `-2.8833`
- `news_risk_high->crypto_major_1h` score `1.8402` n `54` status `ready` deltaP `12.7024` edge `0.1084` maxDD `-1.1783`
- `news_risk_high->crypto_alt_1h` score `1.8231` n `54` status `ready` deltaP `14.8536` edge `0.0963` maxDD `-1.1388`
- `market_context_high->equity_1h` score `1.7632` n `30` status `ready` deltaP `8.8024` edge `0.1029` maxDD `-0.1718`
- `market_context_high->crypto_major_1h` score `1.4111` n `30` status `ready` deltaP `13.4431` edge `0.0475` maxDD `-0.5626`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

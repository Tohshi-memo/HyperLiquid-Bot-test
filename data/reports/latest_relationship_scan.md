# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-28T18:52:37.919109+00:00`
- Price records: `672`
- Market context records: `8224`
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

- `news_risk_high->unknown_24h` score `7957.0538` n `43` status `ready` deltaP `37.8472` edge `662.8355` maxDD `0.0`
- `market_context_high->equity_24h` score `21.86` n `30` status `ready` deltaP `38.2639` edge `1.6576` maxDD `-4.9489`
- `market_context_high->crypto_major_24h` score `18.5125` n `30` status `ready` deltaP `36.875` edge `1.3863` maxDD `-4.8208`
- `market_context_high->crypto_alt_24h` score `17.4714` n `30` status `ready` deltaP `38.4375` edge `1.2667` maxDD `-3.0264`
- `market_context_high->equity_4h` score `8.9431` n `30` status `ready` deltaP `47.8862` edge `0.4303` maxDD `-0.0094`
- `market_context_high->metal_24h` score `8.2955` n `30` status `ready` deltaP `47.0139` edge `0.388` maxDD `-0.4771`
- `news_risk_high->equity_4h` score `7.418` n `54` status `ready` deltaP `27.1454` edge `0.4969` maxDD `-3.4427`
- `market_context_high->crypto_major_4h` score `6.5699` n `30` status `ready` deltaP `28.8008` edge `0.3734` maxDD `-0.433`
- `market_context_high->index_24h` score `5.8727` n `30` status `ready` deltaP `37.743` edge `0.2771` maxDD `-0.8132`
- `market_context_high->crypto_alt_4h` score `4.9568` n `30` status `ready` deltaP `23.5061` edge `0.2766` maxDD `-0.6195`
- `market_context_high->metal_4h` score `3.8285` n `30` status `ready` deltaP `37.4085` edge `0.0827` maxDD `-0.0438`
- `market_context_high->index_4h` score `3.538` n `30` status `ready` deltaP `35.7317` edge `0.0609` maxDD `-0.0092`
- `news_risk_high->equity_1h` score `3.1757` n `54` status `ready` deltaP `22.7268` edge `0.144` maxDD `-1.1366`
- `market_context_high->fx_24h` score `2.7398` n `30` status `ready` deltaP `45.3819` edge `0.0818` maxDD `-0.3134`
- `news_risk_high->index_4h` score `2.5984` n `54` status `ready` deltaP `21.6576` edge `0.0912` maxDD `-0.191`
- `news_risk_high->crypto_major_4h` score `2.3375` n `54` status `ready` deltaP `11.3934` edge `0.2931` maxDD `-2.8833`
- `news_risk_high->crypto_alt_1h` score `1.8255` n `54` status `ready` deltaP `14.8536` edge `0.0965` maxDD `-1.1388`
- `news_risk_high->crypto_major_1h` score `1.8199` n `54` status `ready` deltaP `12.5527` edge `0.1077` maxDD `-1.1783`
- `market_context_high->equity_1h` score `1.7404` n `30` status `ready` deltaP `8.6527` edge `0.102` maxDD `-0.1718`
- `market_context_high->crypto_major_1h` score `1.3907` n `30` status `ready` deltaP `13.2934` edge `0.0468` maxDD `-0.5626`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-11T19:31:03.644464+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `8222`

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

- `market_context_high->unknown_24h` score `1380.8928` n `40` status `ready` deltaP `-21.875` edge `115.2566` maxDD `-1.2425`
- `market_context_high->unknown_4h` score `55.0819` n `87` status `ready` deltaP `-4.7536` edge `4.6799` maxDD `-2.3109`
- `market_context_high->equity_24h` score `8.7888` n `40` status `ready` deltaP `27.6736` edge `0.5908` maxDD `-1.0977`
- `market_context_high->unknown_1h` score `7.436` n `99` status `ready` deltaP `-2.7611` edge `0.6717` maxDD `-1.0231`
- `market_context_high->index_24h` score `6.3928` n `40` status `ready` deltaP `52.4306` edge `0.1832` maxDD `0.0`
- `market_context_high->fx_24h` score `3.1853` n `40` status `ready` deltaP `36.0764` edge `0.0379` maxDD `-0.0374`
- `market_context_high->crypto_major_24h` score `1.4572` n `40` status `ready` deltaP `-21.1111` edge `0.577` maxDD `-17.8526`
- `market_context_high->fx_4h` score `0.7627` n `87` status `ready` deltaP `12.6332` edge `0.0077` maxDD `-0.2692`
- `market_context_high->commodity_4h` score `0.4609` n `87` status `ready` deltaP `11.496` edge `0.0151` maxDD `-1.6002`
- `market_context_high->crypto_major_4h` score `0.3414` n `87` status `ready` deltaP `2.779` edge `0.2358` maxDD `-11.1784`
- `market_context_high->crypto_alt_1h` score `0.2798` n `99` status `ready` deltaP `4.8056` edge `0.0947` maxDD `-4.9401`
- `market_context_high->commodity_1h` score `0.134` n `99` status `ready` deltaP `5.105` edge `0.0055` maxDD `-0.6025`
- `market_context_high->crypto_alt_4h` score `0.0134` n `87` status `ready` deltaP `-1.1599` edge `0.2653` maxDD `-13.8008`
- `market_context_high->metal_4h` score `0.004` n `87` status `ready` deltaP `7.636` edge `0.0217` maxDD `-1.1153`
- `market_context_high->fx_1h` score `-0.0205` n `99` status `ready` deltaP `3.1967` edge `0.0012` maxDD `-0.271`
- `market_context_high->metal_1h` score `-0.2514` n `99` status `ready` deltaP `5.1806` edge `0.0034` maxDD `-0.7107`
- `market_context_high->crypto_major_1h` score `-0.2591` n `99` status `ready` deltaP `-0.0937` edge `0.0563` maxDD `-3.7778`
- `market_context_high->index_4h` score `-0.5612` n `87` status `ready` deltaP `-1.1722` edge `0.0059` maxDD `-0.9364`
- `market_context_high->index_1h` score `-0.7148` n `99` status `ready` deltaP `-3.7607` edge `-0.0015` maxDD `-0.5392`
- `market_context_high->equity_1h` score `-1.026` n `99` status `ready` deltaP `-6.9422` edge `0.0017` maxDD `-2.2898`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

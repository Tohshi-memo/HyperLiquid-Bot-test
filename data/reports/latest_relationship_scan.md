# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-05T15:52:29.736678+00:00`
- Price records: `672`
- Market context records: `5787`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `8556`

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

- `market_context_high->equity_24h` score `0.4498` n `243` status `ready` deltaP `15.1299` edge `0.4647` maxDD `-31.6316`
- `market_context_high->equity_4h` score `0.0046` n `300` status `ready` deltaP `6.7866` edge `0.119` maxDD `-7.4425`
- `market_context_high->fx_1h` score `-0.2388` n `305` status `ready` deltaP `2.5233` edge `0.0011` maxDD `-0.5499`
- `market_context_high->equity_1h` score `-0.6401` n `305` status `ready` deltaP `3.1423` edge `0.0264` maxDD `-5.0555`
- `market_context_high->metal_1h` score `-0.6575` n `305` status `ready` deltaP `2.0595` edge `-0.001` maxDD `-2.0682`
- `market_context_high->commodity_1h` score `-0.7259` n `305` status `ready` deltaP `-1.1971` edge `-0.0046` maxDD `-3.7721`
- `market_context_high->index_1h` score `-0.9772` n `305` status `ready` deltaP `0.2705` edge `0.0036` maxDD `-0.9472`
- `market_context_high->crypto_major_1h` score `-0.9882` n `305` status `ready` deltaP `2.7226` edge `0.0316` maxDD `-6.2348`
- `market_context_high->fx_24h` score `-1.0081` n `243` status `ready` deltaP `14.0818` edge `0.0398` maxDD `-4.0337`
- `market_context_high->crypto_alt_1h` score `-1.1011` n `305` status `ready` deltaP `1.6178` edge `0.0309` maxDD `-6.6758`
- `market_context_high->index_4h` score `-1.2003` n `300` status `ready` deltaP `0.6362` edge `0.0106` maxDD `-3.165`
- `market_context_high->fx_4h` score `-1.4289` n `300` status `ready` deltaP `0.628` edge `0.0037` maxDD `-1.9528`
- `market_context_high->commodity_4h` score `-2.4589` n `300` status `ready` deltaP `-3.3293` edge `-0.0255` maxDD `-14.071`
- `market_context_high->index_24h` score `-2.848` n `243` status `ready` deltaP `2.9` edge `0.03` maxDD `-18.1572`
- `market_context_high->crypto_major_4h` score `-2.958` n `300` status `ready` deltaP `7.5508` edge `0.1404` maxDD `-25.6458`
- `market_context_high->metal_4h` score `-3.8348` n `300` status `ready` deltaP `-5.4024` edge `-0.0476` maxDD `-11.5426`
- `market_context_high->crypto_alt_4h` score `-4.5472` n `300` status `ready` deltaP `5.313` edge `0.0865` maxDD `-28.7346`
- `market_context_high->metal_24h` score `-7.0984` n `243` status `ready` deltaP `-7.909` edge `-0.2504` maxDD `-27.5543`
- `market_context_high->crypto_major_24h` score `-7.3749` n `243` status `ready` deltaP `1.6332` edge `-0.1131` maxDD `-29.6555`
- `market_context_high->commodity_24h` score `-11.0019` n `243` status `ready` deltaP `-14.4611` edge `-0.0828` maxDD `-40.676`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

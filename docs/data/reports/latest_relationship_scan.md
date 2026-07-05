# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-05T17:52:26.021800+00:00`
- Price records: `672`
- Market context records: `5796`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `8128`

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

- `market_context_high->equity_24h` score `0.5825` n `248` status `ready` deltaP `15.3954` edge `0.4538` maxDD `-31.6316`
- `market_context_high->equity_4h` score `-0.0264` n `302` status `ready` deltaP `6.5952` edge `0.1177` maxDD `-7.4425`
- `market_context_high->fx_1h` score `-0.2622` n `302` status `ready` deltaP `2.1047` edge `0.0009` maxDD `-0.5499`
- `market_context_high->equity_1h` score `-0.639` n `302` status `ready` deltaP `3.111` edge `0.0267` maxDD `-5.0555`
- `market_context_high->index_1h` score `-0.6422` n `302` status `ready` deltaP `0.1358` edge `0.0036` maxDD `-0.9472`
- `market_context_high->metal_1h` score `-0.6467` n `302` status `ready` deltaP `2.2088` edge `-0.0011` maxDD `-2.0682`
- `market_context_high->commodity_1h` score `-0.7611` n `302` status `ready` deltaP `-1.8143` edge `-0.005` maxDD `-3.7721`
- `market_context_high->crypto_major_1h` score `-0.9634` n `302` status `ready` deltaP `2.9573` edge `0.0321` maxDD `-6.2348`
- `market_context_high->crypto_alt_1h` score `-1.1358` n `302` status `ready` deltaP `1.3652` edge `0.0297` maxDD `-6.6758`
- `market_context_high->fx_24h` score `-1.1409` n `248` status `ready` deltaP `13.1161` edge `0.0375` maxDD `-4.6968`
- `market_context_high->index_4h` score `-1.1938` n `302` status `ready` deltaP `0.7774` edge `0.0105` maxDD `-3.165`
- `market_context_high->fx_4h` score `-1.4806` n `302` status `ready` deltaP `0.2836` edge `0.0032` maxDD `-2.2593`
- `market_context_high->commodity_4h` score `-2.3767` n `302` status `ready` deltaP `-3.184` edge `-0.0255` maxDD `-13.3045`
- `market_context_high->metal_4h` score `-2.4876` n `302` status `ready` deltaP `-5.3354` edge `-0.0474` maxDD `-11.5426`
- `market_context_high->index_24h` score `-2.7964` n `248` status `ready` deltaP `3.7131` edge `0.0312` maxDD `-18.1572`
- `market_context_high->crypto_major_4h` score `-2.9714` n `302` status `ready` deltaP `7.5785` edge `0.1391` maxDD `-25.6458`
- `market_context_high->crypto_alt_4h` score `-4.5625` n `302` status `ready` deltaP `5.3606` edge `0.0849` maxDD `-28.7346`
- `market_context_high->metal_24h` score `-6.7918` n `248` status `ready` deltaP `-7.2917` edge `-0.2504` maxDD `-25.7388`
- `market_context_high->crypto_major_24h` score `-8.5149` n `248` status `ready` deltaP `0.3024` edge `-0.1659` maxDD `-29.6555`
- `market_context_high->commodity_24h` score `-10.6255` n `248` status `ready` deltaP `-14.5274` edge `-0.0817` maxDD `-39.2197`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

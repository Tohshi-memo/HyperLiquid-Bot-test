# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-05T20:07:26.014896+00:00`
- Price records: `672`
- Market context records: `5807`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9058`

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

- `market_context_high->equity_24h` score `0.2681` n `248` status `ready` deltaP `15.3954` edge `0.4276` maxDD `-31.6316`
- `market_context_high->equity_4h` score `-0.0606` n `293` status `ready` deltaP `5.584` edge `0.1172` maxDD `-7.4251`
- `market_context_high->fx_1h` score `-0.2098` n `293` status `ready` deltaP `3.0507` edge `0.0013` maxDD `-0.5499`
- `market_context_high->index_1h` score `-0.6465` n `293` status `ready` deltaP `0.0986` edge `0.0033` maxDD `-0.9472`
- `market_context_high->metal_1h` score `-0.652` n `293` status `ready` deltaP `2.1285` edge `-0.001` maxDD `-2.0682`
- `market_context_high->commodity_1h` score `-0.6564` n `293` status `ready` deltaP `-1.6375` edge `-0.0038` maxDD `-2.8878`
- `market_context_high->equity_1h` score `-0.6806` n `293` status `ready` deltaP `2.6671` edge `0.0262` maxDD `-5.0555`
- `market_context_high->crypto_major_1h` score `-0.9511` n `293` status `ready` deltaP `2.8111` edge `0.0341` maxDD `-6.2348`
- `market_context_high->crypto_alt_1h` score `-1.1523` n `293` status `ready` deltaP `1.0387` edge `0.0305` maxDD `-6.6758`
- `market_context_high->index_4h` score `-1.2573` n `293` status `ready` deltaP `-0.2341` edge `0.0091` maxDD `-3.165`
- `market_context_high->fx_24h` score `-1.3368` n `248` status `ready` deltaP `11.0496` edge `0.0334` maxDD `-5.2758`
- `market_context_high->fx_4h` score `-1.4133` n `293` status `ready` deltaP `1.413` edge `0.0043` maxDD `-2.2593`
- `market_context_high->metal_4h` score `-2.3069` n `293` status `ready` deltaP `-4.4457` edge `-0.0456` maxDD `-10.3082`
- `market_context_high->crypto_major_4h` score `-2.785` n `293` status `ready` deltaP `7.9138` edge `0.1524` maxDD `-25.6458`
- `market_context_high->index_24h` score `-2.8081` n `248` status `ready` deltaP `3.7131` edge `0.0297` maxDD `-18.1572`
- `market_context_high->commodity_4h` score `-2.9546` n `293` status `ready` deltaP `-2.3599` edge `-0.0195` maxDD `-9.5452`
- `market_context_high->crypto_alt_4h` score `-4.4357` n `293` status `ready` deltaP `5.6407` edge `0.0936` maxDD `-28.7346`
- `market_context_high->metal_24h` score `-5.9072` n `248` status `ready` deltaP `-5.2252` edge `-0.24` maxDD `-21.5998`
- `market_context_high->commodity_24h` score `-9.5639` n `248` status `ready` deltaP `-13.1496` edge `-0.0692` maxDD `-33.8772`
- `market_context_high->crypto_major_24h` score `-10.8175` n `248` status `ready` deltaP `-1.7641` edge `-0.2426` maxDD `-34.7679`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

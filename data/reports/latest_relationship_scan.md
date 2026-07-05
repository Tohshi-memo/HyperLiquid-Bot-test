# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-05T16:22:31.778543+00:00`
- Price records: `672`
- Market context records: `5789`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `8104`

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

- `market_context_high->equity_24h` score `0.4398` n `245` status `ready` deltaP `15.2374` edge `0.4627` maxDD `-31.6316`
- `market_context_high->equity_4h` score `-0.0153` n `302` status `ready` deltaP `6.674` edge `0.1181` maxDD `-7.4425`
- `market_context_high->fx_1h` score `-0.2396` n `305` status `ready` deltaP `2.5233` edge `0.001` maxDD `-0.5499`
- `market_context_high->equity_1h` score `-0.627` n `305` status `ready` deltaP `3.292` edge `0.0265` maxDD `-5.0555`
- `market_context_high->metal_1h` score `-0.6455` n `305` status `ready` deltaP `2.2092` edge `-0.001` maxDD `-2.0682`
- `market_context_high->commodity_1h` score `-0.7337` n `305` status `ready` deltaP `-1.3468` edge `-0.0046` maxDD `-3.7721`
- `market_context_high->index_1h` score `-0.9772` n `305` status `ready` deltaP `0.2705` edge `0.0036` maxDD `-0.9472`
- `market_context_high->crypto_major_1h` score `-0.9966` n `305` status `ready` deltaP `2.7226` edge `0.0309` maxDD `-6.2348`
- `market_context_high->fx_24h` score `-1.0379` n `245` status `ready` deltaP `13.9654` edge `0.0393` maxDD `-4.2372`
- `market_context_high->crypto_alt_1h` score `-1.1119` n `305` status `ready` deltaP `1.6178` edge `0.03` maxDD `-6.6758`
- `market_context_high->index_4h` score `-1.2009` n `302` status `ready` deltaP `0.6249` edge `0.0106` maxDD `-3.165`
- `market_context_high->fx_4h` score `-1.4678` n `302` status `ready` deltaP `0.2836` edge `0.0033` maxDD `-2.1362`
- `market_context_high->commodity_4h` score `-2.4613` n `302` status `ready` deltaP `-3.389` edge `-0.0254` maxDD `-14.071`
- `market_context_high->index_24h` score `-2.827` n `245` status `ready` deltaP `3.2292` edge `0.0305` maxDD `-18.1572`
- `market_context_high->crypto_major_4h` score `-2.9849` n `302` status `ready` deltaP `7.4998` edge `0.1385` maxDD `-25.6458`
- `market_context_high->metal_4h` score `-3.8207` n `302` status `ready` deltaP `-5.2566` edge `-0.0474` maxDD `-11.5426`
- `market_context_high->crypto_alt_4h` score `-4.582` n `302` status `ready` deltaP `5.2819` edge `0.0838` maxDD `-28.7346`
- `market_context_high->metal_24h` score `-7.1114` n `245` status `ready` deltaP `-7.9337` edge `-0.2519` maxDD `-27.5543`
- `market_context_high->crypto_major_24h` score `-7.6412` n `245` status `ready` deltaP `1.369` edge `-0.1252` maxDD `-29.6555`
- `market_context_high->commodity_24h` score `-11.0371` n `245` status `ready` deltaP `-14.7668` edge `-0.0837` maxDD `-40.676`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-26T23:52:32.975294+00:00`
- Price records: `672`
- Market context records: `4878`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7594`

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

- `market_context_high->unknown_1h` score `15.2623` n `110` status `ready` deltaP `9.8721` edge `1.2478` maxDD `-1.674`
- `market_context_high->unknown_4h` score `9.6118` n `110` status `ready` deltaP `23.1624` edge `0.6997` maxDD `-1.917`
- `market_context_high->crypto_alt_4h` score `6.4556` n `110` status `ready` deltaP `21.2084` edge `0.5318` maxDD `-7.8181`
- `market_context_high->crypto_major_4h` score `6.1784` n `110` status `ready` deltaP `18.4922` edge `0.514` maxDD `-7.1265`
- `market_context_high->unknown_24h` score `5.1296` n `91` status `ready` deltaP `24.9485` edge `0.2954` maxDD `-1.4072`
- `market_context_high->metal_4h` score `1.1854` n `110` status `ready` deltaP `8.6724` edge `0.1072` maxDD `-1.9651`
- `market_context_high->equity_4h` score `0.8711` n `110` status `ready` deltaP `12.439` edge `0.1669` maxDD `-6.3852`
- `market_context_high->index_4h` score `0.5913` n `110` status `ready` deltaP `12.1452` edge `0.0411` maxDD `-0.7006`
- `market_context_high->crypto_major_1h` score `0.4703` n `110` status `ready` deltaP `6.4698` edge `0.121` maxDD `-5.6406`
- `market_context_high->crypto_alt_1h` score `0.4659` n `110` status `ready` deltaP `8.4703` edge `0.1055` maxDD `-5.5126`
- `market_context_high->equity_1h` score `0.2153` n `110` status `ready` deltaP `4.2352` edge `0.0591` maxDD `-2.779`
- `market_context_high->metal_1h` score `-0.169` n `110` status `ready` deltaP `0.8437` edge `0.0307` maxDD `-1.3057`
- `market_context_high->commodity_1h` score `-0.2285` n `110` status `ready` deltaP `3.2825` edge `0.0148` maxDD `-1.278`
- `market_context_high->index_1h` score `-0.4853` n `110` status `ready` deltaP `0.3103` edge `0.0112` maxDD `-0.7054`
- `market_context_high->fx_4h` score `-0.6355` n `110` status `ready` deltaP `1.5244` edge `0.0054` maxDD `-1.0967`
- `market_context_high->commodity_4h` score `-0.9362` n `110` status `ready` deltaP `5.6624` edge `0.0029` maxDD `-4.4933`
- `market_context_high->fx_1h` score `-1.3226` n `110` status `ready` deltaP `-6.7175` edge `-0.0041` maxDD `-0.5734`
- `market_context_high->fx_24h` score `-1.8066` n `91` status `ready` deltaP `-5.9887` edge `-0.0096` maxDD `-2.749`
- `market_context_high->index_24h` score `-4.6023` n `91` status `ready` deltaP `-6.1031` edge `-0.1408` maxDD `-24.6845`
- `market_context_high->commodity_24h` score `-5.0457` n `91` status `ready` deltaP `13.1105` edge `0.003` maxDD `-27.5371`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

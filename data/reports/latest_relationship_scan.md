# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-11T06:52:27.755349+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `5976`

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

- `market_context_high->unknown_4h` score `42.8067` n `85` status `ready` deltaP `-12.9484` edge `3.7116` maxDD `-2.3109`
- `market_context_high->equity_24h` score `9.6191` n `74` status `ready` deltaP `38.5322` edge `0.5876` maxDD `-1.0977`
- `market_context_high->crypto_major_24h` score `7.6953` n `74` status `ready` deltaP `13.9499` edge `1.2084` maxDD `-17.8526`
- `market_context_high->fx_4h` score `1.4483` n `85` status `ready` deltaP `20.6779` edge `0.0112` maxDD `-0.2692`
- `market_context_high->fx_1h` score `0.1132` n `97` status `ready` deltaP `5.5852` edge `0.0015` maxDD `-0.271`
- `market_context_high->crypto_major_4h` score `0.0734` n `85` status `ready` deltaP `6.5566` edge `0.1491` maxDD `-10.0052`
- `market_context_high->index_24h` score `-0.0113` n `74` status `ready` deltaP `9.6097` edge `0.0986` maxDD `-1.7962`
- `market_context_high->commodity_4h` score `-0.0523` n `85` status `ready` deltaP `6.1693` edge `0.0055` maxDD `-1.6002`
- `market_context_high->commodity_1h` score `-0.1165` n `97` status `ready` deltaP `2.5094` edge `0.007` maxDD `-0.3417`
- `market_context_high->crypto_major_1h` score `-0.131` n `97` status `ready` deltaP `4.9046` edge `0.0394` maxDD `-3.7778`
- `market_context_high->metal_1h` score `-0.6148` n `97` status `ready` deltaP `-3.0434` edge `0.001` maxDD `-0.7626`
- `market_context_high->metal_24h` score `-0.7229` n `74` status `ready` deltaP `1.4123` edge `0.0464` maxDD `-3.5466`
- `market_context_high->crypto_alt_1h` score `-0.8692` n `97` status `ready` deltaP `-2.6282` edge `0.022` maxDD `-4.9401`
- `market_context_high->fx_24h` score `-1.2714` n `74` status `ready` deltaP `0.3472` edge `0.0012` maxDD `-1.9877`
- `market_context_high->crypto_alt_24h` score `-1.3906` n `74` status `ready` deltaP `-0.0235` edge `0.4331` maxDD `-35.5652`
- `market_context_high->metal_4h` score `-1.4024` n `85` status `ready` deltaP `-13.7483` edge `0.0133` maxDD `-1.1153`
- `market_context_high->index_4h` score `-1.4775` n `85` status `ready` deltaP `-14.401` edge `-0.0002` maxDD `-1.1242`
- `market_context_high->index_1h` score `-1.7129` n `97` status `ready` deltaP `-8.0314` edge `-0.003` maxDD `-0.5627`
- `market_context_high->equity_1h` score `-1.8438` n `97` status `ready` deltaP `-8.8647` edge `-0.0076` maxDD `-2.2898`
- `market_context_high->equity_4h` score `-3.06` n `85` status `ready` deltaP `-13.2873` edge `-0.0081` maxDD `-6.3323`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

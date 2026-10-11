# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-11T06:37:25.236774+00:00`
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

- `market_context_high->unknown_4h` score `42.7575` n `85` status `ready` deltaP `-12.9484` edge `3.7075` maxDD `-2.3109`
- `market_context_high->equity_24h` score `9.6417` n `75` status `ready` deltaP `38.6944` edge `0.5884` maxDD `-1.0977`
- `market_context_high->crypto_major_24h` score `7.7817` n `75` status `ready` deltaP `14.5625` edge `1.2154` maxDD `-17.8526`
- `market_context_high->fx_4h` score `1.3639` n `85` status `ready` deltaP `19.6539` edge `0.011` maxDD `-0.2692`
- `market_context_high->crypto_major_4h` score `0.2309` n `85` status `ready` deltaP `7.5807` edge `0.1557` maxDD `-9.7973`
- `market_context_high->fx_1h` score `0.1124` n `97` status `ready` deltaP `5.5852` edge `0.0014` maxDD `-0.271`
- `market_context_high->commodity_4h` score `-0.0601` n `85` status `ready` deltaP `6.1693` edge `0.0045` maxDD `-1.6002`
- `market_context_high->index_24h` score `-0.0931` n `75` status `ready` deltaP `8.8889` edge `0.0975` maxDD `-1.8289`
- `market_context_high->commodity_1h` score `-0.1189` n `97` status `ready` deltaP `2.5094` edge `0.0068` maxDD `-0.3417`
- `market_context_high->crypto_major_1h` score `-0.1372` n `97` status `ready` deltaP `4.9046` edge `0.0386` maxDD `-3.7778`
- `market_context_high->metal_1h` score `-0.6164` n `97` status `ready` deltaP `-3.0434` edge `0.0008` maxDD `-0.7626`
- `market_context_high->metal_24h` score `-0.6967` n `75` status `ready` deltaP `2.0069` edge `0.0458` maxDD `-3.5466`
- `market_context_high->crypto_alt_1h` score `-0.8981` n `97` status `ready` deltaP `-2.6282` edge `0.0183` maxDD `-4.9401`
- `market_context_high->crypto_alt_24h` score `-1.2898` n `75` status `ready` deltaP `0.7152` edge `0.4411` maxDD `-35.5652`
- `market_context_high->fx_24h` score `-1.3572` n `75` status `ready` deltaP `-0.3195` edge `0.0001` maxDD `-2.0905`
- `market_context_high->metal_4h` score `-1.4024` n `85` status `ready` deltaP `-13.7483` edge `0.0133` maxDD `-1.1153`
- `market_context_high->index_4h` score `-1.4767` n `85` status `ready` deltaP `-14.401` edge `-0.0001` maxDD `-1.1242`
- `market_context_high->index_1h` score `-1.7117` n `97` status `ready` deltaP `-8.0314` edge `-0.0029` maxDD `-0.5627`
- `market_context_high->equity_1h` score `-1.8426` n `97` status `ready` deltaP `-8.8647` edge `-0.0075` maxDD `-2.2898`
- `market_context_high->equity_4h` score `-2.9561` n `85` status `ready` deltaP `-12.2633` edge `-0.0072` maxDD `-6.2576`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-10T13:52:29.026963+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7647`

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

- `market_context_high->unknown_4h` score `40.8761` n `91` status `ready` deltaP `-6.3404` edge `3.5025` maxDD `-2.3109`
- `market_context_high->equity_24h` score `10.0636` n `91` status `ready` deltaP `38.4635` edge `0.6251` maxDD `-1.0977`
- `market_context_high->crypto_major_24h` score `9.2992` n `91` status `ready` deltaP `20.8696` edge `1.3679` maxDD `-17.8526`
- `market_context_high->crypto_alt_24h` score `1.7622` n `91` status `ready` deltaP `10.0578` edge `0.7701` maxDD `-35.5652`
- `market_context_high->crypto_major_4h` score `1.4913` n `91` status `ready` deltaP `17.554` edge `0.2072` maxDD `-6.9761`
- `market_context_high->crypto_major_1h` score `0.1665` n `91` status `ready` deltaP `9.2453` edge `0.0486` maxDD `-3.7778`
- `market_context_high->fx_1h` score `0.1637` n `91` status `ready` deltaP `5.4995` edge `0.0012` maxDD `-0.271`
- `market_context_high->index_24h` score `-0.1376` n `91` status `ready` deltaP `12.1965` edge `0.092` maxDD `-1.9432`
- `market_context_high->fx_4h` score `-0.1696` n `91` status `ready` deltaP `7.9118` edge `0.0078` maxDD `-0.3077`
- `market_context_high->metal_1h` score `-0.3217` n `91` status `ready` deltaP `3.4481` edge `0.0014` maxDD `-0.7626`
- `market_context_high->commodity_1h` score `-0.3411` n `91` status `ready` deltaP `0.8522` edge `0.0035` maxDD `-0.3417`
- `market_context_high->metal_24h` score `-0.4337` n `91` status `ready` deltaP `5.5041` edge `0.0562` maxDD `-3.5466`
- `market_context_high->commodity_4h` score `-0.63` n `91` status `ready` deltaP `-0.8794` edge `-0.0049` maxDD `-1.6002`
- `market_context_high->unknown_1h` score `-0.8788` n `91` status `ready` deltaP `-4.667` edge `-0.0006` maxDD `-0.9885`
- `market_context_high->crypto_alt_4h` score `-0.9179` n `91` status `ready` deltaP `-6.1897` edge `0.1169` maxDD `-8.7986`
- `market_context_high->equity_1h` score `-0.9617` n `91` status `ready` deltaP `-5.1868` edge `-0.0047` maxDD `-2.0542`
- `market_context_high->metal_4h` score `-1.0132` n `91` status `ready` deltaP `-6.3807` edge `0.0134` maxDD `-1.0609`
- `market_context_high->crypto_alt_1h` score `-1.1508` n `91` status `ready` deltaP `-2.0941` edge `0.0319` maxDD `-4.7735`
- `market_context_high->index_1h` score `-1.2255` n `91` status `ready` deltaP `-10.1879` edge `-0.003` maxDD `-0.5627`
- `market_context_high->index_4h` score `-1.3096` n `91` status `ready` deltaP `-11.3224` edge `0.0008` maxDD `-1.1242`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

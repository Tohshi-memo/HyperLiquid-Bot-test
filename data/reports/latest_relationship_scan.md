# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-11T00:07:31.006350+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `5511`

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

- `market_context_high->unknown_4h` score `39.8714` n `91` status `ready` deltaP `-7.5599` edge `3.4269` maxDD `-2.3109`
- `market_context_high->equity_24h` score `10.0715` n `91` status `ready` deltaP `38.5474` edge `0.6252` maxDD `-1.0977`
- `market_context_high->crypto_major_24h` score `9.402` n `91` status `ready` deltaP `20.9707` edge `1.3804` maxDD `-17.8526`
- `market_context_high->crypto_major_4h` score `1.5181` n `91` status `ready` deltaP `17.8588` edge `0.2086` maxDD `-6.9761`
- `market_context_high->crypto_alt_24h` score `0.9934` n `91` status `ready` deltaP `10.1534` edge `0.6709` maxDD `-35.5652`
- `market_context_high->crypto_major_1h` score `0.242` n `91` status `ready` deltaP `10.4429` edge `0.0503` maxDD `-3.7778`
- `market_context_high->fx_1h` score `0.1649` n `91` status `ready` deltaP `5.4995` edge `0.0013` maxDD `-0.271`
- `market_context_high->fx_4h` score `0.0047` n `91` status `ready` deltaP `10.0459` edge `0.0081` maxDD `-0.3077`
- `market_context_high->index_24h` score `-0.3264` n `91` status `ready` deltaP `8.8218` edge `0.0903` maxDD `-1.9432`
- `market_context_high->commodity_1h` score `-0.3495` n `91` status `ready` deltaP `0.7025` edge `0.0038` maxDD `-0.3417`
- `market_context_high->metal_24h` score `-0.3809` n `91` status `ready` deltaP `6.4446` edge `0.0567` maxDD `-3.5466`
- `market_context_high->metal_1h` score `-0.3816` n `91` status `ready` deltaP `2.6996` edge `0.0014` maxDD `-0.7626`
- `market_context_high->commodity_4h` score `-0.6703` n `91` status `ready` deltaP `-1.4892` edge `-0.006` maxDD `-1.6002`
- `market_context_high->equity_1h` score `-0.9196` n `91` status `ready` deltaP `-4.4383` edge `-0.0043` maxDD `-2.0542`
- `market_context_high->crypto_alt_4h` score `-0.9677` n `91` status `ready` deltaP `-6.0373` edge `0.1095` maxDD `-8.7986`
- `market_context_high->metal_4h` score `-0.9887` n `91` status `ready` deltaP `-5.9234` edge `0.0135` maxDD `-1.0609`
- `market_context_high->index_1h` score `-1.1072` n `91` status `ready` deltaP `-7.9424` edge `-0.0028` maxDD `-0.5627`
- `market_context_high->crypto_alt_1h` score `-1.1544` n `91` status `ready` deltaP `-2.0941` edge `0.0316` maxDD `-4.7735`
- `market_context_high->index_4h` score `-1.2091` n `91` status `ready` deltaP `-9.4931` edge `0.0015` maxDD `-1.1242`
- `market_context_high->equity_4h` score `-1.2501` n `91` status `ready` deltaP `-3.439` edge `0.0096` maxDD `-5.4217`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

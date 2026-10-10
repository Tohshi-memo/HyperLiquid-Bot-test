# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-10T23:52:27.108714+00:00`
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

- `market_context_high->unknown_4h` score `39.9088` n `91` status `ready` deltaP `-7.4075` edge `3.429` maxDD `-2.3109`
- `market_context_high->equity_24h` score `10.0703` n `91` status `ready` deltaP `38.5474` edge `0.6251` maxDD `-1.0977`
- `market_context_high->crypto_major_24h` score `9.3918` n `91` status `ready` deltaP `20.9707` edge `1.3791` maxDD `-17.8526`
- `market_context_high->crypto_major_4h` score `1.5086` n `91` status `ready` deltaP `17.7064` edge `0.2084` maxDD `-6.9761`
- `market_context_high->crypto_alt_24h` score `1.0059` n `91` status `ready` deltaP `10.1534` edge `0.6725` maxDD `-35.5652`
- `market_context_high->crypto_major_1h` score `0.2319` n `91` status `ready` deltaP `10.2932` edge `0.05` maxDD `-3.7778`
- `market_context_high->fx_1h` score `0.1649` n `91` status `ready` deltaP `5.4995` edge `0.0013` maxDD `-0.271`
- `market_context_high->fx_4h` score `0.0169` n `91` status `ready` deltaP `10.1984` edge `0.0081` maxDD `-0.3077`
- `market_context_high->index_24h` score `-0.3174` n `91` status `ready` deltaP `8.9954` edge `0.0903` maxDD `-1.9432`
- `market_context_high->commodity_1h` score `-0.3363` n `91` status `ready` deltaP `0.8522` edge `0.0039` maxDD `-0.3417`
- `market_context_high->metal_1h` score `-0.3816` n `91` status `ready` deltaP `2.6996` edge `0.0014` maxDD `-0.7626`
- `market_context_high->metal_24h` score `-0.3899` n `91` status `ready` deltaP `6.271` edge `0.0567` maxDD `-3.5466`
- `market_context_high->commodity_4h` score `-0.6592` n `91` status `ready` deltaP `-1.3367` edge `-0.0056` maxDD `-1.6002`
- `market_context_high->equity_1h` score `-0.9282` n `91` status `ready` deltaP `-4.588` edge `-0.0044` maxDD `-2.0542`
- `market_context_high->crypto_alt_4h` score `-0.9764` n `91` status `ready` deltaP `-6.1897` edge `0.1094` maxDD `-8.7986`
- `market_context_high->metal_4h` score `-0.9799` n `91` status `ready` deltaP `-5.7709` edge `0.0136` maxDD `-1.0609`
- `market_context_high->index_1h` score `-1.1072` n `91` status `ready` deltaP `-7.9424` edge `-0.0028` maxDD `-0.5627`
- `market_context_high->crypto_alt_1h` score `-1.1699` n `91` status `ready` deltaP `-2.2438` edge `0.0313` maxDD `-4.7735`
- `market_context_high->index_4h` score `-1.2011` n `91` status `ready` deltaP `-9.3407` edge `0.0015` maxDD `-1.1242`
- `market_context_high->equity_4h` score `-1.2501` n `91` status `ready` deltaP `-3.439` edge `0.0096` maxDD `-5.4217`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

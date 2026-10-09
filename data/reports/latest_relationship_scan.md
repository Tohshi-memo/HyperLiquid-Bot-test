# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-09T10:37:33.697826+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8370`

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

- `market_context_high->unknown_4h` score `40.1599` n `91` status `ready` deltaP `-5.2734` edge `3.4357` maxDD `-2.3109`
- `market_context_high->equity_24h` score `10.1783` n `90` status `ready` deltaP `34.1667` edge `0.6633` maxDD `-1.0977`
- `market_context_high->crypto_major_24h` score `10.03` n `90` status `ready` deltaP `22.3611` edge `1.4342` maxDD `-16.7906`
- `market_context_high->crypto_alt_24h` score `3.5673` n `90` status `ready` deltaP `14.0625` edge `0.9574` maxDD `-34.5048`
- `market_context_high->crypto_major_4h` score `1.928` n `91` status `ready` deltaP `18.3162` edge `0.2581` maxDD `-6.9761`
- `market_context_high->metal_24h` score `0.637` n `90` status `ready` deltaP `15.0694` edge `0.1297` maxDD `-3.5466`
- `market_context_high->crypto_major_1h` score `0.3279` n `91` status `ready` deltaP `10.1435` edge `0.0633` maxDD `-3.7778`
- `market_context_high->fx_1h` score `0.2691` n `91` status `ready` deltaP `6.8468` edge `0.001` maxDD `-0.271`
- `market_context_high->fx_4h` score `0.0953` n `91` status `ready` deltaP `11.4179` edge `0.0065` maxDD `-0.3077`
- `market_context_high->metal_1h` score `-0.2079` n `91` status `ready` deltaP `4.496` edge `0.0039` maxDD `-0.7626`
- `market_context_high->index_24h` score `-0.3282` n `90` status `ready` deltaP `7.8125` edge `0.0968` maxDD `-1.9432`
- `market_context_high->crypto_alt_4h` score `-0.3871` n `91` status `ready` deltaP `-6.6471` edge `0.188` maxDD `-8.7986`
- `market_context_high->commodity_1h` score `-0.4035` n `91` status `ready` deltaP `0.7025` edge `-0.0007` maxDD `-0.3417`
- `market_context_high->crypto_alt_1h` score `-0.8221` n `91` status `ready` deltaP `-1.3456` edge `0.0543` maxDD `-4.7735`
- `market_context_high->metal_4h` score `-0.8406` n `91` status `ready` deltaP `-4.2466` edge `0.0213` maxDD `-1.0609`
- `market_context_high->equity_1h` score `-0.8433` n `91` status `ready` deltaP `-2.7916` edge `-0.0055` maxDD `-2.0542`
- `market_context_high->commodity_4h` score `-0.9301` n `91` status `ready` deltaP `-3.4709` edge `-0.0261` maxDD `-1.6002`
- `market_context_high->index_1h` score `-1.2318` n `91` status `ready` deltaP `-10.1879` edge `-0.0038` maxDD `-0.5627`
- `market_context_high->index_4h` score `-1.3718` n `91` status `ready` deltaP `-11.9322` edge `-0.0031` maxDD `-1.1242`
- `market_context_high->equity_4h` score `-1.4027` n `91` status `ready` deltaP `-4.9634` edge `0.0002` maxDD `-5.4217`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

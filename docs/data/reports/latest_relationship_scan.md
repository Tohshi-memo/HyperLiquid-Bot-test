# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-09T20:07:29.137000+00:00`
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

- `market_context_high->unknown_4h` score `40.9495` n `91` status `ready` deltaP `-4.3889` edge `3.4956` maxDD `-2.3109`
- `market_context_high->equity_24h` score `9.7557` n `91` status `ready` deltaP `33.2641` edge `0.6341` maxDD `-1.0977`
- `market_context_high->crypto_major_24h` score `8.4804` n `91` status `ready` deltaP `18.4433` edge `1.2791` maxDD `-17.8526`
- `market_context_high->crypto_alt_24h` score `1.7076` n `91` status `ready` deltaP `10.0578` edge `0.7631` maxDD `-35.5652`
- `market_context_high->crypto_major_4h` score `1.5027` n `91` status `ready` deltaP `18.0892` edge `0.2051` maxDD `-6.9761`
- `market_context_high->fx_1h` score `0.299` n `91` status `ready` deltaP `7.1462` edge `0.0015` maxDD `-0.271`
- `market_context_high->crypto_major_1h` score `0.2834` n `91` status `ready` deltaP `10.2932` edge `0.0566` maxDD `-3.7778`
- `market_context_high->fx_4h` score `0.2022` n `91` status `ready` deltaP `12.4091` edge `0.0088` maxDD `-0.3077`
- `market_context_high->metal_24h` score `0.0281` n `91` status `ready` deltaP `10.5301` edge `0.0819` maxDD `-3.5466`
- `market_context_high->metal_1h` score `-0.3158` n `91` status `ready` deltaP `3.5978` edge `0.0009` maxDD `-0.7626`
- `market_context_high->commodity_1h` score `-0.3315` n `91` status `ready` deltaP `1.1516` edge `0.0023` maxDD `-0.3417`
- `market_context_high->index_24h` score `-0.3442` n `91` status `ready` deltaP `7.8638` edge `0.0944` maxDD `-1.9432`
- `market_context_high->commodity_4h` score `-0.7457` n `91` status `ready` deltaP `-1.7094` edge `-0.0142` maxDD `-1.6002`
- `market_context_high->equity_1h` score `-0.876` n `91` status `ready` deltaP `-3.5401` edge `-0.0047` maxDD `-2.0542`
- `market_context_high->crypto_alt_1h` score `-0.9013` n `91` status `ready` deltaP `-1.3456` edge `0.0477` maxDD `-4.7735`
- `market_context_high->crypto_alt_4h` score `-0.9268` n `91` status `ready` deltaP `-7.1705` edge `0.1223` maxDD `-8.7986`
- `market_context_high->metal_4h` score `-0.9491` n `91` status `ready` deltaP `-5.0881` edge `0.013` maxDD `-1.0609`
- `market_context_high->index_1h` score `-1.2107` n `91` status `ready` deltaP `-9.8885` edge `-0.0031` maxDD `-0.5627`
- `market_context_high->index_4h` score `-1.2343` n `91` status `ready` deltaP `-9.8734` edge `0.0008` maxDD `-1.1242`
- `market_context_high->equity_4h` score `-1.2953` n `91` status `ready` deltaP `-4.2634` edge `0.0093` maxDD `-5.4217`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

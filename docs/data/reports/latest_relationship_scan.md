# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-10T05:37:28.060068+00:00`
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

- `market_context_high->unknown_4h` score `40.8351` n `91` status `ready` deltaP `-6.4929` edge `3.5001` maxDD `-2.3109`
- `market_context_high->equity_24h` score `9.3741` n `91` status `ready` deltaP `33.2641` edge `0.6023` maxDD `-1.0977`
- `market_context_high->crypto_major_24h` score `8.7429` n `91` status `ready` deltaP `18.6166` edge `1.3116` maxDD `-17.8526`
- `market_context_high->crypto_alt_24h` score `1.5968` n `91` status `ready` deltaP `10.0578` edge `0.7489` maxDD `-35.5652`
- `market_context_high->crypto_major_4h` score `1.4323` n `91` status `ready` deltaP `16.9442` edge `0.2037` maxDD `-6.9761`
- `market_context_high->fx_1h` score `0.2248` n `91` status `ready` deltaP `6.248` edge `0.0013` maxDD `-0.271`
- `market_context_high->crypto_major_1h` score `0.1789` n `91` status `ready` deltaP `9.5447` edge `0.0482` maxDD `-3.7778`
- `market_context_high->fx_4h` score `0.0059` n `91` status `ready` deltaP `10.0459` edge `0.0082` maxDD `-0.3077`
- `market_context_high->metal_1h` score `-0.2966` n `91` status `ready` deltaP `3.7475` edge `0.0015` maxDD `-0.7626`
- `market_context_high->commodity_1h` score `-0.3483` n `91` status `ready` deltaP `0.8522` edge `0.0029` maxDD `-0.3417`
- `market_context_high->index_24h` score `-0.377` n `91` status `ready` deltaP `7.8638` edge `0.0902` maxDD `-1.9432`
- `market_context_high->metal_24h` score `-0.3903` n `91` status `ready` deltaP `6.024` edge `0.0583` maxDD `-3.5466`
- `market_context_high->commodity_4h` score `-0.7005` n `91` status `ready` deltaP `-1.3367` edge `-0.0109` maxDD `-1.6002`
- `market_context_high->equity_1h` score `-0.9313` n `91` status `ready` deltaP `-4.588` edge `-0.0048` maxDD `-2.0542`
- `market_context_high->metal_4h` score `-0.9974` n `91` status `ready` deltaP `-6.0758` edge `0.0134` maxDD `-1.0609`
- `market_context_high->unknown_1h` score `-1.0073` n `91` status `ready` deltaP `-4.0682` edge `-0.0153` maxDD `-0.9885`
- `market_context_high->crypto_alt_4h` score `-1.0775` n `91` status `ready` deltaP `-7.7141` edge `0.1066` maxDD `-8.7986`
- `market_context_high->crypto_alt_1h` score `-1.1688` n `91` status `ready` deltaP `-2.0941` edge `0.0304` maxDD `-4.7735`
- `market_context_high->index_1h` score `-1.2419` n `91` status `ready` deltaP `-10.4873` edge `-0.0031` maxDD `-0.5627`
- `market_context_high->index_4h` score `-1.2636` n `91` status `ready` deltaP `-10.4078` edge `0.0006` maxDD `-1.1242`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

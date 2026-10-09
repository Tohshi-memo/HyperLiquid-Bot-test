# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-09T14:07:29.204957+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8541`

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

- `market_context_high->unknown_4h` score `40.2451` n `91` status `ready` deltaP `-5.2734` edge `3.4428` maxDD `-2.3109`
- `market_context_high->equity_24h` score `10.2609` n `91` status `ready` deltaP `34.5543` edge `0.6676` maxDD `-1.0977`
- `market_context_high->crypto_major_24h` score `9.4802` n `91` status `ready` deltaP `21.6652` edge `1.3858` maxDD `-17.8526`
- `market_context_high->crypto_alt_24h` score `3.1079` n `91` status `ready` deltaP `13.452` edge `0.92` maxDD `-35.5652`
- `market_context_high->crypto_major_4h` score `1.9478` n `91` status `ready` deltaP `18.7735` edge `0.2576` maxDD `-6.9761`
- `market_context_high->metal_24h` score `0.4153` n `91` status `ready` deltaP `13.0419` edge `0.1148` maxDD `-3.5466`
- `market_context_high->crypto_major_1h` score `0.3731` n `91` status `ready` deltaP `10.5926` edge `0.0661` maxDD `-3.7778`
- `market_context_high->fx_1h` score `0.2823` n `91` status `ready` deltaP `6.9965` edge `0.0011` maxDD `-0.271`
- `market_context_high->fx_4h` score `0.2108` n `91` status `ready` deltaP `12.6374` edge `0.008` maxDD `-0.3077`
- `market_context_high->crypto_alt_4h` score `-0.1486` n `91` status `ready` deltaP `-4.9702` edge `0.2074` maxDD `-8.7986`
- `market_context_high->metal_1h` score `-0.2391` n `91` status `ready` deltaP `4.1966` edge `0.0033` maxDD `-0.7626`
- `market_context_high->index_24h` score `-0.2456` n `91` status `ready` deltaP `8.9954` edge `0.0995` maxDD `-1.9432`
- `market_context_high->commodity_1h` score `-0.4933` n `91` status `ready` deltaP `-0.1957` edge `-0.0022` maxDD `-0.3417`
- `market_context_high->crypto_alt_1h` score `-0.7322` n `91` status `ready` deltaP `-0.7468` edge `0.0578` maxDD `-4.7735`
- `market_context_high->metal_4h` score `-0.812` n `91` status `ready` deltaP `-3.6368` edge `0.0209` maxDD `-1.0609`
- `market_context_high->equity_1h` score `-0.8488` n `91` status `ready` deltaP `-3.091` edge `-0.0042` maxDD `-2.0542`
- `market_context_high->commodity_4h` score `-0.9086` n `91` status `ready` deltaP `-3.0136` edge `-0.0264` maxDD `-1.6002`
- `market_context_high->index_1h` score `-1.1967` n `91` status `ready` deltaP `-9.5891` edge `-0.0033` maxDD `-0.5627`
- `market_context_high->index_4h` score `-1.228` n `91` status `ready` deltaP `-9.798` edge `0.0011` maxDD `-1.1242`
- `market_context_high->equity_4h` score `-1.2488` n `91` status `ready` deltaP `-3.7439` edge `0.0118` maxDD `-5.4217`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

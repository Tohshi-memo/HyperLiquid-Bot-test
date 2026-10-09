# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-09T22:52:23.221804+00:00`
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

- `market_context_high->unknown_4h` score `40.8971` n `91` status `ready` deltaP `-4.9685` edge `3.4951` maxDD `-2.3109`
- `market_context_high->equity_24h` score `9.6129` n `91` status `ready` deltaP `33.2641` edge `0.6222` maxDD `-1.0977`
- `market_context_high->crypto_major_24h` score `8.5779` n `91` status `ready` deltaP `18.4433` edge `1.2916` maxDD `-17.8526`
- `market_context_high->crypto_alt_24h` score `1.7263` n `91` status `ready` deltaP `10.0578` edge `0.7655` maxDD `-35.5652`
- `market_context_high->crypto_major_4h` score `1.5429` n `91` status `ready` deltaP `18.621` edge `0.2067` maxDD `-6.9761`
- `market_context_high->fx_1h` score `0.2487` n `91` status `ready` deltaP `6.5474` edge `0.0013` maxDD `-0.271`
- `market_context_high->crypto_major_1h` score `0.1813` n `91` status `ready` deltaP `9.8441` edge `0.0465` maxDD `-3.7778`
- `market_context_high->fx_4h` score `0.1047` n `91` status `ready` deltaP `11.2654` edge `0.0083` maxDD `-0.3077`
- `market_context_high->metal_24h` score `-0.0914` n `91` status `ready` deltaP `9.8368` edge `0.0712` maxDD `-3.5466`
- `market_context_high->metal_1h` score `-0.2607` n `91` status `ready` deltaP `4.1966` edge `0.0015` maxDD `-0.7626`
- `market_context_high->commodity_1h` score `-0.2656` n `91` status `ready` deltaP `1.7504` edge `0.0038` maxDD `-0.3417`
- `market_context_high->index_24h` score `-0.3551` n `91` status `ready` deltaP `7.8638` edge `0.093` maxDD `-1.9432`
- `market_context_high->commodity_4h` score `-0.6013` n `91` status `ready` deltaP `-0.1172` edge `-0.0063` maxDD `-1.6002`
- `market_context_high->equity_1h` score `-0.8893` n `91` status `ready` deltaP `-3.8395` edge `-0.0044` maxDD `-2.0542`
- `market_context_high->metal_4h` score `-0.9316` n `91` status `ready` deltaP `-4.8563` edge `0.0137` maxDD `-1.0609`
- `market_context_high->crypto_alt_4h` score `-0.9421` n `91` status `ready` deltaP `-7.1044` edge `0.1199` maxDD `-8.7986`
- `market_context_high->crypto_alt_1h` score `-1.2071` n `91` status `ready` deltaP `-2.3935` edge `0.0292` maxDD `-4.7735`
- `market_context_high->index_1h` score `-1.2092` n `91` status `ready` deltaP `-9.8885` edge `-0.0029` maxDD `-0.5627`
- `market_context_high->index_4h` score `-1.2383` n `91` status `ready` deltaP `-9.9505` edge `0.0008` maxDD `-1.1242`
- `market_context_high->equity_4h` score `-1.2738` n `91` status `ready` deltaP `-3.8964` edge `0.0096` maxDD `-5.4217`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

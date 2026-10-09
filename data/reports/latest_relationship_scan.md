# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-09T18:52:30.828403+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7791`

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

- `market_context_high->unknown_4h` score `41.0995` n `91` status `ready` deltaP `-4.3889` edge `3.5081` maxDD `-2.3109`
- `market_context_high->equity_24h` score `9.8799` n `91` status `ready` deltaP `33.4375` edge `0.6433` maxDD `-1.0977`
- `market_context_high->crypto_major_24h` score `8.5859` n `91` status `ready` deltaP `19.1365` edge `1.288` maxDD `-17.8526`
- `market_context_high->crypto_alt_24h` score `1.9149` n `91` status `ready` deltaP `10.9243` edge `0.7839` maxDD `-35.5652`
- `market_context_high->crypto_major_4h` score `1.5768` n `91` status `ready` deltaP `18.0892` edge `0.2146` maxDD `-6.9761`
- `market_context_high->crypto_major_1h` score `0.2922` n `91` status `ready` deltaP `10.3731` edge `0.0572` maxDD `-3.7778`
- `market_context_high->fx_1h` score `0.2683` n `91` status `ready` deltaP `6.7774` edge `0.0014` maxDD `-0.271`
- `market_context_high->fx_4h` score `0.2277` n `91` status `ready` deltaP `12.7135` edge `0.0089` maxDD `-0.3077`
- `market_context_high->metal_24h` score `0.0632` n `91` status `ready` deltaP `10.5301` edge `0.0864` maxDD `-3.5466`
- `market_context_high->index_24h` score `-0.3341` n `91` status `ready` deltaP `7.8638` edge `0.0957` maxDD `-1.9432`
- `market_context_high->metal_1h` score `-0.3359` n `91` status `ready` deltaP `3.3756` edge `0.0007` maxDD `-0.7626`
- `market_context_high->commodity_1h` score `-0.3935` n `91` status `ready` deltaP `0.6324` edge `0.0006` maxDD `-0.3417`
- `market_context_high->crypto_alt_4h` score `-0.737` n `91` status `ready` deltaP `-6.8661` edge `0.1446` maxDD `-8.7986`
- `market_context_high->commodity_4h` score `-0.8289` n `91` status `ready` deltaP `-2.4704` edge `-0.0198` maxDD `-1.6002`
- `market_context_high->crypto_alt_1h` score `-0.8517` n `91` status `ready` deltaP `-1.2664` edge `0.0513` maxDD `-4.7735`
- `market_context_high->equity_1h` score `-0.8685` n `91` status `ready` deltaP `-3.456` edge `-0.0043` maxDD `-2.0542`
- `market_context_high->metal_4h` score `-0.9712` n `91` status `ready` deltaP `-5.3925` edge `0.0122` maxDD `-1.0609`
- `market_context_high->index_1h` score `-1.1904` n `91` status `ready` deltaP `-9.5124` edge `-0.003` maxDD `-0.5627`
- `market_context_high->index_4h` score `-1.2335` n `91` status `ready` deltaP `-9.8734` edge `0.0009` maxDD `-1.1242`
- `market_context_high->equity_4h` score `-1.2701` n `91` status `ready` deltaP `-3.959` edge `0.0105` maxDD `-5.4217`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

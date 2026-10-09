# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-09T16:22:36.644125+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7887`

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

- `market_context_high->unknown_4h` score `40.3627` n `91` status `ready` deltaP `-5.2734` edge `3.4526` maxDD `-2.3109`
- `market_context_high->equity_24h` score `10.2885` n `91` status `ready` deltaP `34.5543` edge `0.6699` maxDD `-1.0977`
- `market_context_high->crypto_major_24h` score `9.1051` n `91` status `ready` deltaP `20.7971` edge `1.3435` maxDD `-17.8526`
- `market_context_high->crypto_alt_24h` score `2.6852` n `91` status `ready` deltaP `12.584` edge `0.8716` maxDD `-35.5652`
- `market_context_high->crypto_major_4h` score `1.776` n `91` status `ready` deltaP `18.4686` edge `0.2376` maxDD `-6.9761`
- `market_context_high->crypto_major_1h` score `0.3458` n `91` status `ready` deltaP `10.5926` edge `0.0626` maxDD `-3.7778`
- `market_context_high->fx_1h` score `0.311` n `91` status `ready` deltaP `7.2959` edge `0.0015` maxDD `-0.271`
- `market_context_high->fx_4h` score `0.2838` n `91` status `ready` deltaP `13.3996` edge `0.009` maxDD `-0.3077`
- `market_context_high->metal_24h` score `0.2093` n `91` status `ready` deltaP `11.4794` edge `0.0988` maxDD `-3.5466`
- `market_context_high->index_24h` score `-0.2531` n `91` status `ready` deltaP `8.8218` edge `0.0997` maxDD `-1.9432`
- `market_context_high->metal_1h` score `-0.2534` n `91` status `ready` deltaP `4.0469` edge `0.0031` maxDD `-0.7626`
- `market_context_high->crypto_alt_4h` score `-0.2714` n `91` status `ready` deltaP `-5.4275` edge `0.1947` maxDD `-8.7986`
- `market_context_high->commodity_1h` score `-0.546` n `91` status `ready` deltaP `-0.6448` edge `-0.0036` maxDD `-0.3417`
- `market_context_high->crypto_alt_1h` score `-0.7657` n `91` status `ready` deltaP `-0.8965` edge `0.056` maxDD `-4.7735`
- `market_context_high->equity_1h` score `-0.7677` n `91` status `ready` deltaP `-2.3425` edge `0.0012` maxDD `-2.0542`
- `market_context_high->commodity_4h` score `-0.918` n `91` status `ready` deltaP `-3.0136` edge `-0.0276` maxDD `-1.6002`
- `market_context_high->metal_4h` score `-0.938` n `91` status `ready` deltaP `-5.0088` edge `0.0139` maxDD `-1.0609`
- `market_context_high->index_1h` score `-1.1477` n `91` status `ready` deltaP `-8.8406` edge `-0.002` maxDD `-0.5627`
- `market_context_high->equity_4h` score `-1.1875` n `91` status `ready` deltaP `-3.2866` edge `0.0166` maxDD `-5.4217`
- `market_context_high->index_4h` score `-1.1972` n `91` status `ready` deltaP `-9.3407` edge `0.002` maxDD `-1.1242`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-10T15:52:29.503676+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6186`

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

- `market_context_high->unknown_4h` score `40.6823` n `91` status `ready` deltaP `-6.7978` edge `3.4894` maxDD `-2.3109`
- `market_context_high->equity_24h` score `10.0396` n `91` status `ready` deltaP `38.4635` edge `0.6231` maxDD `-1.0977`
- `market_context_high->crypto_major_24h` score `9.3374` n `91` status `ready` deltaP `20.8696` edge `1.3728` maxDD `-17.8526`
- `market_context_high->crypto_alt_24h` score `1.6553` n `91` status `ready` deltaP `10.0578` edge `0.7564` maxDD `-35.5652`
- `market_context_high->crypto_major_4h` score `1.4734` n `91` status `ready` deltaP `17.554` edge `0.2049` maxDD `-6.9761`
- `market_context_high->crypto_major_1h` score `0.1439` n `91` status `ready` deltaP `9.2453` edge `0.0457` maxDD `-3.7778`
- `market_context_high->fx_1h` score `0.1158` n `91` status `ready` deltaP `4.9007` edge `0.0012` maxDD `-0.271`
- `market_context_high->index_24h` score `-0.14` n `91` status `ready` deltaP `12.1965` edge `0.0917` maxDD `-1.9432`
- `market_context_high->fx_4h` score `-0.1708` n `91` status `ready` deltaP `7.9118` edge `0.0077` maxDD `-0.3077`
- `market_context_high->commodity_1h` score `-0.3219` n `91` status `ready` deltaP `1.0019` edge `0.0041` maxDD `-0.3417`
- `market_context_high->metal_1h` score `-0.3696` n `91` status `ready` deltaP `2.8493` edge `0.0014` maxDD `-0.7626`
- `market_context_high->metal_24h` score `-0.4525` n `91` status `ready` deltaP `5.1574` edge `0.0561` maxDD `-3.5466`
- `market_context_high->commodity_4h` score `-0.6214` n `91` status `ready` deltaP `-0.8794` edge `-0.0038` maxDD `-1.6002`
- `market_context_high->unknown_1h` score `-0.8801` n `91` status `ready` deltaP `-4.5173` edge `-0.0017` maxDD `-0.9885`
- `market_context_high->crypto_alt_4h` score `-0.921` n `91` status `ready` deltaP `-6.1897` edge `0.1165` maxDD `-8.7986`
- `market_context_high->equity_1h` score `-1.013` n `91` status `ready` deltaP `-6.085` edge `-0.0053` maxDD `-2.0542`
- `market_context_high->metal_4h` score `-1.0298` n `91` status `ready` deltaP `-6.6856` edge `0.0133` maxDD `-1.0609`
- `market_context_high->index_1h` score `-1.2107` n `91` status `ready` deltaP `-9.8885` edge `-0.0031` maxDD `-0.5627`
- `market_context_high->crypto_alt_1h` score `-1.2311` n `91` status `ready` deltaP `-2.5432` edge `0.0282` maxDD `-4.7735`
- `market_context_high->index_4h` score `-1.2843` n `91` status `ready` deltaP `-10.8651` edge `0.001` maxDD `-1.1242`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

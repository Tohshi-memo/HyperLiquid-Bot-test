# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-10T16:52:26.628985+00:00`
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

- `market_context_high->unknown_4h` score `40.5764` n `91` status `ready` deltaP `-7.1026` edge `3.4826` maxDD `-2.3109`
- `market_context_high->equity_24h` score `10.0348` n `91` status `ready` deltaP `38.4635` edge `0.6227` maxDD `-1.0977`
- `market_context_high->crypto_major_24h` score `9.3554` n `91` status `ready` deltaP `20.8696` edge `1.3751` maxDD `-17.8526`
- `market_context_high->crypto_alt_24h` score `1.6046` n `91` status `ready` deltaP `10.0578` edge `0.7499` maxDD `-35.5652`
- `market_context_high->crypto_major_4h` score `1.4788` n `91` status `ready` deltaP `17.554` edge `0.2056` maxDD `-6.9761`
- `market_context_high->crypto_major_1h` score `0.1937` n `91` status `ready` deltaP `9.8441` edge `0.0481` maxDD `-3.7778`
- `market_context_high->fx_1h` score `0.1278` n `91` status `ready` deltaP `5.0504` edge `0.0012` maxDD `-0.271`
- `market_context_high->index_24h` score `-0.1415` n `91` status `ready` deltaP `12.1965` edge `0.0915` maxDD `-1.9432`
- `market_context_high->fx_4h` score `-0.1708` n `91` status `ready` deltaP `7.9118` edge `0.0077` maxDD `-0.3077`
- `market_context_high->commodity_1h` score `-0.28` n `91` status `ready` deltaP `1.451` edge `0.0046` maxDD `-0.3417`
- `market_context_high->metal_1h` score `-0.3816` n `91` status `ready` deltaP `2.6996` edge `0.0014` maxDD `-0.7626`
- `market_context_high->metal_24h` score `-0.4525` n `91` status `ready` deltaP `5.1574` edge `0.0561` maxDD `-3.5466`
- `market_context_high->commodity_4h` score `-0.6309` n `91` status `ready` deltaP `-1.0318` edge `-0.004` maxDD `-1.6002`
- `market_context_high->crypto_alt_4h` score `-0.9335` n `91` status `ready` deltaP `-6.1897` edge `0.1149` maxDD `-8.7986`
- `market_context_high->equity_1h` score `-0.9959` n `91` status `ready` deltaP `-5.7856` edge `-0.0051` maxDD `-2.0542`
- `market_context_high->metal_4h` score `-1.0291` n `91` status `ready` deltaP `-6.6856` edge `0.0134` maxDD `-1.0609`
- `market_context_high->index_1h` score `-1.2107` n `91` status `ready` deltaP `-9.8885` edge `-0.0031` maxDD `-0.5627`
- `market_context_high->crypto_alt_1h` score `-1.2119` n `91` status `ready` deltaP `-2.5432` edge `0.0298` maxDD `-4.7735`
- `market_context_high->index_4h` score `-1.2843` n `91` status `ready` deltaP `-10.8651` edge `0.001` maxDD `-1.1242`
- `market_context_high->equity_4h` score `-1.3196` n `91` status `ready` deltaP `-4.5061` edge `0.0078` maxDD `-5.4217`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

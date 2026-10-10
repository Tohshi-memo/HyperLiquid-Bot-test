# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-10T14:52:24.463018+00:00`
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

- `market_context_high->unknown_4h` score `40.8233` n `91` status `ready` deltaP `-6.3404` edge `3.4981` maxDD `-2.3109`
- `market_context_high->equity_24h` score `10.0528` n `91` status `ready` deltaP `38.4635` edge `0.6242` maxDD `-1.0977`
- `market_context_high->crypto_major_24h` score `9.3304` n `91` status `ready` deltaP `20.8696` edge `1.3719` maxDD `-17.8526`
- `market_context_high->crypto_alt_24h` score `1.7091` n `91` status `ready` deltaP `10.0578` edge `0.7633` maxDD `-35.5652`
- `market_context_high->crypto_major_4h` score `1.4819` n `91` status `ready` deltaP `17.554` edge `0.206` maxDD `-6.9761`
- `market_context_high->crypto_major_1h` score `0.1416` n `91` status `ready` deltaP `9.0956` edge `0.0464` maxDD `-3.7778`
- `market_context_high->fx_1h` score `0.1398` n `91` status `ready` deltaP `5.2001` edge `0.0012` maxDD `-0.271`
- `market_context_high->index_24h` score `-0.1384` n `91` status `ready` deltaP `12.1965` edge `0.0919` maxDD `-1.9432`
- `market_context_high->fx_4h` score `-0.1708` n `91` status `ready` deltaP `7.9118` edge `0.0077` maxDD `-0.3077`
- `market_context_high->commodity_1h` score `-0.3543` n `91` status `ready` deltaP `0.7025` edge `0.0034` maxDD `-0.3417`
- `market_context_high->metal_1h` score `-0.3577` n `91` status `ready` deltaP `2.999` edge `0.0014` maxDD `-0.7626`
- `market_context_high->metal_24h` score `-0.4427` n `91` status `ready` deltaP `5.3308` edge `0.0562` maxDD `-3.5466`
- `market_context_high->commodity_4h` score `-0.6253` n `91` status `ready` deltaP `-0.8794` edge `-0.0043` maxDD `-1.6002`
- `market_context_high->unknown_1h` score `-0.8561` n `91` status `ready` deltaP `-4.5173` edge `0.0003` maxDD `-0.9885`
- `market_context_high->crypto_alt_4h` score `-0.9249` n `91` status `ready` deltaP `-6.1897` edge `0.116` maxDD `-8.7986`
- `market_context_high->equity_1h` score `-0.9866` n `91` status `ready` deltaP `-5.6359` edge `-0.0049` maxDD `-2.0542`
- `market_context_high->metal_4h` score `-1.0298` n `91` status `ready` deltaP `-6.6856` edge `0.0133` maxDD `-1.0609`
- `market_context_high->index_1h` score `-1.2177` n `91` status `ready` deltaP `-10.0382` edge `-0.003` maxDD `-0.5627`
- `market_context_high->crypto_alt_1h` score `-1.2455` n `91` status `ready` deltaP `-2.6929` edge `0.028` maxDD `-4.7735`
- `market_context_high->index_4h` score `-1.2851` n `91` status `ready` deltaP `-10.8651` edge `0.0009` maxDD `-1.1242`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

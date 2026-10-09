# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-09T23:52:27.659308+00:00`
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

- `market_context_high->unknown_4h` score `40.9703` n `91` status `ready` deltaP `-4.9685` edge `3.5012` maxDD `-2.3109`
- `market_context_high->equity_24h` score `9.5553` n `91` status `ready` deltaP `33.2641` edge `0.6174` maxDD `-1.0977`
- `market_context_high->crypto_major_24h` score `8.6333` n `91` status `ready` deltaP `18.4433` edge `1.2987` maxDD `-17.8526`
- `market_context_high->crypto_alt_24h` score `1.7614` n `91` status `ready` deltaP `10.0578` edge `0.77` maxDD `-35.5652`
- `market_context_high->crypto_major_4h` score `1.5733` n `91` status `ready` deltaP `18.621` edge `0.2106` maxDD `-6.9761`
- `market_context_high->fx_1h` score `0.2499` n `91` status `ready` deltaP `6.5474` edge `0.0014` maxDD `-0.271`
- `market_context_high->crypto_major_1h` score `0.1797` n `91` status `ready` deltaP `9.8441` edge `0.0463` maxDD `-3.7778`
- `market_context_high->fx_4h` score `0.1047` n `91` status `ready` deltaP `11.2654` edge `0.0083` maxDD `-0.3077`
- `market_context_high->metal_24h` score `-0.1458` n `91` status `ready` deltaP `9.3169` edge `0.0677` maxDD `-3.5466`
- `market_context_high->commodity_1h` score `-0.262` n `91` status `ready` deltaP `1.7504` edge `0.0041` maxDD `-0.3417`
- `market_context_high->metal_1h` score `-0.2834` n `91` status `ready` deltaP `3.8972` edge `0.0016` maxDD `-0.7626`
- `market_context_high->index_24h` score `-0.3606` n `91` status `ready` deltaP `7.8638` edge `0.0923` maxDD `-1.9432`
- `market_context_high->commodity_4h` score `-0.5641` n `91` status `ready` deltaP `0.4925` edge `-0.0056` maxDD `-1.6002`
- `market_context_high->equity_1h` score `-0.9056` n `91` status `ready` deltaP `-4.1389` edge `-0.0045` maxDD `-2.0542`
- `market_context_high->metal_4h` score `-0.9142` n `91` status `ready` deltaP `-4.5514` edge `0.0139` maxDD `-1.0609`
- `market_context_high->crypto_alt_4h` score `-0.9218` n `91` status `ready` deltaP `-7.1044` edge `0.1225` maxDD `-8.7986`
- `market_context_high->unknown_1h` score `-1.0733` n `91` status `ready` deltaP `-4.0682` edge `-0.0208` maxDD `-0.9885`
- `market_context_high->index_1h` score `-1.2177` n `91` status `ready` deltaP `-10.0382` edge `-0.003` maxDD `-0.5627`
- `market_context_high->index_4h` score `-1.2304` n `91` status `ready` deltaP `-9.798` edge `0.0008` maxDD `-1.1242`
- `market_context_high->crypto_alt_1h` score `-1.2431` n `91` status `ready` deltaP `-2.5432` edge `0.0272` maxDD `-4.7735`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-09T09:52:29.749928+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8370`

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

- `market_context_high->unknown_4h` score `40.2719` n `91` status `ready` deltaP `-4.9685` edge `3.443` maxDD `-2.3109`
- `market_context_high->equity_24h` score `10.1006` n `90` status `ready` deltaP `33.6458` edge `0.6603` maxDD `-1.0977`
- `market_context_high->crypto_major_24h` score `10.0245` n `90` status `ready` deltaP `22.3611` edge `1.4335` maxDD `-16.7906`
- `market_context_high->crypto_alt_24h` score `3.5766` n `90` status `ready` deltaP `14.0625` edge `0.9586` maxDD `-34.5048`
- `market_context_high->crypto_major_4h` score `1.8887` n `91` status `ready` deltaP `18.0113` edge `0.2551` maxDD `-6.9761`
- `market_context_high->metal_24h` score `0.6984` n `90` status `ready` deltaP `15.5902` edge `0.1341` maxDD `-3.5466`
- `market_context_high->crypto_major_1h` score `0.2897` n `91` status `ready` deltaP `9.8441` edge `0.0604` maxDD `-3.7778`
- `market_context_high->fx_1h` score `0.2823` n `91` status `ready` deltaP `6.9965` edge `0.0011` maxDD `-0.271`
- `market_context_high->fx_4h` score `0.0965` n `91` status `ready` deltaP `11.4179` edge `0.0066` maxDD `-0.3077`
- `market_context_high->metal_1h` score `-0.2199` n `91` status `ready` deltaP `4.3463` edge `0.0039` maxDD `-0.7626`
- `market_context_high->index_24h` score `-0.3313` n `90` status `ready` deltaP `7.8125` edge `0.0964` maxDD `-1.9432`
- `market_context_high->commodity_1h` score `-0.3891` n `91` status `ready` deltaP `0.7025` edge `0.0005` maxDD `-0.3417`
- `market_context_high->crypto_alt_4h` score `-0.4232` n `91` status `ready` deltaP `-6.9519` edge `0.1854` maxDD `-8.7986`
- `market_context_high->metal_4h` score `-0.8304` n `91` status `ready` deltaP `-4.0941` edge `0.0216` maxDD `-1.0609`
- `market_context_high->equity_1h` score `-0.8698` n `91` status `ready` deltaP `-3.091` edge `-0.0069` maxDD `-2.0542`
- `market_context_high->crypto_alt_1h` score `-0.8976` n `91` status `ready` deltaP `-1.7947` edge `0.051` maxDD `-4.7735`
- `market_context_high->commodity_4h` score `-0.9333` n `91` status `ready` deltaP `-3.6233` edge `-0.0255` maxDD `-1.6002`
- `market_context_high->index_1h` score `-1.2497` n `91` status `ready` deltaP `-10.4873` edge `-0.0041` maxDD `-0.5627`
- `market_context_high->index_4h` score `-1.3718` n `91` status `ready` deltaP `-11.9322` edge `-0.0031` maxDD `-1.1242`
- `market_context_high->equity_4h` score `-1.3908` n `91` status `ready` deltaP `-4.811` edge `0.0007` maxDD `-5.4217`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

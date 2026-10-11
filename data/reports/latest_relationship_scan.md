# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-11T12:22:29.319365+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `7893`

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

- `market_context_high->unknown_24h` score `419.6612` n `52` status `ready` deltaP `-13.6752` edge `35.0993` maxDD `-1.2425`
- `market_context_high->unknown_4h` score `44.1109` n `84` status `ready` deltaP `-7.0702` edge `3.7811` maxDD `-2.3109`
- `market_context_high->equity_24h` score `8.9879` n `52` status `ready` deltaP `33.3867` edge `0.5693` maxDD `-1.0977`
- `market_context_high->crypto_major_24h` score `4.2799` n `52` status `ready` deltaP `-2.711` edge `0.8816` maxDD `-17.8526`
- `market_context_high->index_24h` score `3.4236` n `52` status `ready` deltaP `31.0898` edge `0.1377` maxDD `-0.7733`
- `market_context_high->fx_4h` score `1.2406` n `84` status `ready` deltaP `18.3217` edge `0.0096` maxDD `-0.2692`
- `market_context_high->fx_24h` score `0.7573` n `52` status `ready` deltaP `19.7649` edge `0.0227` maxDD `-0.5903`
- `market_context_high->commodity_1h` score `0.3692` n `85` status `ready` deltaP `6.8352` edge `0.0103` maxDD `-0.3417`
- `market_context_high->commodity_4h` score `0.075` n `84` status `ready` deltaP `7.9777` edge `0.0064` maxDD `-1.6002`
- `market_context_high->fx_1h` score `-0.0908` n `85` status `ready` deltaP `2.2579` edge `0.0016` maxDD `-0.271`
- `market_context_high->metal_1h` score `-0.4314` n `85` status `ready` deltaP `0.2677` edge `0.002` maxDD `-0.7275`
- `market_context_high->metal_4h` score `-0.5374` n `84` status `ready` deltaP `-1.9237` edge `0.0162` maxDD `-1.1153`
- `market_context_high->unknown_1h` score `-0.6405` n `85` status `ready` deltaP `-7.448` edge `0.0299` maxDD `-1.0231`
- `market_context_high->crypto_alt_1h` score `-0.9362` n `85` status `ready` deltaP `-1.2293` edge `0.0336` maxDD `-4.9401`
- `market_context_high->crypto_major_1h` score `-1.0494` n `85` status `ready` deltaP `-2.3635` edge `0.0172` maxDD `-3.7778`
- `market_context_high->crypto_major_4h` score `-1.2918` n `84` status `ready` deltaP `-5.4079` edge `0.081` maxDD `-11.1784`
- `market_context_high->index_4h` score `-1.4644` n `84` status `ready` deltaP `-14.1333` edge `-0.0003` maxDD `-1.1242`
- `market_context_high->index_1h` score `-1.7493` n `85` status `ready` deltaP `-8.3956` edge `-0.0036` maxDD `-0.5627`
- `market_context_high->equity_1h` score `-1.8292` n `85` status `ready` deltaP `-8.5012` edge `-0.0088` maxDD `-2.2898`
- `market_context_high->crypto_alt_4h` score `-1.8906` n `84` status `ready` deltaP `-6.8017` edge `0.0588` maxDD `-13.8008`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

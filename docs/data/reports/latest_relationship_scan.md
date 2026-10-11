# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-11T13:07:29.759391+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `7286`

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

- `market_context_high->unknown_24h` score `615.6842` n `49` status `ready` deltaP `-14.8526` edge `51.4424` maxDD `-1.2425`
- `market_context_high->unknown_4h` score `46.4811` n `81` status `ready` deltaP `-7.908` edge `3.9842` maxDD `-2.3109`
- `market_context_high->equity_24h` score `8.9523` n `49` status `ready` deltaP `32.3271` edge `0.5734` maxDD `-1.0977`
- `market_context_high->index_24h` score `4.091` n `49` status `ready` deltaP `35.4521` edge `0.1483` maxDD `-0.4987`
- `market_context_high->crypto_major_24h` score `3.633` n `49` status `ready` deltaP `-6.5406` edge `0.8242` maxDD `-17.8526`
- `market_context_high->fx_24h` score `1.6767` n `49` status `ready` deltaP `23.6005` edge `0.0258` maxDD `-0.4732`
- `market_context_high->fx_4h` score `1.1582` n `81` status `ready` deltaP `17.3517` edge `0.0092` maxDD `-0.2692`
- `market_context_high->commodity_1h` score `0.275` n `85` status `ready` deltaP `5.8084` edge `0.0093` maxDD `-0.3417`
- `market_context_high->commodity_4h` score `0.121` n `81` status `ready` deltaP `8.2826` edge `0.0082` maxDD `-1.6002`
- `market_context_high->fx_1h` score `-0.2623` n `85` status `ready` deltaP `0.2043` edge `0.001` maxDD `-0.271`
- `market_context_high->metal_4h` score `-0.4632` n `81` status `ready` deltaP `-0.6173` edge `0.017` maxDD `-1.1153`
- `market_context_high->metal_1h` score `-0.497` n `85` status `ready` deltaP `2.3212` edge `0.0022` maxDD `-0.7275`
- `market_context_high->crypto_alt_1h` score `-0.5865` n `85` status `ready` deltaP `1.851` edge `0.0422` maxDD `-4.9401`
- `market_context_high->unknown_1h` score `-0.6112` n `85` status `ready` deltaP `-6.4213` edge `0.0255` maxDD `-1.0231`
- `market_context_high->crypto_major_1h` score `-0.9588` n `85` status `ready` deltaP `-1.3367` edge `0.0179` maxDD `-3.7778`
- `market_context_high->index_1h` score `-1.137` n `85` status `ready` deltaP `-8.3956` edge `-0.0036` maxDD `-0.5627`
- `market_context_high->crypto_major_4h` score `-1.1977` n `81` status `ready` deltaP `-4.2137` edge `0.0851` maxDD `-11.1784`
- `market_context_high->equity_1h` score `-1.2346` n `85` status `ready` deltaP `-9.528` edge `-0.0078` maxDD `-2.2898`
- `market_context_high->index_4h` score `-1.3223` n `81` status `ready` deltaP `-13.2679` edge `-0.0005` maxDD `-1.1124`
- `market_context_high->crypto_alt_4h` score `-1.8569` n `81` status `ready` deltaP `-6.2726` edge `0.0596` maxDD `-13.8008`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

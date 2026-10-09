# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-09T14:52:29.012592+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8541`

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

- `market_context_high->unknown_4h` score `40.2307` n `91` status `ready` deltaP `-5.2734` edge `3.4416` maxDD `-2.3109`
- `market_context_high->equity_24h` score `10.3686` n `91` status `ready` deltaP `35.0752` edge `0.6731` maxDD `-1.0977`
- `market_context_high->crypto_major_24h` score `9.4381` n `91` status `ready` deltaP `21.6652` edge `1.3804` maxDD `-17.8526`
- `market_context_high->crypto_alt_24h` score `3.1024` n `91` status `ready` deltaP `13.452` edge `0.9193` maxDD `-35.5652`
- `market_context_high->crypto_major_4h` score `1.8821` n `91` status `ready` deltaP `18.4686` edge `0.2512` maxDD `-6.9761`
- `market_context_high->crypto_major_1h` score `0.3816` n `91` status `ready` deltaP `10.7423` edge `0.0662` maxDD `-3.7778`
- `market_context_high->metal_24h` score `0.3555` n `91` status `ready` deltaP `12.521` edge `0.1106` maxDD `-3.5466`
- `market_context_high->fx_1h` score `0.2559` n `91` status `ready` deltaP `6.6971` edge `0.0009` maxDD `-0.271`
- `market_context_high->fx_4h` score `0.2522` n `91` status `ready` deltaP `13.0947` edge `0.0084` maxDD `-0.3077`
- `market_context_high->crypto_alt_4h` score `-0.1589` n `91` status `ready` deltaP `-5.1227` edge `0.2071` maxDD `-8.7986`
- `market_context_high->metal_1h` score `-0.2055` n `91` status `ready` deltaP `4.496` edge `0.0041` maxDD `-0.7626`
- `market_context_high->index_24h` score `-0.2107` n `91` status `ready` deltaP `9.5162` edge `0.1005` maxDD `-1.9432`
- `market_context_high->commodity_1h` score `-0.5137` n `91` status `ready` deltaP `-0.3454` edge `-0.0029` maxDD `-0.3417`
- `market_context_high->crypto_alt_1h` score `-0.6974` n `91` status `ready` deltaP `-0.5971` edge `0.0597` maxDD `-4.7735`
- `market_context_high->equity_1h` score `-0.8043` n `91` status `ready` deltaP `-2.7916` edge `-0.0005` maxDD `-2.0542`
- `market_context_high->metal_4h` score `-0.8522` n `91` status `ready` deltaP `-4.0941` edge `0.0188` maxDD `-1.0609`
- `market_context_high->commodity_4h` score `-0.9149` n `91` status `ready` deltaP `-3.0136` edge `-0.0272` maxDD `-1.6002`
- `market_context_high->index_1h` score `-1.1741` n `91` status `ready` deltaP `-9.2897` edge `-0.0024` maxDD `-0.5627`
- `market_context_high->equity_4h` score `-1.1938` n `91` status `ready` deltaP `-3.2866` edge `0.0158` maxDD `-5.4217`
- `market_context_high->index_4h` score `-1.1972` n `91` status `ready` deltaP `-9.3407` edge `0.002` maxDD `-1.1242`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

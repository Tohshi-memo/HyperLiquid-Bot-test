# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-11T09:07:27.620251+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `5973`

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

- `market_context_high->unknown_4h` score `42.6495` n `85` status `ready` deltaP `-12.9484` edge `3.6985` maxDD `-2.3109`
- `market_context_high->equity_24h` score `9.4556` n `65` status `ready` deltaP `36.8482` edge `0.5852` maxDD `-1.0977`
- `market_context_high->crypto_major_24h` score `6.8954` n `65` status `ready` deltaP `8.977` edge `1.139` maxDD `-17.8526`
- `market_context_high->fx_4h` score `1.4531` n `85` status `ready` deltaP `20.6779` edge `0.0116` maxDD `-0.2692`
- `market_context_high->index_24h` score `0.7673` n `65` status `ready` deltaP `16.0524` edge `0.112` maxDD `-1.3185`
- `market_context_high->commodity_4h` score `0.1953` n `85` status `ready` deltaP `9.2414` edge `0.008` maxDD `-1.6002`
- `market_context_high->commodity_1h` score `0.1305` n `97` status `ready` deltaP `4.2719` edge `0.0075` maxDD `-0.3417`
- `market_context_high->fx_1h` score `0.0721` n `97` status `ready` deltaP `4.704` edge `0.0021` maxDD `-0.271`
- `market_context_high->crypto_major_1h` score `-0.3269` n `97` status `ready` deltaP `2.2609` edge `0.0319` maxDD `-3.7778`
- `market_context_high->fx_24h` score `-0.497` n `65` status `ready` deltaP `7.0967` edge `0.0096` maxDD `-1.3174`
- `market_context_high->metal_1h` score `-0.5666` n `97` status `ready` deltaP `-2.1622` edge `0.0013` maxDD `-0.7626`
- `market_context_high->crypto_major_4h` score `-0.7325` n `85` status `ready` deltaP `0.4125` edge `0.1057` maxDD `-10.5224`
- `market_context_high->metal_4h` score `-0.9643` n `85` status `ready` deltaP `-8.628` edge `0.0145` maxDD `-1.1153`
- `market_context_high->crypto_alt_1h` score `-0.9648` n `97` status `ready` deltaP `-4.3907` edge `0.0215` maxDD `-4.9401`
- `market_context_high->metal_24h` score `-1.0596` n `65` status `ready` deltaP `-4.7623` edge `0.0444` maxDD `-3.5466`
- `market_context_high->index_4h` score `-1.2606` n `85` status `ready` deltaP `-10.3049` edge `0.0003` maxDD `-1.1242`
- `market_context_high->equity_1h` score `-1.471` n `97` status `ready` deltaP `-4.4586` edge `-0.0059` maxDD `-2.2898`
- `market_context_high->index_1h` score `-1.4978` n `97` status `ready` deltaP `-5.3877` edge `-0.0027` maxDD `-0.5627`
- `market_context_high->crypto_alt_24h` score `-2.2459` n `65` status `ready` deltaP `-6.3302` edge `0.3655` maxDD `-35.5652`
- `market_context_high->crypto_alt_4h` score `-2.5162` n `85` status `ready` deltaP `-13.5061` edge `0.0233` maxDD `-13.8008`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-11T13:37:32.322456+00:00`
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

- `market_context_high->unknown_24h` score `760.5735` n `47` status `ready` deltaP `-15.721` edge `63.5223` maxDD `-1.2425`
- `market_context_high->unknown_4h` score `48.1676` n `79` status `ready` deltaP `-8.5018` edge `4.1287` maxDD `-2.3109`
- `market_context_high->equity_24h` score `8.9498` n `47` status `ready` deltaP `31.5455` edge `0.5784` maxDD `-1.0977`
- `market_context_high->index_24h` score `4.5691` n `47` status `ready` deltaP `38.7522` edge `0.1558` maxDD `-0.3379`
- `market_context_high->crypto_major_24h` score `3.1367` n `47` status `ready` deltaP `-9.3196` edge `0.7791` maxDD `-17.8526`
- `market_context_high->fx_24h` score `2.0709` n `47` status `ready` deltaP `26.4665` edge `0.0294` maxDD `-0.3282`
- `market_context_high->fx_4h` score `1.1043` n `79` status `ready` deltaP `16.6641` edge `0.0093` maxDD `-0.2692`
- `market_context_high->commodity_4h` score `0.1873` n `79` status `ready` deltaP `8.8569` edge `0.0099` maxDD `-1.6002`
- `market_context_high->commodity_1h` score `0.1584` n `84` status `ready` deltaP `4.4411` edge `0.0087` maxDD `-0.3417`
- `market_context_high->unknown_1h` score `-0.1674` n `84` status `ready` deltaP `-5.6886` edge `0.0576` maxDD `-1.0231`
- `market_context_high->fx_1h` score `-0.2929` n `84` status `ready` deltaP `-0.1782` edge `0.001` maxDD `-0.271`
- `market_context_high->crypto_alt_1h` score `-0.5158` n `84` status `ready` deltaP `2.3596` edge `0.0447` maxDD `-4.9401`
- `market_context_high->metal_4h` score `-0.526` n `79` status `ready` deltaP `-1.8987` edge `0.0175` maxDD `-1.1153`
- `market_context_high->metal_1h` score `-0.5419` n `84` status `ready` deltaP `1.775` edge `0.0021` maxDD `-0.7275`
- `market_context_high->crypto_major_1h` score `-1.0166` n `84` status `ready` deltaP `-1.939` edge `0.0171` maxDD `-3.7778`
- `market_context_high->index_4h` score `-1.2058` n `79` status `ready` deltaP `-12.3302` edge `-0.0004` maxDD `-1.0926`
- `market_context_high->index_1h` score `-1.2206` n `84` status `ready` deltaP `-9.9729` edge `-0.0038` maxDD `-0.5627`
- `market_context_high->crypto_major_4h` score `-1.2295` n `79` status `ready` deltaP `-4.5693` edge `0.0834` maxDD `-11.1784`
- `market_context_high->equity_1h` score `-1.272` n `84` status `ready` deltaP `-10.1582` edge `-0.0084` maxDD `-2.2898`
- `market_context_high->crypto_alt_4h` score `-1.9665` n `79` status `ready` deltaP `-7.5853` edge `0.0543` maxDD `-13.8008`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

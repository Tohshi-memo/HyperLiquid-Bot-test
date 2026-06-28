# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-28T09:07:26.352723+00:00`
- Price records: `672`
- Market context records: `5024`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10174`

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

- `market_context_high->unknown_1h` score `15.2096` n `93` status `ready` deltaP `3.8182` edge `1.2921` maxDD `-1.674`
- `market_context_high->unknown_4h` score `8.9741` n `93` status `ready` deltaP `21.1447` edge `0.7091` maxDD `-5.5109`
- `market_context_high->crypto_major_4h` score `5.6509` n `93` status `ready` deltaP `17.5568` edge `0.5123` maxDD `-8.3416`
- `market_context_high->crypto_alt_4h` score `5.3807` n `93` status `ready` deltaP `14.7883` edge `0.4892` maxDD `-7.8181`
- `market_context_high->metal_4h` score `1.3231` n `93` status `ready` deltaP `14.1538` edge `0.1238` maxDD `-1.9651`
- `market_context_high->equity_1h` score `0.8656` n `93` status `ready` deltaP `8.1868` edge `0.0749` maxDD `-2.5875`
- `market_context_high->crypto_major_1h` score `0.7493` n `93` status `ready` deltaP `5.9542` edge `0.1145` maxDD `-4.6734`
- `market_context_high->equity_4h` score `0.4846` n `93` status `ready` deltaP `3.7307` edge `0.1754` maxDD `-6.3852`
- `market_context_high->metal_1h` score `0.376` n `93` status `ready` deltaP `6.4033` edge `0.0383` maxDD `-1.3057`
- `market_context_high->crypto_alt_1h` score `0.1734` n `93` status `ready` deltaP `5.1107` edge `0.0904` maxDD `-5.5126`
- `market_context_high->fx_24h` score `-0.0639` n `74` status `ready` deltaP `9.2108` edge `0.0066` maxDD `-1.7626`
- `market_context_high->index_4h` score `-0.0705` n `93` status `ready` deltaP `4.4764` edge `0.0404` maxDD `-1.0893`
- `market_context_high->commodity_1h` score `-0.3135` n `93` status `ready` deltaP `1.7079` edge `0.0144` maxDD `-1.278`
- `market_context_high->index_1h` score `-0.5599` n `93` status `ready` deltaP `2.2117` edge `0.0127` maxDD `-0.5946`
- `market_context_high->commodity_4h` score `-0.8193` n `93` status `ready` deltaP `3.393` edge `-0.0024` maxDD `-5.021`
- `market_context_high->fx_4h` score `-1.0101` n `93` status `ready` deltaP `-4.2207` edge `-0.0025` maxDD `-1.2426`
- `market_context_high->unknown_24h` score `-1.6543` n `74` status `ready` deltaP `27.21` edge `-0.285` maxDD `-1.4072`
- `market_context_high->fx_1h` score `-1.7952` n `93` status `ready` deltaP `-12.4477` edge `-0.0056` maxDD `-0.5482`
- `market_context_high->metal_24h` score `-3.8294` n `74` status `ready` deltaP `4.3403` edge `0.0256` maxDD `-32.9721`
- `market_context_high->commodity_24h` score `-4.5026` n `74` status `ready` deltaP `2.149` edge `-0.0807` maxDD `-27.5371`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

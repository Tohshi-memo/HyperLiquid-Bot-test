# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-28T08:52:25.862988+00:00`
- Price records: `672`
- Market context records: `5023`
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

- `market_context_high->unknown_1h` score `15.2516` n `93` status `ready` deltaP `3.8182` edge `1.2956` maxDD `-1.674`
- `market_context_high->unknown_4h` score `8.9595` n `93` status `ready` deltaP `20.9923` edge `0.7089` maxDD `-5.5109`
- `market_context_high->crypto_major_4h` score `5.6629` n `93` status `ready` deltaP `17.5568` edge `0.5133` maxDD `-8.3416`
- `market_context_high->crypto_alt_4h` score `5.3831` n `93` status `ready` deltaP `14.7883` edge `0.4894` maxDD `-7.8181`
- `market_context_high->metal_4h` score `1.3365` n `93` status `ready` deltaP `14.3063` edge `0.1239` maxDD `-1.9651`
- `market_context_high->equity_1h` score `0.868` n `93` status `ready` deltaP `8.1868` edge `0.0751` maxDD `-2.5875`
- `market_context_high->crypto_major_1h` score `0.7493` n `93` status `ready` deltaP `5.9542` edge `0.1145` maxDD `-4.6734`
- `market_context_high->equity_4h` score `0.4877` n `93` status `ready` deltaP `3.7307` edge `0.1758` maxDD `-6.3852`
- `market_context_high->metal_1h` score `0.376` n `93` status `ready` deltaP `6.4033` edge `0.0383` maxDD `-1.3057`
- `market_context_high->crypto_alt_1h` score `0.1726` n `93` status `ready` deltaP `5.1107` edge `0.0903` maxDD `-5.5126`
- `market_context_high->index_4h` score `-0.0571` n `93` status `ready` deltaP `4.6289` edge `0.0405` maxDD `-1.0893`
- `market_context_high->fx_24h` score `-0.0647` n `74` status `ready` deltaP `9.2108` edge `0.0065` maxDD `-1.7626`
- `market_context_high->commodity_1h` score `-0.3143` n `93` status `ready` deltaP `1.7079` edge `0.0143` maxDD `-1.278`
- `market_context_high->index_1h` score `-0.5599` n `93` status `ready` deltaP `2.2117` edge `0.0127` maxDD `-0.5946`
- `market_context_high->commodity_4h` score `-0.8106` n `93` status `ready` deltaP `3.5454` edge `-0.0023` maxDD `-5.021`
- `market_context_high->fx_4h` score `-1.0014` n `93` status `ready` deltaP `-4.0683` edge `-0.0024` maxDD `-1.2426`
- `market_context_high->unknown_24h` score `-1.3159` n `74` status `ready` deltaP `27.21` edge `-0.2568` maxDD `-1.4072`
- `market_context_high->fx_1h` score `-1.7952` n `93` status `ready` deltaP `-12.4477` edge `-0.0056` maxDD `-0.5482`
- `market_context_high->metal_24h` score `-3.8455` n `74` status `ready` deltaP `4.1667` edge `0.0247` maxDD `-32.9721`
- `market_context_high->commodity_24h` score `-4.4873` n `74` status `ready` deltaP `2.3226` edge `-0.0799` maxDD `-27.5371`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

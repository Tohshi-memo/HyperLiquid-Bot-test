# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-26T04:22:29.808023+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11738`

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

- `news_risk_high->unknown_24h` score `3123.1404` n `93` status `ready` deltaP `-0.7281` edge `260.271` maxDD `-0.0226`
- `market_context_high->unknown_1h` score `70.807` n `47` status `ready` deltaP `8.0201` edge `5.8542` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `49.0014` n `47` status `ready` deltaP `25.9087` edge `3.95` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `30.4336` n `47` status `ready` deltaP `23.5667` edge `2.417` maxDD `-2.7051`
- `market_context_high->equity_24h` score `25.2843` n `47` status `ready` deltaP `33.3739` edge `1.9201` maxDD `-2.1786`
- `market_context_high->index_24h` score `7.4131` n `47` status `ready` deltaP `32.8531` edge `0.4117` maxDD `-0.3705`
- `market_context_high->metal_24h` score `3.5782` n `47` status `ready` deltaP `30.1973` edge `0.1207` maxDD `-0.2401`
- `market_context_high->equity_4h` score `2.7313` n `47` status `ready` deltaP `17.2969` edge `0.1541` maxDD `-1.3444`
- `market_context_high->index_4h` score `2.542` n `47` status `ready` deltaP `29.3007` edge `0.0319` maxDD `-0.2323`
- `market_context_high->equity_1h` score `1.0901` n `47` status `ready` deltaP `12.5143` edge `0.0477` maxDD `-1.5564`
- `market_context_high->crypto_alt_4h` score `1.0896` n `47` status `ready` deltaP `10.4502` edge `0.0879` maxDD `-3.3417`
- `news_risk_high->metal_24h` score `1.056` n `93` status `ready` deltaP `26.6969` edge `0.1235` maxDD `-6.9545`
- `market_context_high->index_1h` score `0.7702` n `47` status `ready` deltaP `12.3646` edge `0.0096` maxDD `-0.2275`
- `market_context_high->fx_1h` score `0.4961` n `47` status `ready` deltaP `10.4089` edge `0.0076` maxDD `-0.1854`
- `news_risk_high->index_24h` score `0.4008` n `93` status `ready` deltaP `13.4296` edge `0.044` maxDD `-2.344`
- `market_context_high->crypto_major_1h` score `0.3075` n `47` status `ready` deltaP `5.0516` edge `0.0737` maxDD `-4.5405`
- `market_context_high->crypto_major_4h` score `0.2824` n `47` status `ready` deltaP `3.9277` edge `0.0878` maxDD `-5.2359`
- `news_risk_high->index_1h` score `0.2717` n `122` status `ready` deltaP `7.0629` edge `0.0048` maxDD `-0.3395`
- `news_risk_high->crypto_alt_1h` score `0.0605` n `122` status `ready` deltaP `6.528` edge `0.0553` maxDD `-4.2849`
- `market_context_high->fx_4h` score `0.0347` n `47` status `ready` deltaP `9.3215` edge `0.0075` maxDD `-0.6736`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

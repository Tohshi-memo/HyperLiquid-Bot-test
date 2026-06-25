# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-25T02:37:29.150412+00:00`
- Price records: `672`
- Market context records: `4682`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9736`

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

- `market_context_high->unknown_1h` score `78.7034` n `135` status `ready` deltaP `12.026` edge `6.5202` maxDD `-1.674`
- `market_context_high->unknown_4h` score `5.092` n `135` status `ready` deltaP `10.9169` edge `0.4726` maxDD `-4.6834`
- `market_context_high->unknown_24h` score `1.6568` n `135` status `ready` deltaP `9.9306` edge `0.1642` maxDD `-4.7201`
- `market_context_high->commodity_1h` score `-0.4919` n `135` status `ready` deltaP `1.9062` edge `0.0259` maxDD `-2.0345`
- `market_context_high->index_4h` score `-0.831` n `135` status `ready` deltaP `3.007` edge `-0.0143` maxDD `-5.9823`
- `market_context_high->equity_1h` score `-0.8812` n `135` status `ready` deltaP `-3.0417` edge `0.006` maxDD `-5.5624`
- `market_context_high->fx_4h` score `-0.9323` n `135` status `ready` deltaP `-1.4826` edge `-0.0014` maxDD `-1.9927`
- `market_context_high->fx_1h` score `-1.073` n `135` status `ready` deltaP `-4.3424` edge `-0.005` maxDD `-1.1038`
- `market_context_high->commodity_4h` score `-1.2307` n `135` status `ready` deltaP `5.2462` edge `0.018` maxDD `-9.1941`
- `market_context_high->equity_4h` score `-1.3637` n `135` status `ready` deltaP `0.3275` edge `-0.0001` maxDD `-8.8203`
- `market_context_high->index_1h` score `-1.79` n `135` status `ready` deltaP `-5.2872` edge `-0.0135` maxDD `-2.6999`
- `market_context_high->metal_1h` score `-2.8481` n `135` status `ready` deltaP `-4.3269` edge `-0.0795` maxDD `-17.2107`
- `market_context_high->fx_24h` score `-4.5718` n `135` status `ready` deltaP `-10.9607` edge `-0.0119` maxDD `-5.3476`
- `market_context_high->commodity_24h` score `-5.0986` n `135` status `ready` deltaP `12.5926` edge `0.0416` maxDD `-30.7016`
- `market_context_high->crypto_alt_1h` score `-5.6119` n `135` status `ready` deltaP `-2.7501` edge `-0.1206` maxDD `-22.2982`
- `market_context_high->crypto_major_1h` score `-6.7622` n `135` status `ready` deltaP `-5.5556` edge `-0.1512` maxDD `-27.356`
- `market_context_high->index_24h` score `-8.3519` n `135` status `ready` deltaP `-10.6366` edge `-0.0876` maxDD `-29.3321`
- `market_context_high->crypto_alt_4h` score `-8.6989` n `135` status `ready` deltaP `-3.7692` edge `-0.2244` maxDD `-63.9243`
- `market_context_high->metal_4h` score `-9.2955` n `135` status `ready` deltaP `-1.7683` edge `-0.2946` maxDD `-64.494`
- `market_context_high->crypto_major_4h` score `-11.7357` n `135` status `ready` deltaP `-4.3575` edge `-0.3855` maxDD `-81.8692`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

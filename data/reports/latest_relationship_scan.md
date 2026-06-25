# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-25T03:37:32.538352+00:00`
- Price records: `672`
- Market context records: `4686`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9742`

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

- `market_context_high->unknown_1h` score `78.7046` n `135` status `ready` deltaP `12.026` edge `6.5203` maxDD `-1.674`
- `market_context_high->unknown_4h` score `5.146` n `135` status `ready` deltaP `10.9169` edge `0.4771` maxDD `-4.6834`
- `market_context_high->unknown_24h` score `1.8264` n `135` status `ready` deltaP `10.625` edge `0.1737` maxDD `-4.7201`
- `market_context_high->commodity_1h` score `-0.4919` n `135` status `ready` deltaP `1.9062` edge `0.0259` maxDD `-2.0345`
- `market_context_high->index_4h` score `-0.7899` n `135` status `ready` deltaP `3.6168` edge `-0.0131` maxDD `-5.9823`
- `market_context_high->equity_1h` score `-0.8789` n `135` status `ready` deltaP `-3.0417` edge `0.0063` maxDD `-5.5624`
- `market_context_high->fx_4h` score `-0.9434` n `135` status `ready` deltaP `-1.6351` edge `-0.0018` maxDD `-1.9927`
- `market_context_high->fx_1h` score `-1.0346` n `135` status `ready` deltaP `-3.8933` edge `-0.0048` maxDD `-1.1038`
- `market_context_high->commodity_4h` score `-1.2471` n `135` status `ready` deltaP `5.2462` edge `0.0159` maxDD `-9.1941`
- `market_context_high->equity_4h` score `-1.2977` n `135` status `ready` deltaP `0.9373` edge `0.0043` maxDD `-8.8203`
- `market_context_high->index_1h` score `-1.8139` n `135` status `ready` deltaP `-5.5866` edge `-0.0135` maxDD `-2.6999`
- `market_context_high->metal_1h` score `-2.8653` n `135` status `ready` deltaP `-4.4766` edge `-0.0807` maxDD `-17.2107`
- `market_context_high->fx_24h` score `-4.6417` n `135` status `ready` deltaP `-11.6551` edge `-0.0131` maxDD `-5.3476`
- `market_context_high->commodity_24h` score `-4.9891` n `135` status `ready` deltaP `13.287` edge `0.0461` maxDD `-30.7016`
- `market_context_high->crypto_alt_1h` score `-5.552` n `135` status `ready` deltaP `-2.301` edge `-0.1186` maxDD `-22.2982`
- `market_context_high->crypto_major_1h` score `-6.7155` n `135` status `ready` deltaP `-5.2562` edge `-0.1493` maxDD `-27.356`
- `market_context_high->index_24h` score `-8.3663` n `135` status `ready` deltaP `-10.6366` edge `-0.0888` maxDD `-29.3321`
- `market_context_high->crypto_alt_4h` score `-8.6848` n `135` status `ready` deltaP `-3.6168` edge `-0.2236` maxDD `-63.9243`
- `market_context_high->metal_4h` score `-9.2295` n `135` status `ready` deltaP `-1.1585` edge `-0.2902` maxDD `-64.494`
- `market_context_high->crypto_major_4h` score `-11.7145` n `135` status `ready` deltaP `-4.205` edge `-0.3838` maxDD `-81.8692`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-25T04:07:39.521582+00:00`
- Price records: `672`
- Market context records: `4688`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9744`

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

- `market_context_high->unknown_1h` score `78.7406` n `135` status `ready` deltaP `12.1757` edge `6.5223` maxDD `-1.674`
- `market_context_high->unknown_4h` score `5.1772` n `135` status `ready` deltaP `10.9169` edge `0.4797` maxDD `-4.6834`
- `market_context_high->unknown_24h` score `1.9262` n `135` status `ready` deltaP `10.9723` edge `0.1797` maxDD `-4.7201`
- `market_context_high->commodity_1h` score `-0.5147` n `135` status `ready` deltaP `1.7565` edge `0.025` maxDD `-2.0345`
- `market_context_high->index_4h` score `-0.7812` n `135` status `ready` deltaP `3.7692` edge `-0.013` maxDD `-5.9823`
- `market_context_high->equity_1h` score `-0.8789` n `135` status `ready` deltaP `-3.0417` edge `0.0063` maxDD `-5.5624`
- `market_context_high->fx_4h` score `-0.9441` n `135` status `ready` deltaP `-1.6351` edge `-0.0019` maxDD `-1.9927`
- `market_context_high->fx_1h` score `-1.0478` n `135` status `ready` deltaP `-4.043` edge `-0.0049` maxDD `-1.1038`
- `market_context_high->commodity_4h` score `-1.2541` n `135` status `ready` deltaP `5.2462` edge `0.015` maxDD `-9.1941`
- `market_context_high->equity_4h` score `-1.2655` n `135` status `ready` deltaP `1.2421` edge `0.0064` maxDD `-8.8203`
- `market_context_high->index_1h` score `-1.8127` n `135` status `ready` deltaP `-5.5866` edge `-0.0134` maxDD `-2.6999`
- `market_context_high->metal_1h` score `-2.8692` n `135` status `ready` deltaP `-4.4766` edge `-0.0812` maxDD `-17.2107`
- `market_context_high->fx_24h` score `-4.6779` n `135` status `ready` deltaP `-12.0023` edge `-0.0138` maxDD `-5.3476`
- `market_context_high->commodity_24h` score `-4.9289` n `135` status `ready` deltaP `13.6342` edge `0.0488` maxDD `-30.7016`
- `market_context_high->crypto_alt_1h` score `-5.5412` n `135` status `ready` deltaP `-2.1513` edge `-0.1187` maxDD `-22.2982`
- `market_context_high->crypto_major_1h` score `-6.6987` n `135` status `ready` deltaP `-5.1065` edge `-0.1489` maxDD `-27.356`
- `market_context_high->index_24h` score `-8.3759` n `135` status `ready` deltaP `-10.6366` edge `-0.0896` maxDD `-29.3321`
- `market_context_high->crypto_alt_4h` score `-8.669` n `135` status `ready` deltaP `-3.4643` edge `-0.2226` maxDD `-63.9243`
- `market_context_high->metal_4h` score `-9.1965` n `135` status `ready` deltaP `-0.8537` edge `-0.288` maxDD `-64.494`
- `market_context_high->crypto_major_4h` score `-11.6815` n `135` status `ready` deltaP `-3.9002` edge `-0.3816` maxDD `-81.8692`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

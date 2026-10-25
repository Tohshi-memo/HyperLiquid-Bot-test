# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-25T05:52:27.381736+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7778`

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

- `market_context_high->unknown_4h` score `52.3185` n `95` status `ready` deltaP `-0.0593` edge `4.3938` maxDD `-1.016`
- `market_context_high->unknown_1h` score `18.3703` n `107` status `ready` deltaP `3.7271` edge `1.5549` maxDD `-1.5781`
- `market_context_high->crypto_alt_24h` score `11.7165` n `35` status `ready` deltaP `31.7361` edge `0.8256` maxDD `-4.1975`
- `market_context_high->crypto_major_24h` score `3.4373` n `35` status `ready` deltaP `20.2926` edge `0.2571` maxDD `-5.8084`
- `market_context_high->commodity_24h` score `0.5903` n `35` status `ready` deltaP `12.1627` edge `0.0855` maxDD `-3.6055`
- `market_context_high->fx_24h` score `-0.0212` n `35` status `ready` deltaP `9.7917` edge `0.0062` maxDD `-0.9352`
- `market_context_high->fx_1h` score `-0.0767` n `107` status `ready` deltaP `3.3116` edge `0.003` maxDD `-0.1258`
- `market_context_high->fx_4h` score `-0.2162` n `95` status `ready` deltaP `3.604` edge `0.0081` maxDD `-0.4545`
- `market_context_high->metal_1h` score `-0.344` n `107` status `ready` deltaP `5.8929` edge `-0.0042` maxDD `-1.6682`
- `market_context_high->commodity_1h` score `-0.4642` n `107` status `ready` deltaP `-2.377` edge `0.0064` maxDD `-1.0053`
- `market_context_high->index_1h` score `-0.5289` n `107` status `ready` deltaP `0.3582` edge `-0.005` maxDD `-1.2155`
- `market_context_high->commodity_4h` score `-0.9245` n `95` status `ready` deltaP `-5.1139` edge `0.0343` maxDD `-1.165`
- `market_context_high->crypto_major_1h` score `-1.1579` n `107` status `ready` deltaP `3.8293` edge `-0.0159` maxDD `-9.3126`
- `market_context_high->metal_4h` score `-1.8437` n `95` status `ready` deltaP `6.1007` edge `-0.0233` maxDD `-5.3474`
- `market_context_high->equity_1h` score `-2.2919` n `107` status `ready` deltaP `2.7897` edge `-0.0851` maxDD `-12.1865`
- `market_context_high->metal_24h` score `-2.3348` n `35` status `ready` deltaP `-2.6637` edge `-0.0375` maxDD `-6.1446`
- `market_context_high->crypto_alt_1h` score `-2.6024` n `107` status `ready` deltaP `0.5079` edge `-0.0412` maxDD `-11.3243`
- `market_context_high->index_4h` score `-3.168` n `95` status `ready` deltaP `-5.4701` edge `-0.0401` maxDD `-4.3282`
- `market_context_high->crypto_major_4h` score `-5.6291` n `95` status `ready` deltaP `-7.423` edge `-0.1725` maxDD `-33.3092`
- `market_context_high->index_24h` score `-6.5753` n `35` status `ready` deltaP `-32.4306` edge `-0.2016` maxDD `-5.078`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

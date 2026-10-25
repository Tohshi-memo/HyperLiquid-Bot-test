# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-25T04:52:28.246234+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7734`

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

- `market_context_high->unknown_4h` score `51.7329` n `95` status `ready` deltaP `-0.0593` edge `4.345` maxDD `-1.016`
- `market_context_high->unknown_1h` score `18.3058` n `107` status `ready` deltaP `4.512` edge `1.5443` maxDD `-1.5781`
- `market_context_high->crypto_alt_24h` score `4.5283` n `39` status `ready` deltaP `23.531` edge `0.4466` maxDD `-16.0892`
- `market_context_high->commodity_24h` score `0.6223` n `39` status `ready` deltaP `13.4082` edge `0.0813` maxDD `-3.6055`
- `market_context_high->crypto_major_24h` score `0.2164` n `39` status `ready` deltaP `13.0209` edge `0.1088` maxDD `-10.2057`
- `market_context_high->fx_1h` score `-0.2014` n `107` status `ready` deltaP `0.957` edge `0.0027` maxDD `-0.1258`
- `market_context_high->fx_24h` score `-0.3836` n `39` status `ready` deltaP `5.6891` edge `0.0043` maxDD `-0.9352`
- `market_context_high->fx_4h` score `-0.4144` n `95` status `ready` deltaP `0.0032` edge `0.0067` maxDD `-0.4545`
- `market_context_high->metal_1h` score `-0.4279` n `107` status `ready` deltaP `4.3231` edge `-0.0045` maxDD `-1.6682`
- `market_context_high->index_1h` score `-0.4889` n `107` status `ready` deltaP `1.143` edge `-0.0051` maxDD `-1.2155`
- `market_context_high->commodity_1h` score `-0.5126` n `107` status `ready` deltaP `-0.0224` edge `0.0075` maxDD `-1.0053`
- `market_context_high->commodity_4h` score `-0.975` n `95` status `ready` deltaP `-2.4134` edge `0.0369` maxDD `-1.165`
- `market_context_high->crypto_major_1h` score `-1.0679` n `107` status `ready` deltaP `4.6141` edge `-0.0096` maxDD `-9.3126`
- `market_context_high->metal_4h` score `-2.0962` n `95` status `ready` deltaP `3.4002` edge `-0.0252` maxDD `-5.4385`
- `market_context_high->equity_1h` score `-2.3428` n `107` status `ready` deltaP `2.0049` edge `-0.0864` maxDD `-12.1865`
- `market_context_high->metal_24h` score `-2.4287` n `39` status `ready` deltaP `-5.008` edge `-0.0263` maxDD `-6.4167`
- `market_context_high->crypto_alt_1h` score `-2.4288` n `107` status `ready` deltaP `2.0776` edge `-0.0372` maxDD `-11.3243`
- `market_context_high->index_4h` score `-3.499` n `95` status `ready` deltaP `-9.0709` edge `-0.0428` maxDD `-4.398`
- `market_context_high->crypto_major_4h` score `-5.9154` n `95` status `ready` deltaP `-9.2233` edge `-0.1838` maxDD `-34.3815`
- `market_context_high->index_24h` score `-6.7569` n `39` status `ready` deltaP `-34.1346` edge `-0.1991` maxDD `-5.5798`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

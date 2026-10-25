# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-25T04:22:25.683799+00:00`
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

- `market_context_high->unknown_4h` score `52.3809` n `95` status `ready` deltaP `0.8408` edge `4.393` maxDD `-1.016`
- `market_context_high->unknown_1h` score `18.109` n `107` status `ready` deltaP `4.512` edge `1.5279` maxDD `-1.5781`
- `market_context_high->crypto_alt_24h` score `1.4701` n `41` status `ready` deltaP `20.0288` edge `0.3361` maxDD `-19.8258`
- `market_context_high->commodity_24h` score `1.1059` n `41` status `ready` deltaP `15.1593` edge `0.082` maxDD `-3.6055`
- `market_context_high->fx_1h` score `-0.2857` n `107` status `ready` deltaP `-0.6128` edge `0.0025` maxDD `-0.137`
- `market_context_high->commodity_1h` score `-0.375` n `107` status `ready` deltaP `1.5474` edge `0.0085` maxDD `-1.0053`
- `market_context_high->crypto_major_24h` score `-0.4047` n `41` status `ready` deltaP `10.116` edge `0.0771` maxDD `-11.0468`
- `market_context_high->index_1h` score `-0.4896` n `107` status `ready` deltaP `1.143` edge `-0.0052` maxDD `-1.2155`
- `market_context_high->fx_4h` score `-0.5135` n `95` status `ready` deltaP `-1.7971` edge `0.006` maxDD `-0.4545`
- `market_context_high->fx_24h` score `-0.5356` n `41` status `ready` deltaP `3.938` edge `0.0033` maxDD `-0.9352`
- `market_context_high->commodity_4h` score `-0.7058` n `95` status `ready` deltaP `-0.6129` edge `0.039` maxDD `-1.165`
- `market_context_high->metal_1h` score `-0.7912` n `107` status `ready` deltaP `2.7534` edge `-0.0051` maxDD `-1.6682`
- `market_context_high->crypto_major_1h` score `-1.0554` n `107` status `ready` deltaP `4.6141` edge `-0.008` maxDD `-9.3126`
- `market_context_high->metal_4h` score `-2.2707` n `95` status `ready` deltaP `1.5998` edge `-0.0266` maxDD `-5.53`
- `market_context_high->equity_1h` score `-2.3405` n `107` status `ready` deltaP `2.0049` edge `-0.0861` maxDD `-12.1865`
- `market_context_high->crypto_alt_1h` score `-2.3568` n `107` status `ready` deltaP `2.0776` edge `-0.0312` maxDD `-11.3243`
- `market_context_high->metal_24h` score `-2.5002` n `41` status `ready` deltaP `-6.0086` edge `-0.0204` maxDD `-6.4983`
- `market_context_high->index_4h` score `-3.6793` n `95` status `ready` deltaP `-10.8713` edge `-0.0443` maxDD `-4.5198`
- `market_context_high->crypto_major_4h` score `-6.1765` n `95` status `ready` deltaP `-11.0238` edge `-0.1959` maxDD `-35.1303`
- `market_context_high->index_24h` score `-6.837` n `41` status `ready` deltaP `-34.6629` edge `-0.196` maxDD `-5.7463`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

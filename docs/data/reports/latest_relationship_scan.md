# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-25T05:07:29.796613+00:00`
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

- `market_context_high->unknown_4h` score `51.4929` n `95` status `ready` deltaP `-0.0593` edge `4.325` maxDD `-1.016`
- `market_context_high->unknown_1h` score `18.511` n `107` status `ready` deltaP `4.512` edge `1.5614` maxDD `-1.5781`
- `market_context_high->crypto_alt_24h` score `6.0047` n `38` status `ready` deltaP `25.4203` edge `0.5217` maxDD `-13.5956`
- `market_context_high->crypto_major_24h` score `0.8108` n `38` status `ready` deltaP `14.6017` edge `0.1342` maxDD `-9.4516`
- `market_context_high->commodity_24h` score `0.5732` n `38` status `ready` deltaP `12.4635` edge `0.0813` maxDD `-3.6055`
- `market_context_high->fx_1h` score `-0.1599` n `107` status `ready` deltaP `1.7418` edge `0.0028` maxDD `-0.1258`
- `market_context_high->fx_24h` score `-0.1963` n `38` status `ready` deltaP `6.6338` edge `0.0048` maxDD `-0.9352`
- `market_context_high->fx_4h` score `-0.3645` n `95` status `ready` deltaP `0.9034` edge `0.0071` maxDD `-0.4545`
- `market_context_high->metal_1h` score `-0.3848` n `107` status `ready` deltaP `5.108` edge `-0.0042` maxDD `-1.6682`
- `market_context_high->index_1h` score `-0.4881` n `107` status `ready` deltaP `1.143` edge `-0.005` maxDD `-1.2155`
- `market_context_high->commodity_1h` score `-0.5802` n `107` status `ready` deltaP `-0.8073` edge `0.0071` maxDD `-1.0053`
- `market_context_high->crypto_major_1h` score `-1.0796` n `107` status `ready` deltaP `4.6141` edge `-0.0111` maxDD `-9.3126`
- `market_context_high->commodity_4h` score `-1.109` n `95` status `ready` deltaP `-3.3135` edge `0.0359` maxDD `-1.165`
- `market_context_high->metal_4h` score `-2.0112` n `95` status `ready` deltaP `4.3004` edge `-0.0247` maxDD `-5.3919`
- `market_context_high->equity_1h` score `-2.3428` n `107` status `ready` deltaP `2.0049` edge `-0.0864` maxDD `-12.1865`
- `market_context_high->metal_24h` score `-2.4104` n `38` status `ready` deltaP `-4.4682` edge `-0.0291` maxDD `-6.3582`
- `market_context_high->crypto_alt_1h` score `-2.524` n `107` status `ready` deltaP `1.2927` edge `-0.0399` maxDD `-11.3243`
- `market_context_high->index_4h` score `-3.4072` n `95` status `ready` deltaP `-8.1707` edge `-0.042` maxDD `-4.3303`
- `market_context_high->crypto_major_4h` score `-5.7842` n `95` status `ready` deltaP `-8.3232` edge `-0.1778` maxDD `-33.9952`
- `market_context_high->index_24h` score `-6.7272` n `38` status `ready` deltaP `-33.8358` edge `-0.2` maxDD `-5.4688`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

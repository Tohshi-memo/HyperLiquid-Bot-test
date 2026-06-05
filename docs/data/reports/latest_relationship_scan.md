# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-05T16:22:21.916268+00:00`
- Price records: `672`
- Market context records: `2985`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6970`

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

- `market_context_high->crypto_alt_24h` score `16.0247` n `99` status `ready` deltaP `5.0505` edge `1.6934` maxDD `-22.6673`
- `market_context_high->commodity_24h` score `11.8034` n `99` status `ready` deltaP `41.3037` edge `0.7193` maxDD `-0.2165`
- `market_context_high->unknown_24h` score `11.0706` n `99` status `ready` deltaP `16.9981` edge `0.8557` maxDD `-1.7175`
- `market_context_high->equity_24h` score `6.962` n `99` status `ready` deltaP `15.5303` edge `0.677` maxDD `-12.6963`
- `market_context_high->index_24h` score `4.422` n `99` status `ready` deltaP `15.6408` edge `0.3623` maxDD `-2.5127`
- `market_context_high->equity_4h` score `3.1825` n `100` status `ready` deltaP `14.9024` edge `0.2048` maxDD `-0.7819`
- `market_context_high->commodity_4h` score `2.2698` n `100` status `ready` deltaP `17.1402` edge `0.1396` maxDD `-2.8438`
- `market_context_high->index_4h` score `2.268` n `100` status `ready` deltaP `19.6098` edge `0.1371` maxDD `-1.9733`
- `market_context_high->crypto_alt_4h` score `0.8427` n `100` status `ready` deltaP `23.7561` edge `0.4058` maxDD `-30.8239`
- `market_context_high->index_1h` score `0.3365` n `103` status `ready` deltaP `6.9822` edge `0.0284` maxDD `-1.4189`
- `market_context_high->equity_1h` score `0.0626` n `103` status `ready` deltaP `5.4808` edge `0.0416` maxDD `-3.609`
- `market_context_high->commodity_1h` score `-0.2212` n `103` status `ready` deltaP `-0.1904` edge `0.0158` maxDD `-0.9706`
- `market_context_high->fx_1h` score `-0.4656` n `103` status `ready` deltaP `-1.311` edge `0.0012` maxDD `-0.1672`
- `market_context_high->crypto_alt_1h` score `-0.8489` n `103` status `ready` deltaP `8.5518` edge `0.0475` maxDD `-11.6869`
- `market_context_high->crypto_major_1h` score `-0.9593` n `103` status `ready` deltaP `6.1697` edge `0.019` maxDD `-11.9831`
- `market_context_high->fx_4h` score `-1.0181` n `100` status `ready` deltaP `-8.1524` edge `0.0017` maxDD `-0.5631`
- `market_context_high->unknown_4h` score `-1.2378` n `100` status `ready` deltaP `-0.6768` edge `0.0067` maxDD `-3.7602`
- `market_context_high->unknown_1h` score `-1.6624` n `103` status `ready` deltaP `2.2731` edge `-0.0806` maxDD `-3.1801`
- `market_context_high->metal_1h` score `-1.6667` n `103` status `ready` deltaP `-2.7179` edge `-0.0073` maxDD `-5.4112`
- `market_context_high->crypto_major_4h` score `-1.985` n `100` status `ready` deltaP `9.128` edge `0.1972` maxDD `-33.6701`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

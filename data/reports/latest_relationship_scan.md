# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-19T21:37:43.562481+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `10828`

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

- `market_context_high->equity_4h` score `2.2651` n `96` status `ready` deltaP `11.6107` edge `0.2002` maxDD `-2.4411`
- `market_context_high->equity_1h` score `1.7805` n `96` status `ready` deltaP `14.7019` edge `0.0805` maxDD `-0.4112`
- `market_context_high->index_1h` score `0.9845` n `96` status `ready` deltaP `16.5107` edge `0.0107` maxDD `-0.0982`
- `market_context_high->metal_4h` score `0.5016` n `96` status `ready` deltaP `13.2113` edge `0.0113` maxDD `-1.273`
- `market_context_high->index_4h` score `0.2942` n `96` status `ready` deltaP `9.7815` edge `0.0248` maxDD `-0.5728`
- `market_context_high->commodity_24h` score `0.2285` n `96` status `ready` deltaP `6.4236` edge `0.1698` maxDD `-4.666`
- `market_context_high->fx_4h` score `0.0359` n `96` status `ready` deltaP `7.4949` edge `0.0049` maxDD `-0.3539`
- `market_context_high->unknown_24h` score `0.0195` n `96` status `ready` deltaP `17.7083` edge `-0.0658` maxDD `-1.0505`
- `market_context_high->unknown_1h` score `-0.1608` n `96` status `ready` deltaP `6.0629` edge `-0.0311` maxDD `-0.4843`
- `market_context_high->metal_1h` score `-0.1795` n `96` status `ready` deltaP `2.9753` edge `0.0039` maxDD `-0.4291`
- `market_context_high->fx_1h` score `-0.3276` n `96` status `ready` deltaP `-1.3224` edge `0.0027` maxDD `-0.2043`
- `market_context_high->commodity_4h` score `-0.6599` n `96` status `ready` deltaP `-0.94` edge `0.0067` maxDD `-2.4692`
- `market_context_high->crypto_alt_1h` score `-0.8812` n `96` status `ready` deltaP `-0.7672` edge `-0.0277` maxDD `-2.413`
- `market_context_high->commodity_1h` score `-0.897` n `96` status `ready` deltaP `-7.8905` edge `-0.0058` maxDD `-1.1941`
- `market_context_high->crypto_major_1h` score `-0.9623` n `96` status `ready` deltaP `1.0354` edge `-0.0458` maxDD `-2.7581`
- `market_context_high->crypto_major_4h` score `-1.6805` n `96` status `ready` deltaP `5.5132` edge `-0.0747` maxDD `-3.1677`
- `market_context_high->crypto_alt_4h` score `-1.7896` n `96` status `ready` deltaP `3.3537` edge `-0.0445` maxDD `-5.4926`
- `market_context_high->crypto_major_24h` score `-1.8373` n `96` status `ready` deltaP `2.9514` edge `-0.052` maxDD `-4.9964`
- `market_context_high->metal_24h` score `-3.1552` n `96` status `ready` deltaP `-9.7222` edge `-0.0089` maxDD `-11.4635`
- `market_context_high->fx_24h` score `-3.3781` n `96` status `ready` deltaP `-17.5347` edge `-0.0063` maxDD `-1.9981`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

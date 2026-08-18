# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-18T02:52:37.238603+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11837`

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

- `market_context_high->crypto_major_24h` score `4.6739` n `73` status `ready` deltaP `16.8871` edge `0.3977` maxDD `-4.9964`
- `market_context_high->commodity_4h` score `0.5715` n `108` status `ready` deltaP `11.9185` edge `0.0532` maxDD `-2.4692`
- `market_context_high->equity_24h` score `0.5247` n `73` status `ready` deltaP `13.3947` edge `-0.0076` maxDD `-2.0376`
- `market_context_high->metal_24h` score `0.5203` n `73` status `ready` deltaP `4.8384` edge `0.0772` maxDD `-1.2881`
- `market_context_high->commodity_24h` score `0.4859` n `73` status `ready` deltaP `12.6469` edge `0.1395` maxDD `-4.666`
- `market_context_high->unknown_1h` score `0.2762` n `108` status `ready` deltaP `8.1171` edge `-0.0052` maxDD `-0.7386`
- `market_context_high->index_1h` score `0.1262` n `108` status `ready` deltaP `8.228` edge `0.0033` maxDD `-0.3584`
- `market_context_high->index_24h` score `0.0988` n `73` status `ready` deltaP `11.7115` edge `-0.0401` maxDD `-0.7126`
- `market_context_high->equity_1h` score `-0.0769` n `108` status `ready` deltaP `4.0641` edge `0.0233` maxDD `-1.8201`
- `market_context_high->fx_4h` score `-0.1651` n `108` status `ready` deltaP `5.2733` edge `0.0018` maxDD `-0.3904`
- `market_context_high->crypto_major_4h` score `-0.3546` n `108` status `ready` deltaP `3.1166` edge `0.0517` maxDD `-4.4346`
- `market_context_high->metal_4h` score `-0.3874` n `108` status `ready` deltaP `6.7976` edge `-0.007` maxDD `-3.039`
- `market_context_high->metal_1h` score `-0.6321` n `108` status `ready` deltaP `-1.5525` edge `-0.0036` maxDD `-1.3669`
- `market_context_high->fx_1h` score `-0.7672` n `108` status `ready` deltaP `-4.2083` edge `0.0003` maxDD `-0.2273`
- `market_context_high->commodity_1h` score `-0.7707` n `108` status `ready` deltaP `-5.7053` edge `0.0005` maxDD `-1.5684`
- `market_context_high->index_4h` score `-0.8809` n `108` status `ready` deltaP `-6.0072` edge `-0.0045` maxDD `-0.8045`
- `market_context_high->crypto_major_1h` score `-0.9033` n `108` status `ready` deltaP `-2.7501` edge `-0.0019` maxDD `-3.6463`
- `market_context_high->unknown_24h` score `-1.1388` n `73` status `ready` deltaP `1.4221` edge `-0.0876` maxDD `-1.4306`
- `market_context_high->crypto_alt_1h` score `-1.3466` n `108` status `ready` deltaP `-3.4043` edge `0.0009` maxDD `-3.2337`
- `market_context_high->equity_4h` score `-1.837` n `108` status `ready` deltaP `-9.5021` edge `-0.038` maxDD `-5.4002`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

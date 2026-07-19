# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-19T22:06:45.276471+00:00`
- Price records: `672`
- Market context records: `7295`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `13807`

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

- `market_context_high->fx_1h` score `-0.1114` n `128` status `ready` deltaP `4.8986` edge `0.002` maxDD `-0.5817`
- `market_context_high->commodity_1h` score `-0.6153` n `128` status `ready` deltaP `-0.9901` edge `-0.0139` maxDD `-1.6708`
- `market_context_high->crypto_alt_1h` score `-0.6341` n `128` status `ready` deltaP `-0.3321` edge `0.0248` maxDD `-5.9775`
- `market_context_high->crypto_major_1h` score `-0.7292` n `128` status `ready` deltaP `3.4899` edge `0.0243` maxDD `-7.6171`
- `market_context_high->fx_4h` score `-0.8429` n `126` status `ready` deltaP `5.6575` edge `0.0142` maxDD `-1.4649`
- `market_context_high->fx_24h` score `-0.9457` n `122` status `ready` deltaP `0.0371` edge `0.0013` maxDD `-2.1564`
- `market_context_high->commodity_4h` score `-1.1254` n `126` status `ready` deltaP `2.2135` edge `-0.0117` maxDD `-2.4139`
- `market_context_high->unknown_1h` score `-1.238` n `128` status `ready` deltaP `0.3508` edge `-0.0987` maxDD `-1.3217`
- `market_context_high->unknown_4h` score `-1.3039` n `126` status `ready` deltaP `6.1822` edge `0.086` maxDD `-6.2031`
- `market_context_high->index_1h` score `-1.3945` n `128` status `ready` deltaP `-6.1632` edge `-0.0098` maxDD `-2.2257`
- `market_context_high->metal_1h` score `-2.1966` n `128` status `ready` deltaP `-10.0206` edge `-0.0052` maxDD `-1.5506`
- `market_context_high->metal_4h` score `-2.4886` n `126` status `ready` deltaP `-9.8699` edge `-0.0077` maxDD `-4.6441`
- `market_context_high->commodity_24h` score `-3.0572` n `122` status `ready` deltaP `-5.9544` edge `-0.1353` maxDD `-2.3815`
- `market_context_high->crypto_major_4h` score `-3.1688` n `126` status `ready` deltaP `0.7307` edge `-0.0217` maxDD `-23.4879`
- `market_context_high->crypto_alt_4h` score `-3.4576` n `126` status `ready` deltaP `0.3581` edge `-0.015` maxDD `-15.3752`
- `market_context_high->equity_1h` score `-4.6096` n `128` status `ready` deltaP `-10.0694` edge `-0.0713` maxDD `-14.9894`
- `market_context_high->index_4h` score `-5.1841` n `126` status `ready` deltaP `-14.9119` edge `-0.062` maxDD `-11.3142`
- `market_context_high->unknown_24h` score `-5.5244` n `123` status `ready` deltaP `-9.9255` edge `-0.0505` maxDD `-15.4956`
- `market_context_high->metal_24h` score `-11.3337` n `123` status `ready` deltaP `-29.1709` edge `-0.1324` maxDD `-22.7414`
- `market_context_high->index_24h` score `-13.5314` n `122` status `ready` deltaP `-29.7149` edge `-0.1709` maxDD `-35.6892`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

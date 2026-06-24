# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-24T23:37:27.504327+00:00`
- Price records: `672`
- Market context records: `4669`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9870`

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

- `market_context_high->unknown_1h` score `72.4542` n `143` status `ready` deltaP `9.8447` edge `6.017` maxDD `-1.916`
- `market_context_high->unknown_4h` score `4.3386` n `143` status `ready` deltaP `10.0941` edge `0.4153` maxDD `-4.6834`
- `market_context_high->unknown_24h` score `1.3992` n `143` status `ready` deltaP `9.2148` edge `0.1475` maxDD `-4.7201`
- `market_context_high->commodity_1h` score `-0.433` n `143` status `ready` deltaP `2.4925` edge `0.0269` maxDD `-2.0345`
- `market_context_high->fx_1h` score `-0.5336` n `143` status `ready` deltaP `-1.4018` edge `-0.0036` maxDD `-1.1038`
- `market_context_high->fx_4h` score `-0.7373` n `143` status `ready` deltaP `1.8473` edge `0.0014` maxDD `-1.9927`
- `market_context_high->index_4h` score `-0.7494` n `143` status `ready` deltaP `3.81` edge `-0.0092` maxDD `-5.9823`
- `market_context_high->equity_1h` score `-0.8438` n `143` status `ready` deltaP `-2.0969` edge `0.0045` maxDD `-5.5624`
- `market_context_high->equity_4h` score `-1.2842` n `143` status `ready` deltaP `1.4072` edge `0.0029` maxDD `-8.8203`
- `market_context_high->commodity_4h` score `-1.294` n `143` status `ready` deltaP `4.2693` edge `0.0164` maxDD `-9.1941`
- `market_context_high->index_1h` score `-1.6946` n `143` status `ready` deltaP `-4.1927` edge `-0.0124` maxDD `-2.7358`
- `market_context_high->metal_1h` score `-2.9093` n `143` status `ready` deltaP `-4.5497` edge `-0.0775` maxDD `-17.8795`
- `market_context_high->commodity_24h` score `-4.7581` n `143` status `ready` deltaP `13.5343` edge `0.0637` maxDD `-30.7016`
- `market_context_high->fx_24h` score `-4.9945` n `143` status `ready` deltaP `-10.4106` edge `-0.0105` maxDD `-5.9042`
- `market_context_high->crypto_alt_1h` score `-5.4085` n `143` status `ready` deltaP `-1.9472` edge `-0.109` maxDD `-22.2982`
- `market_context_high->crypto_major_1h` score `-6.6506` n `143` status `ready` deltaP `-5.7944` edge `-0.1403` maxDD `-27.356`
- `market_context_high->index_24h` score `-7.62` n `143` status `ready` deltaP `-7.4872` edge `-0.0476` maxDD `-29.3321`
- `market_context_high->crypto_alt_4h` score `-8.247` n `143` status `ready` deltaP `-1.049` edge `-0.1846` maxDD `-63.9243`
- `market_context_high->metal_4h` score `-9.5704` n `143` status `ready` deltaP `-3.4592` edge `-0.286` maxDD `-67.0999`
- `market_context_high->crypto_major_4h` score `-11.4016` n `143` status `ready` deltaP `-3.326` edge `-0.3452` maxDD `-82.2164`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

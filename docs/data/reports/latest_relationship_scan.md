# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-28T00:07:30.308599+00:00`
- Price records: `672`
- Market context records: `4987`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `9536`

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

- `market_context_high->unknown_1h` score `19.8075` n `88` status `ready` deltaP `3.3479` edge `1.6784` maxDD `-1.674`
- `market_context_high->crypto_major_4h` score `6.1436` n `87` status `ready` deltaP `17.7916` edge `0.5419` maxDD `-7.8836`
- `market_context_high->unknown_24h` score `5.8055` n `74` status `ready` deltaP `28.2517` edge `0.3297` maxDD `-1.4072`
- `market_context_high->crypto_alt_4h` score `5.1322` n `87` status `ready` deltaP `12.4317` edge `0.4842` maxDD `-7.8181`
- `market_context_high->unknown_4h` score `1.4387` n `87` status `ready` deltaP `20.4321` edge `0.0859` maxDD `-5.5109`
- `market_context_high->metal_4h` score `1.1109` n `87` status `ready` deltaP `11.0352` edge `0.1269` maxDD `-1.9651`
- `market_context_high->equity_1h` score `0.8592` n `88` status `ready` deltaP `7.417` edge `0.0795` maxDD `-2.5875`
- `market_context_high->crypto_major_1h` score `0.8539` n `88` status `ready` deltaP `5.9268` edge `0.1234` maxDD `-4.6734`
- `market_context_high->equity_4h` score `0.5802` n `87` status `ready` deltaP `4.5504` edge `0.1822` maxDD `-6.3852`
- `market_context_high->index_4h` score `0.332` n `87` status `ready` deltaP `4.9954` edge `0.0426` maxDD `-0.8587`
- `market_context_high->metal_1h` score `0.3199` n `88` status `ready` deltaP `5.6274` edge `0.0388` maxDD `-1.3057`
- `market_context_high->crypto_alt_1h` score `0.067` n `88` status `ready` deltaP `3.62` edge `0.0867` maxDD `-5.5126`
- `market_context_high->fx_24h` score `-0.2373` n `74` status `ready` deltaP `6.0858` edge `0.0052` maxDD `-1.7626`
- `market_context_high->commodity_1h` score `-0.4777` n `88` status `ready` deltaP `-0.4151` edge `0.0075` maxDD `-1.278`
- `market_context_high->index_1h` score `-0.5633` n `88` status `ready` deltaP `1.9733` edge `0.014` maxDD `-0.5946`
- `market_context_high->fx_4h` score `-0.8271` n `87` status `ready` deltaP `-1.1845` edge `-0.0011` maxDD `-1.0967`
- `market_context_high->commodity_4h` score `-1.2618` n `87` status `ready` deltaP `3.5867` edge `-0.0038` maxDD `-5.021`
- `market_context_high->fx_1h` score `-1.6071` n `88` status `ready` deltaP `-10.343` edge `-0.005` maxDD `-0.4646`
- `market_context_high->commodity_24h` score `-3.9356` n `74` status `ready` deltaP `7.8782` edge `-0.0462` maxDD `-27.5371`
- `market_context_high->metal_24h` score `-4.3252` n `74` status `ready` deltaP `-1.9097` edge `0.0037` maxDD `-32.9721`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

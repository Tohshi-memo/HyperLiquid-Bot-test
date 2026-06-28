# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-28T02:52:32.298883+00:00`
- Price records: `672`
- Market context records: `4999`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10290`

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

- `market_context_high->unknown_1h` score `15.9907` n `93` status `ready` deltaP `4.417` edge `1.3532` maxDD `-1.674`
- `market_context_high->crypto_major_4h` score `6.1918` n `87` status `ready` deltaP `17.944` edge `0.5449` maxDD `-7.8836`
- `market_context_high->unknown_24h` score `6.0025` n `74` status `ready` deltaP `29.8142` edge `0.3357` maxDD `-1.4072`
- `market_context_high->crypto_alt_4h` score `5.154` n `87` status `ready` deltaP `12.5841` edge `0.485` maxDD `-7.8181`
- `market_context_high->metal_4h` score `1.1121` n `87` status `ready` deltaP `11.0352` edge `0.127` maxDD `-1.9651`
- `market_context_high->unknown_4h` score `1.0677` n `87` status `ready` deltaP `21.1943` edge `0.0499` maxDD `-5.5109`
- `market_context_high->equity_1h` score `0.874` n `93` status `ready` deltaP `8.1868` edge `0.0756` maxDD `-2.5875`
- `market_context_high->crypto_major_1h` score `0.8596` n `93` status `ready` deltaP `6.553` edge `0.1197` maxDD `-4.6734`
- `market_context_high->equity_4h` score `0.7049` n `87` status `ready` deltaP `6.2273` edge `0.187` maxDD `-6.3852`
- `market_context_high->index_4h` score `0.4842` n `87` status `ready` deltaP `6.6723` edge `0.0441` maxDD `-0.8587`
- `market_context_high->metal_1h` score `0.3736` n `93` status `ready` deltaP `6.4033` edge `0.0381` maxDD `-1.3057`
- `market_context_high->crypto_alt_1h` score `0.1773` n `93` status `ready` deltaP `5.1107` edge `0.0909` maxDD `-5.5126`
- `market_context_high->fx_24h` score `-0.211` n `74` status `ready` deltaP `6.6066` edge `0.0051` maxDD `-1.7626`
- `market_context_high->commodity_1h` score `-0.3111` n `93` status `ready` deltaP `1.8576` edge `0.0137` maxDD `-1.278`
- `market_context_high->index_1h` score `-0.5814` n `93` status `ready` deltaP `1.9123` edge `0.0129` maxDD `-0.5946`
- `market_context_high->fx_4h` score `-0.8073` n `87` status `ready` deltaP `-0.8796` edge `-0.0006` maxDD `-1.0967`
- `market_context_high->commodity_4h` score `-1.3632` n `87` status `ready` deltaP `3.1294` edge `-0.0092` maxDD `-5.021`
- `market_context_high->fx_1h` score `-1.7461` n `93` status `ready` deltaP `-11.8489` edge `-0.0055` maxDD `-0.5482`
- `market_context_high->commodity_24h` score `-4.0967` n `74` status `ready` deltaP `6.4893` edge `-0.0576` maxDD `-27.5371`
- `market_context_high->metal_24h` score `-4.1713` n `74` status `ready` deltaP `0.0` edge `0.0107` maxDD `-32.9721`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

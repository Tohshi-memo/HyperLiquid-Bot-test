# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-28T02:37:30.853893+00:00`
- Price records: `672`
- Market context records: `4998`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10448`

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

- `market_context_high->unknown_1h` score `16.293` n `93` status `ready` deltaP `4.5667` edge `1.3774` maxDD `-1.674`
- `market_context_high->crypto_major_4h` score `6.187` n `87` status `ready` deltaP `17.944` edge `0.5445` maxDD `-7.8836`
- `market_context_high->unknown_24h` score `6.1249` n `74` status `ready` deltaP `29.8142` edge `0.3459` maxDD `-1.4072`
- `market_context_high->crypto_alt_4h` score `5.1528` n `87` status `ready` deltaP `12.5841` edge `0.4849` maxDD `-7.8181`
- `market_context_high->unknown_4h` score `1.3473` n `87` status `ready` deltaP `21.1943` edge `0.0732` maxDD `-5.5109`
- `market_context_high->metal_4h` score `1.1109` n `87` status `ready` deltaP `11.0352` edge `0.1269` maxDD `-1.9651`
- `market_context_high->equity_1h` score `0.8596` n `93` status `ready` deltaP `8.0371` edge `0.0754` maxDD `-2.5875`
- `market_context_high->crypto_major_1h` score `0.8417` n `93` status `ready` deltaP `6.4033` edge `0.1192` maxDD `-4.6734`
- `market_context_high->equity_4h` score `0.693` n `87` status `ready` deltaP `6.0748` edge `0.1865` maxDD `-6.3852`
- `market_context_high->index_4h` score `0.4708` n `87` status `ready` deltaP `6.5198` edge `0.044` maxDD `-0.8587`
- `market_context_high->metal_1h` score `0.3616` n `93` status `ready` deltaP `6.2536` edge `0.0381` maxDD `-1.3057`
- `market_context_high->crypto_alt_1h` score `0.1672` n `93` status `ready` deltaP `4.961` edge `0.0906` maxDD `-5.5126`
- `market_context_high->fx_24h` score `-0.2208` n `74` status `ready` deltaP `6.433` edge `0.005` maxDD `-1.7626`
- `market_context_high->commodity_1h` score `-0.3197` n `93` status `ready` deltaP `1.7079` edge `0.0136` maxDD `-1.278`
- `market_context_high->index_1h` score `-0.5946` n `93` status `ready` deltaP `1.7626` edge `0.0128` maxDD `-0.5946`
- `market_context_high->fx_4h` score `-0.8073` n `87` status `ready` deltaP `-0.8796` edge `-0.0006` maxDD `-1.0967`
- `market_context_high->commodity_4h` score `-1.345` n `87` status `ready` deltaP `3.2819` edge `-0.0087` maxDD `-5.021`
- `market_context_high->fx_1h` score `-1.7461` n `93` status `ready` deltaP `-11.8489` edge `-0.0055` maxDD `-0.5482`
- `market_context_high->commodity_24h` score `-4.0768` n `74` status `ready` deltaP `6.6629` edge `-0.0562` maxDD `-27.5371`
- `market_context_high->metal_24h` score `-4.1835` n `74` status `ready` deltaP `-0.1736` edge `0.0103` maxDD `-32.9721`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

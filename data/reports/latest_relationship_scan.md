# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-28T12:37:25.649953+00:00`
- Price records: `672`
- Market context records: `5040`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10202`

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

- `market_context_high->unknown_1h` score `12.5733` n `99` status `ready` deltaP `3.6095` edge `1.0738` maxDD `-1.674`
- `market_context_high->unknown_4h` score `9.0729` n `93` status `ready` deltaP `22.3642` edge `0.7092` maxDD `-5.5109`
- `market_context_high->crypto_major_4h` score `5.4623` n `93` status `ready` deltaP `16.4897` edge `0.5037` maxDD `-8.3416`
- `market_context_high->crypto_alt_4h` score `5.3092` n `93` status `ready` deltaP `14.1785` edge `0.4873` maxDD `-7.8181`
- `market_context_high->metal_4h` score `1.2014` n `93` status `ready` deltaP `12.7819` edge `0.1228` maxDD `-1.9651`
- `market_context_high->equity_1h` score `0.7729` n `99` status `ready` deltaP `7.7633` edge `0.07` maxDD `-2.5875`
- `market_context_high->crypto_major_1h` score `0.7564` n `99` status `ready` deltaP `6.5672` edge `0.111` maxDD `-4.6734`
- `market_context_high->equity_4h` score `0.3655` n `93` status `ready` deltaP `2.2063` edge `0.1703` maxDD `-6.3852`
- `market_context_high->metal_1h` score `0.3442` n `99` status `ready` deltaP `6.3056` edge `0.0363` maxDD `-1.3057`
- `market_context_high->crypto_alt_1h` score `0.2312` n `99` status `ready` deltaP `5.7431` edge `0.0936` maxDD `-5.5126`
- `market_context_high->fx_24h` score `-0.0004` n `74` status `ready` deltaP `10.2525` edge `0.0078` maxDD `-1.7626`
- `market_context_high->index_4h` score `-0.2324` n `93` status `ready` deltaP `2.6472` edge `0.0391` maxDD `-1.0893`
- `market_context_high->commodity_1h` score `-0.2725` n `99` status `ready` deltaP `2.3015` edge `0.0157` maxDD `-1.278`
- `market_context_high->index_1h` score `-0.3807` n `99` status `ready` deltaP `1.9643` edge `0.0122` maxDD `-0.5946`
- `market_context_high->commodity_4h` score `-0.7633` n `93` status `ready` deltaP `4.1552` edge `-0.0003` maxDD `-5.021`
- `market_context_high->fx_4h` score `-1.0252` n `93` status `ready` deltaP `-4.5256` edge `-0.0024` maxDD `-1.2426`
- `market_context_high->fx_1h` score `-1.5467` n `99` status `ready` deltaP `-9.3707` edge `-0.0054` maxDD `-0.5482`
- `market_context_high->metal_24h` score `-3.613` n `74` status `ready` deltaP `6.5972` edge `0.0383` maxDD `-32.9721`
- `market_context_high->commodity_24h` score `-4.7148` n `74` status `ready` deltaP `-0.2816` edge `-0.0917` maxDD `-27.5371`
- `market_context_high->crypto_major_24h` score `-6.1002` n `74` status `ready` deltaP `14.635` edge `0.3999` maxDD `-90.3633`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

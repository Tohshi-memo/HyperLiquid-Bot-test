# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-27T14:52:28.137433+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8880`

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

- `market_context_high->unknown_4h` score `80.467` n `135` status `ready` deltaP `4.5472` edge `6.6905` maxDD `-0.5521`
- `market_context_high->unknown_1h` score `14.9808` n `135` status `ready` deltaP `1.069` edge `1.2902` maxDD `-1.5807`
- `market_context_high->index_24h` score `2.0107` n `135` status `ready` deltaP `27.1875` edge `0.0551` maxDD `-2.17`
- `market_context_high->fx_1h` score `0.4943` n `135` status `ready` deltaP `11.0557` edge `0.0033` maxDD `-0.1986`
- `market_context_high->fx_4h` score `0.3434` n `135` status `ready` deltaP `11.8293` edge `0.0096` maxDD `-0.4545`
- `market_context_high->metal_1h` score `-0.0233` n `135` status `ready` deltaP `9.4478` edge `0.0087` maxDD `-1.3073`
- `market_context_high->commodity_1h` score `-0.2554` n `135` status `ready` deltaP `2.5771` edge `0.0116` maxDD `-1.0053`
- `market_context_high->crypto_major_1h` score `-0.4926` n `135` status `ready` deltaP `5.7363` edge `0.0269` maxDD `-6.9306`
- `market_context_high->commodity_4h` score `-0.5358` n `135` status `ready` deltaP `5.1648` edge `0.0428` maxDD `-1.0837`
- `market_context_high->index_1h` score `-0.5718` n `135` status `ready` deltaP `-0.3626` edge `-0.0026` maxDD `-1.4631`
- `market_context_high->fx_24h` score `-0.6622` n `135` status `ready` deltaP `8.0903` edge `0.0184` maxDD `-1.2451`
- `market_context_high->metal_4h` score `-0.8086` n `135` status `ready` deltaP `8.0137` edge `-0.003` maxDD `-4.6603`
- `market_context_high->metal_24h` score `-0.9525` n `135` status `ready` deltaP `16.0995` edge `0.0911` maxDD `-8.2244`
- `market_context_high->equity_1h` score `-1.4495` n `135` status `ready` deltaP `1.8906` edge `-0.0072` maxDD `-9.2993`
- `market_context_high->crypto_alt_1h` score `-1.9476` n `135` status `ready` deltaP `-1.0413` edge `-0.0064` maxDD `-12.2409`
- `market_context_high->equity_24h` score `-1.9806` n `135` status `ready` deltaP `8.0671` edge `0.0776` maxDD `-15.7143`
- `market_context_high->index_4h` score `-2.7387` n `135` status `ready` deltaP `-5.5556` edge `-0.029` maxDD `-5.6417`
- `market_context_high->crypto_major_4h` score `-3.7406` n `135` status `ready` deltaP `3.3548` edge `-0.07` maxDD `-27.2215`
- `market_context_high->crypto_major_24h` score `-4.054` n `135` status `ready` deltaP `0.3704` edge `-0.0365` maxDD `-29.1905`
- `market_context_high->equity_4h` score `-5.177` n `135` status `ready` deltaP `1.3279` edge `-0.1492` maxDD `-35.2032`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-05T20:43:06.958553+00:00`
- Price records: `672`
- Market context records: `5810`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9076`

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

- `market_context_high->equity_24h` score `0.1973` n `248` status `ready` deltaP `15.3954` edge `0.4217` maxDD `-31.6316`
- `market_context_high->equity_4h` score `0.1488` n `291` status `ready` deltaP `5.7272` edge `0.12` maxDD `-6.9958`
- `market_context_high->fx_1h` score `-0.1979` n `291` status `ready` deltaP `3.2646` edge `0.0014` maxDD `-0.5499`
- `market_context_high->commodity_1h` score `-0.627` n `291` status `ready` deltaP `-1.5124` edge `-0.0032` maxDD `-2.7017`
- `market_context_high->index_1h` score `-0.6484` n `291` status `ready` deltaP `0.0767` edge `0.0032` maxDD `-0.9472`
- `market_context_high->metal_1h` score `-0.6773` n `291` status `ready` deltaP `1.8118` edge `-0.001` maxDD `-2.0682`
- `market_context_high->equity_1h` score `-0.7033` n `291` status `ready` deltaP `2.3973` edge `0.0261` maxDD `-5.0555`
- `market_context_high->crypto_major_1h` score `-0.9187` n `291` status `ready` deltaP `3.0367` edge `0.0353` maxDD `-6.2348`
- `market_context_high->crypto_alt_1h` score `-1.0964` n `291` status `ready` deltaP `1.407` edge `0.0327` maxDD `-6.6758`
- `market_context_high->index_4h` score `-1.248` n `291` status `ready` deltaP `-0.1613` edge `0.0098` maxDD `-3.165`
- `market_context_high->fx_24h` score `-1.376` n `248` status `ready` deltaP `10.5903` edge `0.0325` maxDD `-5.3614`
- `market_context_high->fx_4h` score `-1.4121` n `291` status `ready` deltaP `1.4353` edge `0.0043` maxDD `-2.2593`
- `market_context_high->metal_4h` score `-2.2363` n `291` status `ready` deltaP `-4.3987` edge `-0.0445` maxDD `-9.6969`
- `market_context_high->crypto_major_4h` score `-2.7189` n `291` status `ready` deltaP `8.0499` edge `0.157` maxDD `-25.6458`
- `market_context_high->commodity_4h` score `-2.8198` n `291` status `ready` deltaP `-2.0996` edge `-0.0183` maxDD `-8.8815`
- `market_context_high->index_24h` score `-4.3249` n `248` status `ready` deltaP `3.7131` edge `0.0293` maxDD `-18.1572`
- `market_context_high->crypto_alt_4h` score `-4.3843` n `291` status `ready` deltaP `5.7581` edge `0.0971` maxDD `-28.7346`
- `market_context_high->metal_24h` score `-5.7054` n `248` status `ready` deltaP `-4.7659` edge `-0.2375` maxDD `-20.6416`
- `market_context_high->commodity_24h` score `-9.4008` n `248` status `ready` deltaP `-13.1496` edge `-0.0671` maxDD `-32.9577`
- `market_context_high->crypto_major_24h` score `-11.2092` n `248` status `ready` deltaP `-2.2234` edge `-0.2571` maxDD `-35.3078`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

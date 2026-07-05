# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-05T13:07:29.030192+00:00`
- Price records: `672`
- Market context records: `5774`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `8674`

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

- `market_context_high->equity_24h` score `0.6736` n `232` status `ready` deltaP `15.5472` edge `0.4906` maxDD `-31.6316`
- `market_context_high->equity_4h` score `0.1493` n `289` status `ready` deltaP `7.6357` edge `0.1254` maxDD `-7.4425`
- `market_context_high->fx_1h` score `-0.2653` n `301` status `ready` deltaP `1.9769` edge `0.0009` maxDD `-0.5144`
- `market_context_high->equity_1h` score `-0.5968` n `301` status `ready` deltaP `3.5789` edge `0.0271` maxDD `-5.0555`
- `market_context_high->metal_1h` score `-0.6287` n `301` status `ready` deltaP `2.3892` edge `-0.0008` maxDD `-2.0682`
- `market_context_high->commodity_1h` score `-0.8018` n `301` status `ready` deltaP `-2.5061` edge `-0.0056` maxDD `-3.7721`
- `market_context_high->crypto_major_1h` score `-0.8667` n `301` status `ready` deltaP `3.5212` edge `0.0364` maxDD `-6.2348`
- `market_context_high->fx_24h` score `-0.9184` n `232` status `ready` deltaP `14.8647` edge `0.0415` maxDD `-3.6674`
- `market_context_high->index_1h` score `-0.9488` n `301` status `ready` deltaP `0.6112` edge `0.0037` maxDD `-0.9472`
- `market_context_high->crypto_alt_1h` score `-1.0787` n `301` status `ready` deltaP `1.8088` edge `0.0315` maxDD `-6.6758`
- `market_context_high->fx_4h` score `-1.2593` n `289` status `ready` deltaP `2.6072` edge `0.0057` maxDD `-1.4288`
- `market_context_high->index_4h` score `-1.8475` n `289` status `ready` deltaP `0.6255` edge `0.0106` maxDD `-3.165`
- `market_context_high->commodity_4h` score `-2.447` n `289` status `ready` deltaP `-2.8737` edge `-0.027` maxDD `-14.071`
- `market_context_high->metal_4h` score `-2.5366` n `289` status `ready` deltaP `-6.1592` edge `-0.0482` maxDD `-11.5426`
- `market_context_high->crypto_major_4h` score `-2.8338` n `289` status `ready` deltaP `7.7686` edge `0.1493` maxDD `-25.6458`
- `market_context_high->index_24h` score `-2.8866` n `232` status `ready` deltaP `2.203` edge `0.0297` maxDD `-18.1572`
- `market_context_high->crypto_alt_4h` score `-4.3938` n `289` status `ready` deltaP `5.6101` edge `0.0973` maxDD `-28.7346`
- `market_context_high->crypto_major_24h` score `-5.7726` n `232` status `ready` deltaP `4.3164` edge `-0.0433` maxDD `-29.6555`
- `market_context_high->metal_24h` score `-7.0357` n `232` status `ready` deltaP `-7.8724` edge `-0.2426` maxDD `-27.5543`
- `market_context_high->commodity_24h` score `-10.8906` n `232` status `ready` deltaP `-13.7153` edge `-0.0785` maxDD `-40.676`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

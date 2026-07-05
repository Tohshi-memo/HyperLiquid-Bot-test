# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-05T10:07:27.464522+00:00`
- Price records: `672`
- Market context records: `5760`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `8666`

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

- `market_context_high->equity_24h` score `0.7536` n `226` status `ready` deltaP `15.181` edge `0.5033` maxDD `-31.6316`
- `market_context_high->equity_4h` score `0.1658` n `283` status `ready` deltaP `7.4372` edge `0.1281` maxDD `-7.4425`
- `market_context_high->fx_1h` score `-0.2167` n `295` status `ready` deltaP `2.8814` edge `0.0011` maxDD `-0.5144`
- `market_context_high->metal_1h` score `-0.4425` n `295` status `ready` deltaP `1.7233` edge `-0.0007` maxDD `-2.0682`
- `market_context_high->equity_1h` score `-0.6707` n `295` status `ready` deltaP `2.7748` edge `0.0263` maxDD `-5.0555`
- `market_context_high->commodity_1h` score `-0.7857` n `295` status `ready` deltaP `-2.1329` edge `-0.0058` maxDD `-3.7906`
- `market_context_high->crypto_major_1h` score `-0.9104` n `295` status `ready` deltaP `3.2203` edge `0.0323` maxDD `-6.0378`
- `market_context_high->fx_24h` score `-0.9223` n `226` status `ready` deltaP `14.5956` edge `0.0428` maxDD `-3.6674`
- `market_context_high->crypto_alt_1h` score `-0.9783` n `295` status `ready` deltaP `1.873` edge `0.0311` maxDD `-6.0087`
- `market_context_high->index_1h` score `-1.0142` n `295` status `ready` deltaP `-0.1918` edge `0.0036` maxDD `-0.9472`
- `market_context_high->index_4h` score `-1.1541` n `283` status `ready` deltaP `1.4652` edge `0.011` maxDD `-3.165`
- `market_context_high->fx_4h` score `-1.2262` n `283` status `ready` deltaP `3.1975` edge `0.006` maxDD `-1.4288`
- `market_context_high->metal_4h` score `-2.6272` n `283` status `ready` deltaP `-7.5212` edge `-0.0494` maxDD `-11.649`
- `market_context_high->crypto_major_4h` score `-2.6643` n `283` status `ready` deltaP `7.9366` edge `0.1556` maxDD `-25.1094`
- `market_context_high->index_24h` score `-2.9496` n `226` status `ready` deltaP `1.0816` edge `0.0291` maxDD `-18.1572`
- `market_context_high->commodity_4h` score `-3.7703` n `283` status `ready` deltaP `-2.7951` edge `-0.028` maxDD `-14.071`
- `market_context_high->crypto_alt_4h` score `-3.7761` n `283` status `ready` deltaP `6.6201` edge `0.1102` maxDD `-26.1874`
- `market_context_high->crypto_major_24h` score `-4.8365` n `226` status `ready` deltaP `6.3376` edge `0.0004` maxDD `-29.6555`
- `market_context_high->metal_24h` score `-7.6331` n `226` status `ready` deltaP `-9.5424` edge `-0.2484` maxDD `-30.3268`
- `market_context_high->commodity_24h` score `-11.5958` n `226` status `ready` deltaP `-12.7197` edge `-0.0838` maxDD `-43.4841`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

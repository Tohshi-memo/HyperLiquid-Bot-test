# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-24T20:22:26.156804+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7806`

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

- `market_context_high->unknown_4h` score `17.2618` n `102` status `ready` deltaP `-2.1431` edge `1.4863` maxDD `-1.016`
- `market_context_high->commodity_24h` score `1.3117` n `73` status `ready` deltaP `19.6513` edge `0.0692` maxDD `-3.6055`
- `market_context_high->commodity_4h` score `0.9177` n `102` status `ready` deltaP `12.9453` edge `0.0464` maxDD `-1.165`
- `market_context_high->fx_1h` score `-0.1476` n `111` status `ready` deltaP `2.0917` edge `0.0026` maxDD `-0.1712`
- `market_context_high->commodity_1h` score `-0.2264` n `111` status `ready` deltaP `3.7655` edge `0.0061` maxDD `-1.0053`
- `market_context_high->fx_4h` score `-0.3987` n `102` status `ready` deltaP `0.5858` edge `0.0056` maxDD `-0.5168`
- `market_context_high->index_1h` score `-1.0677` n `111` status `ready` deltaP `-2.5625` edge `-0.0067` maxDD `-1.2155`
- `market_context_high->metal_1h` score `-1.1503` n `111` status `ready` deltaP `-1.6697` edge `-0.0053` maxDD `-1.6873`
- `market_context_high->crypto_major_1h` score `-2.9258` n `111` status `ready` deltaP `-1.6481` edge `-0.0529` maxDD `-11.0607`
- `market_context_high->fx_24h` score `-3.1984` n `73` status `ready` deltaP `-11.0302` edge `-0.0056` maxDD `-2.3255`
- `market_context_high->metal_4h` score `-3.6149` n `102` status `ready` deltaP `-12.4253` edge `-0.031` maxDD `-5.9927`
- `market_context_high->equity_1h` score `-4.0645` n `111` status `ready` deltaP `-1.667` edge `-0.0947` maxDD `-12.6316`
- `market_context_high->metal_24h` score `-4.5171` n `73` status `ready` deltaP `-14.5619` edge `0.0233` maxDD `-8.2115`
- `market_context_high->crypto_alt_1h` score `-4.8569` n `111` status `ready` deltaP `-8.4224` edge `-0.0862` maxDD `-16.3245`
- `market_context_high->index_4h` score `-4.9366` n `102` status `ready` deltaP `-23.924` edge `-0.0516` maxDD `-5.3565`
- `market_context_high->crypto_major_24h` score `-6.6328` n `73` status `ready` deltaP `-13.0518` edge `-0.2773` maxDD `-29.8836`
- `market_context_high->index_24h` score `-8.857` n `73` status `ready` deltaP `-39.1957` edge `-0.1679` maxDD `-8.377`
- `market_context_high->crypto_major_4h` score `-16.5753` n `102` status `ready` deltaP `-31.528` edge `-0.4212` maxDD `-47.9909`
- `market_context_high->equity_4h` score `-17.3222` n `102` status `ready` deltaP `-24.8176` edge `-0.4827` maxDD `-51.2958`
- `market_context_high->crypto_alt_24h` score `-17.67` n `73` status `ready` deltaP `-9.9077` edge `-0.8086` maxDD `-97.925`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

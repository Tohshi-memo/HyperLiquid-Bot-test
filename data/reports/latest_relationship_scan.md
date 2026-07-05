# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-05T16:52:25.906294+00:00`
- Price records: `672`
- Market context records: `5792`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `8104`

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

- `market_context_high->equity_24h` score `0.6695` n `247` status `ready` deltaP `15.3431` edge `0.4614` maxDD `-31.6316`
- `market_context_high->equity_4h` score `-0.0357` n `304` status `ready` deltaP `6.5389` edge `0.1173` maxDD `-7.4425`
- `market_context_high->fx_1h` score `-0.256` n `305` status `ready` deltaP `2.2239` edge `0.0009` maxDD `-0.5499`
- `market_context_high->metal_1h` score `-0.6335` n `305` status `ready` deltaP `2.3589` edge `-0.001` maxDD `-2.0682`
- `market_context_high->equity_1h` score `-0.6401` n `305` status `ready` deltaP `3.1423` edge `0.0264` maxDD `-5.0555`
- `market_context_high->commodity_1h` score `-0.7524` n `305` status `ready` deltaP `-1.6462` edge `-0.005` maxDD `-3.7721`
- `market_context_high->crypto_major_1h` score `-0.9774` n `305` status `ready` deltaP `2.8723` edge `0.0315` maxDD `-6.2348`
- `market_context_high->index_1h` score `-0.9892` n `305` status `ready` deltaP `0.1208` edge `0.0036` maxDD `-0.9472`
- `market_context_high->fx_24h` score `-1.0607` n `247` status `ready` deltaP `13.8565` edge `0.039` maxDD `-4.3888`
- `market_context_high->crypto_alt_1h` score `-1.1119` n `305` status `ready` deltaP `1.6178` edge `0.03` maxDD `-6.6758`
- `market_context_high->index_4h` score `-1.1851` n `304` status `ready` deltaP `0.9146` edge `0.0107` maxDD `-3.165`
- `market_context_high->fx_4h` score `-1.4982` n `304` status `ready` deltaP `-0.0562` edge `0.0028` maxDD `-2.2265`
- `market_context_high->commodity_4h` score `-2.4699` n `304` status `ready` deltaP `-3.4499` edge `-0.0261` maxDD `-14.071`
- `market_context_high->index_24h` score `-2.8063` n `247` status `ready` deltaP `3.5531` edge `0.031` maxDD `-18.1572`
- `market_context_high->crypto_major_4h` score `-3.0132` n `304` status `ready` deltaP `7.4455` edge `0.1365` maxDD `-25.6458`
- `market_context_high->metal_4h` score `-3.8208` n `304` status `ready` deltaP `-5.2872` edge `-0.0472` maxDD `-11.5426`
- `market_context_high->crypto_alt_4h` score `-4.61` n `304` status `ready` deltaP `5.2471` edge `0.0817` maxDD `-28.7346`
- `market_context_high->metal_24h` score `-7.1301` n `247` status `ready` deltaP `-7.9636` edge `-0.2541` maxDD `-27.5543`
- `market_context_high->crypto_major_24h` score `-7.8863` n `247` status `ready` deltaP `1.1148` edge `-0.1356` maxDD `-29.6555`
- `market_context_high->commodity_24h` score `-11.0523` n `247` status `ready` deltaP `-14.8363` edge `-0.0845` maxDD `-40.676`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

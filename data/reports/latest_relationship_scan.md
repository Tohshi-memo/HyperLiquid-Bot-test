# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-05T13:52:29.847800+00:00`
- Price records: `672`
- Market context records: `5777`
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

- `market_context_high->equity_24h` score `0.6515` n `235` status `ready` deltaP `15.7233` edge `0.4866` maxDD `-31.6316`
- `market_context_high->equity_4h` score `0.1366` n `292` status `ready` deltaP `7.6721` edge `0.1241` maxDD `-7.4425`
- `market_context_high->fx_1h` score `-0.2884` n `304` status `ready` deltaP `1.6152` edge `0.0008` maxDD `-0.5499`
- `market_context_high->equity_1h` score `-0.5823` n `304` status `ready` deltaP `3.7898` edge `0.0269` maxDD `-5.0555`
- `market_context_high->metal_1h` score `-0.6059` n `304` status `ready` deltaP `2.6887` edge `-0.0009` maxDD `-2.0682`
- `market_context_high->commodity_1h` score `-0.7716` n `304` status `ready` deltaP `-1.9717` edge `-0.0053` maxDD `-3.7721`
- `market_context_high->crypto_major_1h` score `-0.853` n `304` status `ready` deltaP `3.648` edge `0.0367` maxDD `-6.2348`
- `market_context_high->fx_24h` score `-0.9331` n `235` status `ready` deltaP `14.6262` edge `0.0412` maxDD `-3.6674`
- `market_context_high->index_1h` score `-0.9369` n `304` status `ready` deltaP `0.7446` edge `0.0038` maxDD `-0.9472`
- `market_context_high->crypto_alt_1h` score `-1.02` n `304` status `ready` deltaP `2.0919` edge `0.0345` maxDD `-6.6758`
- `market_context_high->index_4h` score `-1.2001` n `292` status `ready` deltaP `0.6411` edge `0.0106` maxDD `-3.165`
- `market_context_high->fx_4h` score `-1.2912` n `292` status `ready` deltaP `2.0527` edge `0.0053` maxDD `-1.4288`
- `market_context_high->commodity_4h` score `-2.4472` n `292` status `ready` deltaP `-2.9527` edge `-0.0265` maxDD `-14.071`
- `market_context_high->index_24h` score `-2.8547` n `235` status `ready` deltaP `2.7423` edge `0.0302` maxDD `-18.1572`
- `market_context_high->crypto_major_4h` score `-2.8653` n `292` status `ready` deltaP `7.7201` edge `0.147` maxDD `-25.6458`
- `market_context_high->metal_4h` score `-3.8964` n `292` status `ready` deltaP `-6.0976` edge `-0.0481` maxDD `-11.5426`
- `market_context_high->crypto_alt_4h` score `-4.4334` n `292` status `ready` deltaP `5.4001` edge `0.0954` maxDD `-28.7346`
- `market_context_high->crypto_major_24h` score `-6.1639` n `235` status `ready` deltaP `3.8357` edge `-0.0602` maxDD `-29.6555`
- `market_context_high->metal_24h` score `-7.047` n `235` status `ready` deltaP `-7.865` edge `-0.2441` maxDD `-27.5543`
- `market_context_high->commodity_24h` score `-10.922` n `235` status `ready` deltaP `-13.9421` edge `-0.0796` maxDD `-40.676`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

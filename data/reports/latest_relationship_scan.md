# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-26T02:22:30.676045+00:00`
- Price records: `672`
- Market context records: `4784`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7510`

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

- `market_context_high->unknown_1h` score `8.1313` n `122` status `ready` deltaP `12.7295` edge `0.6345` maxDD `-1.674`
- `market_context_high->unknown_4h` score `7.5379` n `122` status `ready` deltaP `17.8054` edge `0.6305` maxDD `-4.6834`
- `market_context_high->unknown_24h` score `1.9208` n `107` status `ready` deltaP `11.52` edge `0.1756` maxDD `-4.7201`
- `market_context_high->commodity_4h` score `0.0964` n `122` status `ready` deltaP `11.8153` edge `0.0508` maxDD `-4.377`
- `market_context_high->commodity_1h` score `0.0818` n `122` status `ready` deltaP `5.0824` edge `0.0317` maxDD `-2.0345`
- `market_context_high->equity_4h` score `-0.4463` n `122` status `ready` deltaP `7.0147` edge `0.0646` maxDD `-8.8203`
- `market_context_high->fx_4h` score `-0.4622` n `122` status `ready` deltaP `2.5165` edge `0.0016` maxDD `-1.5439`
- `market_context_high->index_4h` score `-0.4849` n `122` status `ready` deltaP `5.9277` edge `0.0052` maxDD `-5.5505`
- `market_context_high->equity_1h` score `-0.853` n `122` status `ready` deltaP `0.9694` edge `-0.0008` maxDD `-4.1397`
- `market_context_high->fx_1h` score `-0.8873` n `122` status `ready` deltaP `-0.8835` edge `-0.0031` maxDD `-0.8626`
- `market_context_high->index_1h` score `-1.4578` n `122` status `ready` deltaP `-2.0958` edge `-0.0071` maxDD `-2.6999`
- `market_context_high->commodity_24h` score `-2.1904` n `107` status `ready` deltaP `19.7495` edge `0.0984` maxDD `-27.5371`
- `market_context_high->metal_1h` score `-2.2899` n `122` status `ready` deltaP `-1.097` edge `-0.0687` maxDD `-14.0715`
- `market_context_high->crypto_alt_1h` score `-3.1975` n `122` status `ready` deltaP `0.4491` edge `-0.0455` maxDD `-15.2495`
- `market_context_high->fx_24h` score `-3.3771` n `107` status `ready` deltaP `-15.5942` edge `-0.0225` maxDD `-3.3968`
- `market_context_high->crypto_major_1h` score `-4.5223` n `122` status `ready` deltaP `0.2356` edge `-0.0694` maxDD `-22.0555`
- `market_context_high->crypto_alt_4h` score `-5.0569` n `122` status `ready` deltaP `3.6785` edge `-0.0304` maxDD `-46.0617`
- `market_context_high->index_24h` score `-5.6762` n `107` status `ready` deltaP `-5.1029` edge `-0.1056` maxDD `-18.6716`
- `market_context_high->crypto_major_4h` score `-8.3634` n `122` status `ready` deltaP `2.439` edge `-0.1654` maxDD `-68.5143`
- `market_context_high->metal_4h` score `-8.536` n `122` status `ready` deltaP `5.163` edge `-0.3047` maxDD `-61.2596`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

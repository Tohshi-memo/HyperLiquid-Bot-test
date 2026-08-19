# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-19T12:52:28.051323+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11762`

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

- `market_context_high->equity_4h` score `2.0303` n `96` status `ready` deltaP `11.001` edge `0.1847` maxDD `-2.4411`
- `market_context_high->crypto_major_24h` score `1.7819` n `96` status `ready` deltaP `5.3819` edge `0.2334` maxDD `-4.9964`
- `market_context_high->equity_1h` score `1.772` n `96` status `ready` deltaP `14.8516` edge `0.0788` maxDD `-0.4112`
- `market_context_high->metal_4h` score `1.1998` n `96` status `ready` deltaP `17.7845` edge `0.039` maxDD `-1.273`
- `market_context_high->index_1h` score `0.9558` n `96` status `ready` deltaP `16.2113` edge `0.0103` maxDD `-0.0982`
- `market_context_high->crypto_major_4h` score `0.7985` n `96` status `ready` deltaP `10.0863` edge `0.1014` maxDD `-3.1677`
- `market_context_high->commodity_24h` score `0.7502` n `96` status `ready` deltaP `10.5903` edge `0.2089` maxDD `-4.666`
- `market_context_high->unknown_24h` score `0.3072` n `96` status `ready` deltaP `18.2291` edge `-0.0453` maxDD `-1.0505`
- `market_context_high->unknown_1h` score `0.1605` n `96` status `ready` deltaP `7.8593` edge `-0.0163` maxDD `-0.4843`
- `market_context_high->metal_1h` score `0.1488` n `96` status `ready` deltaP `5.9693` edge `0.0113` maxDD `-0.4291`
- `market_context_high->index_4h` score `0.1482` n `96` status `ready` deltaP `8.2571` edge `0.0228` maxDD `-0.5728`
- `market_context_high->fx_4h` score `0.1428` n `96` status `ready` deltaP `9.3242` edge `0.0064` maxDD `-0.3539`
- `market_context_high->crypto_alt_4h` score `-0.0408` n `96` status `ready` deltaP `8.3841` edge `0.0677` maxDD `-5.4926`
- `market_context_high->fx_1h` score `-0.3019` n `96` status `ready` deltaP `-0.8733` edge `0.003` maxDD `-0.2043`
- `market_context_high->crypto_major_1h` score `-0.3752` n `96` status `ready` deltaP `3.1312` edge `0.0155` maxDD `-2.7581`
- `market_context_high->crypto_alt_1h` score `-0.4486` n `96` status `ready` deltaP `1.7777` edge `0.0108` maxDD `-2.413`
- `market_context_high->commodity_4h` score `-0.6018` n `96` status `ready` deltaP `0.4319` edge `0.005` maxDD `-2.4692`
- `market_context_high->commodity_1h` score `-0.8939` n `96` status `ready` deltaP `-7.7408` edge `-0.0064` maxDD `-1.1941`
- `market_context_high->metal_24h` score `-2.2285` n `96` status `ready` deltaP `-3.6458` edge `0.0694` maxDD `-11.4635`
- `market_context_high->fx_24h` score `-3.8753` n `96` status `ready` deltaP `-21.875` edge `-0.0188` maxDD `-1.9981`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

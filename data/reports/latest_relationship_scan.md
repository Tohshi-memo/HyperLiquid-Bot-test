# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-18T14:37:36.762436+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11630`

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

- `market_context_high->crypto_major_24h` score `2.4083` n `91` status `ready` deltaP `9.6121` edge `0.2574` maxDD `-4.9964`
- `market_context_high->commodity_24h` score `1.77` n `91` status `ready` deltaP `19.3727` edge `0.2811` maxDD `-4.666`
- `market_context_high->equity_1h` score `1.1935` n `96` status `ready` deltaP `10.2109` edge `0.0618` maxDD `-0.4329`
- `market_context_high->metal_4h` score `0.7031` n `96` status `ready` deltaP `14.126` edge `0.022` maxDD `-1.273`
- `market_context_high->index_1h` score `0.6911` n `96` status `ready` deltaP `13.2173` edge `0.0082` maxDD `-0.0982`
- `market_context_high->unknown_1h` score `0.5843` n `96` status `ready` deltaP `9.8054` edge `0.006` maxDD `-0.4807`
- `market_context_high->crypto_major_4h` score `0.4786` n `96` status `ready` deltaP `8.562` edge `0.0849` maxDD `-3.1677`
- `market_context_high->equity_4h` score `0.1325` n `96` status `ready` deltaP `3.0742` edge `0.081` maxDD `-2.5696`
- `market_context_high->crypto_alt_4h` score `0.1102` n `96` status `ready` deltaP `9.1463` edge `0.0752` maxDD `-5.4926`
- `market_context_high->metal_1h` score `-0.0273` n `96` status `ready` deltaP `4.1729` edge `0.0086` maxDD `-0.4291`
- `market_context_high->fx_4h` score `-0.2068` n `96` status `ready` deltaP `3.5315` edge `0.0002` maxDD `-0.3539`
- `market_context_high->commodity_4h` score `-0.3719` n `96` status `ready` deltaP `3.938` edge `0.0111` maxDD `-2.4692`
- `market_context_high->crypto_alt_1h` score `-0.415` n `96` status `ready` deltaP `1.7777` edge `0.0151` maxDD `-2.413`
- `market_context_high->fx_1h` score `-0.4717` n `96` status `ready` deltaP `-3.8673` edge `0.0012` maxDD `-0.2043`
- `market_context_high->crypto_major_1h` score `-0.5255` n `96` status `ready` deltaP `0.8857` edge `0.0112` maxDD `-2.7581`
- `market_context_high->index_4h` score `-0.6395` n `96` status `ready` deltaP `0.3303` edge `0.01` maxDD `-0.5728`
- `market_context_high->unknown_24h` score `-0.7164` n `91` status `ready` deltaP `8.6427` edge `-0.0929` maxDD `-0.6204`
- `market_context_high->commodity_1h` score `-0.8643` n `96` status `ready` deltaP `-7.2917` edge `-0.0056` maxDD `-1.1941`
- `market_context_high->metal_24h` score `-2.5578` n `91` status `ready` deltaP `-8.9511` edge `0.0088` maxDD `-8.831`
- `market_context_high->fx_24h` score `-4.6367` n `91` status `ready` deltaP `-30.9369` edge `-0.0302` maxDD `-1.3293`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-20T22:22:15.737325+00:00`
- Price records: `672`
- Market context records: `1362`
- Flow alert records: `5836`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8804`

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

- `market_context_high->crypto_major_24h` score `13.2611` n `136` status `ready` deltaP `32.3529` edge `1.0026` maxDD `-8.0553`
- `market_context_high->metal_24h` score `12.6539` n `136` status `ready` deltaP `13.2762` edge `1.1327` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `10.0287` n `136` status `ready` deltaP `28.5233` edge `0.8472` maxDD `-15.1306`
- `market_context_high->index_24h` score `4.1419` n `136` status `ready` deltaP `23.0392` edge `0.3002` maxDD `-5.3574`
- `market_context_high->equity_24h` score `2.7728` n `136` status `ready` deltaP `16.0131` edge `0.357` maxDD `-14.2815`
- `market_context_high->equity_4h` score `2.1646` n `161` status `ready` deltaP `11.397` edge `0.1749` maxDD `-3.6396`
- `market_context_high->fx_24h` score `1.0849` n `136` status `ready` deltaP `13.0515` edge `0.0537` maxDD `-0.6911`
- `market_context_high->metal_4h` score `0.1362` n `161` status `ready` deltaP `12.6373` edge `0.0702` maxDD `-6.4478`
- `market_context_high->index_1h` score `-0.0071` n `173` status `ready` deltaP `4.5603` edge `0.0141` maxDD `-1.6329`
- `market_context_high->index_4h` score `-0.0558` n `161` status `ready` deltaP `4.1916` edge `0.0738` maxDD `-3.7119`
- `market_context_high->equity_1h` score `-0.0696` n `173` status `ready` deltaP `2.1858` edge `0.0251` maxDD `-2.2214`
- `market_context_high->metal_1h` score `-0.3068` n `173` status `ready` deltaP `6.3523` edge `0.0009` maxDD `-3.2728`
- `market_context_high->fx_1h` score `-0.3533` n `173` status `ready` deltaP `0.8048` edge `-0.0041` maxDD `-0.3914`
- `market_context_high->commodity_24h` score `-0.4656` n `136` status `ready` deltaP `-10.2022` edge `0.3213` maxDD `-18.3666`
- `market_context_high->commodity_1h` score `-0.6136` n `173` status `ready` deltaP `0.2475` edge `0.0087` maxDD `-2.252`
- `market_context_high->crypto_alt_1h` score `-0.8845` n `173` status `ready` deltaP `-0.713` edge `0.0181` maxDD `-3.6309`
- `market_context_high->crypto_major_1h` score `-1.1359` n `173` status `ready` deltaP `-3.3912` edge `-0.0165` maxDD `-6.1883`
- `market_context_high->crypto_alt_4h` score `-1.4291` n `161` status `ready` deltaP `7.5841` edge `0.1623` maxDD `-19.5565`
- `market_context_high->fx_4h` score `-2.0072` n `161` status `ready` deltaP `-8.9494` edge `-0.0147` maxDD `-1.0987`
- `market_context_high->crypto_major_4h` score `-2.0419` n `161` status `ready` deltaP `1.9988` edge `0.0874` maxDD `-13.3376`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

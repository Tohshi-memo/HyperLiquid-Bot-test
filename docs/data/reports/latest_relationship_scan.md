# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-18T05:37:27.568935+00:00`
- Price records: `672`
- Market context records: `7107`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11488`

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

- `market_context_high->fx_4h` score `0.3827` n `150` status `ready` deltaP `15.7744` edge `0.0139` maxDD `-0.9333`
- `market_context_high->fx_1h` score `-0.1561` n `150` status `ready` deltaP `4.3812` edge `0.0029` maxDD `-0.276`
- `market_context_high->unknown_1h` score `-0.1581` n `150` status `ready` deltaP `-0.1218` edge `0.0435` maxDD `-1.4688`
- `market_context_high->crypto_alt_1h` score `-0.3373` n `150` status `ready` deltaP `1.7685` edge `0.0314` maxDD `-4.5815`
- `market_context_high->crypto_major_1h` score `-0.5376` n `150` status `ready` deltaP `4.2176` edge `0.0382` maxDD `-7.1523`
- `market_context_high->index_1h` score `-0.5984` n `150` status `ready` deltaP `-1.2096` edge `-0.0067` maxDD `-2.2895`
- `market_context_high->commodity_1h` score `-0.8286` n `150` status `ready` deltaP `-3.8104` edge `-0.0192` maxDD `-1.9306`
- `market_context_high->commodity_4h` score `-1.3722` n `150` status `ready` deltaP `-4.4228` edge `-0.0429` maxDD `-2.9494`
- `market_context_high->unknown_4h` score `-1.5138` n `150` status `ready` deltaP `-5.996` edge `0.0061` maxDD `-4.4825`
- `market_context_high->metal_1h` score `-1.564` n `150` status `ready` deltaP `-7.1956` edge `-0.0058` maxDD `-2.1249`
- `market_context_high->equity_1h` score `-2.0817` n `150` status `ready` deltaP `3.0898` edge `-0.0452` maxDD `-14.716`
- `market_context_high->index_4h` score `-2.5772` n `150` status `ready` deltaP `-2.0549` edge `-0.0468` maxDD `-12.2591`
- `market_context_high->crypto_major_4h` score `-3.0086` n `150` status `ready` deltaP `4.4004` edge `0.0134` maxDD `-24.6094`
- `market_context_high->crypto_alt_4h` score `-3.0252` n `150` status `ready` deltaP `0.8394` edge `-0.0149` maxDD `-22.2831`
- `market_context_high->commodity_24h` score `-3.4606` n `150` status `ready` deltaP `-8.4305` edge `-0.1013` maxDD `-4.4704`
- `market_context_high->metal_4h` score `-4.3677` n `150` status `ready` deltaP `-8.3171` edge `-0.0114` maxDD `-5.4368`
- `market_context_high->fx_24h` score `-4.5093` n `150` status `ready` deltaP `-10.75` edge `-0.0214` maxDD `-3.9503`
- `market_context_high->equity_4h` score `-8.7961` n `150` status `ready` deltaP `-1.9594` edge `-0.2276` maxDD `-63.963`
- `market_context_high->unknown_24h` score `-9.1672` n `150` status `ready` deltaP `-25.9583` edge `-0.0762` maxDD `-23.5076`
- `market_context_high->metal_24h` score `-14.8216` n `150` status `ready` deltaP `-26.0278` edge `-0.15` maxDD `-42.5959`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-14T19:22:27.285282+00:00`
- Price records: `672`
- Market context records: `6739`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11724`

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

- `market_context_high->unknown_24h` score `1.3006` n `176` status `ready` deltaP `2.6199` edge `0.5245` maxDD `-12.3511`
- `market_context_high->crypto_major_1h` score `0.0524` n `176` status `ready` deltaP `8.1009` edge `0.0387` maxDD `-4.2122`
- `market_context_high->crypto_alt_1h` score `0.0399` n `176` status `ready` deltaP `6.2466` edge `0.0381` maxDD `-3.7803`
- `market_context_high->commodity_24h` score `-0.2278` n `176` status `ready` deltaP `7.9704` edge `0.1147` maxDD `-5.2791`
- `market_context_high->fx_1h` score `-0.3563` n `176` status `ready` deltaP `0.3334` edge `0.0006` maxDD `-0.5468`
- `market_context_high->index_1h` score `-0.5866` n `176` status `ready` deltaP `-0.7179` edge `0.001` maxDD `-0.7136`
- `market_context_high->commodity_1h` score `-0.604` n `176` status `ready` deltaP `0.1463` edge `-0.0101` maxDD `-2.1314`
- `market_context_high->metal_1h` score `-0.6653` n `176` status `ready` deltaP `-4.6918` edge `-0.0015` maxDD `-1.2017`
- `market_context_high->equity_1h` score `-1.032` n `176` status `ready` deltaP `4.0045` edge `-0.01` maxDD `-3.8827`
- `market_context_high->index_4h` score `-1.1892` n `176` status `ready` deltaP `6.9013` edge `-0.0105` maxDD `-5.7046`
- `market_context_high->fx_4h` score `-1.2169` n `176` status `ready` deltaP `7.5388` edge `0.0001` maxDD `-2.1765`
- `market_context_high->commodity_4h` score `-1.4711` n `176` status `ready` deltaP `-1.7738` edge `-0.0278` maxDD `-5.5853`
- `market_context_high->unknown_1h` score `-1.7944` n `176` status `ready` deltaP `-7.4748` edge `-0.0096` maxDD `-3.2083`
- `market_context_high->crypto_major_4h` score `-2.2025` n `176` status `ready` deltaP `5.4878` edge `0.0125` maxDD `-16.8495`
- `market_context_high->crypto_alt_4h` score `-2.3558` n `176` status `ready` deltaP `3.8941` edge `0.0122` maxDD `-19.2145`
- `market_context_high->metal_4h` score `-2.5948` n `176` status `ready` deltaP `-6.1669` edge `-0.0055` maxDD `-5.2172`
- `market_context_high->unknown_4h` score `-3.8782` n `176` status `ready` deltaP `-17.2395` edge `0.0283` maxDD `-10.2579`
- `market_context_high->equity_4h` score `-3.9236` n `176` status `ready` deltaP `5.2938` edge `-0.1114` maxDD `-27.1529`
- `market_context_high->fx_24h` score `-4.3635` n `176` status `ready` deltaP `-8.7437` edge `-0.0017` maxDD `-5.6237`
- `market_context_high->metal_24h` score `-7.899` n `176` status `ready` deltaP `-10.5114` edge `-0.0941` maxDD `-28.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

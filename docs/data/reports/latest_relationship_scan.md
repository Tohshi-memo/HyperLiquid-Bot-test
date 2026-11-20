# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-20T02:52:26.710853+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `24`

- Symbol pattern count: `2778`

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

- `market_context_high->unknown_1h` score `12007.7144` n `108` status `ready` deltaP `1.1367` edge `1000.6551` maxDD `-0.9181`
- `market_context_high->unknown_4h` score `7455.5373` n `108` status `ready` deltaP `-0.0903` edge `621.3238` maxDD `-0.6072`
- `market_context_high->crypto_major_24h` score `21.6957` n `91` status `ready` deltaP `39.4212` edge `1.6385` maxDD `-5.4667`
- `market_context_high->crypto_alt_24h` score `11.001` n `91` status `ready` deltaP `23.5177` edge `1.4065` maxDD `-8.5654`
- `market_context_high->crypto_major_4h` score `1.346` n `108` status `ready` deltaP `3.7883` edge `0.3688` maxDD `-16.2179`
- `market_context_high->crypto_alt_4h` score `0.8317` n `108` status `ready` deltaP `5.0079` edge `0.2435` maxDD `-12.9396`
- `market_context_high->metal_4h` score `0.7587` n `108` status `ready` deltaP `20.0034` edge `0.0643` maxDD `-6.4211`
- `market_context_high->metal_1h` score `-0.0739` n `108` status `ready` deltaP `5.8383` edge `0.0214` maxDD `-2.6517`
- `market_context_high->crypto_major_1h` score `-0.1705` n `108` status `ready` deltaP `5.1453` edge `0.0835` maxDD `-6.5061`
- `market_context_high->index_1h` score `-0.2257` n `108` status `ready` deltaP `3.8645` edge `0.0065` maxDD `-1.2295`
- `market_context_high->metal_24h` score `-0.4265` n `91` status `ready` deltaP `17.9792` edge `0.2117` maxDD `-19.3683`
- `market_context_high->crypto_alt_1h` score `-0.6225` n `108` status `ready` deltaP `-1.3362` edge `0.0513` maxDD `-5.4428`
- `market_context_high->equity_1h` score `-0.9576` n `108` status `ready` deltaP `7.3908` edge `0.0488` maxDD `-10.8962`
- `market_context_high->fx_1h` score `-1.6337` n `108` status `ready` deltaP `-11.6988` edge `-0.0022` maxDD `-0.4757`
- `market_context_high->index_4h` score `-1.8272` n `108` status `ready` deltaP `-2.2245` edge `-0.0031` maxDD `-4.7471`
- `market_context_high->commodity_1h` score `-2.4187` n `108` status `ready` deltaP `-9.8193` edge `-0.0279` maxDD `-3.9892`
- `market_context_high->fx_4h` score `-2.4198` n `108` status `ready` deltaP `-15.56` edge `-0.0049` maxDD `-1.794`
- `market_context_high->fx_24h` score `-7.1317` n `91` status `ready` deltaP `-23.3249` edge `-0.0115` maxDD `-5.5179`
- `market_context_high->commodity_4h` score `-8.1272` n `108` status `ready` deltaP `-29.2626` edge `-0.1129` maxDD `-15.5426`
- `market_context_high->equity_4h` score `-9.3055` n `108` status `ready` deltaP `-6.8992` edge `-0.0473` maxDD `-44.2396`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

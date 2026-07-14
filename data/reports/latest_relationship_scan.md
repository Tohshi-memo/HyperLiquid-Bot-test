# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-14T13:37:31.177911+00:00`
- Price records: `672`
- Market context records: `6713`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11784`

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

- `market_context_high->unknown_24h` score `1.4765` n `176` status `ready` deltaP `2.7935` edge `0.5459` maxDD `-12.3511`
- `market_context_high->crypto_major_1h` score `0.082` n `176` status `ready` deltaP `8.6997` edge `0.0385` maxDD `-4.2122`
- `market_context_high->crypto_alt_1h` score `0.0123` n `176` status `ready` deltaP `6.0969` edge `0.0368` maxDD `-3.7803`
- `market_context_high->fx_1h` score `-0.3392` n `176` status `ready` deltaP `0.6328` edge `0.0008` maxDD `-0.5468`
- `market_context_high->commodity_24h` score `-0.5014` n `176` status `ready` deltaP `7.9704` edge `0.0919` maxDD `-5.2791`
- `market_context_high->index_1h` score `-0.5469` n `176` status `ready` deltaP `-0.1191` edge `0.0021` maxDD `-0.7136`
- `market_context_high->metal_1h` score `-0.6615` n `176` status `ready` deltaP `-4.5421` edge `-0.002` maxDD `-1.2017`
- `market_context_high->commodity_1h` score `-0.6671` n `176` status `ready` deltaP `-0.7519` edge `-0.0122` maxDD `-2.1314`
- `market_context_high->equity_1h` score `-0.9456` n `176` status `ready` deltaP `4.0045` edge `-0.0028` maxDD `-3.8827`
- `market_context_high->index_4h` score `-1.03` n `176` status `ready` deltaP `8.883` edge `-0.0033` maxDD `-5.7046`
- `market_context_high->unknown_1h` score `-1.1247` n `176` status `ready` deltaP `-8.5227` edge `0.0532` maxDD `-3.2083`
- `market_context_high->fx_4h` score `-1.1972` n `176` status `ready` deltaP `7.8437` edge `0.0006` maxDD `-2.1765`
- `market_context_high->commodity_4h` score `-1.7221` n `176` status `ready` deltaP `-4.3653` edge `-0.0427` maxDD `-5.5853`
- `market_context_high->crypto_major_4h` score `-1.8702` n `176` status `ready` deltaP `6.4024` edge `0.049` maxDD `-16.8495`
- `market_context_high->crypto_alt_4h` score `-2.0344` n `176` status `ready` deltaP `4.8087` edge `0.0473` maxDD `-19.2145`
- `market_context_high->metal_4h` score `-2.4416` n `176` status `ready` deltaP `-4.9474` edge `0.006` maxDD `-5.2172`
- `market_context_high->equity_4h` score `-3.5548` n `176` status `ready` deltaP `6.9706` edge `-0.0753` maxDD `-27.1529`
- `market_context_high->unknown_4h` score `-3.9736` n `176` status `ready` deltaP `-17.6968` edge `0.0234` maxDD `-10.2579`
- `market_context_high->fx_24h` score `-4.2616` n `176` status `ready` deltaP `-7.8756` edge `0.001` maxDD `-5.6237`
- `market_context_high->metal_24h` score `-7.0845` n `176` status `ready` deltaP `-6.5183` edge `-0.0163` maxDD `-28.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

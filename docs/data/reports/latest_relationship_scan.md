# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-28T09:22:25.685796+00:00`
- Price records: `672`
- Market context records: `5025`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10174`

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

- `market_context_high->unknown_1h` score `15.2108` n `93` status `ready` deltaP `3.8182` edge `1.2922` maxDD `-1.674`
- `market_context_high->unknown_4h` score `8.9923` n `93` status `ready` deltaP `21.2972` edge `0.7096` maxDD `-5.5109`
- `market_context_high->crypto_major_4h` score `5.6243` n `93` status `ready` deltaP `17.4043` edge `0.5111` maxDD `-8.3416`
- `market_context_high->crypto_alt_4h` score `5.3783` n `93` status `ready` deltaP `14.7883` edge `0.489` maxDD `-7.8181`
- `market_context_high->metal_4h` score `1.3097` n `93` status `ready` deltaP `14.0014` edge `0.1237` maxDD `-1.9651`
- `market_context_high->equity_1h` score `0.8644` n `93` status `ready` deltaP `8.1868` edge `0.0748` maxDD `-2.5875`
- `market_context_high->crypto_major_1h` score `0.7493` n `93` status `ready` deltaP `5.9542` edge `0.1145` maxDD `-4.6734`
- `market_context_high->equity_4h` score `0.4727` n `93` status `ready` deltaP `3.5783` edge `0.1749` maxDD `-6.3852`
- `market_context_high->metal_1h` score `0.376` n `93` status `ready` deltaP `6.4033` edge `0.0383` maxDD `-1.3057`
- `market_context_high->crypto_alt_1h` score `0.1757` n `93` status `ready` deltaP `5.1107` edge `0.0907` maxDD `-5.5126`
- `market_context_high->fx_24h` score `-0.0639` n `74` status `ready` deltaP `9.2108` edge `0.0066` maxDD `-1.7626`
- `market_context_high->index_4h` score `-0.0839` n `93` status `ready` deltaP `4.324` edge `0.0403` maxDD `-1.0893`
- `market_context_high->commodity_1h` score `-0.3127` n `93` status `ready` deltaP `1.7079` edge `0.0145` maxDD `-1.278`
- `market_context_high->index_1h` score `-0.5599` n `93` status `ready` deltaP `2.2117` edge `0.0127` maxDD `-0.5946`
- `market_context_high->commodity_4h` score `-0.8201` n `93` status `ready` deltaP `3.393` edge `-0.0025` maxDD `-5.021`
- `market_context_high->fx_4h` score `-1.0188` n `93` status `ready` deltaP `-4.3732` edge `-0.0026` maxDD `-1.2426`
- `market_context_high->fx_1h` score `-1.8072` n `93` status `ready` deltaP `-12.5974` edge `-0.0056` maxDD `-0.5482`
- `market_context_high->unknown_24h` score `-1.9915` n `74` status `ready` deltaP `27.21` edge `-0.3131` maxDD `-1.4072`
- `market_context_high->metal_24h` score `-3.8134` n `74` status `ready` deltaP `4.5139` edge `0.0265` maxDD `-32.9721`
- `market_context_high->commodity_24h` score `-4.5171` n `74` status `ready` deltaP `1.9754` edge `-0.0814` maxDD `-27.5371`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

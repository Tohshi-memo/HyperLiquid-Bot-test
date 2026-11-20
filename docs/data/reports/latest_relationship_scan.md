# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-20T13:52:39.960088+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `24`

- Symbol pattern count: `2634`

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

- `market_context_high->unknown_1h` score `10632.9646` n `121` status `ready` deltaP `1.6035` edge `886.0895` maxDD `-0.9181`
- `market_context_high->unknown_4h` score `7034.8107` n `113` status `ready` deltaP `0.8472` edge `586.257` maxDD `-0.6072`
- `market_context_high->crypto_major_24h` score `10.9245` n `104` status `ready` deltaP `29.3937` edge `1.2613` maxDD `-38.4176`
- `market_context_high->crypto_alt_24h` score `5.2226` n `104` status `ready` deltaP `15.8254` edge `1.0618` maxDD `-53.2333`
- `market_context_high->crypto_major_4h` score `1.2093` n `113` status `ready` deltaP `4.5543` edge `0.3523` maxDD `-16.2179`
- `market_context_high->crypto_alt_4h` score `0.7696` n `113` status `ready` deltaP `5.6214` edge `0.2589` maxDD `-14.9128`
- `market_context_high->metal_4h` score `0.2705` n `113` status `ready` deltaP `16.114` edge `0.0554` maxDD `-6.8892`
- `market_context_high->metal_1h` score `-0.1273` n `121` status `ready` deltaP `4.898` edge `0.0175` maxDD `-2.6517`
- `market_context_high->index_1h` score `-0.3164` n `121` status `ready` deltaP `2.6463` edge `0.003` maxDD `-1.2295`
- `market_context_high->crypto_major_1h` score `-1.1632` n `121` status `ready` deltaP `2.5746` edge `0.0425` maxDD `-7.8611`
- `market_context_high->fx_1h` score `-1.2142` n `121` status `ready` deltaP `-6.666` edge `-0.0008` maxDD `-0.4757`
- `market_context_high->equity_1h` score `-1.5358` n `121` status `ready` deltaP `5.4251` edge `0.022` maxDD `-11.559`
- `market_context_high->index_4h` score `-1.8983` n `113` status `ready` deltaP `-2.2798` edge `-0.0082` maxDD `-4.7832`
- `market_context_high->crypto_alt_1h` score `-1.938` n `121` status `ready` deltaP `-3.2105` edge `0.0195` maxDD `-8.4343`
- `market_context_high->commodity_1h` score `-1.9883` n `121` status `ready` deltaP `-5.6119` edge `-0.0151` maxDD `-4.3877`
- `market_context_high->fx_4h` score `-2.1924` n `113` status `ready` deltaP `-11.7432` edge `-0.0012` maxDD `-1.794`
- `market_context_high->metal_24h` score `-5.1096` n `104` status `ready` deltaP `13.9957` edge `0.1095` maxDD `-40.2887`
- `market_context_high->fx_24h` score `-6.5988` n `104` status `ready` deltaP `-17.1741` edge `-0.0081` maxDD `-5.5179`
- `market_context_high->commodity_4h` score `-7.3008` n `113` status `ready` deltaP `-23.5821` edge `-0.0819` maxDD `-15.5426`
- `market_context_high->equity_4h` score `-10.3714` n `113` status `ready` deltaP `-5.8237` edge `-0.0754` maxDD `-49.6711`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

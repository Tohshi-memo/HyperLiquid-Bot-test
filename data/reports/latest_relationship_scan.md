# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-18T08:37:33.468383+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11633`

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

- `market_context_high->crypto_major_24h` score `2.0957` n `80` status `ready` deltaP `5.7647` edge `0.257` maxDD `-4.9964`
- `market_context_high->commodity_24h` score `1.3676` n `80` status `ready` deltaP `15.3228` edge `0.2565` maxDD `-4.666`
- `market_context_high->equity_1h` score `0.9524` n `97` status `ready` deltaP `8.5762` edge `0.0526` maxDD `-0.4329`
- `market_context_high->crypto_major_4h` score `0.7502` n `97` status `ready` deltaP `9.7216` edge `0.0998` maxDD `-3.1677`
- `market_context_high->metal_4h` score `0.6841` n `97` status `ready` deltaP `13.9175` edge `0.0218` maxDD `-1.273`
- `market_context_high->index_1h` score `0.5871` n `97` status `ready` deltaP `12.0532` edge `0.0073` maxDD `-0.0982`
- `market_context_high->unknown_1h` score `0.5136` n `97` status `ready` deltaP `9.3108` edge `0.0034` maxDD `-0.4807`
- `market_context_high->crypto_alt_4h` score `0.4627` n `97` status `ready` deltaP `11.8557` edge `0.112` maxDD `-5.5373`
- `market_context_high->unknown_24h` score `-0.0368` n `80` status `ready` deltaP `13.7327` edge `-0.0758` maxDD `-0.1719`
- `market_context_high->metal_1h` score `-0.0522` n `97` status `ready` deltaP `3.9076` edge `0.0083` maxDD `-0.4291`
- `market_context_high->fx_4h` score `-0.2549` n `97` status `ready` deltaP `2.6575` edge `0.0001` maxDD `-0.3734`
- `market_context_high->crypto_alt_1h` score `-0.2871` n `97` status `ready` deltaP `3.1591` edge `0.0223` maxDD `-2.413`
- `market_context_high->commodity_4h` score `-0.3907` n `97` status `ready` deltaP `3.6522` edge `0.0106` maxDD `-2.4692`
- `market_context_high->equity_4h` score `-0.4012` n `97` status `ready` deltaP `0.6632` edge `0.0526` maxDD `-2.5696`
- `market_context_high->crypto_major_1h` score `-0.4499` n `97` status `ready` deltaP `1.6791` edge `0.0156` maxDD `-2.7581`
- `market_context_high->fx_1h` score `-0.4611` n `97` status `ready` deltaP `-3.5913` edge `0.001` maxDD `-0.2273`
- `market_context_high->index_4h` score `-0.7073` n `97` status `ready` deltaP `-0.187` edge `0.0078` maxDD `-0.5728`
- `market_context_high->commodity_1h` score `-0.9019` n `97` status `ready` deltaP `-7.1332` edge `-0.0068` maxDD `-1.5684`
- `market_context_high->metal_24h` score `-1.4838` n `80` status `ready` deltaP `-4.6079` edge `0.029` maxDD `-5.7476`
- `market_context_high->index_24h` score `-3.7266` n `80` status `ready` deltaP `-12.3332` edge `-0.1614` maxDD `-9.3981`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

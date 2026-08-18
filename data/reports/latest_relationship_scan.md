# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-18T08:22:30.841769+00:00`
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

- `market_context_high->crypto_major_24h` score `2.0651` n `79` status `ready` deltaP `5.3375` edge `0.2573` maxDD `-4.9964`
- `market_context_high->commodity_24h` score `1.3269` n `79` status `ready` deltaP `15.0056` edge `0.2534` maxDD `-4.666`
- `market_context_high->equity_1h` score `0.9488` n `97` status `ready` deltaP `8.5762` edge `0.0523` maxDD `-0.4329`
- `market_context_high->crypto_major_4h` score `0.743` n `97` status `ready` deltaP `9.7216` edge `0.0992` maxDD `-3.1677`
- `market_context_high->metal_4h` score `0.6683` n `97` status `ready` deltaP `13.7651` edge `0.0215` maxDD `-1.273`
- `market_context_high->index_1h` score `0.5871` n `97` status `ready` deltaP `12.0532` edge `0.0073` maxDD `-0.0982`
- `market_context_high->unknown_1h` score `0.5136` n `97` status `ready` deltaP `9.3108` edge `0.0034` maxDD `-0.4807`
- `market_context_high->crypto_alt_4h` score `0.4658` n `97` status `ready` deltaP `11.8557` edge `0.1124` maxDD `-5.5373`
- `market_context_high->unknown_24h` score `-0.0286` n `79` status `ready` deltaP `13.7003` edge `-0.0749` maxDD `-0.1719`
- `market_context_high->metal_1h` score `-0.0665` n `97` status `ready` deltaP `3.7579` edge `0.0081` maxDD `-0.4291`
- `market_context_high->fx_4h` score `-0.2542` n `97` status `ready` deltaP `2.6575` edge `0.0002` maxDD `-0.3734`
- `market_context_high->crypto_alt_1h` score `-0.2863` n `97` status `ready` deltaP `3.1591` edge `0.0224` maxDD `-2.413`
- `market_context_high->commodity_4h` score `-0.3868` n `97` status `ready` deltaP `3.6522` edge `0.0111` maxDD `-2.4692`
- `market_context_high->equity_4h` score `-0.4362` n `97` status `ready` deltaP `0.5107` edge `0.0507` maxDD `-2.5696`
- `market_context_high->crypto_major_1h` score `-0.46` n `97` status `ready` deltaP `1.5294` edge `0.0153` maxDD `-2.7581`
- `market_context_high->fx_1h` score `-0.4619` n `97` status `ready` deltaP `-3.5913` edge `0.0009` maxDD `-0.2273`
- `market_context_high->index_4h` score `-0.7243` n `97` status `ready` deltaP `-0.3394` edge `0.0074` maxDD `-0.5728`
- `market_context_high->commodity_1h` score `-0.9104` n `97` status `ready` deltaP `-7.2829` edge `-0.0069` maxDD `-1.5684`
- `market_context_high->metal_24h` score `-1.3736` n `79` status `ready` deltaP `-4.0059` edge `0.0317` maxDD `-5.4879`
- `market_context_high->index_24h` score `-3.5784` n `79` status `ready` deltaP `-11.6995` edge `-0.157` maxDD `-8.9022`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

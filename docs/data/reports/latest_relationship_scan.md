# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-08T01:37:27.900984+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4422`

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

- `market_context_high->unknown_4h` score `120.8761` n `37` status `ready` deltaP `-7.4448` edge `10.1674` maxDD `-0.9139`
- `market_context_high->fx_4h` score `3.4544` n `37` status `ready` deltaP `37.5824` edge `0.0463` maxDD `-0.0521`
- `market_context_high->equity_1h` score `3.2065` n `37` status `ready` deltaP `9.9086` edge `0.2471` maxDD `-2.3425`
- `market_context_high->index_4h` score `1.8343` n `37` status `ready` deltaP `24.2213` edge `0.0384` maxDD `-2.4279`
- `news_risk_high->fx_24h` score `1.7456` n `52` status `ready` deltaP `10.6303` edge `0.0967` maxDD `-0.1014`
- `news_risk_high->equity_4h` score `0.8698` n `52` status `ready` deltaP `7.1412` edge `0.1378` maxDD `-4.2454`
- `market_context_high->crypto_major_1h` score `0.7843` n `37` status `ready` deltaP `9.7508` edge `0.0589` maxDD `-3.0172`
- `market_context_high->fx_1h` score `0.52` n `37` status `ready` deltaP `8.27` edge `0.0153` maxDD `-0.1681`
- `market_context_high->crypto_alt_1h` score `0.4483` n `37` status `ready` deltaP `10.9484` edge `0.066` maxDD `-3.1881`
- `news_risk_high->index_4h` score `0.2298` n `52` status `ready` deltaP `8.5248` edge `0.0204` maxDD `-0.4888`
- `market_context_high->index_1h` score `0.2099` n `37` status `ready` deltaP `0.9023` edge `0.0385` maxDD `-0.1621`
- `news_risk_high->index_24h` score `0.2071` n `52` status `ready` deltaP `6.851` edge `0.1477` maxDD `-6.6786`
- `news_risk_high->fx_4h` score `0.1532` n `52` status `ready` deltaP `8.3724` edge `0.0077` maxDD `-0.1771`
- `market_context_high->commodity_1h` score `0.1358` n `37` status `ready` deltaP `9.3179` edge `0.0099` maxDD `-1.7019`
- `market_context_high->commodity_4h` score `0.0343` n `37` status `ready` deltaP `3.9017` edge `0.0238` maxDD `-1.633`
- `market_context_high->metal_1h` score `-0.0342` n `37` status `ready` deltaP `1.8005` edge `0.0164` maxDD `-0.6226`
- `news_risk_high->index_1h` score `-0.0551` n `52` status `ready` deltaP `5.3201` edge `0.0028` maxDD `-0.2931`
- `news_risk_high->equity_1h` score `-0.2745` n `52` status `ready` deltaP `-3.3971` edge `0.0424` maxDD `-1.396`
- `news_risk_high->fx_1h` score `-0.2795` n `52` status `ready` deltaP `-0.046` edge `0.003` maxDD `-0.0826`
- `market_context_high->equity_4h` score `-0.7535` n `37` status `ready` deltaP `21.6423` edge `0.0871` maxDD `-24.9053`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

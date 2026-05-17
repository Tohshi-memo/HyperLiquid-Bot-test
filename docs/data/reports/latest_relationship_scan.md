# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-17T10:52:14.152232+00:00`
- Price records: `672`
- Market context records: `1005`
- Flow alert records: `4800`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8634`

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

- `market_context_high->crypto_major_24h` score `13.0307` n `207` status `ready` deltaP `31.9568` edge `0.9317` maxDD `-3.3749`
- `market_context_high->crypto_alt_24h` score `4.1698` n `207` status `ready` deltaP `10.9324` edge `0.398` maxDD `-9.5387`
- `market_context_high->fx_1h` score `-0.5108` n `207` status `ready` deltaP `2.2961` edge `0.0002` maxDD `-0.3124`
- `market_context_high->index_24h` score `-0.5121` n `207` status `ready` deltaP `3.8647` edge `0.1274` maxDD `-5.6669`
- `market_context_high->commodity_1h` score `-0.5958` n `207` status `ready` deltaP `2.1197` edge `0.017` maxDD `-3.7959`
- `market_context_high->index_1h` score `-0.6814` n `207` status `ready` deltaP `3.4452` edge `0.0056` maxDD `-2.8282`
- `market_context_high->equity_1h` score `-0.6908` n `207` status `ready` deltaP `0.465` edge `0.0162` maxDD `-4.4826`
- `market_context_high->fx_4h` score `-0.7248` n `207` status `ready` deltaP `0.8272` edge `0.0012` maxDD `-1.6381`
- `market_context_high->equity_24h` score `-1.1157` n `207` status `ready` deltaP `4.5` edge `0.1375` maxDD `-10.5047`
- `market_context_high->crypto_major_1h` score `-1.2216` n `207` status `ready` deltaP `4.977` edge `-0.0175` maxDD `-11.4508`
- `market_context_high->crypto_alt_1h` score `-1.3782` n `207` status `ready` deltaP `-1.2627` edge `-0.0243` maxDD `-8.1842`
- `market_context_high->equity_4h` score `-1.5073` n `207` status `ready` deltaP `1.6941` edge `0.0783` maxDD `-10.5498`
- `market_context_high->index_4h` score `-1.7723` n `207` status `ready` deltaP `-1.8927` edge `0.0172` maxDD `-6.5149`
- `market_context_high->metal_1h` score `-1.8639` n `207` status `ready` deltaP `-0.6501` edge `-0.0387` maxDD `-9.0076`
- `market_context_high->crypto_major_4h` score `-2.8809` n `207` status `ready` deltaP `7.114` edge `0.0831` maxDD `-22.648`
- `market_context_high->commodity_4h` score `-3.1704` n `207` status `ready` deltaP `-1.4757` edge `0.0624` maxDD `-13.0076`
- `market_context_high->crypto_alt_4h` score `-3.2795` n `207` status `ready` deltaP `-1.9324` edge `0.0174` maxDD `-15.2248`
- `market_context_high->fx_24h` score `-3.4884` n `207` status `ready` deltaP `-1.4294` edge `-0.0223` maxDD `-19.8983`
- `market_context_high->metal_4h` score `-4.6245` n `207` status `ready` deltaP `-4.8243` edge `-0.1656` maxDD `-24.9433`
- `market_context_high->commodity_24h` score `-8.2536` n `207` status `ready` deltaP `2.4949` edge `0.39` maxDD `-102.8492`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

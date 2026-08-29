# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-29T04:07:25.584092+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11666`

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

- `news_risk_high->unknown_24h` score `57.583` n `50` status `ready` deltaP `20.2773` edge `4.6634` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `34.2995` n `50` status `ready` deltaP `46.6066` edge `2.5917` maxDD `-2.8629`
- `news_risk_high->crypto_major_24h` score `10.0953` n `50` status `ready` deltaP `28.0208` edge `0.7038` maxDD `-2.6128`
- `news_risk_high->unknown_4h` score `8.0282` n `74` status `ready` deltaP `15.3799` edge `0.5975` maxDD `-1.4812`
- `news_risk_high->equity_24h` score `7.2547` n `50` status `ready` deltaP `30.1005` edge `0.4967` maxDD `-4.7584`
- `market_context_high->unknown_24h` score `6.8917` n `120` status `ready` deltaP `13.6106` edge `0.5568` maxDD `-3.1917`
- `news_risk_high->metal_24h` score `4.5258` n `50` status `ready` deltaP `43.4073` edge `0.092` maxDD `-0.0053`
- `market_context_high->metal_24h` score `3.343` n `120` status `ready` deltaP `28.7406` edge `0.1889` maxDD `-3.1535`
- `news_risk_high->index_24h` score `2.4886` n `50` status `ready` deltaP `26.9948` edge `0.0425` maxDD `-0.2064`
- `news_risk_high->unknown_1h` score `2.3999` n `79` status `ready` deltaP `4.6635` edge `0.2046` maxDD `-0.8558`
- `market_context_high->unknown_4h` score `2.3784` n `120` status `ready` deltaP `18.4655` edge `0.1158` maxDD `-0.5894`
- `news_risk_high->fx_4h` score `1.4713` n `74` status `ready` deltaP `33.1452` edge `0.0226` maxDD `-0.3953`
- `market_context_high->unknown_1h` score `0.9371` n `120` status `ready` deltaP `9.2416` edge `0.0615` maxDD `-1.6015`
- `news_risk_high->fx_1h` score `0.6` n `79` status `ready` deltaP `12.4877` edge `0.0056` maxDD `-0.108`
- `news_risk_high->commodity_1h` score `0.4223` n `79` status `ready` deltaP `12.175` edge `0.005` maxDD `-0.5618`
- `market_context_high->metal_4h` score `-0.1067` n `120` status `ready` deltaP `10.1016` edge `0.0107` maxDD `-3.3377`
- `market_context_high->fx_1h` score `-0.332` n `120` status `ready` deltaP `4.6607` edge `-0.0004` maxDD `-0.8587`
- `news_risk_high->index_1h` score `-0.388` n `79` status `ready` deltaP `0.3203` edge `-0.0082` maxDD `-0.8275`
- `market_context_high->crypto_major_4h` score `-0.4507` n `120` status `ready` deltaP `13.6382` edge `0.2166` maxDD `-20.9394`
- `news_risk_high->equity_1h` score `-0.5662` n `79` status `ready` deltaP `8.7319` edge `-0.0374` maxDD `-5.1385`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

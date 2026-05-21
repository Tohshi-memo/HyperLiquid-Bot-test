# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-21T20:22:23.499238+00:00`
- Price records: `672`
- Market context records: `1457`
- Flow alert records: `6106`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8809`

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

- `market_context_high->crypto_alt_24h` score `13.0255` n `163` status `ready` deltaP `28.8887` edge `1.0945` maxDD `-15.1306`
- `market_context_high->crypto_major_24h` score `12.0348` n `163` status `ready` deltaP `27.569` edge `0.9323` maxDD `-8.0553`
- `market_context_high->metal_24h` score `11.5146` n `163` status `ready` deltaP `15.0094` edge `1.0262` maxDD `-6.3373`
- `market_context_high->index_24h` score `4.2758` n `163` status `ready` deltaP `19.8832` edge `0.3324` maxDD `-5.3574`
- `market_context_high->equity_24h` score `4.1838` n `163` status `ready` deltaP `13.1007` edge `0.494` maxDD `-14.2815`
- `market_context_high->equity_4h` score `1.548` n `222` status `ready` deltaP `7.1687` edge `0.1642` maxDD `-3.6396`
- `market_context_high->fx_24h` score `0.246` n `163` status `ready` deltaP `11.6404` edge `0.0478` maxDD `-1.3925`
- `market_context_high->index_1h` score `-0.0652` n `225` status `ready` deltaP `3.9561` edge `0.0147` maxDD `-1.7205`
- `market_context_high->equity_1h` score `-0.1054` n `225` status `ready` deltaP `2.1503` edge `0.0369` maxDD `-2.8014`
- `market_context_high->crypto_alt_4h` score `-0.3052` n `222` status `ready` deltaP `11.4631` edge `0.2301` maxDD `-19.5565`
- `market_context_high->index_4h` score `-0.4502` n `222` status `ready` deltaP `1.0767` edge `0.0642` maxDD `-3.7119`
- `market_context_high->fx_1h` score `-0.472` n `225` status `ready` deltaP `0.7977` edge `-0.0026` maxDD `-0.3914`
- `market_context_high->crypto_alt_1h` score `-0.5214` n `225` status `ready` deltaP `2.2528` edge `0.0439` maxDD `-4.1892`
- `market_context_high->fx_4h` score `-1.0312` n `222` status `ready` deltaP `-3.9222` edge `-0.009` maxDD `-1.4313`
- `market_context_high->metal_1h` score `-1.107` n `225` status `ready` deltaP `5.2096` edge `0.0066` maxDD `-6.3532`
- `market_context_high->crypto_major_4h` score `-1.1296` n `222` status `ready` deltaP `5.3024` edge `0.1414` maxDD `-13.3376`
- `market_context_high->commodity_1h` score `-1.264` n `225` status `ready` deltaP `-1.7099` edge `-0.0018` maxDD `-4.7041`
- `market_context_high->crypto_major_1h` score `-1.5925` n `225` status `ready` deltaP `-0.7086` edge `0.0077` maxDD `-6.1883`
- `market_context_high->metal_4h` score `-1.772` n `222` status `ready` deltaP `8.0875` edge `0.0676` maxDD `-12.5349`
- `market_context_high->commodity_4h` score `-3.9105` n `222` status `ready` deltaP `-11.7049` edge `-0.068` maxDD `-16.0917`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

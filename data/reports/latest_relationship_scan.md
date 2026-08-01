# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-01T13:22:27.315372+00:00`
- Price records: `672`
- Market context records: `8625`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5898`

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

- `news_risk_high->unknown_24h` score `5191.7922` n `60` status `ready` deltaP `34.2345` edge `432.4632` maxDD `-2.0332`
- `market_context_high->crypto_alt_24h` score `17.4848` n `47` status `ready` deltaP `53.5345` edge `1.1399` maxDD `-2.1786`
- `news_risk_high->equity_4h` score `6.2129` n `60` status `ready` deltaP `21.3211` edge `0.4353` maxDD `-3.4427`
- `news_risk_high->index_4h` score `2.4876` n `60` status `ready` deltaP `21.4735` edge `0.0832` maxDD `-0.191`
- `news_risk_high->equity_1h` score `1.6856` n `60` status `ready` deltaP `14.9302` edge `0.0886` maxDD `-2.4803`
- `news_risk_high->crypto_major_4h` score `1.164` n `60` status `ready` deltaP `7.439` edge `0.1772` maxDD `-3.5385`
- `market_context_high->crypto_alt_4h` score `0.984` n `59` status `ready` deltaP `12.084` edge `0.1413` maxDD `-5.323`
- `news_risk_high->crypto_alt_1h` score `0.442` n `60` status `ready` deltaP `8.3333` edge `0.0538` maxDD `-1.8813`
- `news_risk_high->crypto_alt_4h` score `0.4259` n `60` status `ready` deltaP `11.0671` edge `0.12` maxDD `-5.8012`
- `news_risk_high->crypto_major_1h` score `0.3388` n `60` status `ready` deltaP `6.3673` edge `0.0522` maxDD `-2.0972`
- `news_risk_high->fx_4h` score `0.3132` n `60` status `ready` deltaP `14.6037` edge `0.0245` maxDD `-0.6604`
- `market_context_high->fx_24h` score `0.2913` n `47` status `ready` deltaP `13.2343` edge `0.0429` maxDD `-2.1692`
- `news_risk_high->metal_4h` score `0.1202` n `60` status `ready` deltaP `4.2174` edge `0.0349` maxDD `-0.8085`
- `news_risk_high->fx_1h` score `0.111` n `60` status `ready` deltaP `5.5988` edge `0.005` maxDD `-0.2475`
- `market_context_high->fx_4h` score `0.0524` n `59` status `ready` deltaP `10.4512` edge `0.0143` maxDD `-1.3685`
- `news_risk_high->metal_1h` score `0.044` n `60` status `ready` deltaP `5.3393` edge `0.0084` maxDD `-0.5599`
- `news_risk_high->index_1h` score `0.0009` n `60` status `ready` deltaP `3.3733` edge `0.0093` maxDD `-0.5338`
- `market_context_high->commodity_1h` score `-0.2244` n `59` status `ready` deltaP `4.3388` edge `-0.0003` maxDD `-1.5912`
- `market_context_high->fx_1h` score `-0.2248` n `59` status `ready` deltaP `3.1412` edge `0.0005` maxDD `-0.6874`
- `market_context_high->commodity_24h` score `-0.3013` n `47` status `ready` deltaP `16.8922` edge `0.1056` maxDD `-13.8809`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

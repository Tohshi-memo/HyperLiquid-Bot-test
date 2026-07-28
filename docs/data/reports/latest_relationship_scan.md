# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-28T08:52:26.700606+00:00`
- Price records: `672`
- Market context records: `8180`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5904`

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

- `news_risk_high->unknown_24h` score `8684.6931` n `42` status `ready` deltaP `36.9792` edge `723.4779` maxDD `0.0`
- `market_context_high->equity_24h` score `19.2477` n `51` status `ready` deltaP `43.5151` edge `1.4049` maxDD `-4.9489`
- `market_context_high->equity_4h` score `9.5254` n `52` status `ready` deltaP `37.7931` edge `0.5653` maxDD `-0.5442`
- `market_context_high->metal_24h` score `8.4102` n `51` status `ready` deltaP `43.4028` edge `0.4115` maxDD `0.0`
- `news_risk_high->equity_4h` score `8.2108` n `47` status `ready` deltaP `30.3872` edge `0.511` maxDD `-1.3479`
- `market_context_high->index_4h` score `4.0808` n `52` status `ready` deltaP `36.6675` edge `0.0999` maxDD `-0.0092`
- `news_risk_high->equity_1h` score `3.4299` n `50` status `ready` deltaP `25.6048` edge `0.146` maxDD `-1.1366`
- `news_risk_high->crypto_major_4h` score `3.275` n `47` status `ready` deltaP `17.7932` edge `0.3628` maxDD `-2.2569`
- `market_context_high->equity_1h` score `3.0794` n `52` status `ready` deltaP `16.8356` edge `0.1647` maxDD `-0.6254`
- `market_context_high->crypto_alt_24h` score `3.0082` n `51` status `ready` deltaP `7.1998` edge `0.659` maxDD `-16.0402`
- `news_risk_high->index_4h` score `2.7544` n `47` status `ready` deltaP `23.0832` edge `0.0947` maxDD `-0.191`
- `market_context_high->metal_4h` score `2.425` n `52` status `ready` deltaP `25.7974` edge `0.067` maxDD `-0.6188`
- `market_context_high->index_24h` score `1.9165` n `51` status `ready` deltaP `16.4829` edge `0.2026` maxDD `-1.342`
- `news_risk_high->crypto_major_1h` score `1.8942` n `50` status `ready` deltaP `12.0419` edge `0.1173` maxDD `-1.1783`
- `market_context_high->index_1h` score `1.8838` n `52` status `ready` deltaP `21.7526` edge `0.0258` maxDD `-0.1069`
- `news_risk_high->metal_4h` score `1.6314` n `47` status `ready` deltaP `15.0363` edge `0.0825` maxDD `-0.7433`
- `news_risk_high->crypto_alt_1h` score `1.6101` n `50` status `ready` deltaP `12.0419` edge `0.0973` maxDD `-1.1388`
- `news_risk_high->crypto_alt_4h` score `1.3915` n `47` status `ready` deltaP `16.1228` edge `0.2101` maxDD `-5.8012`
- `market_context_high->fx_24h` score `1.0004` n `51` status `ready` deltaP `20.5474` edge `0.0569` maxDD `-0.5835`
- `market_context_high->crypto_alt_4h` score `0.6358` n `52` status `ready` deltaP `2.4976` edge `0.1652` maxDD `-3.0268`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

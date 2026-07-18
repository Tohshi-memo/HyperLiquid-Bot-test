# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-18T15:52:30.139285+00:00`
- Price records: `672`
- Market context records: `7155`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11762`

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

- `market_context_high->fx_4h` score `0.2791` n `155` status `ready` deltaP `12.0388` edge `0.013` maxDD `-0.9333`
- `market_context_high->fx_1h` score `-0.2199` n `163` status `ready` deltaP `3.6736` edge `0.0023` maxDD `-0.276`
- `market_context_high->unknown_1h` score `-0.5245` n `163` status `ready` deltaP `-1.4722` edge `0.0303` maxDD `-1.4688`
- `market_context_high->crypto_alt_1h` score `-0.6133` n `163` status `ready` deltaP `-0.1864` edge `0.0265` maxDD `-5.9775`
- `market_context_high->crypto_major_1h` score `-0.6384` n `163` status `ready` deltaP `3.5092` edge `0.0358` maxDD `-7.6171`
- `market_context_high->commodity_1h` score `-0.678` n `163` status `ready` deltaP `-1.2812` edge `-0.0163` maxDD `-1.9668`
- `market_context_high->index_1h` score `-0.688` n `163` status `ready` deltaP `2.015` edge `-0.0043` maxDD `-2.3175`
- `market_context_high->metal_1h` score `-1.6625` n `163` status `ready` deltaP `-6.7384` edge `-0.005` maxDD `-2.0897`
- `market_context_high->unknown_4h` score `-1.9414` n `155` status `ready` deltaP `-6.2628` edge `0.0135` maxDD `-5.9846`
- `market_context_high->commodity_4h` score `-2.0808` n `155` status `ready` deltaP `-4.765` edge `-0.0381` maxDD `-2.9494`
- `market_context_high->metal_4h` score `-2.9434` n `155` status `ready` deltaP `-10.5449` edge `-0.0122` maxDD `-5.2551`
- `market_context_high->equity_1h` score `-3.5298` n `163` status `ready` deltaP `-0.6181` edge `-0.0406` maxDD `-15.2875`
- `market_context_high->index_4h` score `-3.9389` n `155` status `ready` deltaP `-2.2256` edge `-0.0435` maxDD `-12.2591`
- `market_context_high->commodity_24h` score `-4.5036` n `133` status `ready` deltaP `-13.4581` edge `-0.1547` maxDD `-4.4704`
- `market_context_high->crypto_major_4h` score `-4.9077` n `155` status `ready` deltaP `2.6199` edge `0.0089` maxDD `-25.1605`
- `market_context_high->fx_24h` score `-4.9295` n `133` status `ready` deltaP `-15.3574` edge `-0.0257` maxDD `-3.9503`
- `market_context_high->crypto_alt_4h` score `-5.5484` n `155` status `ready` deltaP `-3.5867` edge `-0.0315` maxDD `-24.5561`
- `market_context_high->unknown_24h` score `-10.0992` n `133` status `ready` deltaP `-32.7029` edge `-0.1089` maxDD `-23.5076`
- `market_context_high->equity_4h` score `-14.7351` n `155` status `ready` deltaP `-4.4551` edge `-0.2197` maxDD `-66.2822`
- `market_context_high->metal_24h` score `-14.7363` n `133` status `ready` deltaP `-31.9496` edge `-0.1969` maxDD `-40.7836`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

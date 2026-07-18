# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-18T14:37:26.401324+00:00`
- Price records: `672`
- Market context records: `7149`
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

- `market_context_high->fx_4h` score `0.4343` n `150` status `ready` deltaP `13.8882` edge `0.0136` maxDD `-0.9333`
- `market_context_high->fx_1h` score `-0.1472` n `159` status `ready` deltaP `4.5372` edge `0.0026` maxDD `-0.276`
- `market_context_high->unknown_1h` score `-0.481` n `159` status `ready` deltaP `-1.4236` edge `0.0336` maxDD `-1.4688`
- `market_context_high->crypto_alt_1h` score `-0.6286` n `159` status `ready` deltaP `-0.225` edge `0.0248` maxDD `-5.9775`
- `market_context_high->crypto_major_1h` score `-0.6411` n `159` status `ready` deltaP `3.5787` edge `0.035` maxDD `-7.6171`
- `market_context_high->commodity_1h` score `-0.7282` n `159` status `ready` deltaP `-2.1702` edge `-0.0168` maxDD `-1.9668`
- `market_context_high->index_1h` score `-0.7751` n `159` status `ready` deltaP `1.0017` edge `-0.0048` maxDD `-2.3175`
- `market_context_high->metal_1h` score `-1.448` n `159` status `ready` deltaP `-5.9466` edge `-0.0049` maxDD `-2.0897`
- `market_context_high->unknown_4h` score `-1.741` n `150` status `ready` deltaP `-6.0143` edge `0.0145` maxDD `-5.8085`
- `market_context_high->commodity_4h` score `-2.0271` n `150` status `ready` deltaP `-4.2134` edge `-0.0373` maxDD `-2.9494`
- `market_context_high->metal_4h` score `-2.8985` n `150` status `ready` deltaP `-9.7277` edge `-0.0119` maxDD `-5.2551`
- `market_context_high->equity_1h` score `-3.5672` n `159` status `ready` deltaP `-0.7956` edge `-0.0427` maxDD `-15.2742`
- `market_context_high->index_4h` score `-3.916` n `150` status `ready` deltaP `-1.6545` edge `-0.0454` maxDD `-12.2591`
- `market_context_high->commodity_24h` score `-4.4988` n `133` status `ready` deltaP `-13.4581` edge `-0.1543` maxDD `-4.4704`
- `market_context_high->fx_24h` score `-4.9899` n `133` status `ready` deltaP `-16.0518` edge `-0.0261` maxDD `-3.9503`
- `market_context_high->crypto_major_4h` score `-5.1322` n `150` status `ready` deltaP `0.878` edge `0.0018` maxDD `-25.1605`
- `market_context_high->crypto_alt_4h` score `-5.7002` n `150` status `ready` deltaP `-4.6443` edge `-0.0375` maxDD `-24.5243`
- `market_context_high->unknown_24h` score `-10.0992` n `133` status `ready` deltaP `-32.7029` edge `-0.1089` maxDD `-23.5076`
- `market_context_high->equity_4h` score `-14.5191` n `150` status `ready` deltaP `-4.0345` edge `-0.2321` maxDD `-65.7408`
- `market_context_high->metal_24h` score `-14.6616` n `133` status `ready` deltaP `-31.2552` edge `-0.1953` maxDD `-40.7836`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

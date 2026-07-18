# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-18T14:22:30.988413+00:00`
- Price records: `672`
- Market context records: `7148`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11740`

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

- `market_context_high->fx_4h` score `0.4662` n `149` status `ready` deltaP `14.273` edge `0.0137` maxDD `-0.9333`
- `market_context_high->fx_1h` score `-0.1352` n `159` status `ready` deltaP `4.6869` edge `0.0026` maxDD `-0.276`
- `market_context_high->unknown_1h` score `-0.4822` n `159` status `ready` deltaP `-1.4236` edge `0.0335` maxDD `-1.4688`
- `market_context_high->crypto_alt_1h` score `-0.6293` n `159` status `ready` deltaP `-0.225` edge `0.0247` maxDD `-5.9775`
- `market_context_high->crypto_major_1h` score `-0.6434` n `159` status `ready` deltaP `3.5787` edge `0.0347` maxDD `-7.6171`
- `market_context_high->commodity_1h` score `-0.7282` n `159` status `ready` deltaP `-2.1702` edge `-0.0168` maxDD `-1.9668`
- `market_context_high->index_1h` score `-0.7871` n `159` status `ready` deltaP `0.852` edge `-0.0048` maxDD `-2.3175`
- `market_context_high->metal_1h` score `-1.448` n `159` status `ready` deltaP `-5.9466` edge `-0.0049` maxDD `-2.0897`
- `market_context_high->unknown_4h` score `-1.7032` n `149` status `ready` deltaP `-5.9564` edge `0.0145` maxDD `-5.7849`
- `market_context_high->commodity_4h` score `-1.9922` n `149` status `ready` deltaP `-3.8376` edge `-0.0369` maxDD `-2.9494`
- `market_context_high->metal_4h` score `-2.8881` n `149` status `ready` deltaP `-9.5576` edge `-0.0117` maxDD `-5.2551`
- `market_context_high->equity_1h` score `-3.5672` n `159` status `ready` deltaP `-0.7956` edge `-0.0427` maxDD `-15.2742`
- `market_context_high->index_4h` score `-3.9108` n `149` status `ready` deltaP `-1.5295` edge `-0.0458` maxDD `-12.2591`
- `market_context_high->commodity_24h` score `-4.4988` n `133` status `ready` deltaP `-13.4581` edge `-0.1543` maxDD `-4.4704`
- `market_context_high->fx_24h` score `-4.9887` n `133` status `ready` deltaP `-16.0518` edge `-0.026` maxDD `-3.9503`
- `market_context_high->crypto_major_4h` score `-5.1864` n `149` status `ready` deltaP `0.5156` edge `-0.0003` maxDD `-25.1605`
- `market_context_high->crypto_alt_4h` score `-5.6948` n `149` status `ready` deltaP `-4.5506` edge `-0.0385` maxDD `-24.4582`
- `market_context_high->unknown_24h` score `-10.1016` n `133` status `ready` deltaP `-32.7029` edge `-0.1091` maxDD `-23.5076`
- `market_context_high->equity_4h` score `-14.4781` n `149` status `ready` deltaP `-3.9409` edge `-0.2346` maxDD `-65.6507`
- `market_context_high->metal_24h` score `-14.6405` n `133` status `ready` deltaP `-31.0816` edge `-0.1947` maxDD `-40.7836`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

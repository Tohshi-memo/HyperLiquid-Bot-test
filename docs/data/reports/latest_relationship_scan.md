# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-08T13:52:27.276242+00:00`
- Price records: `672`
- Market context records: `6093`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11095`

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

- `news_risk_high->fx_24h` score `8.163` n `30` status `ready` deltaP `72.7431` edge `0.1953` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `6.7747` n `30` status `ready` deltaP `33.0902` edge `0.3587` maxDD `-0.5131`
- `news_risk_high->fx_4h` score `4.2737` n `32` status `ready` deltaP `44.436` edge `0.0645` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.4063` n `32` status `ready` deltaP `28.8922` edge `0.0218` maxDD `-0.1113`
- `market_context_high->equity_4h` score `1.7256` n `195` status `ready` deltaP `9.5427` edge `0.1719` maxDD `-2.671`
- `news_risk_high->crypto_major_1h` score `1.2417` n `32` status `ready` deltaP `13.6789` edge `0.1147` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.6969` n `32` status `ready` deltaP `9.375` edge `0.073` maxDD `-1.6923`
- `news_risk_high->commodity_24h` score `0.2548` n `30` status `ready` deltaP `17.3959` edge `-0.0742` maxDD `-0.3101`
- `news_risk_high->index_24h` score `0.1218` n `30` status `ready` deltaP `9.2361` edge `0.0412` maxDD `-2.3058`
- `market_context_high->fx_1h` score `-0.2661` n `195` status `ready` deltaP `1.5845` edge `-0.0001` maxDD `-0.5659`
- `market_context_high->metal_4h` score `-0.5613` n `195` status `ready` deltaP `4.1518` edge `0.0191` maxDD `-3.4996`
- `market_context_high->equity_1h` score `-0.5695` n `195` status `ready` deltaP `1.8363` edge `0.0263` maxDD `-4.2573`
- `market_context_high->index_4h` score `-0.6756` n `195` status `ready` deltaP `4.4426` edge `0.0302` maxDD `-1.381`
- `market_context_high->commodity_1h` score `-0.6876` n `195` status `ready` deltaP `-1.3903` edge `-0.0034` maxDD `-0.5708`
- `news_risk_high->metal_1h` score `-0.692` n `32` status `ready` deltaP `-1.7964` edge `-0.027` maxDD `-1.6464`
- `market_context_high->metal_1h` score `-0.699` n `195` status `ready` deltaP `3.5882` edge `-0.0023` maxDD `-2.0564`
- `market_context_high->crypto_alt_1h` score `-0.879` n `195` status `ready` deltaP `4.359` edge `0.0335` maxDD `-9.3536`
- `market_context_high->crypto_major_1h` score `-0.9562` n `195` status `ready` deltaP `4.4642` edge `0.0244` maxDD `-9.807`
- `news_risk_high->index_1h` score `-1.0478` n `32` status `ready` deltaP `-8.9259` edge `-0.0185` maxDD `-1.1725`
- `market_context_high->index_1h` score `-1.1389` n `195` status `ready` deltaP `-1.8586` edge `0.0044` maxDD `-0.9531`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-02T09:22:28.650182+00:00`
- Price records: `672`
- Market context records: `2649`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9223`

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

- `market_context_high->unknown_24h` score `7.6902` n `128` status `ready` deltaP `17.6215` edge `0.5562` maxDD `-1.626`
- `market_context_high->crypto_alt_24h` score `6.0833` n `128` status `ready` deltaP `9.1146` edge `0.8277` maxDD `-22.5216`
- `market_context_high->crypto_alt_4h` score `5.6994` n `128` status `ready` deltaP `26.2576` edge `0.5678` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `4.3021` n `128` status `ready` deltaP `16.997` edge `0.4262` maxDD `-10.1468`
- `market_context_high->unknown_4h` score `1.4062` n `128` status `ready` deltaP `8.003` edge `0.1688` maxDD `-3.7312`
- `market_context_high->crypto_alt_1h` score `1.1622` n `133` status `ready` deltaP `10.3035` edge `0.1469` maxDD `-6.1656`
- `market_context_high->index_24h` score `0.9542` n `128` status `ready` deltaP `11.0243` edge `0.1041` maxDD `-2.5127`
- `market_context_high->crypto_major_1h` score `0.5176` n `133` status `ready` deltaP `6.8468` edge `0.1169` maxDD `-4.2199`
- `market_context_high->index_4h` score `0.3024` n `128` status `ready` deltaP `9.6227` edge `0.0452` maxDD `-2.3986`
- `market_context_high->index_1h` score `-0.054` n `133` status `ready` deltaP `4.455` edge `0.0152` maxDD `-1.2855`
- `market_context_high->metal_4h` score `-0.115` n `128` status `ready` deltaP `6.0213` edge `0.0319` maxDD `-2.5301`
- `market_context_high->unknown_1h` score `-0.2095` n `133` status `ready` deltaP `1.138` edge `0.0291` maxDD `-1.665`
- `market_context_high->commodity_1h` score `-0.4156` n `133` status `ready` deltaP `4.132` edge `0.007` maxDD `-4.3601`
- `market_context_high->fx_1h` score `-0.5073` n `133` status `ready` deltaP `-0.2161` edge `0.0038` maxDD `-0.2373`
- `market_context_high->fx_24h` score `-0.5613` n `128` status `ready` deltaP `6.1632` edge `0.0` maxDD `-0.6957`
- `market_context_high->metal_1h` score `-0.6903` n `133` status `ready` deltaP `-0.6787` edge `0.0039` maxDD `-1.5521`
- `market_context_high->equity_1h` score `-0.8611` n `133` status `ready` deltaP `-1.3799` edge `0.0213` maxDD `-2.7085`
- `market_context_high->fx_4h` score `-1.0528` n `128` status `ready` deltaP `-2.2866` edge `0.0106` maxDD `-0.6474`
- `market_context_high->equity_24h` score `-1.2669` n `128` status `ready` deltaP `8.2465` edge `-0.0628` maxDD `-3.1535`
- `market_context_high->commodity_4h` score `-1.2966` n `128` status `ready` deltaP `2.8391` edge `0.0091` maxDD `-10.2078`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

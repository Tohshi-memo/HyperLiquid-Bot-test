# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-22T13:07:27.540181+00:00`
- Price records: `672`
- Market context records: `7567`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14475`

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

- `market_context_high->commodity_4h` score `0.0998` n `171` status `ready` deltaP `8.5091` edge `0.0276` maxDD `-2.4139`
- `market_context_high->index_1h` score `-0.0991` n `171` status `ready` deltaP `5.8006` edge `0.0082` maxDD `-1.7657`
- `market_context_high->fx_1h` score `-0.2541` n `171` status `ready` deltaP `2.5289` edge `0.0005` maxDD `-0.6615`
- `market_context_high->commodity_24h` score `-0.2564` n `153` status `ready` deltaP `12.4024` edge `0.0543` maxDD `-7.0012`
- `market_context_high->commodity_1h` score `-0.3372` n `171` status `ready` deltaP `4.0224` edge `0.0023` maxDD `-1.5775`
- `market_context_high->unknown_1h` score `-0.4934` n `171` status `ready` deltaP `2.3602` edge `0.0055` maxDD `-1.3217`
- `market_context_high->unknown_4h` score `-0.5519` n `171` status `ready` deltaP `11.1183` edge `0.091` maxDD `-6.2031`
- `market_context_high->index_4h` score `-0.6343` n `171` status `ready` deltaP `10.647` edge `0.029` maxDD `-4.1702`
- `market_context_high->crypto_major_1h` score `-0.6514` n `171` status `ready` deltaP `5.1205` edge `0.0234` maxDD `-7.6171`
- `market_context_high->crypto_alt_1h` score `-0.6696` n `171` status `ready` deltaP `0.1707` edge `0.0169` maxDD `-5.9775`
- `market_context_high->metal_1h` score `-0.7329` n `171` status `ready` deltaP `0.5121` edge `0.013` maxDD `-1.4971`
- `market_context_high->fx_24h` score `-0.8264` n `153` status `ready` deltaP `8.9488` edge `0.0155` maxDD `-3.8554`
- `market_context_high->fx_4h` score `-1.2825` n `171` status `ready` deltaP `0.1556` edge `0.003` maxDD `-2.1439`
- `market_context_high->equity_1h` score `-1.4399` n `171` status `ready` deltaP `4.1963` edge `0.0285` maxDD `-14.6193`
- `market_context_high->unknown_24h` score `-1.4412` n `154` status `ready` deltaP `5.4631` edge `0.0537` maxDD `-9.9917`
- `market_context_high->metal_4h` score `-1.524` n `171` status `ready` deltaP `0.5696` edge `0.049` maxDD `-4.8549`
- `market_context_high->crypto_alt_4h` score `-1.8843` n `171` status `ready` deltaP `0.2148` edge `0.0313` maxDD `-15.2776`
- `market_context_high->crypto_major_4h` score `-2.4931` n `171` status `ready` deltaP `4.7408` edge `0.0382` maxDD `-23.4879`
- `market_context_high->equity_4h` score `-2.9301` n `171` status `ready` deltaP `2.6396` edge `0.1663` maxDD `-31.7644`
- `market_context_high->index_24h` score `-4.268` n `153` status `ready` deltaP `-19.7604` edge `-0.0107` maxDD `-17.7124`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

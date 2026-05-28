# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-28T04:52:21.584016+00:00`
- Price records: `672`
- Market context records: `2109`
- Flow alert records: `7967`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9146`

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

- `market_context_high->crypto_alt_4h` score `11.4785` n `172` status `ready` deltaP `32.6716` edge `0.8407` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `10.9557` n `172` status `ready` deltaP `39.0102` edge `0.7059` maxDD `-1.9063`
- `market_context_high->unknown_4h` score `6.0014` n `172` status `ready` deltaP `24.5143` edge `0.4116` maxDD `-2.6599`
- `market_context_high->equity_4h` score `4.3568` n `172` status `ready` deltaP `22.9828` edge `0.3193` maxDD `-5.0894`
- `market_context_high->index_4h` score `2.6098` n `172` status `ready` deltaP `19.1613` edge `0.1581` maxDD `-1.8022`
- `market_context_high->index_24h` score `2.5139` n `171` status `ready` deltaP `12.0339` edge `0.2521` maxDD `-4.1604`
- `market_context_high->crypto_major_1h` score `2.3388` n `172` status `ready` deltaP `16.0667` edge `0.1864` maxDD `-3.2225`
- `market_context_high->metal_4h` score `2.2128` n `172` status `ready` deltaP `17.7928` edge `0.2174` maxDD `-5.7961`
- `market_context_high->crypto_alt_1h` score `2.1588` n `172` status `ready` deltaP `12.641` edge `0.207` maxDD `-4.9097`
- `market_context_high->unknown_24h` score `2.0315` n `171` status `ready` deltaP `23.5253` edge `0.5445` maxDD `-35.8966`
- `market_context_high->equity_24h` score `1.7654` n `171` status `ready` deltaP `23.3038` edge `0.4816` maxDD `-33.1875`
- `market_context_high->equity_1h` score `0.8802` n `172` status `ready` deltaP `10.7228` edge `0.0807` maxDD `-2.6402`
- `market_context_high->crypto_major_24h` score `0.5903` n `171` status `ready` deltaP `21.1164` edge `0.767` maxDD `-62.3533`
- `market_context_high->metal_1h` score `0.2012` n `172` status `ready` deltaP `7.4607` edge `0.0466` maxDD `-3.3654`
- `market_context_high->index_1h` score `0.1489` n `172` status `ready` deltaP `5.8418` edge `0.0325` maxDD `-1.3898`
- `market_context_high->fx_24h` score `-0.076` n `171` status `ready` deltaP `14.8294` edge `0.0307` maxDD `-2.811`
- `market_context_high->unknown_1h` score `-0.1164` n `172` status `ready` deltaP `4.5989` edge `0.0316` maxDD `-3.0902`
- `market_context_high->metal_24h` score `-0.4488` n `171` status `ready` deltaP `10.8773` edge `0.2802` maxDD `-23.2095`
- `market_context_high->fx_1h` score `-0.5639` n `172` status `ready` deltaP `-1.5945` edge `0.0011` maxDD `-0.3548`
- `market_context_high->fx_4h` score `-1.0992` n `172` status `ready` deltaP `-7.4518` edge `-0.0031` maxDD `-1.0513`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

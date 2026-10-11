# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-11T21:37:29.128501+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `9116`

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

- `market_context_high->unknown_24h` score `1380.8841` n `40` status `ready` deltaP `-22.5694` edge `115.2605` maxDD `-1.2425`
- `market_context_high->unknown_4h` score `49.0899` n `95` status `ready` deltaP `-3.1081` edge `4.1696` maxDD `-2.3109`
- `market_context_high->equity_24h` score `8.796` n `40` status `ready` deltaP `27.6736` edge `0.5914` maxDD `-1.0977`
- `market_context_high->index_24h` score `6.4084` n `40` status `ready` deltaP `52.4306` edge `0.1845` maxDD `0.0`
- `market_context_high->unknown_1h` score `4.7699` n `107` status `ready` deltaP `-3.1185` edge `0.4519` maxDD `-1.0231`
- `market_context_high->fx_24h` score `3.0701` n `40` status `ready` deltaP `34.8611` edge `0.0364` maxDD `-0.0374`
- `market_context_high->crypto_major_24h` score `1.3972` n `40` status `ready` deltaP `-21.1111` edge `0.572` maxDD `-17.8526`
- `market_context_high->fx_4h` score `0.7465` n `95` status `ready` deltaP `12.4904` edge `0.0073` maxDD `-0.2692`
- `market_context_high->commodity_4h` score `0.606` n `95` status `ready` deltaP `12.8899` edge `0.0179` maxDD `-1.6002`
- `market_context_high->commodity_1h` score `0.3614` n `107` status `ready` deltaP `7.6767` edge `0.0073` maxDD `-0.6025`
- `market_context_high->crypto_alt_1h` score `0.1268` n `107` status `ready` deltaP `5.3221` edge `0.0842` maxDD `-4.9401`
- `market_context_high->metal_4h` score `0.1152` n `95` status `ready` deltaP `9.0709` edge `0.0214` maxDD `-1.1153`
- `market_context_high->crypto_major_4h` score `-0.0425` n `95` status `ready` deltaP `0.7365` edge `0.2002` maxDD `-11.1784`
- `market_context_high->fx_1h` score `-0.0506` n `107` status `ready` deltaP `2.5547` edge `0.0007` maxDD `-0.271`
- `market_context_high->metal_1h` score `-0.1352` n `107` status `ready` deltaP `6.633` edge `0.0034` maxDD `-0.7107`
- `market_context_high->crypto_alt_4h` score `-0.2494` n `95` status `ready` deltaP `-1.7891` edge `0.2358` maxDD `-13.8008`
- `market_context_high->crypto_major_1h` score `-0.3518` n `107` status `ready` deltaP `-0.617` edge `0.0479` maxDD `-3.7778`
- `market_context_high->index_4h` score `-0.5324` n `95` status `ready` deltaP `-0.7077` edge `0.0065` maxDD `-0.9364`
- `market_context_high->index_1h` score `-0.7812` n `107` status `ready` deltaP `-5.0674` edge `-0.0013` maxDD `-0.5392`
- `market_context_high->equity_1h` score `-0.9692` n `107` status `ready` deltaP `-5.9698` edge `0.0025` maxDD `-2.2898`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

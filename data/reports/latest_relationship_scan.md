# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-08T10:52:20.243132+00:00`
- Price records: `672`
- Market context records: `3273`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10506`

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

- `risk_on_high->crypto_major_4h` score `16.3343` n `32` status `ready` deltaP `31.0976` edge `1.2661` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `16.3343` n `32` status `ready` deltaP `31.0976` edge `1.2661` maxDD `-5.9781`
- `market_context_high->crypto_alt_24h` score `13.9668` n `108` status `ready` deltaP `17.6505` edge `2.6571` maxDD `-70.3986`
- `market_context_high->commodity_24h` score `12.1577` n `108` status `ready` deltaP `43.75` edge `0.7643` maxDD `-2.0927`
- `market_context_high->index_24h` score `9.2821` n `108` status `ready` deltaP `29.919` edge `0.8295` maxDD `-16.1026`
- `risk_on_high->crypto_alt_4h` score `7.6085` n `32` status `ready` deltaP `11.814` edge `0.7397` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `7.6085` n `32` status `ready` deltaP `11.814` edge `0.7397` maxDD `-11.7537`
- `market_context_high->equity_24h` score `6.6768` n `108` status `ready` deltaP `19.5023` edge `1.5676` maxDD `-53.663`
- `risk_on_high->equity_4h` score `3.8218` n `32` status `ready` deltaP `15.1677` edge `0.5023` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `3.8218` n `32` status `ready` deltaP `15.1677` edge `0.5023` maxDD `-5.7426`
- `market_context_high->commodity_4h` score `2.2288` n `165` status `ready` deltaP `19.8384` edge `0.1493` maxDD `-3.9989`
- `risk_on_high->crypto_major_1h` score `2.2076` n `32` status `ready` deltaP `8.0651` edge `0.3362` maxDD `-5.8885`
- `risk_on_and_context->crypto_major_1h` score `2.2076` n `32` status `ready` deltaP `8.0651` edge `0.3362` maxDD `-5.8885`
- `market_context_high->crypto_major_24h` score `1.4776` n `108` status `ready` deltaP `19.7338` edge `2.1278` maxDD `-152.2601`
- `risk_on_high->index_4h` score `1.2769` n `32` status `ready` deltaP `2.3628` edge `0.2067` maxDD `-1.7001`
- `risk_on_and_context->index_4h` score `1.2769` n `32` status `ready` deltaP `2.3628` edge `0.2067` maxDD `-1.7001`
- `risk_on_high->metal_1h` score `0.3453` n `32` status `ready` deltaP `6.6991` edge `0.0681` maxDD `-1.4793`
- `risk_on_and_context->metal_1h` score `0.3453` n `32` status `ready` deltaP `6.6991` edge `0.0681` maxDD `-1.4793`
- `risk_on_high->crypto_alt_1h` score `0.296` n `32` status `ready` deltaP `1.3473` edge `0.1727` maxDD `-8.1649`
- `risk_on_and_context->crypto_alt_1h` score `0.296` n `32` status `ready` deltaP `1.3473` edge `0.1727` maxDD `-8.1649`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

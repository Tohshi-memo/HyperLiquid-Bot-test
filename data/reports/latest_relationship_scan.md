# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-08T21:52:20.896936+00:00`
- Price records: `672`
- Market context records: `3320`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13151`

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

- `risk_on_high->crypto_major_4h` score `15.8193` n `32` status `ready` deltaP `30.0305` edge `1.2303` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `15.8193` n `32` status `ready` deltaP `30.0305` edge `1.2303` maxDD `-5.9781`
- `market_context_high->crypto_alt_24h` score `15.5721` n `135` status `ready` deltaP `22.1065` edge `2.8332` maxDD `-70.3986`
- `market_context_high->index_24h` score `10.978` n `135` status `ready` deltaP `33.6574` edge `0.9459` maxDD `-16.1026`
- `market_context_high->equity_24h` score `9.5198` n `135` status `ready` deltaP `26.4004` edge `1.8861` maxDD `-53.663`
- `risk_on_high->crypto_alt_4h` score `7.232` n `32` status `ready` deltaP `9.2226` edge `0.7256` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `7.232` n `32` status `ready` deltaP `9.2226` edge `0.7256` maxDD `-11.7537`
- `market_context_high->crypto_major_24h` score `3.6069` n `135` status `ready` deltaP `23.3912` edge `2.3764` maxDD `-152.2601`
- `risk_on_high->equity_4h` score `3.5429` n `32` status `ready` deltaP `13.7957` edge `0.4757` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `3.5429` n `32` status `ready` deltaP `13.7957` edge `0.4757` maxDD `-5.7426`
- `market_context_high->commodity_24h` score `2.4643` n `135` status `ready` deltaP `26.25` edge `0.4947` maxDD `-19.3011`
- `risk_on_high->crypto_major_1h` score `2.0221` n `32` status `ready` deltaP `6.8675` edge `0.3204` maxDD `-5.8885`
- `risk_on_and_context->crypto_major_1h` score `2.0221` n `32` status `ready` deltaP `6.8675` edge `0.3204` maxDD `-5.8885`
- `market_context_high->commodity_4h` score `1.8974` n `185` status `ready` deltaP `17.9004` edge `0.1346` maxDD `-3.9989`
- `risk_on_high->index_4h` score `1.0507` n `32` status `ready` deltaP `0.5335` edge `0.1899` maxDD `-1.7001`
- `risk_on_and_context->index_4h` score `1.0507` n `32` status `ready` deltaP `0.5335` edge `0.1899` maxDD `-1.7001`
- `risk_on_high->metal_1h` score `0.2541` n `32` status `ready` deltaP `5.9506` edge `0.0614` maxDD `-1.4793`
- `risk_on_and_context->metal_1h` score `0.2541` n `32` status `ready` deltaP `5.9506` edge `0.0614` maxDD `-1.4793`
- `risk_on_high->crypto_alt_1h` score `0.1815` n `32` status `ready` deltaP `0.1497` edge `0.166` maxDD `-8.1649`
- `risk_on_and_context->crypto_alt_1h` score `0.1815` n `32` status `ready` deltaP `0.1497` edge `0.166` maxDD `-8.1649`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

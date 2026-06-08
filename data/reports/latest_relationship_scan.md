# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-08T10:07:26.767339+00:00`
- Price records: `672`
- Market context records: `3270`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10503`

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

- `risk_on_high->crypto_major_4h` score `16.4439` n `32` status `ready` deltaP `31.4024` edge `1.2732` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `16.4439` n `32` status `ready` deltaP `31.4024` edge `1.2732` maxDD `-5.9781`
- `market_context_high->crypto_alt_24h` score `13.8406` n `105` status `ready` deltaP `16.5426` edge `2.6483` maxDD `-70.3986`
- `market_context_high->commodity_24h` score `12.3007` n `105` status `ready` deltaP `44.1121` edge `0.7738` maxDD `-2.0927`
- `market_context_high->index_24h` score `9.1537` n `105` status `ready` deltaP `29.4841` edge `0.8217` maxDD `-16.1026`
- `risk_on_high->crypto_alt_4h` score `7.7218` n `32` status `ready` deltaP `12.2713` edge `0.7461` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `7.7218` n `32` status `ready` deltaP `12.2713` edge `0.7461` maxDD `-11.7537`
- `market_context_high->equity_24h` score `6.4191` n `105` status `ready` deltaP `18.4177` edge `1.5418` maxDD `-53.663`
- `risk_on_high->equity_4h` score `3.8986` n `32` status `ready` deltaP `15.625` edge `0.5091` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `3.8986` n `32` status `ready` deltaP `15.625` edge `0.5091` maxDD `-5.7426`
- `risk_on_high->crypto_major_1h` score `2.192` n `32` status `ready` deltaP `7.9154` edge `0.3352` maxDD `-5.8885`
- `risk_on_and_context->crypto_major_1h` score `2.192` n `32` status `ready` deltaP `7.9154` edge `0.3352` maxDD `-5.8885`
- `market_context_high->commodity_4h` score `2.1515` n `165` status `ready` deltaP `19.3811` edge `0.1459` maxDD `-3.9989`
- `risk_on_high->index_4h` score `1.3295` n `32` status `ready` deltaP `2.8201` edge `0.2104` maxDD `-1.7001`
- `risk_on_and_context->index_4h` score `1.3295` n `32` status `ready` deltaP `2.8201` edge `0.2104` maxDD `-1.7001`
- `market_context_high->crypto_major_24h` score `1.1696` n `105` status `ready` deltaP `18.6409` edge `2.0956` maxDD `-152.2601`
- `risk_on_high->metal_1h` score `0.3367` n `32` status `ready` deltaP `6.5494` edge `0.068` maxDD `-1.4793`
- `risk_on_and_context->metal_1h` score `0.3367` n `32` status `ready` deltaP `6.5494` edge `0.068` maxDD `-1.4793`
- `risk_on_high->crypto_alt_1h` score `0.2867` n `32` status `ready` deltaP `1.1976` edge `0.1725` maxDD `-8.1649`
- `risk_on_and_context->crypto_alt_1h` score `0.2867` n `32` status `ready` deltaP `1.1976` edge `0.1725` maxDD `-8.1649`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

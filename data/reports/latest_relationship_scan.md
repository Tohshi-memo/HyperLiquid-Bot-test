# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-08T10:37:25.148600+00:00`
- Price records: `672`
- Market context records: `3272`
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

- `risk_on_high->crypto_major_4h` score `16.3643` n `32` status `ready` deltaP `31.0976` edge `1.2686` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `16.3643` n `32` status `ready` deltaP `31.0976` edge `1.2686` maxDD `-5.9781`
- `market_context_high->crypto_alt_24h` score `13.9168` n `107` status `ready` deltaP `17.3481` edge `2.6527` maxDD `-70.3986`
- `market_context_high->commodity_24h` score `12.2166` n `107` status `ready` deltaP `43.8717` edge `0.7684` maxDD `-2.0927`
- `market_context_high->index_24h` score `9.2549` n `107` status `ready` deltaP `29.8936` edge `0.8274` maxDD `-16.1026`
- `risk_on_high->crypto_alt_4h` score `7.6519` n `32` status `ready` deltaP `11.9665` edge `0.7423` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `7.6519` n `32` status `ready` deltaP `11.9665` edge `0.7423` maxDD `-11.7537`
- `market_context_high->equity_24h` score `6.5889` n `107` status `ready` deltaP `19.1475` edge `1.5587` maxDD `-53.663`
- `risk_on_high->equity_4h` score `3.8461` n `32` status `ready` deltaP `15.3201` edge `0.5044` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `3.8461` n `32` status `ready` deltaP `15.3201` edge `0.5044` maxDD `-5.7426`
- `risk_on_high->crypto_major_1h` score `2.2061` n `32` status `ready` deltaP `8.0651` edge `0.336` maxDD `-5.8885`
- `risk_on_and_context->crypto_major_1h` score `2.2061` n `32` status `ready` deltaP `8.0651` edge `0.336` maxDD `-5.8885`
- `market_context_high->commodity_4h` score `2.201` n `165` status `ready` deltaP `19.6859` edge `0.148` maxDD `-3.9989`
- `market_context_high->crypto_major_24h` score `1.375` n `107` status `ready` deltaP `19.3796` edge `2.117` maxDD `-152.2601`
- `risk_on_high->index_4h` score `1.2949` n `32` status `ready` deltaP `2.5152` edge `0.208` maxDD `-1.7001`
- `risk_on_and_context->index_4h` score `1.2949` n `32` status `ready` deltaP `2.5152` edge `0.208` maxDD `-1.7001`
- `risk_on_high->metal_1h` score `0.3367` n `32` status `ready` deltaP `6.5494` edge `0.068` maxDD `-1.4793`
- `risk_on_and_context->metal_1h` score `0.3367` n `32` status `ready` deltaP `6.5494` edge `0.068` maxDD `-1.4793`
- `risk_on_high->crypto_alt_1h` score `0.2984` n `32` status `ready` deltaP `1.3473` edge `0.173` maxDD `-8.1649`
- `risk_on_and_context->crypto_alt_1h` score `0.2984` n `32` status `ready` deltaP `1.3473` edge `0.173` maxDD `-8.1649`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

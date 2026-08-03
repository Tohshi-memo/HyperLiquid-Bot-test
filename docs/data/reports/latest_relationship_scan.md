# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-03T00:22:29.998828+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5935`

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

- `news_risk_high->unknown_24h` score `5070.7358` n `60` status `ready` deltaP `23.7152` edge `422.4453` maxDD `-2.0332`
- `market_context_high->crypto_alt_24h` score `14.985` n `40` status `ready` deltaP `52.1528` edge `0.9408` maxDD `-2.1786`
- `market_context_high->commodity_24h` score `11.205` n `40` status `ready` deltaP `51.3194` edge `0.6044` maxDD `-0.6889`
- `news_risk_high->equity_4h` score `4.3372` n `60` status `ready` deltaP `13.7704` edge `0.346` maxDD `-3.4427`
- `news_risk_high->index_4h` score `1.5016` n `60` status `ready` deltaP `14.3699` edge `0.0674` maxDD `-0.3783`
- `market_context_high->commodity_4h` score `0.9462` n `41` status `ready` deltaP `12.5` edge `0.1226` maxDD `-2.7703`
- `market_context_high->crypto_alt_4h` score `0.6733` n `41` status `ready` deltaP `7.317` edge `0.1281` maxDD `-4.9116`
- `market_context_high->fx_4h` score `0.5886` n `41` status `ready` deltaP `19.3598` edge `0.026` maxDD `-1.3685`
- `market_context_high->commodity_1h` score `0.3617` n `45` status `ready` deltaP `7.5017` edge `0.0338` maxDD `-1.3282`
- `news_risk_high->equity_1h` score `0.3367` n `60` status `ready` deltaP `7.1757` edge `0.0625` maxDD `-2.916`
- `market_context_high->fx_1h` score `0.1714` n `45` status `ready` deltaP `8.9754` edge `-0.0001` maxDD `-0.6874`
- `news_risk_high->fx_4h` score `-0.0637` n `60` status `ready` deltaP `9.9289` edge `0.0214` maxDD `-0.6604`
- `news_risk_high->fx_1h` score `-0.0707` n `60` status `ready` deltaP `2.8643` edge `0.0041` maxDD `-0.2475`
- `news_risk_high->index_1h` score `-0.0775` n `60` status `ready` deltaP `2.6048` edge `0.005` maxDD `-0.5845`
- `news_risk_high->metal_4h` score `-0.0913` n `60` status `ready` deltaP `3.1707` edge `0.0106` maxDD `-0.8085`
- `news_risk_high->crypto_alt_1h` score `-0.1402` n `60` status `ready` deltaP `5.4491` edge `0.0139` maxDD `-3.1233`
- `news_risk_high->metal_1h` score `-0.2832` n `60` status `ready` deltaP `0.4691` edge `0.0009` maxDD `-0.5599`
- `news_risk_high->commodity_1h` score `-0.3649` n `60` status `ready` deltaP `5.2794` edge `-0.0142` maxDD `-2.0891`
- `news_risk_high->crypto_major_1h` score `-0.4769` n `60` status `ready` deltaP `1.0479` edge `0.0039` maxDD `-3.762`
- `market_context_high->crypto_alt_1h` score `-0.6267` n `45` status `ready` deltaP `-2.8842` edge `0.0016` maxDD `-3.0178`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

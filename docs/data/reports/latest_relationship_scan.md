# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-12T07:37:28.143652+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11512`

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

- `market_context_high->unknown_24h` score `1979.3934` n `125` status `ready` deltaP `13.8514` edge `164.8623` maxDD `-0.082`
- `news_risk_high->unknown_1h` score `383.3196` n `82` status `ready` deltaP `-3.1547` edge `32.0065` maxDD `-1.7068`
- `news_risk_high->crypto_major_24h` score `24.221` n `59` status `ready` deltaP `54.505` edge `1.7451` maxDD `-5.8705`
- `risk_on_high->crypto_alt_24h` score `22.216` n `73` status `ready` deltaP `41.7618` edge `1.5959` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `22.216` n `73` status `ready` deltaP `41.7618` edge `1.5959` maxDD `-0.8386`
- `market_context_high->crypto_alt_24h` score `18.9096` n `125` status `ready` deltaP `35.8111` edge `1.4198` maxDD `-3.9523`
- `news_risk_high->crypto_alt_24h` score `17.5954` n `59` status `ready` deltaP `29.967` edge `1.3153` maxDD `-2.2369`
- `news_risk_high->equity_24h` score `12.1138` n `59` status `ready` deltaP `33.5894` edge `0.7954` maxDD `-0.1212`
- `risk_on_high->equity_24h` score `9.0159` n `73` status `ready` deltaP `36.9792` edge `0.5048` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `9.0159` n `73` status `ready` deltaP `36.9792` edge `0.5048` maxDD `0.0`
- `market_context_high->equity_24h` score `8.6907` n `125` status `ready` deltaP `36.9792` edge `0.4777` maxDD `0.0`
- `news_risk_high->metal_24h` score `8.2376` n `59` status `ready` deltaP `51.9097` edge `0.3404` maxDD `0.0`
- `risk_on_high->crypto_alt_4h` score `8.1767` n `73` status `ready` deltaP `43.1485` edge `0.4309` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `8.1767` n `73` status `ready` deltaP `43.1485` edge `0.4309` maxDD `-1.9733`
- `news_risk_high->index_24h` score `7.9189` n `59` status `ready` deltaP `51.4713` edge `0.3261` maxDD `-0.0797`
- `risk_on_high->crypto_major_4h` score `5.6793` n `73` status `ready` deltaP `28.0864` edge `0.3719` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `5.6793` n `73` status `ready` deltaP `28.0864` edge `0.3719` maxDD `-3.8693`
- `risk_on_high->index_24h` score `5.081` n `73` status `ready` deltaP `50.7515` edge `0.0893` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `5.081` n `73` status `ready` deltaP `50.7515` edge `0.0893` maxDD `-0.0051`
- `risk_on_high->crypto_major_24h` score `4.0038` n `73` status `ready` deltaP `16.0792` edge `0.8129` maxDD `-24.5429`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

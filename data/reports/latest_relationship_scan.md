# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-12T15:22:25.169207+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `12636`

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

- `market_context_high->unknown_24h` score `5887.024` n `94` status `ready` deltaP `13.3237` edge `490.5017` maxDD `-0.082`
- `risk_on_high->unknown_24h` score `3107.6017` n `49` status `ready` deltaP `15.4514` edge `258.8638` maxDD `0.0`
- `risk_on_and_context->unknown_24h` score `3107.6017` n `49` status `ready` deltaP `15.4514` edge `258.8638` maxDD `0.0`
- `news_risk_high->unknown_1h` score `382.9972` n `82` status `ready` deltaP `-5.4002` edge `31.9946` maxDD `-1.7068`
- `news_risk_high->crypto_major_24h` score `24.3242` n `60` status `ready` deltaP `54.3403` edge `1.7548` maxDD `-5.8705`
- `risk_on_high->crypto_alt_24h` score `17.8172` n `49` status `ready` deltaP `39.6223` edge `1.2436` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `17.8172` n `49` status `ready` deltaP `39.6223` edge `1.2436` maxDD `-0.8386`
- `news_risk_high->crypto_alt_24h` score `17.5842` n `60` status `ready` deltaP `29.8264` edge `1.3153` maxDD `-2.2369`
- `market_context_high->crypto_alt_24h` score `15.4964` n `94` status `ready` deltaP `32.8051` edge `1.1554` maxDD `-3.9523`
- `news_risk_high->equity_24h` score `12.2104` n `60` status `ready` deltaP `34.2361` edge `0.8021` maxDD `-0.3576`
- `risk_on_high->equity_24h` score `9.1857` n `49` status `ready` deltaP `39.2361` edge `0.5039` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `9.1857` n `49` status `ready` deltaP `39.2361` edge `0.5039` maxDD `0.0`
- `market_context_high->equity_24h` score `8.9217` n `94` status `ready` deltaP `39.2361` edge `0.4819` maxDD `0.0`
- `risk_on_high->crypto_alt_4h` score `8.6745` n `49` status `ready` deltaP `42.2008` edge `0.4787` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `8.6745` n `49` status `ready` deltaP `42.2008` edge `0.4787` maxDD `-1.9733`
- `news_risk_high->metal_24h` score `8.2546` n `60` status `ready` deltaP `53.0208` edge `0.3396` maxDD `-0.0817`
- `news_risk_high->index_24h` score `7.7773` n `60` status `ready` deltaP `50.5556` edge `0.3204` maxDD `-0.0797`
- `risk_on_high->index_24h` score `4.8651` n `49` status `ready` deltaP `49.4332` edge `0.0801` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `4.8651` n `49` status `ready` deltaP `49.4332` edge `0.0801` maxDD `-0.0051`
- `risk_on_high->equity_4h` score `4.1117` n `49` status `ready` deltaP `36.6538` edge `0.1076` maxDD `-0.079`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

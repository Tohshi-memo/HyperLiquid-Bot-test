# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-03T05:37:30.702081+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11719`

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

- `risk_on_high->unknown_4h` score `40.6142` n `112` status `ready` deltaP `18.5323` edge `3.3228` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `40.6142` n `112` status `ready` deltaP `18.5323` edge `3.3228` maxDD `-2.2797`
- `market_context_high->unknown_4h` score `27.9187` n `154` status `ready` deltaP `14.4738` edge `2.2996` maxDD `-2.563`
- `risk_on_high->unknown_1h` score `18.2779` n `124` status `ready` deltaP `0.8354` edge `1.5753` maxDD `-1.95`
- `risk_on_and_context->unknown_1h` score `18.2779` n `124` status `ready` deltaP `0.8354` edge `1.5753` maxDD `-1.95`
- `market_context_high->unknown_1h` score `12.0066` n `166` status `ready` deltaP `-0.2237` edge `1.0651` maxDD `-2.0446`
- `risk_on_high->equity_24h` score `5.0751` n `107` status `ready` deltaP `23.1812` edge `0.6829` maxDD `-19.828`
- `risk_on_and_context->equity_24h` score `5.0751` n `107` status `ready` deltaP `23.1812` edge `0.6829` maxDD `-19.828`
- `risk_on_high->crypto_alt_24h` score `2.3522` n `107` status `ready` deltaP `21.6041` edge `0.8479` maxDD `-42.8959`
- `risk_on_and_context->crypto_alt_24h` score `2.3522` n `107` status `ready` deltaP `21.6041` edge `0.8479` maxDD `-42.8959`
- `news_risk_high->crypto_alt_24h` score `2.3232` n `59` status `ready` deltaP `21.5249` edge `0.4478` maxDD `-19.4761`
- `news_risk_high->equity_24h` score `2.0752` n `59` status `ready` deltaP `9.1308` edge `0.3588` maxDD `-15.4056`
- `market_context_high->equity_24h` score `1.6442` n `147` status `ready` deltaP `19.1504` edge `0.564` maxDD `-24.4698`
- `news_risk_high->crypto_major_24h` score `1.4501` n `59` status `ready` deltaP `14.6952` edge `0.4612` maxDD `-30.7329`
- `risk_on_high->crypto_major_24h` score `0.7902` n `107` status `ready` deltaP `21.0313` edge `0.8355` maxDD `-56.9519`
- `risk_on_and_context->crypto_major_24h` score `0.7902` n `107` status `ready` deltaP `21.0313` edge `0.8355` maxDD `-56.9519`
- `market_context_high->crypto_major_24h` score `0.6277` n `147` status `ready` deltaP `24.0576` edge `0.8665` maxDD `-61.3797`
- `market_context_high->crypto_alt_24h` score `0.4989` n `147` status `ready` deltaP `15.6215` edge `0.7097` maxDD `-46.3234`
- `news_risk_high->commodity_4h` score `0.1085` n `67` status `ready` deltaP `3.8132` edge `0.0244` maxDD `-0.8733`
- `risk_on_high->metal_1h` score `0.0834` n `124` status `ready` deltaP `11.7636` edge `0.0035` maxDD `-1.699`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

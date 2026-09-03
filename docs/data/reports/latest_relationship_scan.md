# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-03T04:52:26.737622+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11701`

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

- `risk_on_high->unknown_4h` score `41.5784` n `109` status `ready` deltaP `18.0899` edge `3.4061` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `41.5784` n `109` status `ready` deltaP `18.0899` edge `3.4061` maxDD `-2.2797`
- `market_context_high->unknown_4h` score `28.3883` n `151` status `ready` deltaP `14.0739` edge `2.3414` maxDD `-2.563`
- `risk_on_high->unknown_1h` score `18.1833` n `121` status `ready` deltaP `0.7621` edge `1.5679` maxDD `-1.95`
- `risk_on_and_context->unknown_1h` score `18.1833` n `121` status `ready` deltaP `0.7621` edge `1.5679` maxDD `-1.95`
- `market_context_high->unknown_1h` score `11.8711` n `163` status `ready` deltaP `-0.2976` edge `1.0543` maxDD `-2.0446`
- `risk_on_high->equity_24h` score `5.1888` n `107` status `ready` deltaP `23.702` edge `0.6889` maxDD `-19.828`
- `risk_on_and_context->equity_24h` score `5.1888` n `107` status `ready` deltaP `23.702` edge `0.6889` maxDD `-19.828`
- `risk_on_high->crypto_alt_24h` score `2.3201` n `107` status `ready` deltaP `21.2568` edge `0.8461` maxDD `-42.8959`
- `risk_on_and_context->crypto_alt_24h` score `2.3201` n `107` status `ready` deltaP `21.2568` edge `0.8461` maxDD `-42.8959`
- `news_risk_high->crypto_alt_24h` score `2.2911` n `59` status `ready` deltaP `21.1776` edge `0.446` maxDD `-19.4761`
- `news_risk_high->equity_24h` score `2.1889` n `59` status `ready` deltaP `9.6516` edge `0.3648` maxDD `-15.4056`
- `market_context_high->equity_24h` score `1.7181` n `147` status `ready` deltaP `19.6712` edge `0.57` maxDD `-24.4698`
- `news_risk_high->crypto_major_24h` score `1.3239` n `59` status `ready` deltaP `14.348` edge `0.453` maxDD `-30.7329`
- `risk_on_high->crypto_major_24h` score `0.7082` n `107` status `ready` deltaP `20.6841` edge `0.8273` maxDD `-56.9519`
- `risk_on_and_context->crypto_major_24h` score `0.7082` n `107` status `ready` deltaP `20.6841` edge `0.8273` maxDD `-56.9519`
- `market_context_high->crypto_major_24h` score `0.5457` n `147` status `ready` deltaP `23.7104` edge `0.8583` maxDD `-61.3797`
- `market_context_high->crypto_alt_24h` score `0.4668` n `147` status `ready` deltaP `15.2742` edge `0.7079` maxDD `-46.3234`
- `risk_on_high->index_1h` score `0.2539` n `121` status `ready` deltaP `9.055` edge `0.0053` maxDD `-0.5605`
- `risk_on_and_context->index_1h` score `0.2539` n `121` status `ready` deltaP `9.055` edge `0.0053` maxDD `-0.5605`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

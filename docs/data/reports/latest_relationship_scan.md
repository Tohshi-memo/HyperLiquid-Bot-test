# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-30T11:52:37.480056+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7046`

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

- `market_context_high->unknown_24h` score `1801.625` n `134` status `ready` deltaP `-2.7908` edge `150.197` maxDD `-1.1049`
- `news_risk_high->unknown_1h` score `244.1262` n `41` status `ready` deltaP `-4.1989` edge `20.3844` maxDD `-0.3382`
- `market_context_high->unknown_4h` score `33.3561` n `134` status `ready` deltaP `3.1602` edge `2.7719` maxDD `-0.3966`
- `market_context_high->index_24h` score `3.2103` n `134` status `ready` deltaP `33.8749` edge `0.06` maxDD `-0.1315`
- `news_risk_high->crypto_alt_1h` score `2.5154` n `41` status `ready` deltaP `15.3169` edge `0.1492` maxDD `-1.669`
- `market_context_high->equity_24h` score `2.3296` n `134` status `ready` deltaP `16.3117` edge `0.3611` maxDD `-14.0571`
- `market_context_high->metal_1h` score `0.3688` n `134` status `ready` deltaP `10.7539` edge `0.0135` maxDD `-0.3659`
- `market_context_high->metal_4h` score `0.294` n `134` status `ready` deltaP `15.3736` edge `0.0248` maxDD `-1.8344`
- `market_context_high->equity_1h` score `0.1202` n `134` status `ready` deltaP `4.3324` edge `0.0687` maxDD `-2.3383`
- `market_context_high->commodity_4h` score `0.0741` n `134` status `ready` deltaP `12.4135` edge `0.0453` maxDD `-1.0837`
- `news_risk_high->index_1h` score `0.0491` n `41` status `ready` deltaP `8.4307` edge `-0.0027` maxDD `-0.4437`
- `market_context_high->crypto_major_1h` score `-0.0023` n `134` status `ready` deltaP `7.0158` edge `0.0558` maxDD `-5.2213`
- `market_context_high->fx_1h` score `-0.1205` n `134` status `ready` deltaP `3.28` edge `-0.0015` maxDD `-0.1986`
- `news_risk_high->commodity_1h` score `-0.3327` n `41` status `ready` deltaP `-5.6485` edge `0.0252` maxDD `-0.4158`
- `market_context_high->equity_4h` score `-0.3478` n `134` status `ready` deltaP `1.4766` edge `0.104` maxDD `-6.008`
- `market_context_high->commodity_1h` score `-0.3715` n `134` status `ready` deltaP `1.1954` edge `0.0125` maxDD `-0.4475`
- `market_context_high->fx_4h` score `-0.5931` n `134` status `ready` deltaP `-1.6927` edge `-0.0049` maxDD `-0.4545`
- `market_context_high->crypto_alt_1h` score `-0.861` n `134` status `ready` deltaP `2.8488` edge `0.0571` maxDD `-8.251`
- `market_context_high->index_1h` score `-0.8762` n `134` status `ready` deltaP `-2.5449` edge `-0.0002` maxDD `-1.1344`
- `news_risk_high->fx_1h` score `-1.0591` n `41` status `ready` deltaP `-4.8561` edge `-0.0034` maxDD `-0.1986`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

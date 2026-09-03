# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-03T13:52:26.057160+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11565`

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

- `risk_on_high->unknown_4h` score `35.8734` n `133` status `ready` deltaP `12.657` edge `2.9669` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `35.8734` n `133` status `ready` deltaP `12.657` edge `2.9669` maxDD `-2.2797`
- `market_context_high->unknown_4h` score `29.1084` n `167` status `ready` deltaP `14.2553` edge `2.4002` maxDD `-2.563`
- `risk_on_high->unknown_1h` score `18.682` n `133` status `ready` deltaP `1.7907` edge `1.6026` maxDD `-1.95`
- `risk_on_and_context->unknown_1h` score `18.682` n `133` status `ready` deltaP `1.7907` edge `1.6026` maxDD `-1.95`
- `market_context_high->unknown_1h` score `14.2021` n `167` status `ready` deltaP `2.2455` edge `1.2316` maxDD `-2.0446`
- `market_context_high->equity_24h` score `3.6021` n `127` status `ready` deltaP `22.2058` edge `0.5867` maxDD `-20.7654`
- `news_risk_high->crypto_alt_24h` score `3.2159` n `66` status `ready` deltaP `21.3068` edge `0.5637` maxDD `-19.4761`
- `risk_on_high->equity_24h` score `3.1192` n `107` status `ready` deltaP `17.452` edge `0.5581` maxDD `-19.828`
- `risk_on_and_context->equity_24h` score `3.1192` n `107` status `ready` deltaP `17.452` edge `0.5581` maxDD `-19.828`
- `news_risk_high->crypto_major_24h` score `2.6224` n `66` status `ready` deltaP `17.6452` edge `0.6569` maxDD `-30.7329`
- `news_risk_high->equity_24h` score `1.6621` n `66` status `ready` deltaP `9.1541` edge `0.3988` maxDD `-15.4056`
- `risk_on_high->crypto_alt_24h` score `1.3209` n `107` status `ready` deltaP `17.611` edge `0.7423` maxDD `-42.8959`
- `risk_on_and_context->crypto_alt_24h` score `1.3209` n `107` status `ready` deltaP `17.611` edge `0.7423` maxDD `-42.8959`
- `market_context_high->crypto_alt_24h` score `1.0418` n `127` status `ready` deltaP `19.2667` edge `0.755` maxDD `-46.3234`
- `news_risk_high->commodity_4h` score `0.2222` n `67` status `ready` deltaP `5.4901` edge `0.0278` maxDD `-0.8733`
- `market_context_high->crypto_major_24h` score `0.2112` n `127` status `ready` deltaP `22.2741` edge `0.825` maxDD `-61.3797`
- `risk_on_high->crypto_major_24h` score `0.1647` n `107` status `ready` deltaP `18.9479` edge `0.7692` maxDD `-56.9519`
- `risk_on_and_context->crypto_major_24h` score `0.1647` n `107` status `ready` deltaP `18.9479` edge `0.7692` maxDD `-56.9519`
- `news_risk_high->fx_4h` score `0.0263` n `67` status `ready` deltaP `9.499` edge `0.0045` maxDD `-1.2507`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

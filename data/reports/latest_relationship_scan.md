# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-03T09:37:26.580164+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11581`

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

- `risk_on_high->unknown_4h` score `38.4008` n `128` status `ready` deltaP `14.7294` edge `3.1637` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `38.4008` n `128` status `ready` deltaP `14.7294` edge `3.1637` maxDD `-2.2797`
- `market_context_high->unknown_4h` score `28.7262` n `164` status `ready` deltaP `12.0427` edge `2.3831` maxDD `-2.563`
- `risk_on_high->unknown_1h` score `19.751` n `133` status `ready` deltaP `2.5392` edge `1.6867` maxDD `-1.95`
- `risk_on_and_context->unknown_1h` score `19.751` n `133` status `ready` deltaP `2.5392` edge `1.6867` maxDD `-1.95`
- `market_context_high->unknown_1h` score `13.6332` n `176` status `ready` deltaP `1.8984` edge `1.1865` maxDD `-2.0446`
- `risk_on_high->equity_24h` score `4.1977` n `107` status `ready` deltaP `20.4034` edge `0.6283` maxDD `-19.828`
- `risk_on_and_context->equity_24h` score `4.1977` n `107` status `ready` deltaP `20.4034` edge `0.6283` maxDD `-19.828`
- `market_context_high->equity_24h` score `2.8477` n `141` status `ready` deltaP `18.7463` edge `0.5469` maxDD `-20.7654`
- `risk_on_high->crypto_alt_24h` score `2.1093` n `107` status `ready` deltaP `20.5624` edge `0.8237` maxDD `-42.8959`
- `risk_on_and_context->crypto_alt_24h` score `2.1093` n `107` status `ready` deltaP `20.5624` edge `0.8237` maxDD `-42.8959`
- `news_risk_high->crypto_alt_24h` score `2.0803` n `59` status `ready` deltaP `20.4832` edge `0.4236` maxDD `-19.4761`
- `news_risk_high->crypto_major_24h` score `1.4552` n `59` status `ready` deltaP `14.1743` edge `0.4651` maxDD `-30.7329`
- `news_risk_high->equity_24h` score `1.1978` n `59` status `ready` deltaP `6.353` edge `0.3042` maxDD `-15.4056`
- `risk_on_high->crypto_major_24h` score `0.7936` n `107` status `ready` deltaP `20.5104` edge `0.8394` maxDD `-56.9519`
- `risk_on_and_context->crypto_major_24h` score `0.7936` n `107` status `ready` deltaP `20.5104` edge `0.8394` maxDD `-56.9519`
- `market_context_high->crypto_alt_24h` score `0.6128` n `141` status `ready` deltaP `15.6509` edge `0.7241` maxDD `-46.3234`
- `market_context_high->crypto_major_24h` score `0.4393` n `141` status `ready` deltaP `22.6248` edge `0.8519` maxDD `-61.3797`
- `news_risk_high->commodity_4h` score `0.266` n `67` status `ready` deltaP `5.6425` edge `0.0324` maxDD `-0.8733`
- `risk_on_high->metal_1h` score `0.0393` n `133` status `ready` deltaP `11.0655` edge `0.0025` maxDD `-1.699`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

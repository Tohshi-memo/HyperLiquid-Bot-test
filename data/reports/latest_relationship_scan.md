# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-03T11:37:28.568285+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11584`

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

- `risk_on_high->unknown_4h` score `36.1834` n `133` status `ready` deltaP `12.9619` edge `2.9907` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `36.1834` n `133` status `ready` deltaP `12.9619` edge `2.9907` maxDD `-2.2797`
- `market_context_high->unknown_4h` score `28.9253` n `164` status `ready` deltaP `12.9573` edge `2.3936` maxDD `-2.563`
- `risk_on_high->unknown_1h` score `19.7138` n `133` status `ready` deltaP `2.6889` edge `1.6826` maxDD `-1.95`
- `risk_on_and_context->unknown_1h` score `19.7138` n `133` status `ready` deltaP `2.6889` edge `1.6826` maxDD `-1.95`
- `market_context_high->unknown_1h` score `14.0883` n `173` status `ready` deltaP `1.4372` edge `1.2275` maxDD `-2.0446`
- `risk_on_high->equity_24h` score `3.6366` n `107` status `ready` deltaP `19.0145` edge `0.5908` maxDD `-19.828`
- `risk_on_and_context->equity_24h` score `3.6366` n `107` status `ready` deltaP `19.0145` edge `0.5908` maxDD `-19.828`
- `market_context_high->equity_24h` score `3.362` n `133` status `ready` deltaP `20.8555` edge `0.5757` maxDD `-20.7654`
- `news_risk_high->crypto_alt_24h` score `2.5843` n `62` status `ready` deltaP `20.8165` edge `0.486` maxDD `-19.4761`
- `risk_on_high->crypto_alt_24h` score `1.7282` n `107` status `ready` deltaP `19.1735` edge `0.7841` maxDD `-42.8959`
- `risk_on_and_context->crypto_alt_24h` score `1.7282` n `107` status `ready` deltaP `19.1735` edge `0.7841` maxDD `-42.8959`
- `news_risk_high->crypto_major_24h` score `1.6649` n `62` status `ready` deltaP `15.7762` edge `0.5466` maxDD `-30.7329`
- `news_risk_high->equity_24h` score `1.271` n `62` status `ready` deltaP `7.5885` edge `0.3591` maxDD `-15.4056`
- `market_context_high->crypto_alt_24h` score `1.0061` n `133` status `ready` deltaP `17.8454` edge `0.7599` maxDD `-46.3234`
- `risk_on_high->crypto_major_24h` score `0.4977` n `107` status `ready` deltaP `19.816` edge `0.8061` maxDD `-56.9519`
- `risk_on_and_context->crypto_major_24h` score `0.4977` n `107` status `ready` deltaP `19.816` edge `0.8061` maxDD `-56.9519`
- `market_context_high->crypto_major_24h` score `0.4828` n `133` status `ready` deltaP `22.5916` edge `0.8577` maxDD `-61.3797`
- `news_risk_high->commodity_4h` score `0.2457` n `67` status `ready` deltaP `5.6425` edge `0.0298` maxDD `-0.8733`
- `risk_on_high->metal_1h` score `0.0782` n `133` status `ready` deltaP `11.6643` edge `0.0035` maxDD `-1.699`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

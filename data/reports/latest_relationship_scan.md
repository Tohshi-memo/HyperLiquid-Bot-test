# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-03T13:22:28.364940+00:00`
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

- `risk_on_high->unknown_4h` score `35.985` n `133` status `ready` deltaP `12.657` edge `2.9762` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `35.985` n `133` status `ready` deltaP `12.657` edge `2.9762` maxDD `-2.2797`
- `market_context_high->unknown_4h` score `29.2669` n `165` status `ready` deltaP `14.0013` edge `2.4151` maxDD `-2.563`
- `risk_on_high->unknown_1h` score `18.9964` n `133` status `ready` deltaP `1.7907` edge `1.6288` maxDD `-1.95`
- `risk_on_and_context->unknown_1h` score `18.9964` n `133` status `ready` deltaP `1.7907` edge `1.6288` maxDD `-1.95`
- `market_context_high->unknown_1h` score `14.5166` n `167` status `ready` deltaP `2.2455` edge `1.2578` maxDD `-2.0446`
- `market_context_high->equity_24h` score `3.7114` n `127` status `ready` deltaP `22.553` edge `0.5935` maxDD `-20.7654`
- `risk_on_high->equity_24h` score `3.2285` n `107` status `ready` deltaP `17.7992` edge `0.5649` maxDD `-19.828`
- `risk_on_and_context->equity_24h` score `3.2285` n `107` status `ready` deltaP `17.7992` edge `0.5649` maxDD `-19.828`
- `news_risk_high->crypto_alt_24h` score `3.04` n `65` status `ready` deltaP `21.1645` edge `0.5421` maxDD `-19.4761`
- `news_risk_high->crypto_major_24h` score `2.3229` n `65` status `ready` deltaP `17.1662` edge `0.6217` maxDD `-30.7329`
- `news_risk_high->equity_24h` score `1.5649` n `65` status `ready` deltaP `8.7553` edge `0.389` maxDD `-15.4056`
- `risk_on_high->crypto_alt_24h` score `1.4169` n `107` status `ready` deltaP `17.9582` edge `0.7523` maxDD `-42.8959`
- `risk_on_and_context->crypto_alt_24h` score `1.4169` n `107` status `ready` deltaP `17.9582` edge `0.7523` maxDD `-42.8959`
- `market_context_high->crypto_alt_24h` score `1.1379` n `127` status `ready` deltaP `19.6139` edge `0.765` maxDD `-46.3234`
- `market_context_high->crypto_major_24h` score `0.2873` n `127` status `ready` deltaP `22.4478` edge `0.8336` maxDD `-61.3797`
- `risk_on_high->crypto_major_24h` score `0.2409` n `107` status `ready` deltaP `19.1216` edge `0.7778` maxDD `-56.9519`
- `risk_on_and_context->crypto_major_24h` score `0.2409` n `107` status `ready` deltaP `19.1216` edge `0.7778` maxDD `-56.9519`
- `news_risk_high->commodity_4h` score `0.2206` n `67` status `ready` deltaP `5.4901` edge `0.0276` maxDD `-0.8733`
- `news_risk_high->fx_4h` score `0.0263` n `67` status `ready` deltaP `9.499` edge `0.0045` maxDD `-1.2507`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

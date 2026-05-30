# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-30T16:22:17.983679+00:00`
- Price records: `672`
- Market context records: `2367`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9188`

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

- `news_risk_high->crypto_alt_24h` score `21.7957` n `43` status `ready` deltaP `50.0363` edge `1.5416` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `17.6939` n `43` status `ready` deltaP `47.1536` edge `1.2041` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `15.0247` n `43` status `ready` deltaP `29.7925` edge `1.0849` maxDD `-2.1831`
- `news_risk_high->crypto_major_24h` score `11.6894` n `43` status `ready` deltaP `19.7674` edge `0.9004` maxDD `-3.3119`
- `market_context_high->crypto_major_24h` score `8.3577` n `140` status `ready` deltaP `20.0` edge `0.9524` maxDD `-25.1408`
- `news_risk_high->unknown_24h` score `7.9804` n `43` status `ready` deltaP `27.8141` edge `0.5022` maxDD `-1.4744`
- `market_context_high->unknown_24h` score `5.9872` n `140` status `ready` deltaP `23.8939` edge `0.3808` maxDD `-1.626`
- `market_context_high->crypto_major_4h` score `5.8456` n `150` status `ready` deltaP `24.4553` edge `0.5051` maxDD `-10.1468`
- `news_risk_high->index_24h` score `5.1964` n `43` status `ready` deltaP `13.0976` edge `0.3876` maxDD `-1.3507`
- `market_context_high->crypto_alt_4h` score `5.1715` n `150` status `ready` deltaP `19.7338` edge `0.5673` maxDD `-15.4319`
- `market_context_high->unknown_4h` score `5.0997` n `150` status `ready` deltaP `21.2765` edge `0.3441` maxDD `-1.8773`
- `news_risk_high->commodity_4h` score `3.7669` n `43` status `ready` deltaP `32.0051` edge `0.3367` maxDD `-3.0367`
- `news_risk_high->fx_24h` score `3.4368` n `43` status `ready` deltaP `36.5351` edge `0.0613` maxDD `-0.1442`
- `news_risk_high->fx_4h` score `1.9345` n `43` status `ready` deltaP `24.8404` edge `0.014` maxDD `-0.1382`
- `market_context_high->index_4h` score `1.7923` n `150` status `ready` deltaP `19.3862` edge `0.1027` maxDD `-2.2732`
- `market_context_high->crypto_major_1h` score `1.7352` n `157` status `ready` deltaP `14.5219` edge `0.1672` maxDD `-4.2199`
- `market_context_high->index_24h` score `1.7261` n `140` status `ready` deltaP `12.5992` edge `0.1116` maxDD `-1.4737`
- `market_context_high->crypto_alt_1h` score `1.5112` n `157` status `ready` deltaP `11.2609` edge `0.1696` maxDD `-6.1656`
- `market_context_high->equity_24h` score `1.1696` n `140` status `ready` deltaP `19.9752` edge `0.117` maxDD `-6.8828`
- `news_risk_high->unknown_4h` score `0.9326` n `43` status `ready` deltaP `13.4005` edge `0.0607` maxDD `-2.7857`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

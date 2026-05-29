# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-29T19:07:19.790967+00:00`
- Price records: `672`
- Market context records: `2272`
- Flow alert records: `8435`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9287`

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

- `news_risk_high->crypto_alt_24h` score `21.113` n `43` status `ready` deltaP `51.2516` edge `1.4766` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `15.683` n `43` status `ready` deltaP `41.7716` edge `1.0724` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `14.1863` n `43` status `ready` deltaP `31.7022` edge `1.0023` maxDD `-2.1831`
- `news_risk_high->crypto_major_24h` score `10.9842` n `43` status `ready` deltaP `21.6771` edge `0.8289` maxDD `-3.3119`
- `market_context_high->crypto_alt_4h` score `8.8227` n `154` status `ready` deltaP `27.7241` edge `0.8183` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `8.4565` n `154` status `ready` deltaP `32.5071` edge `0.669` maxDD `-10.1468`
- `market_context_high->unknown_24h` score `8.413` n `115` status `ready` deltaP `27.9362` edge `0.556` maxDD `-1.626`
- `news_risk_high->unknown_24h` score `7.9765` n `43` status `ready` deltaP `31.9807` edge `0.4741` maxDD `-1.4744`
- `market_context_high->unknown_4h` score `5.6652` n `154` status `ready` deltaP `22.6144` edge `0.3823` maxDD `-1.8773`
- `market_context_high->crypto_major_24h` score `5.4181` n `115` status `ready` deltaP `15.388` edge `0.9813` maxDD `-25.1408`
- `news_risk_high->index_24h` score `3.7759` n `43` status `ready` deltaP `12.5767` edge `0.2727` maxDD `-1.3507`
- `news_risk_high->commodity_4h` score `3.7513` n `43` status `ready` deltaP `32.0051` edge `0.3347` maxDD `-3.0367`
- `news_risk_high->fx_24h` score `3.6123` n `43` status `ready` deltaP `37.2295` edge `0.0713` maxDD `-0.1442`
- `market_context_high->index_24h` score `3.3863` n `115` status `ready` deltaP `14.3765` edge `0.2381` maxDD `-1.4737`
- `news_risk_high->commodity_24h` score `3.2963` n `43` status `ready` deltaP `3.0725` edge `0.3359` maxDD `-3.202`
- `market_context_high->index_4h` score `2.6057` n `154` status `ready` deltaP `24.3487` edge `0.1374` maxDD `-2.2732`
- `market_context_high->equity_4h` score `2.4463` n `154` status `ready` deltaP `18.9004` edge `0.2183` maxDD `-5.9024`
- `market_context_high->crypto_alt_1h` score `2.3161` n `159` status `ready` deltaP `13.8214` edge `0.2196` maxDD `-6.1656`
- `news_risk_high->fx_4h` score `2.0601` n `43` status `ready` deltaP `26.3648` edge `0.0143` maxDD `-0.1382`
- `market_context_high->crypto_major_1h` score `1.9923` n `159` status `ready` deltaP `13.8214` edge `0.1933` maxDD `-4.2199`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

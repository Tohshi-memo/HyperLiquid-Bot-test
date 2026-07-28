# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-28T17:07:39.837865+00:00`
- Price records: `672`
- Market context records: `8217`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5920`

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

- `news_risk_high->unknown_24h` score `7957.5471` n `43` status `ready` deltaP `36.9792` edge `662.8824` maxDD `0.0`
- `market_context_high->equity_24h` score `21.4873` n `30` status `ready` deltaP `38.0902` edge `1.6277` maxDD `-4.9489`
- `market_context_high->crypto_major_24h` score `18.2977` n `30` status `ready` deltaP `36.875` edge `1.3684` maxDD `-4.8208`
- `market_context_high->crypto_alt_24h` score `17.0725` n `30` status `ready` deltaP `37.3958` edge `1.2404` maxDD `-3.0264`
- `market_context_high->equity_4h` score `8.9729` n `30` status `ready` deltaP `47.7338` edge `0.4338` maxDD `-0.0094`
- `market_context_high->metal_24h` score `8.0927` n `30` status `ready` deltaP `45.7986` edge `0.3792` maxDD `-0.4771`
- `news_risk_high->equity_4h` score `7.4478` n `54` status `ready` deltaP `26.993` edge `0.5004` maxDD `-3.4427`
- `market_context_high->crypto_major_4h` score `6.7751` n `30` status `ready` deltaP `29.7155` edge `0.3844` maxDD `-0.433`
- `market_context_high->index_24h` score `5.8487` n `30` status `ready` deltaP `37.743` edge `0.2751` maxDD `-0.8132`
- `market_context_high->crypto_alt_4h` score `4.9892` n `30` status `ready` deltaP `23.5061` edge `0.2793` maxDD `-0.6195`
- `market_context_high->metal_4h` score `3.8649` n `30` status `ready` deltaP `37.7134` edge `0.0837` maxDD `-0.0438`
- `market_context_high->index_4h` score `3.5999` n `30` status `ready` deltaP `36.3415` edge `0.062` maxDD `-0.0092`
- `news_risk_high->equity_1h` score `3.1708` n `54` status `ready` deltaP `22.8765` edge `0.1426` maxDD `-1.1366`
- `market_context_high->fx_24h` score `2.7344` n `30` status `ready` deltaP `45.3819` edge `0.0811` maxDD `-0.3134`
- `news_risk_high->index_4h` score `2.6603` n `54` status `ready` deltaP `22.2674` edge `0.0923` maxDD `-0.191`
- `news_risk_high->crypto_major_4h` score `2.4709` n `54` status `ready` deltaP `12.3081` edge `0.3041` maxDD `-2.8833`
- `news_risk_high->crypto_major_1h` score `1.8162` n `54` status `ready` deltaP `12.7024` edge `0.1064` maxDD `-1.1783`
- `news_risk_high->crypto_alt_1h` score `1.7619` n `54` status `ready` deltaP `14.5542` edge `0.0932` maxDD `-1.1388`
- `market_context_high->equity_1h` score `1.7356` n `30` status `ready` deltaP `8.8024` edge `0.1006` maxDD `-0.1718`
- `market_context_high->crypto_major_1h` score `1.3871` n `30` status `ready` deltaP `13.4431` edge `0.0455` maxDD `-0.5626`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

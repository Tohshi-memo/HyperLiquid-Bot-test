# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-28T08:22:29.560818+00:00`
- Price records: `672`
- Market context records: `8178`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5904`

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

- `news_risk_high->unknown_24h` score `8732.9619` n `42` status `ready` deltaP `36.9792` edge `727.5003` maxDD `0.0`
- `market_context_high->equity_24h` score `19.0969` n `53` status `ready` deltaP `43.7599` edge `1.3907` maxDD `-4.9489`
- `market_context_high->equity_4h` score `9.4229` n `54` status `ready` deltaP `37.9968` edge `0.5554` maxDD `-0.5442`
- `news_risk_high->equity_4h` score `8.4455` n `46` status `ready` deltaP `32.0387` edge `0.5192` maxDD `-1.3202`
- `market_context_high->metal_24h` score `8.296` n `53` status `ready` deltaP `43.0556` edge `0.4043` maxDD `0.0`
- `market_context_high->index_4h` score `4.0928` n `54` status `ready` deltaP `36.9524` edge `0.099` maxDD `-0.0092`
- `news_risk_high->equity_1h` score `3.4263` n `50` status `ready` deltaP `25.6048` edge `0.1457` maxDD `-1.1366`
- `news_risk_high->crypto_major_4h` score `3.3906` n `46` status `ready` deltaP `18.8759` edge `0.3694` maxDD `-2.1767`
- `market_context_high->equity_1h` score `3.2618` n `54` status `ready` deltaP `17.9752` edge `0.1723` maxDD `-0.6254`
- `news_risk_high->index_4h` score `2.7306` n `46` status `ready` deltaP `22.6207` edge `0.0958` maxDD `-0.191`
- `market_context_high->crypto_alt_24h` score `2.2288` n `53` status `ready` deltaP `5.5719` edge `0.6052` maxDD `-18.1946`
- `market_context_high->metal_4h` score `2.0446` n `54` status `ready` deltaP `23.0296` edge `0.0633` maxDD `-0.7159`
- `market_context_high->index_1h` score `1.9764` n `54` status `ready` deltaP `22.821` edge `0.0264` maxDD `-0.1069`
- `news_risk_high->crypto_major_1h` score `1.8798` n `50` status `ready` deltaP `11.8922` edge `0.1171` maxDD `-1.1783`
- `market_context_high->index_24h` score `1.8632` n `53` status `ready` deltaP `16.1983` edge `0.1978` maxDD `-1.3533`
- `news_risk_high->metal_4h` score `1.7848` n `46` status `ready` deltaP `16.6689` edge `0.0844` maxDD `-0.7433`
- `news_risk_high->crypto_alt_1h` score `1.6257` n `50` status `ready` deltaP `12.1916` edge `0.0976` maxDD `-1.1388`
- `news_risk_high->crypto_alt_4h` score `1.3483` n `46` status `ready` deltaP `15.2903` edge `0.2101` maxDD `-5.8012`
- `market_context_high->fx_24h` score `0.8845` n `53` status `ready` deltaP `18.6976` edge `0.0549` maxDD `-0.626`
- `news_risk_high->index_1h` score `0.6224` n `50` status `ready` deltaP `8.5988` edge `0.0234` maxDD `-0.3089`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

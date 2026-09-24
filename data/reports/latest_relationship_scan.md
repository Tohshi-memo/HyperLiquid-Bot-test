# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-24T05:22:31.942836+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9858`

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

- `market_context_high->unknown_1h` score `72.165` n `47` status `ready` deltaP `10.8645` edge `5.9484` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `38.5464` n `46` status `ready` deltaP `25.8605` edge `3.0554` maxDD `-0.5817`
- `market_context_high->crypto_alt_24h` score `23.3075` n `46` status `ready` deltaP `20.8333` edge `1.8034` maxDD `0.0`
- `market_context_high->equity_24h` score `22.2586` n `46` status `ready` deltaP `23.2564` edge `1.7099` maxDD `-0.1382`
- `market_context_high->index_24h` score `7.4342` n `46` status `ready` deltaP `32.2841` edge `0.413` maxDD `-0.03`
- `news_risk_high->crypto_alt_4h` score `4.9551` n `103` status `ready` deltaP `14.6889` edge `0.4148` maxDD `-5.9838`
- `news_risk_high->crypto_major_4h` score `4.8219` n `103` status `ready` deltaP `18.8048` edge `0.3342` maxDD `-2.619`
- `news_risk_high->crypto_major_24h` score `4.8052` n `103` status `ready` deltaP `-1.8305` edge `1.3169` maxDD `-63.6743`
- `market_context_high->index_4h` score `2.628` n `47` status `ready` deltaP `30.8251` edge `0.0289` maxDD `-0.2323`
- `news_risk_high->crypto_alt_1h` score `2.5808` n `103` status `ready` deltaP `14.0559` edge `0.1704` maxDD `-1.5895`
- `market_context_high->metal_24h` score `2.5666` n `46` status `ready` deltaP `26.2606` edge `0.0622` maxDD `-0.2042`
- `news_risk_high->commodity_24h` score `2.1835` n `103` status `ready` deltaP `22.0115` edge `0.1531` maxDD `-2.431`
- `news_risk_high->crypto_major_1h` score `2.0672` n `103` status `ready` deltaP `16.1517` edge `0.1081` maxDD `-1.8141`
- `market_context_high->equity_4h` score `1.7642` n `47` status `ready` deltaP `13.6384` edge `0.0979` maxDD `-1.3444`
- `news_risk_high->fx_4h` score `1.6002` n `103` status `ready` deltaP `23.3765` edge `0.0411` maxDD `-0.421`
- `news_risk_high->fx_24h` score `1.2273` n `103` status `ready` deltaP `29.6639` edge `0.1227` maxDD `-1.7159`
- `news_risk_high->crypto_alt_24h` score `1.0454` n `103` status `ready` deltaP `-4.4094` edge `0.8178` maxDD `-49.7699`
- `market_context_high->index_1h` score `0.8289` n `47` status `ready` deltaP `13.2628` edge `0.0085` maxDD `-0.2275`
- `news_risk_high->metal_1h` score `0.6661` n `103` status `ready` deltaP `15.502` edge `0.0115` maxDD `-0.7468`
- `market_context_high->equity_1h` score `0.6502` n `47` status `ready` deltaP `9.3706` edge `0.032` maxDD `-1.5564`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-01T06:37:32.783108+00:00`
- Price records: `672`
- Market context records: `8594`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5898`

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

- `news_risk_high->unknown_24h` score `4749.3562` n `64` status `ready` deltaP `35.5903` edge `395.5845` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `5.8536` n `64` status `ready` deltaP `20.6555` edge `0.4098` maxDD `-3.4427`
- `news_risk_high->index_4h` score `2.2018` n `64` status `ready` deltaP `18.6357` edge `0.0783` maxDD `-0.191`
- `news_risk_high->equity_1h` score `1.8224` n `64` status `ready` deltaP `17.1501` edge `0.0852` maxDD `-2.4803`
- `market_context_high->crypto_alt_4h` score `1.5185` n `62` status `ready` deltaP `11.2264` edge `0.1474` maxDD `-5.323`
- `news_risk_high->crypto_major_4h` score `0.991` n `64` status `ready` deltaP `6.2881` edge `0.1627` maxDD `-3.5385`
- `news_risk_high->crypto_alt_1h` score `0.4087` n `64` status `ready` deltaP `7.8125` edge `0.053` maxDD `-1.8813`
- `news_risk_high->crypto_alt_4h` score `0.396` n `64` status `ready` deltaP `10.8232` edge `0.1178` maxDD `-5.8012`
- `news_risk_high->crypto_major_1h` score `0.3703` n `64` status `ready` deltaP `7.2137` edge `0.0506` maxDD `-2.0972`
- `news_risk_high->fx_4h` score `0.0984` n `64` status `ready` deltaP `12.2332` edge `0.0224` maxDD `-0.6604`
- `news_risk_high->fx_1h` score `0.0971` n `64` status `ready` deltaP `5.436` edge `0.0043` maxDD `-0.2475`
- `news_risk_high->index_1h` score `0.0504` n `64` status `ready` deltaP `4.3694` edge `0.009` maxDD `-0.5338`
- `news_risk_high->metal_4h` score `0.0483` n `64` status `ready` deltaP `3.2393` edge `0.0322` maxDD `-0.8085`
- `market_context_high->fx_4h` score `-0.0699` n `62` status `ready` deltaP `9.0578` edge `0.0134` maxDD `-1.3685`
- `news_risk_high->metal_1h` score `-0.1455` n `64` status `ready` deltaP `3.1063` edge `0.0075` maxDD `-0.5599`
- `market_context_high->fx_1h` score `-0.2677` n `62` status `ready` deltaP `2.3614` edge `0.0002` maxDD `-0.6874`
- `market_context_high->commodity_1h` score `-0.3044` n `62` status `ready` deltaP `4.3075` edge `-0.0052` maxDD `-2.0038`
- `market_context_high->crypto_alt_1h` score `-0.5681` n `62` status `ready` deltaP `-3.2258` edge `0.0114` maxDD `-3.0178`
- `market_context_high->index_1h` score `-0.7058` n `62` status `ready` deltaP `1.3956` edge `-0.0152` maxDD `-1.5667`
- `market_context_high->metal_1h` score `-0.9865` n `62` status `ready` deltaP `-3.1437` edge `-0.0118` maxDD `-1.6224`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-31T16:22:26.300785+00:00`
- Price records: `672`
- Market context records: `8530`
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

- `news_risk_high->unknown_24h` score `6279.9725` n `52` status `ready` deltaP `44.0438` edge `523.0795` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `5.7788` n `64` status `ready` deltaP `21.2652` edge `0.3995` maxDD `-3.4427`
- `news_risk_high->index_4h` score `2.0543` n `64` status `ready` deltaP `16.8064` edge `0.0782` maxDD `-0.191`
- `news_risk_high->equity_1h` score `1.8489` n `64` status `ready` deltaP `16.5513` edge `0.0914` maxDD `-2.4803`
- `news_risk_high->crypto_major_4h` score `0.9592` n `64` status `ready` deltaP `6.4405` edge `0.1576` maxDD `-3.5385`
- `news_risk_high->crypto_alt_4h` score `0.8339` n `64` status `ready` deltaP `14.939` edge `0.1465` maxDD `-5.8012`
- `news_risk_high->crypto_alt_1h` score `0.51` n `64` status `ready` deltaP `8.8604` edge `0.059` maxDD `-1.8813`
- `market_context_high->crypto_alt_4h` score `0.4012` n `46` status `ready` deltaP `6.7868` edge `0.1019` maxDD `-5.323`
- `news_risk_high->crypto_major_1h` score `0.34` n `64` status `ready` deltaP `6.6149` edge `0.0507` maxDD `-2.0972`
- `news_risk_high->fx_1h` score `0.1056` n `64` status `ready` deltaP `5.5857` edge `0.0044` maxDD `-0.2475`
- `news_risk_high->metal_4h` score `0.0644` n `64` status `ready` deltaP `2.9345` edge `0.0363` maxDD `-0.8085`
- `news_risk_high->index_1h` score `0.0582` n `64` status `ready` deltaP `4.3694` edge `0.01` maxDD `-0.5338`
- `news_risk_high->fx_4h` score `0.0338` n `64` status `ready` deltaP `11.471` edge `0.0221` maxDD `-0.6604`
- `news_risk_high->metal_1h` score `-0.082` n `64` status `ready` deltaP `3.7051` edge `0.0088` maxDD `-0.5599`
- `market_context_high->commodity_1h` score `-0.4218` n `58` status `ready` deltaP `2.2455` edge `-0.0065` maxDD `-2.0038`
- `market_context_high->fx_1h` score `-0.4545` n `58` status `ready` deltaP `-0.8259` edge `-0.0025` maxDD `-0.6874`
- `market_context_high->metal_1h` score `-0.5064` n `58` status `ready` deltaP `-0.8208` edge `-0.01` maxDD `-1.6224`
- `market_context_high->crypto_alt_1h` score `-0.7458` n `58` status `ready` deltaP `-5.8487` edge `0.0061` maxDD `-3.0178`
- `market_context_high->commodity_4h` score `-0.8366` n `46` status `ready` deltaP `3.6917` edge `0.0196` maxDD `-5.4508`
- `market_context_high->index_1h` score `-1.0341` n `58` status `ready` deltaP `-1.719` edge `-0.0218` maxDD `-1.5667`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-27T06:52:16.978784+00:00`
- Price records: `672`
- Market context records: `2018`
- Flow alert records: `7701`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9085`

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

- `market_context_high->crypto_major_4h` score `8.9075` n `205` status `ready` deltaP `30.7927` edge `0.59` maxDD `-1.9063`
- `market_context_high->crypto_alt_4h` score `8.3838` n `205` status `ready` deltaP `24.5427` edge `0.6495` maxDD `-5.1574`
- `market_context_high->unknown_4h` score `5.9169` n `205` status `ready` deltaP `18.689` edge `0.4434` maxDD `-2.6599`
- `market_context_high->equity_4h` score `2.8851` n `205` status `ready` deltaP `16.6463` edge `0.2389` maxDD `-5.0894`
- `market_context_high->crypto_major_1h` score `1.4685` n `205` status `ready` deltaP `12.0286` edge `0.1408` maxDD `-3.2225`
- `market_context_high->index_4h` score `1.3024` n `205` status `ready` deltaP `12.1647` edge `0.0958` maxDD `-1.8022`
- `market_context_high->crypto_alt_1h` score `1.1586` n `205` status `ready` deltaP `9.6334` edge `0.1437` maxDD `-4.9097`
- `market_context_high->equity_1h` score `0.2056` n `205` status `ready` deltaP `6.9104` edge `0.0499` maxDD `-2.6402`
- `market_context_high->unknown_24h` score `0.1719` n `188` status `ready` deltaP `15.9101` edge `0.4403` maxDD `-35.8966`
- `market_context_high->equity_24h` score `0.0521` n `188` status `ready` deltaP `14.7734` edge `0.3957` maxDD `-33.1875`
- `market_context_high->metal_24h` score `0.0493` n `188` status `ready` deltaP `12.0919` edge `0.1661` maxDD `-12.7414`
- `market_context_high->unknown_1h` score `0.023` n `205` status `ready` deltaP `3.7462` edge `0.0489` maxDD `-3.0902`
- `market_context_high->index_24h` score `-0.1997` n `188` status `ready` deltaP `3.0749` edge `0.0857` maxDD `-4.1604`
- `market_context_high->fx_24h` score `-0.2376` n `188` status `ready` deltaP `12.9336` edge `0.0255` maxDD `-2.1887`
- `market_context_high->index_1h` score `-0.3445` n `205` status `ready` deltaP `2.1046` edge `0.0163` maxDD `-1.3898`
- `market_context_high->fx_1h` score `-0.8374` n `205` status `ready` deltaP `-1.1421` edge `0.0006` maxDD `-0.3548`
- `market_context_high->metal_1h` score `-1.0085` n `205` status `ready` deltaP `2.91` edge `0.0153` maxDD `-5.166`
- `market_context_high->fx_4h` score `-1.5112` n `205` status `ready` deltaP `-5.5183` edge `-0.001` maxDD `-1.0513`
- `market_context_high->metal_4h` score `-1.607` n `205` status `ready` deltaP `7.0427` edge `0.0814` maxDD `-11.9812`
- `market_context_high->commodity_1h` score `-1.8395` n `205` status `ready` deltaP `2.9049` edge `0.0006` maxDD `-15.7972`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

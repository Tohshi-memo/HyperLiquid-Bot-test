# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-27T07:52:17.732344+00:00`
- Price records: `672`
- Market context records: `2022`
- Flow alert records: `7713`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9091`

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

- `market_context_high->crypto_major_4h` score `8.9243` n `205` status `ready` deltaP `30.7927` edge `0.5914` maxDD `-1.9063`
- `market_context_high->crypto_alt_4h` score `8.427` n `205` status `ready` deltaP `24.5427` edge `0.6531` maxDD `-5.1574`
- `market_context_high->unknown_4h` score `5.9157` n `205` status `ready` deltaP `18.689` edge `0.4433` maxDD `-2.6599`
- `market_context_high->equity_4h` score `2.9987` n `205` status `ready` deltaP `17.2561` edge `0.2443` maxDD `-5.0894`
- `market_context_high->crypto_major_1h` score `1.5045` n `205` status `ready` deltaP `12.1783` edge `0.1428` maxDD `-3.2225`
- `market_context_high->index_4h` score `1.3992` n `205` status `ready` deltaP `12.7744` edge `0.0998` maxDD `-1.8022`
- `market_context_high->crypto_alt_1h` score `1.2162` n `205` status `ready` deltaP `9.7831` edge `0.1475` maxDD `-4.9097`
- `market_context_high->unknown_24h` score `0.4112` n `192` status `ready` deltaP `16.2314` edge `0.4581` maxDD `-35.8966`
- `market_context_high->equity_24h` score `0.2056` n `192` status `ready` deltaP `15.1612` edge `0.4059` maxDD `-33.1875`
- `market_context_high->equity_1h` score `0.2032` n `205` status `ready` deltaP `6.9104` edge `0.0497` maxDD `-2.6402`
- `market_context_high->unknown_1h` score `0.0302` n `205` status `ready` deltaP `3.7462` edge `0.0495` maxDD `-3.0902`
- `market_context_high->index_24h` score `-0.028` n `192` status `ready` deltaP `3.496` edge `0.0972` maxDD `-4.1604`
- `market_context_high->fx_24h` score `-0.2635` n `192` status `ready` deltaP `12.6997` edge `0.0249` maxDD `-2.1887`
- `market_context_high->index_1h` score `-0.3253` n `205` status `ready` deltaP `2.2543` edge `0.0169` maxDD `-1.3898`
- `market_context_high->metal_24h` score `-0.5312` n `192` status `ready` deltaP `11.3585` edge `0.1569` maxDD `-15.4843`
- `market_context_high->fx_1h` score `-0.8757` n `205` status `ready` deltaP `-1.5912` edge `0.0004` maxDD `-0.3548`
- `market_context_high->metal_1h` score `-0.921` n `205` status `ready` deltaP `3.5088` edge `0.0186` maxDD `-5.166`
- `market_context_high->metal_4h` score `-1.419` n `205` status `ready` deltaP `7.6525` edge `0.093` maxDD `-11.9812`
- `market_context_high->fx_4h` score `-1.5683` n `205` status `ready` deltaP `-6.1281` edge `-0.0017` maxDD `-1.0513`
- `market_context_high->commodity_1h` score `-1.8153` n `205` status `ready` deltaP `3.2043` edge `0.0017` maxDD `-15.7972`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

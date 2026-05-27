# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-27T18:37:21.881578+00:00`
- Price records: `672`
- Market context records: `2065`
- Flow alert records: `7839`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9145`

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

- `market_context_high->crypto_major_4h` score `9.6171` n `206` status `ready` deltaP `33.8725` edge `0.6286` maxDD `-1.9063`
- `market_context_high->crypto_alt_4h` score `8.961` n `206` status `ready` deltaP `26.2979` edge `0.6859` maxDD `-5.1574`
- `market_context_high->unknown_4h` score `6.5421` n `206` status `ready` deltaP `21.223` edge `0.4786` maxDD `-2.6599`
- `market_context_high->unknown_24h` score `5.3347` n `205` status `ready` deltaP `19.2447` edge `0.8483` maxDD `-35.8966`
- `market_context_high->equity_4h` score `3.5537` n `206` status `ready` deltaP `19.4545` edge `0.2759` maxDD `-5.0894`
- `market_context_high->index_4h` score `2.0522` n `206` status `ready` deltaP `15.4467` edge `0.1364` maxDD `-1.8022`
- `market_context_high->crypto_major_1h` score `1.8618` n `206` status `ready` deltaP `14.3044` edge `0.1584` maxDD `-3.2225`
- `market_context_high->equity_24h` score `1.6106` n `205` status `ready` deltaP `20.124` edge `0.4899` maxDD `-33.1875`
- `market_context_high->crypto_alt_1h` score `1.5112` n `206` status `ready` deltaP `11.1607` edge `0.1629` maxDD `-4.9097`
- `market_context_high->index_24h` score `1.3676` n `205` status `ready` deltaP `8.626` edge `0.1793` maxDD `-4.1604`
- `market_context_high->equity_1h` score `0.4585` n `206` status `ready` deltaP `8.4211` edge `0.0609` maxDD `-2.6402`
- `market_context_high->unknown_1h` score `0.3755` n `206` status `ready` deltaP `5.4081` edge `0.0672` maxDD `-3.0902`
- `market_context_high->crypto_major_24h` score `0.2592` n `205` status `ready` deltaP `20.3376` edge `0.7446` maxDD `-62.3533`
- `market_context_high->index_1h` score `-0.0492` n `206` status `ready` deltaP `4.3559` edge `0.0259` maxDD `-1.3898`
- `market_context_high->fx_24h` score `-0.2821` n `205` status `ready` deltaP `13.5446` edge `0.0255` maxDD `-2.811`
- `market_context_high->metal_4h` score `-0.5573` n `206` status `ready` deltaP `11.6741` edge `0.138` maxDD `-11.9812`
- `market_context_high->metal_1h` score `-0.7416` n `206` status `ready` deltaP `4.2963` edge `0.0283` maxDD `-5.166`
- `market_context_high->fx_1h` score `-0.7915` n `206` status `ready` deltaP `-0.5988` edge `0.0008` maxDD `-0.3548`
- `market_context_high->fx_4h` score `-1.3823` n `206` status `ready` deltaP `-4.0878` edge `0.0002` maxDD `-1.0513`
- `market_context_high->metal_24h` score `-1.9522` n `205` status `ready` deltaP `10.5359` edge `0.1572` maxDD `-23.2095`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

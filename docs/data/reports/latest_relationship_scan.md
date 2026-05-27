# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-27T10:52:20.915430+00:00`
- Price records: `672`
- Market context records: `2035`
- Flow alert records: `7750`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9105`

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

- `market_context_high->crypto_major_4h` score `8.8763` n `205` status `ready` deltaP `30.7927` edge `0.5874` maxDD `-1.9063`
- `market_context_high->crypto_alt_4h` score `8.3632` n `205` status `ready` deltaP `24.3903` edge `0.6488` maxDD `-5.1574`
- `market_context_high->unknown_4h` score `5.9101` n `205` status `ready` deltaP `18.9939` edge `0.4408` maxDD `-2.6599`
- `market_context_high->equity_4h` score `2.9891` n `205` status `ready` deltaP `17.2561` edge `0.2435` maxDD `-5.0894`
- `market_context_high->crypto_major_1h` score `1.5368` n `205` status `ready` deltaP `12.4777` edge `0.1435` maxDD `-3.2225`
- `market_context_high->index_4h` score `1.4522` n `205` status `ready` deltaP `12.9269` edge `0.1032` maxDD `-1.8022`
- `market_context_high->crypto_alt_1h` score `1.2713` n `205` status `ready` deltaP `10.0825` edge `0.1501` maxDD `-4.9097`
- `market_context_high->unknown_24h` score `1.2358` n `203` status `ready` deltaP `17.1037` edge `0.521` maxDD `-35.8966`
- `market_context_high->equity_24h` score `0.516` n `203` status `ready` deltaP `16.2063` edge `0.4248` maxDD `-33.1875`
- `market_context_high->index_24h` score `0.403` n `203` status `ready` deltaP `4.6084` edge `0.1257` maxDD `-4.1604`
- `market_context_high->equity_1h` score `0.2104` n `205` status `ready` deltaP `6.9104` edge `0.0503` maxDD `-2.6402`
- `market_context_high->unknown_1h` score `0.0361` n `205` status `ready` deltaP `3.8959` edge `0.049` maxDD `-3.0902`
- `market_context_high->index_1h` score `-0.2798` n `205` status `ready` deltaP `2.7034` edge `0.0177` maxDD `-1.3898`
- `market_context_high->fx_24h` score `-0.5639` n `203` status `ready` deltaP `10.4707` edge `0.0215` maxDD `-2.7303`
- `market_context_high->fx_1h` score `-0.8398` n `205` status `ready` deltaP `-1.1421` edge `0.0004` maxDD `-0.3548`
- `market_context_high->metal_1h` score `-0.8563` n `205` status `ready` deltaP `3.9579` edge `0.021` maxDD `-5.166`
- `market_context_high->metal_4h` score `-1.1244` n `205` status `ready` deltaP `9.0244` edge `0.1084` maxDD `-11.9812`
- `market_context_high->fx_4h` score `-1.5561` n `205` status `ready` deltaP `-5.9756` edge `-0.0017` maxDD `-1.0513`
- `market_context_high->metal_24h` score `-1.8096` n `203` status `ready` deltaP `9.7094` edge `0.133` maxDD `-20.5491`
- `market_context_high->commodity_1h` score `-1.8636` n `205` status `ready` deltaP `2.4558` edge `0.0005` maxDD `-15.7972`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

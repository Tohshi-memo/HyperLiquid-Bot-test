# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-27T09:22:22.070518+00:00`
- Price records: `672`
- Market context records: `2029`
- Flow alert records: `7731`
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

- `market_context_high->crypto_major_4h` score `8.8787` n `205` status `ready` deltaP `30.7927` edge `0.5876` maxDD `-1.9063`
- `market_context_high->crypto_alt_4h` score `8.3682` n `205` status `ready` deltaP `24.5427` edge `0.6482` maxDD `-5.1574`
- `market_context_high->unknown_4h` score `5.8591` n `205` status `ready` deltaP `18.5365` edge `0.4396` maxDD `-2.6599`
- `market_context_high->equity_4h` score `3.0263` n `205` status `ready` deltaP `17.2561` edge `0.2466` maxDD `-5.0894`
- `market_context_high->crypto_major_1h` score `1.5332` n `205` status `ready` deltaP `12.4777` edge `0.1432` maxDD `-3.2225`
- `market_context_high->index_4h` score `1.4438` n `205` status `ready` deltaP `12.9269` edge `0.1025` maxDD `-1.8022`
- `market_context_high->crypto_alt_1h` score `1.2533` n `205` status `ready` deltaP `10.0825` edge `0.1486` maxDD `-4.9097`
- `market_context_high->unknown_24h` score `0.875` n `198` status `ready` deltaP `16.6891` edge `0.4937` maxDD `-35.8966`
- `market_context_high->equity_24h` score `0.401` n `198` status `ready` deltaP `15.7136` edge `0.4185` maxDD `-33.1875`
- `market_context_high->index_24h` score `0.2252` n `198` status `ready` deltaP `4.0958` edge `0.1143` maxDD `-4.1604`
- `market_context_high->equity_1h` score `0.2068` n `205` status `ready` deltaP `6.9104` edge `0.05` maxDD `-2.6402`
- `market_context_high->unknown_1h` score `-0.0166` n `205` status `ready` deltaP `3.5965` edge `0.0466` maxDD `-3.0902`
- `market_context_high->index_1h` score `-0.3181` n `205` status `ready` deltaP `2.404` edge `0.0165` maxDD `-1.3898`
- `market_context_high->fx_24h` score `-0.4132` n `198` status `ready` deltaP `11.3913` edge `0.0233` maxDD `-2.3608`
- `market_context_high->fx_1h` score `-0.8637` n `205` status `ready` deltaP `-1.4415` edge `0.0004` maxDD `-0.3548`
- `market_context_high->metal_1h` score `-0.915` n `205` status `ready` deltaP `3.5088` edge `0.0191` maxDD `-5.166`
- `market_context_high->metal_4h` score `-1.2054` n `205` status `ready` deltaP `8.5671` edge `0.1047` maxDD `-11.9812`
- `market_context_high->metal_24h` score `-1.2654` n `198` status `ready` deltaP `10.3657` edge `0.1435` maxDD `-18.7779`
- `market_context_high->fx_4h` score `-1.6353` n `205` status `ready` deltaP `-6.8903` edge `-0.0022` maxDD `-1.0513`
- `market_context_high->commodity_1h` score `-1.7896` n `205` status `ready` deltaP `3.354` edge `0.004` maxDD `-15.7972`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

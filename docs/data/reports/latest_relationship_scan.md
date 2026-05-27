# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-27T10:07:19.501436+00:00`
- Price records: `672`
- Market context records: `2032`
- Flow alert records: `7740`
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
- `market_context_high->crypto_alt_4h` score `8.3718` n `205` status `ready` deltaP `24.5427` edge `0.6485` maxDD `-5.1574`
- `market_context_high->unknown_4h` score `5.8907` n `205` status `ready` deltaP `18.8414` edge `0.4402` maxDD `-2.6599`
- `market_context_high->equity_4h` score `3.0095` n `205` status `ready` deltaP `17.2561` edge `0.2452` maxDD `-5.0894`
- `market_context_high->crypto_major_1h` score `1.5308` n `205` status `ready` deltaP `12.4777` edge `0.143` maxDD `-3.2225`
- `market_context_high->index_4h` score `1.4522` n `205` status `ready` deltaP `12.9269` edge `0.1032` maxDD `-1.8022`
- `market_context_high->crypto_alt_1h` score `1.2821` n `205` status `ready` deltaP `10.2322` edge `0.15` maxDD `-4.9097`
- `market_context_high->unknown_24h` score `1.0077` n `201` status `ready` deltaP `16.9077` edge `0.5033` maxDD `-35.8966`
- `market_context_high->equity_24h` score `0.4533` n `201` status `ready` deltaP `15.9775` edge `0.4211` maxDD `-33.1875`
- `market_context_high->index_24h` score `0.3213` n `201` status `ready` deltaP `4.3822` edge `0.1204` maxDD `-4.1604`
- `market_context_high->equity_1h` score `0.1936` n `205` status `ready` deltaP `6.7607` edge `0.0499` maxDD `-2.6402`
- `market_context_high->unknown_1h` score `-0.0058` n `205` status `ready` deltaP `3.5965` edge `0.0475` maxDD `-3.0902`
- `market_context_high->index_1h` score `-0.2858` n `205` status `ready` deltaP `2.7034` edge `0.0172` maxDD `-1.3898`
- `market_context_high->fx_24h` score `-0.5093` n `201` status `ready` deltaP `10.7893` edge `0.0221` maxDD `-2.5846`
- `market_context_high->fx_1h` score `-0.8398` n `205` status `ready` deltaP `-1.1421` edge `0.0004` maxDD `-0.3548`
- `market_context_high->metal_1h` score `-0.9198` n `205` status `ready` deltaP `3.5088` edge `0.0187` maxDD `-5.166`
- `market_context_high->metal_4h` score `-1.1534` n `205` status `ready` deltaP `8.872` edge `0.107` maxDD `-11.9812`
- `market_context_high->metal_24h` score `-1.4567` n `201` status `ready` deltaP `9.9145` edge `0.1381` maxDD `-19.3802`
- `market_context_high->fx_4h` score `-1.5975` n `205` status `ready` deltaP `-6.4329` edge `-0.0021` maxDD `-1.0513`
- `market_context_high->commodity_1h` score `-1.82` n `205` status `ready` deltaP `2.9049` edge `0.0031` maxDD `-15.7972`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

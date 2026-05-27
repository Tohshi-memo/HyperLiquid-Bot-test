# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-27T19:22:20.082595+00:00`
- Price records: `672`
- Market context records: `2068`
- Flow alert records: `7848`
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

- `market_context_high->crypto_major_4h` score `9.6776` n `206` status `ready` deltaP `34.3298` edge `0.6306` maxDD `-1.9063`
- `market_context_high->crypto_alt_4h` score `9.0058` n `206` status `ready` deltaP `26.6028` edge `0.6876` maxDD `-5.1574`
- `market_context_high->unknown_4h` score `6.6434` n `206` status `ready` deltaP `21.6803` edge `0.484` maxDD `-2.6599`
- `market_context_high->unknown_24h` score `5.903` n `205` status `ready` deltaP `19.7637` edge `0.8922` maxDD `-35.8966`
- `market_context_high->equity_4h` score `3.5308` n `206` status `ready` deltaP `19.302` edge `0.275` maxDD `-5.0894`
- `market_context_high->index_4h` score `2.0438` n `206` status `ready` deltaP `15.4467` edge `0.1357` maxDD `-1.8022`
- `market_context_high->crypto_major_1h` score `1.827` n `206` status `ready` deltaP `14.005` edge `0.1575` maxDD `-3.2225`
- `market_context_high->equity_24h` score `1.7133` n `205` status `ready` deltaP `20.6431` edge `0.495` maxDD `-33.1875`
- `market_context_high->crypto_alt_1h` score `1.4764` n `206` status `ready` deltaP `11.011` edge `0.161` maxDD `-4.9097`
- `market_context_high->index_24h` score `1.4463` n `205` status `ready` deltaP `9.1451` edge `0.1824` maxDD `-4.1604`
- `market_context_high->crypto_major_24h` score `0.4627` n `205` status `ready` deltaP `20.8566` edge `0.7581` maxDD `-62.3533`
- `market_context_high->unknown_1h` score `0.4283` n `206` status `ready` deltaP `5.4081` edge `0.0716` maxDD `-3.0902`
- `market_context_high->equity_1h` score `0.4201` n `206` status `ready` deltaP `8.1217` edge `0.0597` maxDD `-2.6402`
- `market_context_high->index_1h` score `-0.0947` n `206` status `ready` deltaP `3.9068` edge `0.0251` maxDD `-1.3898`
- `market_context_high->fx_24h` score `-0.2785` n `205` status `ready` deltaP `13.5446` edge `0.0258` maxDD `-2.811`
- `market_context_high->metal_4h` score `-0.5621` n `206` status `ready` deltaP `11.6741` edge `0.1376` maxDD `-11.9812`
- `market_context_high->metal_1h` score `-0.7572` n `206` status `ready` deltaP `4.1466` edge `0.028` maxDD `-5.166`
- `market_context_high->fx_1h` score `-0.8155` n `206` status `ready` deltaP `-0.8982` edge `0.0008` maxDD `-0.3548`
- `market_context_high->fx_4h` score `-1.4091` n `206` status `ready` deltaP `-4.3926` edge `0.0` maxDD `-1.0513`
- `market_context_high->metal_24h` score `-1.8657` n `205` status `ready` deltaP `10.8819` edge `0.1621` maxDD `-23.2095`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

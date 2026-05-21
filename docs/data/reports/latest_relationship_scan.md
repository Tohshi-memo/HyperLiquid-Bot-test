# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-21T03:52:17.556282+00:00`
- Price records: `672`
- Market context records: `1386`
- Flow alert records: `5904`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8804`

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

- `market_context_high->crypto_major_24h` score `13.3445` n `155` status `ready` deltaP `29.1645` edge `1.0308` maxDD `-8.0553`
- `market_context_high->metal_24h` score `11.6985` n `155` status `ready` deltaP `12.6881` edge `1.057` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `11.6235` n `155` status `ready` deltaP `28.7937` edge `0.9783` maxDD `-15.1306`
- `market_context_high->index_24h` score `4.2025` n `155` status `ready` deltaP `20.4816` edge `0.3223` maxDD `-5.3574`
- `market_context_high->equity_24h` score `2.6618` n `155` status `ready` deltaP `13.6357` edge `0.3636` maxDD `-14.2815`
- `market_context_high->equity_4h` score `1.6775` n `183` status `ready` deltaP `8.5924` edge `0.1655` maxDD `-3.6396`
- `market_context_high->index_1h` score `0.0316` n `195` status `ready` deltaP `4.9263` edge `0.0163` maxDD `-1.7205`
- `market_context_high->fx_24h` score `0.0139` n `155` status `ready` deltaP `9.5351` edge `0.0425` maxDD `-1.3925`
- `market_context_high->equity_1h` score `-0.0526` n `195` status `ready` deltaP `3.1298` edge `0.0306` maxDD `-2.8014`
- `market_context_high->metal_4h` score `-0.1358` n `183` status `ready` deltaP `10.3766` edge `0.0626` maxDD `-6.4478`
- `market_context_high->fx_1h` score `-0.3484` n `195` status `ready` deltaP `2.9894` edge `-0.0024` maxDD `-0.3914`
- `market_context_high->crypto_alt_1h` score `-0.4516` n `195` status `ready` deltaP `2.2824` edge `0.0342` maxDD `-3.6309`
- `market_context_high->index_4h` score `-0.4735` n `183` status `ready` deltaP `0.8013` edge `0.0641` maxDD `-3.7119`
- `market_context_high->metal_1h` score `-0.5323` n `195` status `ready` deltaP `5.7447` edge `0.0013` maxDD `-4.2945`
- `market_context_high->commodity_1h` score `-0.8514` n `195` status `ready` deltaP `-1.2406` edge `-0.0012` maxDD `-2.252`
- `market_context_high->crypto_alt_4h` score `-1.1644` n `183` status `ready` deltaP `8.1934` edge `0.1803` maxDD `-19.5565`
- `market_context_high->crypto_major_1h` score `-1.2321` n `195` status `ready` deltaP `-0.3232` edge `0.006` maxDD `-6.1883`
- `market_context_high->crypto_major_4h` score `-1.2345` n `183` status `ready` deltaP `4.6965` edge `0.1367` maxDD `-13.3376`
- `market_context_high->fx_4h` score `-1.7921` n `183` status `ready` deltaP `-6.1175` edge `-0.0115` maxDD `-1.4313`
- `market_context_high->unknown_4h` score `-3.4566` n `183` status `ready` deltaP `4.3891` edge `-0.2453` maxDD `-11.1695`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

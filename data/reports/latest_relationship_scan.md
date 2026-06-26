# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-26T17:13:02.925578+00:00`
- Price records: `672`
- Market context records: `4848`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7616`

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

- `market_context_high->unknown_1h` score `13.4946` n `110` status `ready` deltaP `10.4709` edge `1.0965` maxDD `-1.674`
- `market_context_high->unknown_4h` score `11.4098` n `99` status `ready` deltaP `27.8163` edge `0.8259` maxDD `-2.1755`
- `market_context_high->unknown_24h` score `5.1899` n `89` status `ready` deltaP `24.9668` edge `0.3003` maxDD `-1.4072`
- `market_context_high->crypto_alt_4h` score `4.9043` n `99` status `ready` deltaP `18.0771` edge `0.4234` maxDD `-7.8181`
- `market_context_high->crypto_major_4h` score `4.8479` n `99` status `ready` deltaP `14.551` edge `0.4294` maxDD `-7.1265`
- `market_context_high->metal_4h` score `1.5361` n `99` status `ready` deltaP `11.9011` edge `0.1149` maxDD `-1.9651`
- `market_context_high->equity_4h` score `0.4825` n `99` status `ready` deltaP `10.8155` edge `0.1279` maxDD `-6.3852`
- `market_context_high->index_4h` score `0.4233` n `99` status `ready` deltaP `9.7099` edge `0.0358` maxDD `-0.7006`
- `market_context_high->crypto_major_1h` score `0.4227` n `110` status `ready` deltaP `6.1704` edge `0.1169` maxDD `-5.6406`
- `market_context_high->crypto_alt_1h` score `0.4082` n `110` status `ready` deltaP `8.1709` edge `0.1001` maxDD `-5.5126`
- `market_context_high->equity_1h` score `0.1872` n `110` status `ready` deltaP `4.2352` edge `0.0555` maxDD `-2.779`
- `market_context_high->fx_4h` score `-0.1964` n `99` status `ready` deltaP `6.3178` edge `0.0097` maxDD `-0.788`
- `market_context_high->commodity_1h` score `-0.2215` n `110` status `ready` deltaP `3.2825` edge `0.0157` maxDD `-1.278`
- `market_context_high->metal_1h` score `-0.2406` n `110` status `ready` deltaP `-0.3539` edge `0.0295` maxDD `-1.3057`
- `market_context_high->index_1h` score `-0.5289` n `110` status `ready` deltaP `-0.2885` edge `0.0096` maxDD `-0.7054`
- `market_context_high->commodity_4h` score `-0.5769` n `99` status `ready` deltaP `8.9461` edge `0.0095` maxDD `-4.377`
- `market_context_high->fx_1h` score `-1.331` n `110` status `ready` deltaP `-6.8672` edge `-0.0038` maxDD `-0.5734`
- `market_context_high->fx_24h` score `-1.8899` n `89` status `ready` deltaP `-6.7299` edge `-0.0116` maxDD `-2.749`
- `market_context_high->index_24h` score `-4.8009` n `89` status `ready` deltaP `-8.6298` edge `-0.1569` maxDD `-24.085`
- `market_context_high->commodity_24h` score `-5.4454` n `89` status `ready` deltaP `10.5591` edge `-0.0133` maxDD `-27.5371`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

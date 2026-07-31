# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-31T10:52:37.544141+00:00`
- Price records: `672`
- Market context records: `8508`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5882`

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

- `news_risk_high->unknown_24h` score `6275.6241` n `52` status `ready` deltaP `44.7383` edge `522.7125` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `5.9356` n `64` status `ready` deltaP `21.875` edge `0.4085` maxDD `-3.4427`
- `news_risk_high->index_4h` score `2.0303` n `64` status `ready` deltaP `16.8064` edge `0.0762` maxDD `-0.191`
- `news_risk_high->equity_1h` score `1.7374` n `64` status `ready` deltaP `15.9525` edge `0.0861` maxDD `-2.4803`
- `news_risk_high->crypto_major_4h` score `0.9267` n `64` status `ready` deltaP `5.8308` edge `0.1575` maxDD `-3.5385`
- `news_risk_high->crypto_alt_4h` score `0.8585` n `64` status `ready` deltaP `14.4817` edge `0.1527` maxDD `-5.8012`
- `news_risk_high->crypto_alt_1h` score `0.5825` n `64` status `ready` deltaP `9.4592` edge `0.0643` maxDD `-1.8813`
- `market_context_high->equity_1h` score `0.4155` n `36` status `ready` deltaP `3.6261` edge `0.0396` maxDD `-0.9985`
- `news_risk_high->crypto_major_1h` score `0.3657` n `64` status `ready` deltaP `6.9143` edge `0.052` maxDD `-2.0972`
- `market_context_high->index_1h` score `0.2265` n `36` status `ready` deltaP `7.5183` edge `-0.0014` maxDD `-0.2417`
- `news_risk_high->fx_1h` score `0.1173` n `64` status `ready` deltaP `5.8851` edge `0.0039` maxDD `-0.2475`
- `news_risk_high->fx_4h` score `0.0388` n `64` status `ready` deltaP `11.6235` edge `0.0215` maxDD `-0.6604`
- `news_risk_high->index_1h` score `0.0387` n `64` status `ready` deltaP `4.2197` edge `0.0085` maxDD `-0.5338`
- `news_risk_high->metal_4h` score `-0.0682` n `64` status `ready` deltaP `1.1052` edge `0.0315` maxDD `-0.8085`
- `news_risk_high->metal_1h` score `-0.1167` n `64` status `ready` deltaP `3.4057` edge `0.0079` maxDD `-0.5599`
- `market_context_high->metal_1h` score `-0.2022` n `36` status `ready` deltaP `2.7113` edge `-0.0072` maxDD `-0.6101`
- `market_context_high->crypto_major_1h` score `-0.2495` n `36` status `ready` deltaP `4.6574` edge `-0.0133` maxDD `-1.9791`
- `market_context_high->commodity_1h` score `-0.2828` n `36` status `ready` deltaP `4.7239` edge `-0.0052` maxDD `-2.0038`
- `market_context_high->crypto_alt_1h` score `-0.6624` n `36` status `ready` deltaP `-6.6866` edge `0.0098` maxDD `-2.012`
- `market_context_high->fx_1h` score `-0.873` n `36` status `ready` deltaP `-9.9135` edge `0.0007` maxDD `-0.3888`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

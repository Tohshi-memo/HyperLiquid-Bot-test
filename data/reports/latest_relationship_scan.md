# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-18T04:37:24.841491+00:00`
- Price records: `672`
- Market context records: `7103`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11488`

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

- `market_context_high->fx_4h` score `0.3938` n `153` status `ready` deltaP `15.9881` edge `0.0139` maxDD `-0.9333`
- `market_context_high->unknown_1h` score `-0.1205` n `153` status `ready` deltaP `0.2573` edge `0.0441` maxDD `-1.4688`
- `market_context_high->fx_1h` score `-0.1436` n `153` status `ready` deltaP `4.493` edge `0.0032` maxDD `-0.276`
- `market_context_high->crypto_alt_1h` score `-0.4183` n `153` status `ready` deltaP `0.7358` edge `0.0279` maxDD `-4.5815`
- `market_context_high->index_1h` score `-0.5644` n `153` status `ready` deltaP `-0.6155` edge `-0.0063` maxDD `-2.2895`
- `market_context_high->crypto_major_1h` score `-0.5812` n `153` status `ready` deltaP `3.6496` edge `0.0364` maxDD `-7.1523`
- `market_context_high->commodity_1h` score `-0.8665` n `153` status `ready` deltaP `-4.4783` edge `-0.0196` maxDD `-1.9306`
- `market_context_high->commodity_4h` score `-1.3765` n `153` status `ready` deltaP `-4.5054` edge `-0.0429` maxDD `-2.9494`
- `market_context_high->metal_1h` score `-1.5417` n `153` status `ready` deltaP `-6.9616` edge `-0.0055` maxDD `-2.125`
- `market_context_high->unknown_4h` score `-1.5585` n `153` status `ready` deltaP `-6.4971` edge `0.0037` maxDD `-4.4825`
- `market_context_high->equity_1h` score `-2.0834` n `153` status `ready` deltaP `2.8022` edge `-0.0435` maxDD `-14.716`
- `market_context_high->index_4h` score `-2.5024` n `153` status `ready` deltaP `-0.9176` edge `-0.0448` maxDD `-12.2591`
- `market_context_high->crypto_major_4h` score `-3.0149` n `153` status `ready` deltaP `4.2046` edge `0.0139` maxDD `-24.6094`
- `market_context_high->crypto_alt_4h` score `-3.0914` n `153` status `ready` deltaP `-0.0887` edge `-0.0172` maxDD `-22.2831`
- `market_context_high->commodity_24h` score `-3.3245` n `153` status `ready` deltaP `-7.6593` edge `-0.0951` maxDD `-4.4704`
- `market_context_high->fx_24h` score `-4.4053` n `153` status `ready` deltaP `-9.5996` edge `-0.0204` maxDD `-3.9503`
- `market_context_high->metal_4h` score `-4.4093` n `153` status `ready` deltaP `-8.7877` edge `-0.0112` maxDD `-5.4791`
- `market_context_high->equity_4h` score `-8.6772` n `153` status `ready` deltaP `-1.1139` edge `-0.218` maxDD `-63.963`
- `market_context_high->unknown_24h` score `-9.0867` n `153` status `ready` deltaP `-25.5515` edge `-0.0722` maxDD `-23.5076`
- `market_context_high->metal_24h` score `-14.8931` n `153` status `ready` deltaP `-25.4902` edge `-0.1436` maxDD `-42.8713`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

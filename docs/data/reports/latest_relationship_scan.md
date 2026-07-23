# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-23T23:22:28.370338+00:00`
- Price records: `672`
- Market context records: `7718`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14676`

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

- `market_context_high->equity_24h` score `3.5679` n `132` status `ready` deltaP `19.396` edge `0.3022` maxDD `-6.0681`
- `market_context_high->crypto_major_1h` score `1.0489` n `133` status `ready` deltaP `13.1579` edge `0.0438` maxDD `-1.5286`
- `market_context_high->crypto_major_4h` score `1.0148` n `133` status `ready` deltaP `14.6513` edge `0.1587` maxDD `-6.7444`
- `market_context_high->equity_1h` score `0.6423` n `133` status `ready` deltaP `8.7968` edge `0.0808` maxDD `-4.2072`
- `market_context_high->crypto_alt_4h` score `0.6322` n `133` status `ready` deltaP `8.5045` edge `0.1077` maxDD `-3.9374`
- `market_context_high->equity_4h` score `0.579` n `133` status `ready` deltaP `1.9694` edge `0.2524` maxDD `-6.9701`
- `market_context_high->index_1h` score `0.4107` n `133` status `ready` deltaP `9.245` edge `0.0156` maxDD `-0.7743`
- `market_context_high->crypto_alt_1h` score `0.1341` n `133` status `ready` deltaP `3.8292` edge `0.0289` maxDD `-1.4603`
- `market_context_high->fx_24h` score `0.0729` n `132` status `ready` deltaP `13.8608` edge `0.0257` maxDD `-3.0343`
- `market_context_high->commodity_4h` score `-0.1653` n `133` status `ready` deltaP `4.4814` edge `0.0157` maxDD `-1.0817`
- `market_context_high->commodity_1h` score `-0.176` n `133` status `ready` deltaP `3.6951` edge `0.0066` maxDD `-0.6722`
- `market_context_high->index_4h` score `-0.2332` n `133` status `ready` deltaP `10.8643` edge `0.0435` maxDD `-1.3325`
- `market_context_high->metal_24h` score `-0.3933` n `133` status `ready` deltaP `3.3756` edge `0.1538` maxDD `-2.3927`
- `market_context_high->fx_1h` score `-0.5552` n `133` status `ready` deltaP `-0.9776` edge `-0.001` maxDD `-0.4331`
- `market_context_high->metal_1h` score `-0.8543` n `133` status `ready` deltaP `1.4171` edge `0.0197` maxDD `-0.6936`
- `market_context_high->metal_4h` score `-1.4843` n `133` status `ready` deltaP `0.9857` edge `0.0752` maxDD `-1.4368`
- `market_context_high->fx_4h` score `-1.587` n `133` status `ready` deltaP `-5.5379` edge `-0.0037` maxDD `-1.6936`
- `market_context_high->commodity_24h` score `-1.7501` n `132` status `ready` deltaP `5.6858` edge `-0.0254` maxDD `-7.0012`
- `market_context_high->unknown_1h` score `-2.1553` n `133` status `ready` deltaP `-0.9747` edge `-0.1141` maxDD `-1.054`
- `market_context_high->index_24h` score `-2.5965` n `132` status `ready` deltaP `-18.4537` edge `0.0004` maxDD `-2.1544`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

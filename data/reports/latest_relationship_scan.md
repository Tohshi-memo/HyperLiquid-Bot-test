# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-23T08:52:23.791704+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14760`

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

- `news_risk_high->unknown_4h` score `14.7008` n `51` status `ready` deltaP `26.5453` edge `1.0527` maxDD `-0.0347`
- `risk_on_high->unknown_1h` score `4.9961` n `33` status `ready` deltaP `-8.1791` edge `0.7399` maxDD `-1.5876`
- `risk_on_and_context->unknown_1h` score `4.9961` n `33` status `ready` deltaP `-8.1791` edge `0.7399` maxDD `-1.5876`
- `news_risk_high->unknown_1h` score `3.724` n `51` status `ready` deltaP `19.6283` edge `0.2099` maxDD `-0.7674`
- `news_risk_high->equity_4h` score `2.9306` n `51` status `ready` deltaP `24.7938` edge `0.1562` maxDD `-2.1818`
- `news_risk_high->fx_4h` score `2.8464` n `51` status `ready` deltaP `33.8146` edge `0.0252` maxDD `-0.0746`
- `risk_on_high->metal_4h` score `2.3705` n `32` status `ready` deltaP `31.25` edge `-0.002` maxDD `-0.0367`
- `risk_on_and_context->metal_4h` score `2.3705` n `32` status `ready` deltaP `31.25` edge `-0.002` maxDD `-0.0367`
- `risk_on_high->equity_4h` score `1.6961` n `32` status `ready` deltaP `-1.6768` edge `0.2717` maxDD `-0.7794`
- `risk_on_and_context->equity_4h` score `1.6961` n `32` status `ready` deltaP `-1.6768` edge `0.2717` maxDD `-0.7794`
- `market_context_high->unknown_1h` score `1.4374` n `133` status `ready` deltaP `8.704` edge `0.1066` maxDD `-1.5876`
- `market_context_high->commodity_24h` score `1.2402` n `106` status `ready` deltaP `2.3356` edge `0.117` maxDD `-0.6707`
- `news_risk_high->fx_1h` score `1.2242` n `51` status `ready` deltaP `16.8457` edge `0.0067` maxDD `-0.0257`
- `market_context_high->unknown_4h` score `0.9889` n `123` status `ready` deltaP `22.002` edge `-0.0471` maxDD `-0.3736`
- `news_risk_high->equity_1h` score `0.8446` n `51` status `ready` deltaP `18.3427` edge `0.0225` maxDD `-0.9204`
- `risk_on_high->fx_4h` score `0.7953` n `32` status `ready` deltaP `17.4543` edge `0.0042` maxDD `-0.1551`
- `risk_on_and_context->fx_4h` score `0.7953` n `32` status `ready` deltaP `17.4543` edge `0.0042` maxDD `-0.1551`
- `news_risk_high->index_4h` score `0.7056` n `51` status `ready` deltaP `11.7198` edge `0.0204` maxDD `-0.1788`
- `risk_on_high->index_4h` score `0.6471` n `32` status `ready` deltaP `12.2713` edge `0.0448` maxDD `-0.1584`
- `risk_on_and_context->index_4h` score `0.6471` n `32` status `ready` deltaP `12.2713` edge `0.0448` maxDD `-0.1584`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

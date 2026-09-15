# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-15T00:22:31.952890+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `10554`

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

- `news_risk_high->unknown_4h` score `397.8248` n `78` status `ready` deltaP `-22.4554` edge `33.3911` maxDD `-4.1464`
- `news_risk_high->unknown_24h` score `24.5731` n `78` status `ready` deltaP `18.9236` edge `1.9216` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `21.3235` n `78` status `ready` deltaP `44.4712` edge `1.5196` maxDD `-1.4626`
- `news_risk_high->crypto_major_24h` score `15.7817` n `78` status `ready` deltaP `32.265` edge `1.2471` maxDD `-9.098`
- `news_risk_high->equity_24h` score `14.1527` n `78` status `ready` deltaP `43.9503` edge `1.0644` maxDD `-6.5742`
- `news_risk_high->index_24h` score `8.7104` n `78` status `ready` deltaP `61.7655` edge `0.3317` maxDD `-0.075`
- `news_risk_high->metal_24h` score `6.4517` n `78` status `ready` deltaP `37.7938` edge `0.3311` maxDD `-0.6334`
- `risk_on_high->commodity_24h` score `5.963` n `52` status `ready` deltaP `37.8472` edge `0.2446` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `5.963` n `52` status `ready` deltaP `37.8472` edge `0.2446` maxDD `0.0`
- `market_context_high->commodity_24h` score `4.666` n `137` status `ready` deltaP `30.5479` edge `0.2377` maxDD `-0.8682`
- `risk_on_high->fx_24h` score `4.2633` n `52` status `ready` deltaP `48.0769` edge `0.039` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `4.2633` n `52` status `ready` deltaP `48.0769` edge `0.039` maxDD `-0.0054`
- `market_context_high->fx_24h` score `3.8663` n `137` status `ready` deltaP `44.8905` edge `0.0445` maxDD `-0.0593`
- `risk_on_high->commodity_4h` score `1.9537` n `52` status `ready` deltaP `25.5277` edge `0.0276` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `1.9537` n `52` status `ready` deltaP `25.5277` edge `0.0276` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `1.7541` n `137` status `ready` deltaP `20.9376` edge `0.0484` maxDD `-0.345`
- `news_risk_high->index_4h` score `0.7253` n `78` status `ready` deltaP `17.2686` edge `0.0407` maxDD `-0.6935`
- `market_context_high->commodity_1h` score `0.7155` n `137` status `ready` deltaP `12.0635` edge `0.0169` maxDD `-0.3491`
- `risk_on_high->metal_1h` score `0.2128` n `52` status `ready` deltaP `7.462` edge `0.0081` maxDD `-0.1115`
- `risk_on_and_context->metal_1h` score `0.2128` n `52` status `ready` deltaP `7.462` edge `0.0081` maxDD `-0.1115`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
